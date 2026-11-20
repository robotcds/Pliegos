"""Renew expired Druid sessions in memory; never persist bearer tokens."""
import base64
import json
import math
import os
import time

_renewed_tokens = {}
_token_deadlines = {}


def register_token(token, metadata=None):
    """Use provider expiry when available, otherwise a conservative local age."""
    now = time.monotonic()
    lifetime = None
    for name in ('expireInSeconds', 'expiresIn', 'expires_in'):
        value = (metadata or {}).get(name)
        if isinstance(value, (int, float)) and math.isfinite(value) and value > 0:
            lifetime = float(value)
            break
    # Decoding exp only schedules renewal; it never validates or trusts identity.
    try:
        parts = token.split('.')
        if len(parts) == 3:
            claims = json.loads(base64.urlsafe_b64decode(parts[1] + '=' * (-len(parts[1]) % 4)))
            remaining = float(claims['exp']) - time.time()
            if math.isfinite(remaining):
                lifetime = remaining if lifetime is None else min(lifetime, remaining)
    except (ValueError, TypeError, KeyError, AttributeError):
        pass
    interval = float(os.getenv('DRUID_AUTH_RENEW_SECONDS', '600'))
    if not math.isfinite(interval) or interval <= 0:
        raise ValueError('DRUID_AUTH_RENEW_SECONDS debe ser positivo y finito')
    if lifetime is not None:
        # Renew with room for a call; short-lived tokens use 20% of their TTL.
        interval = min(interval, max(0, lifetime - min(120, max(0, lifetime) * .2)))
    _token_deadlines[token] = now + interval

# Exact code fingerprints for transport and recovery changes that preserve checkpoints.
# Any later code change must still invalidate incompatible delivery checkpoints.
COMPATIBLE_DELIVERY_CODE = {
    '6f95c72dbe6b7495fff9ff880194eb4121f1a388f64c0b8a70e3fdd23a053bb6':
        '597e8bcc80f0acf00cc31f1647c6dc361630481be9014e8fe15d75c379cce660',
    '7f2feee77f9f49db3af4a0d047cb9e3ef4c3ed488150923030585595767e987d':
        '597e8bcc80f0acf00cc31f1647c6dc361630481be9014e8fe15d75c379cce660',
    'eba7d7f1aeebf9f4d214f2673ffbdd24de38e0f49727cb4c8ae598d5cc399461':
        '1ce089cc0adce0cc728faf42d99ed920f643e67f77e6bf49419e5a342a3d4655',
}


def delivery_code_signature(fingerprint):
    return COMPATIBLE_DELIVERY_CODE.get(fingerprint, fingerprint)


def call_with_auth_refresh(call, authenticate, system, user, config, token):
    key = (config.get('auth_url'), config.get('gpt_url'),
           config.get('username'), config.get('tenant'), token)
    current = _renewed_tokens.get(key, token)
    if current not in _token_deadlines:
        register_token(current)
    if time.monotonic() >= _token_deadlines[current]:
        print('Renovando sesión Druid preventivamente antes de la siguiente petición...', flush=True)
        current = authenticate(config)
        if current not in _token_deadlines:
            register_token(current)
        _renewed_tokens[key] = current
    try:
        return call(system, user, config, current)
    except Exception as exc:
        if getattr(exc, 'status_code', None) != 401:
            raise
    _renewed_tokens.pop(key, None)
    print('Druid rechazó la sesión (401). Renovando autenticación y repitiendo '
          'la petición pendiente una sola vez...', flush=True)
    current = authenticate(config)
    if current not in _token_deadlines:
        register_token(current)
    _renewed_tokens[key] = current
    try:
        return call(system, user, config, current)
    except Exception as exc:
        if getattr(exc, 'status_code', None) == 401:
            _renewed_tokens.pop(key, None)
        raise
