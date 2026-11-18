import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

import requests

import druid_async_diagnostics as diag


# UUID sintético SOLO para pruebas unitarias, con HTTP simulado. No es configuración real.
ACTION = 'b23debbb-f747-4a83-818f-4d2adcaa6446'
START = f'https://example.invalid/api/Druid/{diag.EXPECTED_BOT}/GPT/{ACTION}/GenericIntegration'
POLL = f'https://example.invalid/api/Druid/{diag.EXPECTED_BOT}/GetGenericIntegrationResponse'
INVOCATION = '8282ecab-8e90-4e63-b8ce-d22ef5f401d1'


def response(status, body, *, text=False, headers=None):
    r = requests.Response()
    r.status_code = status
    r._content = (body if text else json.dumps(body)).encode('utf8')
    r.encoding = 'utf8'
    r.headers.update(headers or {'Content-Type': 'application/json'})
    return r


class Clock:
    def __init__(self):
        self.now = 0

    def __call__(self):
        return self.now

    def sleep(self, seconds):
        self.now += seconds


class AsyncDiagnosticsTests(unittest.TestCase):
    def run_compare(self, session, path, **kwargs):
        clock = Clock()
        return diag.compare(START, POLL, 'fake-secret', path, session=session,
                            clock=clock, sleep=clock.sleep, **kwargs)

    def test_same_payload_sync_then_one_async_post_then_get(self):
        session = Mock()
        session.request.side_effect = [response(200, diag.EXPECTED),
                                       response(200, INVOCATION, text=True),
                                       response(200, diag.EXPECTED)]
        with tempfile.TemporaryDirectory() as tmp:
            state = self.run_compare(session, tmp)
            self.assertEqual(state['status'], 'RESULT_RETRIEVED')
            sync = json.loads((Path(tmp) / 'sync.json').read_text(encoding='utf8'))
            self.assertIn('+00:00', sync['started_at_utc'])
            self.assertEqual(sync['method'], 'POST')
            self.assertIn('asyncResponse=false', sync['url'])
            for path in Path(tmp).glob('*.json'):
                self.assertNotIn('fake-secret', path.read_text(encoding='utf8'))
        calls = session.request.call_args_list
        self.assertEqual([c.args[0] for c in calls], ['POST', 'POST', 'GET'])
        self.assertEqual(calls[0].kwargs['json'], calls[1].kwargs['json'])
        self.assertEqual(calls[2].kwargs['params']['invocationId'], INVOCATION)
        self.assertFalse(calls[1].kwargs['allow_redirects'])

    def test_404_default_stops_without_claiming_pending(self):
        session = Mock()
        session.request.side_effect = [response(200, diag.EXPECTED), response(200, {'invocationId': INVOCATION}),
                                       response(404, 'No response found for invocationId '+INVOCATION, text=True)]
        with tempfile.TemporaryDirectory() as tmp:
            state = self.run_compare(session, tmp)
            self.assertEqual(state['status'], 'HTTP_404_MEANING_UNCONFIRMED')
            self.assertEqual(state['queries'], 1)
        self.assertEqual(session.request.call_count, 3)

    def test_bounded_404_observation_never_resubmits(self):
        session = Mock()
        session.request.side_effect = [response(200, diag.EXPECTED), response(200, INVOCATION, text=True),
                                       response(404, 'missing', text=True), response(404, 'missing', text=True)]
        with tempfile.TemporaryDirectory() as tmp:
            state = self.run_compare(session, tmp, timeout=20, interval=10, continue_404=True)
            self.assertEqual(state['status'], 'POLLING_TIMEOUT')
            self.assertEqual(state['server_job_status'], 'UNKNOWN')
            self.assertEqual(state['observation_categories'], ['HTTP_404_MEANING_UNCONFIRMED'])
        self.assertEqual([c.args[0] for c in session.request.call_args_list], ['POST', 'POST', 'GET', 'GET'])

    def test_404_then_result_preserves_exact_id(self):
        session = Mock()
        session.request.side_effect = [response(200, diag.EXPECTED), response(200, {'invocationId': INVOCATION}),
                                       response(404, 'missing', text=True), response(200, {'ResponseBody': diag.EXPECTED})]
        with tempfile.TemporaryDirectory() as tmp:
            state = self.run_compare(session, tmp, continue_404=True)
            self.assertEqual(state['status'], 'RESULT_RETRIEVED_WRAPPED')
        for c in session.request.call_args_list[2:]:
            self.assertEqual(c.kwargs['params']['invocationId'], INVOCATION)

    def test_wrong_sync_response_prevents_async_call(self):
        session = Mock()
        session.request.return_value = response(200, {'status': 'success', 'message': 'unrelated'})
        with tempfile.TemporaryDirectory() as tmp:
            state = self.run_compare(session, tmp)
            self.assertEqual(state['status'], 'SYNC_CONTROL_FAILED_ASYNC_NOT_SENT')
        self.assertEqual(session.request.call_count, 1)

    def test_lost_async_ack_archived_without_retry(self):
        session = Mock()
        session.request.side_effect = [response(200, diag.EXPECTED), requests.Timeout('DO NOT LOG fake-secret')]
        with tempfile.TemporaryDirectory() as tmp:
            state = self.run_compare(session, tmp)
            self.assertEqual(state['status'], 'SUBMISSION_OUTCOME_UNKNOWN')
            self.assertIsNone(state['invocationId'])
            event = json.loads((Path(tmp) / 'async_start.json').read_text(encoding='utf8'))
            self.assertEqual(event['transport_error'], {'type': 'Timeout'})
            with self.assertRaises(ValueError):
                self.run_compare(session, tmp)
        self.assertEqual(session.request.call_count, 2)

    def test_resume_only_gets(self):
        session = Mock()
        session.request.return_value = response(200, diag.EXPECTED)
        with tempfile.TemporaryDirectory() as tmp:
            state = {'start_url': START, 'poll_url': POLL, 'invocationId': INVOCATION,
                     'queries': 2, 'expected': diag.EXPECTED, 'status': 'POLLING_TIMEOUT'}
            diag.save_json(Path(tmp) / 'estado.json', state)
            diag.poll_result(tmp, 'fake-secret', session=session)
        self.assertEqual(session.request.call_count, 1)
        self.assertEqual(session.request.call_args.args[0], 'GET')

    def test_unverified_pending_word_is_not_assumed(self):
        record = {'http_status': 200, 'body_json': {'status': 'running'}}
        self.assertEqual(diag.classify(record), 'SUCCESS_HTTP_UNKNOWN_BODY')
        self.assertEqual(diag.classify(record, pending_statuses=('running',)),
                         'PENDING_STATUS_EXPLICITLY_CONFIGURED')
        self.assertEqual(diag.classify({'http_status': 202, 'body_json': None}),
                         'HTTP_202_ACCEPTED_RESULT_NOT_PROVEN')

    def test_headers_and_echoed_secrets_are_redacted(self):
        session = Mock()
        session.request.return_value = response(200, {'Authorization': 'Bearer fake-secret',
                                                      'password': 'another-secret', 'ok': 'retained'},
                                               headers={'Set-Cookie': 'private-cookie', 'x-correlation-id': 'server-id'})
        with tempfile.TemporaryDirectory() as tmp:
            result = diag.logged_request(session, 'GET', POLL, Path(tmp), 'event.json',
                                         token='fake-secret', params={'invocationId': INVOCATION})
            saved = (Path(tmp) / 'event.json').read_text(encoding='utf8')
            for secret in ['fake-secret', 'another-secret', 'private-cookie']:
                self.assertNotIn(secret, saved)
            self.assertIn('server-id', saved)
            self.assertIn('retained', saved)
            self.assertEqual(result['response_headers']['Set-Cookie'], '[REDACTED]')

    def test_refuses_gpt_action_and_cross_bot_routes(self):
        with self.assertRaisesRegex(ValueError, 'GPT'):
            diag.endpoints(START, POLL, next(iter(diag.GPT_ACTIONS)), simple=True)
        with self.assertRaises(ValueError):
            diag.endpoints(START, POLL.replace(diag.EXPECTED_BOT, str(UUID_ZERO)))

    def test_bad_ack_or_http_errors_do_not_claim_job_execution(self):
        for event, expected in [
            ({'transport_error': None, 'http_status': 200, 'body_json': {}, 'body_text': '{}'}, 'START_PROTOCOL_UNKNOWN'),
            ({'transport_error': None, 'http_status': 500, 'body_json': {}, 'body_text': '{}'}, 'START_HTTP_ERROR')]:
            self.assertEqual(diag.acknowledgement(event), (None, expected))

    def test_final_http_and_server_errors_differ(self):
        self.assertEqual(diag.classify({'http_status': 401}), 'FINAL_HTTP_ERROR')
        self.assertEqual(diag.classify({'http_status': 503}), 'RETRYABLE_HTTP_ERROR')
        self.assertEqual(diag.classify({'http_status': 200, 'body_json': {'error': 'failed'}}),
                         'INTEGRATION_ERROR_REPORTED')

    def test_nonfinite_or_unbounded_times_rejected(self):
        for timeout, interval, http_timeout in [(float('nan'), 10, 30), (120, 0, 30), (3601, 10, 30), (120, 1, 30)]:
            with self.assertRaises(ValueError):
                diag.validate_limits(timeout, interval, http_timeout)


UUID_ZERO = '00000000-0000-0000-0000-000000000000'

if __name__ == '__main__':
    unittest.main()
