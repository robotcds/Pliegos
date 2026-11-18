import unittest
import base64
import json
from unittest.mock import Mock, patch
from pathlib import Path

import druid_auth_retry as auth
from oportunidades import DruidCallError, call_druid_gpt
from agent_deliveries import digest


class AuthRetryTests(unittest.TestCase):
    def setUp(self):
        auth._renewed_tokens.clear()
        auth._token_deadlines.clear()

    @patch.dict('os.environ', {'DRUID_AUTH_RENEW_SECONDS': '600'})
    @patch('druid_auth_retry.time.monotonic', return_value=100)
    def test_opaque_token_renews_before_next_request(self, clock):
        auth.register_token('opaque')
        call = Mock(return_value='ok')
        login = Mock(return_value='renewed')
        clock.return_value = 699
        auth.call_with_auth_refresh(call, login, 's', 'u', {}, 'opaque')
        login.assert_not_called()
        clock.return_value = 700
        auth.call_with_auth_refresh(call, login, 's', 'u', {}, 'opaque')
        login.assert_called_once()
        self.assertEqual(call.call_args.args[-1], 'renewed')
        clock.return_value = 701
        auth.call_with_auth_refresh(call, login, 's', 'u', {}, 'opaque')
        login.assert_called_once()
        self.assertEqual(call.call_args.args[-1], 'renewed')

    @patch.dict('os.environ', {'DRUID_AUTH_RENEW_SECONDS': '600'})
    @patch('druid_auth_retry.time.monotonic', return_value=100)
    @patch('druid_auth_retry.time.time', return_value=1000)
    def test_expiry_metadata_and_jwt_use_earliest_deadline(self, wall, clock):
        body = base64.urlsafe_b64encode(json.dumps({'exp': 1300}).encode()).decode().rstrip('=')
        token = 'header.' + body + '.signature'
        auth.register_token(token, {'expireInSeconds': 900})
        self.assertEqual(auth._token_deadlines[token], 340)
        auth.register_token('opaque', {'expireInSeconds': 100})
        self.assertEqual(auth._token_deadlines['opaque'], 180)

    @patch('druid_auth_retry.time.monotonic', return_value=100)
    def test_proactive_login_failure_does_not_submit_expired_token(self, clock):
        auth._token_deadlines['old'] = 99
        call = Mock()
        with self.assertRaisesRegex(RuntimeError, 'login failed'):
            auth.call_with_auth_refresh(call, Mock(side_effect=RuntimeError('login failed')),
                                       's', 'u', {}, 'old')
        call.assert_not_called()

    def test_refresh_once_and_reuse_across_config_copies(self):
        call = Mock(side_effect=[DruidCallError('expired', status_code=401), 'ok', 'next'])
        login = Mock(return_value='new')
        config = {'username': 'test'}
        self.assertEqual(auth.call_with_auth_refresh(call, login, 's', 'u', config, 'old'), 'ok')
        self.assertEqual(auth.call_with_auth_refresh(call, login, 's2', 'u2', dict(config), 'old'), 'next')
        login.assert_called_once_with(config)
        self.assertEqual([c.args[-1] for c in call.call_args_list], ['old', 'new', 'new'])

    def test_second_401_stops_without_loop(self):
        call = Mock(side_effect=DruidCallError('unauthorized', status_code=401))
        login = Mock(return_value='new')
        with self.assertRaises(DruidCallError):
            auth.call_with_auth_refresh(call, login, 's', 'u', {}, 'old')
        self.assertEqual(call.call_count, 2)
        login.assert_called_once()
        self.assertFalse(auth._renewed_tokens)

    def test_other_errors_do_not_refresh(self):
        for status in (403, 429, 504):
            login = Mock()
            with self.assertRaises(DruidCallError):
                auth.call_with_auth_refresh(Mock(side_effect=DruidCallError('error', status_code=status)),
                                            login, 's', 'u', {}, 'old')
            login.assert_not_called()

    def test_login_failure_stops(self):
        call = Mock(side_effect=DruidCallError('expired', status_code=401))
        with self.assertRaisesRegex(RuntimeError, 'login failed'):
            auth.call_with_auth_refresh(call, Mock(side_effect=RuntimeError('login failed')),
                                       's', 'u', {}, 'old')
        call.assert_called_once()

    @patch('oportunidades.has_active_run', return_value=False)
    @patch('oportunidades.authenticate_druid', return_value='new')
    @patch('oportunidades._call_druid_gpt_once')
    def test_public_call_renews(self, call, login, active):
        call.side_effect = [DruidCallError('expired', status_code=401), 'complete']
        self.assertEqual(call_druid_gpt('s', 'u', {}, 'old'), 'complete')
        self.assertEqual(call.call_args.args[-1], 'new')

    def test_transport_fix_preserves_existing_delivery_signature(self):
        root = Path(__file__).resolve().parents[1]
        fingerprint = digest([(root / name).read_text(encoding='utf-8')
                              for name in ('oportunidades.py', 'capas.py')])
        self.assertEqual(auth.delivery_code_signature(fingerprint),
                         '597e8bcc80f0acf00cc31f1647c6dc361630481be9014e8fe15d75c379cce660')
        self.assertEqual(auth.delivery_code_signature('changed'), 'changed')
