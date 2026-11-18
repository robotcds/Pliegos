"""Diagnóstico aislado de GenericIntegration sin GPT. Sin argumentos, solo audita archivos.

No modifica el flujo de oportunidades ni crea integraciones en DRUID.
No usa la etiqueta pending para un 404 o para un simple acuse con invocationId.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import time
from urllib.parse import quote, urlsplit, urlunsplit
from uuid import UUID, uuid4

import requests

from druid_async_probe import save_json, validate_urls


ROOT = Path(__file__).resolve().parent
DOC_URL = ('https://docs.druidai.com/1385954/Content/Webhooks/'
           'Exchanging%20Data%20with%20External%20Systems.htm'
           '#ExecuteAsynchronousIntegrationsLongRunningRequests')
EXPECTED = {'status': 'success', 'message': 'PRUEBA_ASYNC_OK', 'test': 'TEST_ASYNC_SIMPLE'}
GPT_ACTIONS = {'7a7e7161-2347-47d9-8134-b869a15c5210',
               '12cbe351-e90c-434d-b931-ea55d3f9c490'}
EXPECTED_BOT = '8805a55b-9947-47b5-d511-08de9ea71a4f'
SENSITIVE = re.compile(r'authorization|cookie|password|passwd|secret|token|api.?key|requestheaders', re.I)


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='milliseconds')


def new_directory(label):
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M-%S_UTC')
    path = ROOT / 'resumenes' / f'{stamp}_{label}_{uuid4().hex[:8]}'
    path.mkdir(parents=True, exist_ok=False)
    return path


def scrub(value, secrets=()):
    """Cuerpos completos salvo secretos: nunca conservar un eco de Authorization."""
    if isinstance(value, dict):
        return {str(k): '[REDACTED]' if SENSITIVE.search(str(k)) else scrub(v, secrets)
                for k, v in value.items()}
    if isinstance(value, list):
        return [scrub(v, secrets) for v in value]
    if isinstance(value, str):
        for secret in secrets:
            if secret:
                value = value.replace(secret, '[REDACTED]')
        value = re.sub(r'(?i)Bearer\s+[A-Za-z0-9._~+/%=-]+', 'Bearer [REDACTED]', value)
        return value
    return value


def load_configuration():
    # Reutiliza el lector existente sin cambiar ni regenerar credenciales.
    from oportunidades import load_env_file
    load_env_file(ROOT / '.env')
    return (os.getenv('DRUID_ASYNC_START_URL', '').strip(),
            os.getenv('DRUID_ASYNC_POLL_URL', '').strip(),
            os.getenv('DRUID_WEBHOOK_TOKEN', '').strip())


def endpoints(start_url, poll_url, integration_id=None, entity=None, *, simple=False):
    validate_urls(start_url, poll_url)
    start = urlsplit(start_url)
    parts = start.path.strip('/').split('/')
    if len(parts) != 6 or parts[:2] != ['api', 'Druid']:
        raise ValueError('La ruta debe ser /api/Druid/BotId/entityName/integrationId/GenericIntegration.')
    bot = str(UUID(parts[2]))
    action = str(UUID(integration_id or parts[4]))
    if bot != EXPECTED_BOT:
        raise ValueError('El Bot ID no coincide con API COIIM; no se enviará la prueba.')
    name = entity or parts[3]
    if not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', name):
        raise ValueError('Nombre de entidad no admitido para este diagnóstico.')
    if simple and action in GPT_ACTIONS:
        raise ValueError('Ese ID pertenece a la integración GPT. Se requiere el ID publicado de TEST_ASYNC_SIMPLE.')
    updated = urlunsplit((start.scheme, start.netloc,
                         f'/api/Druid/{parts[2]}/{quote(name, safe="")}/{action}/GenericIntegration', '', ''))
    validate_urls(updated, poll_url)
    return updated, poll_url, {'botId': bot, 'integrationId': action, 'entityName': name,
                              'host': start.netloc, 'association_verified_by_server': False}


def logged_request(session, method, url, directory, filename, *, token, params,
                   payload=None, timeout=30):
    """Un intento HTTP, sin reintentos ni redirects; sin excepciones con tokens."""
    request = requests.Request(method, url, params=params).prepare()
    record = {'started_at_utc': utc_now(), 'method': method,
              'url': request.url, 'params': params,
              'request_headers': {'Accept': 'application/json'},
              'request_body': payload if method == 'POST' else None,
              'http_status': None, 'response_headers': {}, 'body_text': None,
              'body_json': None, 'transport_error': None}
    headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/json'}
    if method == 'POST':
        headers['Content-Type'] = 'application/json'
        record['request_headers']['Content-Type'] = 'application/json'
    start = time.monotonic()
    try:
        response = session.request(method, url, params=params, headers=headers,
                                   **({'json': payload} if method == 'POST' else {}),
                                   timeout=timeout, allow_redirects=False)
        record['http_status'] = response.status_code
        record['response_headers'] = dict(response.headers)
        # No límite de longitud: conserva texto completo, con redacción de secretos.
        try:
            parsed = response.json()
        except ValueError:
            parsed = None
        record['body_text'] = (json.dumps(scrub(parsed, (token,)), ensure_ascii=False)
                               if parsed is not None and scrub(parsed, (token,)) != parsed
                               else scrub(response.text, (token,)))
        record['body_json'] = parsed
    except requests.RequestException as exc:
        # El mensaje de requests puede contener URLs de proxy u otros datos privados.
        record['transport_error'] = {'type': type(exc).__name__}
    record['finished_at_utc'] = utc_now()
    record['seconds'] = round(time.monotonic() - start, 6)
    record = scrub(record, (token,))
    save_json(directory / filename, record)
    return record


def acknowledgement(record):
    if record['transport_error']:
        return None, 'SUBMISSION_OUTCOME_UNKNOWN'
    if not 200 <= record['http_status'] < 300:
        return None, 'START_HTTP_ERROR'
    data = record['body_json']
    if isinstance(data, dict):
        value = data.get('invocationId')
        if isinstance(value, str) and value and value == value.strip():
            return value, 'ACKNOWLEDGED_NOT_VERIFIED'
    else:
        value = data if isinstance(data, str) else (record['body_text'] or '').strip()
        try:
            if isinstance(value, str) and str(UUID(value)).lower() == value.lower():
                return value, 'ACKNOWLEDGED_NOT_VERIFIED'
        except ValueError:
            pass
    return None, 'START_PROTOCOL_UNKNOWN'


def classify(record, expected=EXPECTED, pending_statuses=()):
    """No inventar un sobre DRUID. Las etiquetas pending exigen selección explícita."""
    if record.get('transport_error'):
        return 'TRANSPORT_ERROR'
    code = record['http_status']
    if code == 404:
        return 'HTTP_404_MEANING_UNCONFIRMED'
    if code in (429, 500, 502, 503, 504):
        return 'RETRYABLE_HTTP_ERROR'
    if not 200 <= code < 300:
        return 'FINAL_HTTP_ERROR'
    body = record.get('body_json')
    if body == expected:
        return 'RESULT_RETRIEVED'
    if isinstance(body, dict) and body.get('ResponseBody') == expected:
        return 'RESULT_RETRIEVED_WRAPPED'
    if isinstance(body, dict):
        status = body.get('status')
        if status in ('failed', 'error', 'cancelled', 'canceled') or body.get('error'):
            return 'INTEGRATION_ERROR_REPORTED'
        if isinstance(status, str) and status in pending_statuses:
            return 'PENDING_STATUS_EXPLICITLY_CONFIGURED'
    if code == 202:
        return 'HTTP_202_ACCEPTED_RESULT_NOT_PROVEN'
    return 'SUCCESS_HTTP_UNKNOWN_BODY'


def validate_limits(timeout, interval, http_timeout):
    if not all(math.isfinite(v) and v > 0 for v in (timeout, interval, http_timeout)):
        raise ValueError('Los tiempos deben ser positivos y finitos.')
    if timeout > 3600 or interval < 1 or http_timeout > 120:
        raise ValueError('Límites de diagnóstico: espera <=3600 s, intervalo >=1 s, timeout HTTP <=120 s.')
    if math.ceil(timeout / interval) > 60:
        raise ValueError('Máximo 60 consultas por observación; aumenta el intervalo.')


def poll_result(directory, token, *, timeout=120, interval=10, http_timeout=30,
                continue_404=False, pending_statuses=(), session=None,
                clock=time.monotonic, sleep=time.sleep):
    validate_limits(timeout, interval, http_timeout)
    directory = Path(directory)
    state_path = directory / 'estado.json'
    state = json.loads(state_path.read_text(encoding='utf8'))
    if not state.get('invocationId'):
        raise ValueError('No existe invocationId recuperable. No se repetirá el POST.')
    endpoints(state['start_url'], state['poll_url'], simple=True)
    if state.get('status') in ('RESULT_RETRIEVED', 'RESULT_RETRIEVED_WRAPPED'):
        return state
    session = session or requests.Session()
    deadline = clock() + timeout
    maximum_attempts = math.ceil(timeout / interval) + 1
    observed = []
    expected = state.get('expected', EXPECTED)
    for _ in range(maximum_attempts):
        remaining = deadline - clock()
        if remaining <= 0:
            break
        state['queries'] = state.get('queries', 0) + 1
        record = logged_request(session, 'GET', state['poll_url'], directory,
            f"poll_{state['queries']:04d}.json", token=token,
            params={'invocationId': state['invocationId'], 'responseContentType': 'application/json'},
            timeout=min(http_timeout, remaining))
        category = classify(record, expected, pending_statuses)
        observed.append(category)
        state.update(status=category, last_poll_at_utc=record['finished_at_utc'])
        save_json(state_path, state)
        if category in ('RESULT_RETRIEVED', 'RESULT_RETRIEVED_WRAPPED'):
            save_json(directory / 'resultado.json', record['body_json'])
            return state
        if category in ('FINAL_HTTP_ERROR', 'INTEGRATION_ERROR_REPORTED', 'SUCCESS_HTTP_UNKNOWN_BODY'):
            return state
        if category == 'HTTP_404_MEANING_UNCONFIRMED' and not continue_404:
            return state
        # 404 / 202 continúan solo como observaciones, nunca como prueba de running.
        remaining = deadline - clock()
        if remaining > 0:
            sleep(min(interval, remaining))
    state.update(status='POLLING_TIMEOUT', observation_categories=sorted(set(observed)),
                 stopped_at_utc=utc_now(), server_job_status='UNKNOWN')
    save_json(state_path, state)
    return state


def compare(start_url, poll_url, token, directory, *, timeout=120, interval=10,
            http_timeout=30, continue_404=False, pending_statuses=(), response_shape='flat',
            session=None, clock=time.monotonic, sleep=time.sleep):
    """Un POST síncrono y, solo si coincide, otro asíncrono. Mismo payload."""
    validate_limits(timeout, interval, http_timeout)
    start_url, poll_url, identity = endpoints(start_url, poll_url, simple=True)
    if not token:
        raise ValueError('Falta el token de Webhooks ya configurado; no se cambia la autenticación.')
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    state_path = directory / 'estado.json'
    if state_path.exists():
        raise ValueError('Ya hay una prueba en esta carpeta. Usa resume; nunca repitas los POST.')
    expected = EXPECTED if response_shape == 'flat' else {'result': EXPECTED}
    correlation = str(uuid4())
    payload = {'test': 'TEST_ASYNC_SIMPLE', 'diagnosticCorrelationId': correlation}
    state = {**identity, 'created_at_utc': utc_now(), 'start_url': start_url,
             'poll_url': poll_url, 'diagnosticCorrelationId': correlation,
             'expected': expected, 'status': 'SYNC_NOT_SENT', 'queries': 0,
             'invocationId': None, 'payload': payload}
    save_json(state_path, state)
    session = session or requests.Session()
    sync = logged_request(session, 'POST', start_url, directory, 'sync.json', token=token,
        params={'asyncResponse': 'false', 'responseContentType': 'application/json'},
        payload=payload, timeout=http_timeout)
    sync_category = classify(sync, expected)
    state['sync_classification'] = sync_category
    if sync_category not in ('RESULT_RETRIEVED', 'RESULT_RETRIEVED_WRAPPED'):
        state['status'] = 'SYNC_CONTROL_FAILED_ASYNC_NOT_SENT'
        save_json(state_path, state)
        return state
    state['association_verified_by_server'] = True  # Exact fixed response from selected route.
    state['status'] = 'ASYNC_SUBMISSION_INTENT_SAVED'
    save_json(state_path, state)
    ack = logged_request(session, 'POST', start_url, directory, 'async_start.json', token=token,
        params={'asyncResponse': 'true', 'responseContentType': 'application/json'},
        payload=payload, timeout=http_timeout)
    state['invocationId'], state['status'] = acknowledgement(ack)
    state['ack_received_at_utc'] = ack['finished_at_utc']
    save_json(state_path, state)
    if not state['invocationId']:
        return state
    return poll_result(directory, token, timeout=timeout, interval=interval,
                       http_timeout=http_timeout, continue_404=continue_404,
                       pending_statuses=pending_statuses, session=session, clock=clock, sleep=sleep)


def audit(directory, configured_start, configured_poll, token_present):
    """Solo archivos locales. No se infieren horas HTTP desde el nombre del directorio."""
    runs = []
    for folder in sorted((ROOT / 'resumenes').glob('*PRUEBA-DRUID-ASYNC*')):
        item = {'directory': str(folder.resolve()), 'event_utc': None,
                'time_note': 'Los registros antiguos no contienen fecha/hora UTC del request.'}
        for name in ('inicio.json', 'invocacion.json', 'diagnostico_sincrono.json'):
            file = folder / name
            if file.exists():
                item[name] = scrub(json.loads(file.read_text(encoding='utf8')))
        polls = [scrub(json.loads(p.read_text(encoding='utf8')))
                 for p in sorted(folder.glob('consulta_*.json'))]
        item['poll_count'] = len(polls)
        item['http_statuses'] = sorted(set(p['http_status'] for p in polls))
        item['first_poll'] = polls[0] if polls else None
        item['last_poll'] = polls[-1] if polls else None
        # Prueba text/plain ya archivada: se reutiliza, no se repite.
        file = folder / 'diagnostico_para_druid.json'
        if file.exists():
            old = json.loads(file.read_text(encoding='utf8'))
            item['archived_text_plain_poll'] = scrub(old.get('async_plain_text_poll'))
        runs.append(item)
    identity = None
    config_error = None
    try:
        _, _, identity = endpoints(configured_start, configured_poll)
    except ValueError as exc:
        config_error = str(exc)
    result = {'audited_at_utc': utc_now(), 'network_calls_performed': 0,
              'documentation': DOC_URL, 'runs': runs,
              'configuration': {'start_url': configured_start if not config_error else '[INVALID]',
                                'poll_url': configured_poll if not config_error else '[INVALID]',
                                'token_present': bool(token_present), 'identity': identity,
                                'error': config_error},
              'summary': {'archived_acknowledgements': sum('inicio.json' in r for r in runs),
                          'archived_poll_requests': sum(r['poll_count'] for r in runs),
                          'fixed_integration_test': 'NOT_EXECUTED_REQUIRES_PUBLISHED_INTEGRATION_ID',
                          'server_cause': 'PENDING_VERIFICATION',
                          'connector_log_absence': 'REPORTED_BY_USER_NOT_INDEPENDENTLY_VERIFIED'}}
    save_json(directory / 'auditoria_existente.json', result)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('audit', 'prepare', 'compare', 'resume'), nargs='?', default='audit')
    parser.add_argument('--integration-id', help='ID real de la nueva acción publicada, nunca el clon GPT.')
    parser.add_argument('--entity', help='Entidad real de TEST_ASYNC_SIMPLE; por defecto la configurada (GPT).')
    parser.add_argument('--directory', type=Path, help='Carpeta de salida o carpeta a reanudar.')
    parser.add_argument('--start-url', help='URL exacta copiada de Webhooks; no se adivina otro host.')
    parser.add_argument('--poll-url', help='URL exacta copiada del mismo bot y host.')
    parser.add_argument('--timeout', type=float, default=120)
    parser.add_argument('--interval', type=float, default=10)
    parser.add_argument('--http-timeout', type=float, default=30)
    parser.add_argument('--observe-404', action='store_true',
                        help='Seguir observando 404 hasta el límite, sin llamarlo pending.')
    parser.add_argument('--verified-pending-status', action='append', default=[],
                        help='Valor exacto de status confirmado por DRUID; no asumirlo sin evidencia.')
    parser.add_argument('--response-shape', choices=('flat', 'nested'), default='flat')
    args = parser.parse_args(argv)
    validate_limits(args.timeout, args.interval, args.http_timeout)
    configured_start, configured_poll, token = load_configuration()
    start = args.start_url or configured_start
    poll = args.poll_url or configured_poll
    directory = args.directory or new_directory('DIAGNOSTICO-DRUID-ASYNC')
    if args.command == 'audit':
        directory.mkdir(parents=True, exist_ok=True)
        result = audit(directory, start, poll, bool(token))
        print(json.dumps(result['summary'], ensure_ascii=False))
    elif args.command == 'prepare':
        directory.mkdir(parents=True, exist_ok=True)
        urls = None
        if args.integration_id:
            u, v, identity = endpoints(start, poll, args.integration_id, args.entity, simple=True)
            urls = {'start_url': u, 'poll_url': v, **identity}
        save_json(directory / 'plan_sin_red.json', {
            'prepared_at_utc': utc_now(), 'network_calls_performed': 0, 'urls': urls,
            'expected': EXPECTED, 'maximum_polling_seconds': args.timeout,
            'required_manual_step': 'Crear y publicar TEST_ASYNC_SIMPLE; proporcionar su ID real.',
            'druid_configuration': 'docs/druid_async_simple_setup.md'})
    elif args.command == 'resume':
        if args.directory is None:
            parser.error('resume requiere --directory con estado.json; nunca hace POST.')
        saved = json.loads((directory / 'estado.json').read_text(encoding='utf8'))
        endpoints(saved['start_url'], saved['poll_url'], simple=True)
        if not token:
            raise ValueError('Falta el token de Webhooks configurado.')
        result = poll_result(directory, token, timeout=args.timeout, interval=args.interval,
                             http_timeout=args.http_timeout, continue_404=args.observe_404,
                             pending_statuses=args.verified_pending_status)
        print(result['status'])
    else:
        if not args.integration_id:
            parser.error('compare requiere --integration-id REAL. No se enviará nada al clon GPT.')
        start, poll, _ = endpoints(start, poll, args.integration_id, args.entity, simple=True)
        result = compare(start, poll, token, directory, timeout=args.timeout,
                         interval=args.interval, http_timeout=args.http_timeout,
                         continue_404=args.observe_404, pending_statuses=args.verified_pending_status,
                         response_shape=args.response_shape)
        print(result['status'])
    print(f'Diagnóstico: {directory}')
    if args.command in ('compare', 'resume'):
        return 0 if result['status'] in ('RESULT_RETRIEVED', 'RESULT_RETRIEVED_WRAPPED') else 2
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except ValueError as exc:
        # Los validadores de este módulo no interpolan credenciales en mensajes.
        print(f'Configuración/protocolo no válido: {exc}')
        raise SystemExit(2)
    except (OSError, KeyError, RuntimeError) as exc:
        # Valores no confiables o errores de red no se imprimen completos.
        print(f'Diagnóstico detenido ({type(exc).__name__}). Revisa los archivos de la prueba y su configuración.')
        raise SystemExit(2)
