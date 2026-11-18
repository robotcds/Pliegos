import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

import requests
from druid_async_probe import AsyncProtocolError, classify_result, invocation_id, probe, validate_urls


START = 'https://example.druidplatform.com/api/Druid/bot/GPT/action/GenericIntegration'
POLL = 'https://example.druidplatform.com/api/Druid/bot/GetGenericIntegrationResponse'
INPUT = {'Messages': {'items': [{'Role': 'user', 'Content': 'documento completo'}]}, 'toolsJSON': []}
FINAL = {'DataSource': {'finish_reason': 'tool_calls', 'responseJSON': {
    'tool_calls': [{'function': {'name': 'KB_response', 'arguments': '{"Response":"PRUEBA_ASYNC_OK"}'}}]}}}


def response(code, body):
    result = Mock(status_code=code)
    result.json.return_value = body
    return result


class DruidAsyncProbeTests(unittest.TestCase):
    def test_specific_initial_missing_response_is_retried_without_post(self):
        session = Mock()
        session.request.side_effect = [response(200, {'invocationId': 'id'}),
            response(404, 'No response found for invocationId id'), response(200, FINAL)]
        with tempfile.TemporaryDirectory() as directory:
            probe(START, POLL, 'token', INPUT, directory, session=session, sleep=lambda _: None)
            self.assertTrue((Path(directory) / 'resultado.json').exists())
        self.assertEqual([c.args[0] for c in session.request.call_args_list], ['POST', 'GET', 'GET'])

    def test_persistent_missing_response_has_bounded_grace(self):
        session = Mock()
        session.request.side_effect = [response(200, {'invocationId': 'id'}),
            response(404, 'No response found for invocationId id'),
            response(404, 'No response found for invocationId id')]
        now = [0]
        def sleep(seconds):
            now[0] += seconds
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(AsyncProtocolError, 'Connector audit log'):
                probe(START, POLL, 'token', INPUT, directory, session=session,
                      clock=lambda: now[0], sleep=sleep, missing_response_grace=10)
            self.assertFalse((Path(directory) / 'resultado.json').exists())
        self.assertEqual(session.request.call_count, 3)

    def test_unrelated_404_is_not_masked_as_pending(self):
        session = Mock()
        session.request.side_effect = [response(200, {'invocationId': 'id'}), response(404, 'Route not found')]
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(AsyncProtocolError, 'HTTP 404'):
                probe(START, POLL, 'token', INPUT, directory, session=session)
        self.assertEqual(session.request.call_count, 2)

    def test_real_plain_guid_and_json_string_ack(self):
        value = 'e32a6ee2-36bb-4476-bbee-ed3759429082'
        for body in (value, '\n' + value + '\n', json.dumps(value), {'invocationId': value}):
            self.assertEqual(invocation_id(body, 200), value)
        for body, status in [('Error de servidor', 200), ('<html>login</html>', 200), (value, 401)]:
            with self.assertRaises(AsyncProtocolError):
                invocation_id(body, status)

    def test_recover_plain_ack_after_previous_parser_failure_without_post(self):
        value = 'e32a6ee2-36bb-4476-bbee-ed3759429082'
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / 'inicio.json').write_text(json.dumps({'http_status': 200, 'body': value}), encoding='utf8')
            session = Mock()
            session.request.return_value = response(200, FINAL)
            probe(START, POLL, 'token', None, directory, resume=True, session=session)
            self.assertEqual(session.request.call_count, 1)
            self.assertEqual(session.request.call_args.args[0], 'GET')
            self.assertEqual(session.request.call_args.kwargs['params']['invocationId'], value)

    def test_one_post_then_same_invocation_even_after_transient_get_failure(self):
        session = Mock()
        session.request.side_effect = [response(200, {'invocationId': 'job-1'}),
            response(200, {'status': 'pending'}), requests.Timeout(), response(503, {}),
            response(200, {'ResponseBody': FINAL})]
        with tempfile.TemporaryDirectory() as directory:
            result = probe(START, POLL, 'secret-value', INPUT, directory,
                           session=session, sleep=lambda _: None)
            self.assertEqual(json.loads(result.read_text(encoding='utf8')), FINAL)
            self.assertEqual((Path(directory) / 'respuesta.md').read_text(encoding='utf8'), 'PRUEBA_ASYNC_OK')
            for p in Path(directory).glob('*.json'):
                self.assertNotIn('secret-value', p.read_text(encoding='utf8'))
        methods = [c.args[0] for c in session.request.call_args_list]
        self.assertEqual(methods, ['POST', 'GET', 'GET', 'GET', 'GET'])
        self.assertEqual(session.request.call_args_list[0].kwargs['json'], INPUT)
        for c in session.request.call_args_list[1:]:
            self.assertEqual(c.kwargs['params']['invocationId'], 'job-1')

    def test_resume_does_not_launch_another_model_call(self):
        with tempfile.TemporaryDirectory() as directory:
            state = {'invocationId': 'existing', 'start_url': START, 'poll_url': POLL, 'queries': 4, 'status': 'pending'}
            (Path(directory) / 'invocacion.json').write_text(json.dumps(state), encoding='utf8')
            session = Mock()
            session.request.return_value = response(200, FINAL)
            probe(START, POLL, 'token', None, directory, resume=True, session=session)
            self.assertEqual(session.request.call_count, 1)
            self.assertEqual(session.request.call_args.args[0], 'GET')
            self.assertEqual(session.request.call_args.kwargs['params']['invocationId'], 'existing')

    def test_lost_ack_never_reposts(self):
        session = Mock()
        session.request.side_effect = requests.Timeout()
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(requests.Timeout):
                probe(START, POLL, 'token', INPUT, directory, session=session)
        self.assertEqual(session.request.call_count, 1)

    def test_unknown_status_and_empty_echo_are_not_success(self):
        for data in ({'status': 'success'}, {'DataSource': {}}, {'invocationId': 'id'}, {'error': 'failure'}):
            with self.subTest(data=data), self.assertRaises(AsyncProtocolError):
                classify_result(data, 200)

    def test_length_is_archived_but_never_published_as_complete(self):
        from oportunidades import DruidOutputLimitError
        session = Mock()
        session.request.side_effect = [response(200, {'invocationId': 'id'}),
            response(200, {'DataSource': {**FINAL['DataSource'], 'finish_reason': 'length'}})]
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(DruidOutputLimitError):
                probe(START, POLL, 'token', INPUT, directory, session=session)
            self.assertTrue((Path(directory) / 'consulta_0001.json').exists())
            self.assertFalse((Path(directory) / 'resultado.json').exists())

    def test_deadline_leaves_resumable_id(self):
        session = Mock()
        session.request.side_effect = [response(200, {'invocationId': 'id'}), response(202, {})]
        ticks = iter([0, 0, 0, 2, 2])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(TimeoutError):
                probe(START, POLL, 'token', INPUT, directory, session=session,
                      total_timeout=1, clock=lambda: next(ticks), sleep=lambda _: None)
            self.assertEqual(json.loads((Path(directory) / 'invocacion.json').read_text())['invocationId'], 'id')

    def test_reject_credentials_in_urls_and_wrong_bot(self):
        for start, poll in [(START.replace('https://', 'http://'), POLL),
                            (START + '?token=hidden', POLL), (START, POLL.replace('/bot/', '/other/'))]:
            with self.subTest(start=start, poll=poll), self.assertRaises(ValueError):
                validate_urls(start, poll)


if __name__ == '__main__':
    unittest.main()
