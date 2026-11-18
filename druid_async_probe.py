"""Prueba aislada de GenericIntegration; no modifica el transporte del programa.

El contrato final esperado es ResponseBody={"DataSource": <resultado GPT>}.
Los sobres/estados reales del tenant deben verificarse con una primera prueba.
"""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import time
from urllib.parse import urlsplit
from uuid import UUID, uuid4

import requests


class AsyncProtocolError(RuntimeError):
    pass


def save_json(path, value):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


def validate_urls(start_url, poll_url):
    start, poll = urlsplit(start_url), urlsplit(poll_url)
    if any(u.scheme != 'https' or not u.netloc or u.username or u.password or u.query or u.fragment
           or '{' in u.path or '}' in u.path for u in (start, poll)):
        raise ValueError('Configura URLs HTTPS completas, sin marcadores, credenciales ni query.')
    if not start.path.endswith('/GenericIntegration') or not poll.path.endswith('/GetGenericIntegrationResponse'):
        raise ValueError('Se requieren GenericIntegration y GetGenericIntegrationResponse.')
    if (start.netloc.lower() != poll.netloc.lower()
            or start.path.rsplit('/', 3)[0] != poll.path.rsplit('/', 1)[0]):
        raise ValueError('Las dos URLs deben corresponder al mismo host y bot de Druid.')


def response_body(data):
    if isinstance(data, dict) and 'ResponseBody' in data:
        data = data['ResponseBody']
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except ValueError as exc:
            raise AsyncProtocolError('Respuesta de webhook no JSON; consulta el diagnóstico.') from exc
    return data


def invocation_id(data, http_status):
    """El tenant devuelve un GUID plano; otros devuelven invocationId en JSON."""
    if not 200 <= http_status < 300:
        raise AsyncProtocolError(f'El inicio devolvió HTTP {http_status}; consulta inicio.json.')
    if isinstance(data, str):
        value = data.strip()
        try:
            data = json.loads(value)
        except ValueError:
            # Solo aceptar un GUID completo, no cualquier texto de una página/error.
            try:
                parsed = UUID(value)
                if str(parsed).lower() == value.lower():
                    return value
            except ValueError:
                pass
            raise AsyncProtocolError('Acuse de inicio desconocido; consulta inicio.json antes de repetir.')
        if isinstance(data, str):
            try:
                if str(UUID(data)).lower() == data.lower():
                    return data
            except ValueError:
                pass
    if isinstance(data, dict) and isinstance(data.get('invocationId'), str) and data['invocationId'].strip():
        return data['invocationId'].strip()
    raise AsyncProtocolError('No se ha recibido invocationId válido. Revisa inicio.json y el log '
                             'de Druid antes de repetir: la ejecución podría haber comenzado.')


def classify_result(data, http_status):
    body = response_body(data)
    if isinstance(body, dict) and isinstance(body.get('DataSource'), dict):
        result = body['DataSource']
        # Una entidad vacía o el eco del prompt no es una finalización válida.
        if not any(result.get(k) is not None for k in ('finish_reason', 'responseJSON', 'response_tool_calls', 'ChatResponse')):
            raise AsyncProtocolError('DataSource no contiene el resultado GPT.')
        return body
    if isinstance(body, dict):
        status = str(body.get('status', '')).lower()
        if status in ('failed', 'error', 'cancelled', 'canceled') or body.get('error'):
            raise AsyncProtocolError('Druid indica fallo de la integración; consulta el diagnóstico.')
        if status in ('pending', 'running', 'queued', 'in_progress', 'processing'):
            return None
    if http_status == 202:
        return None
    raise AsyncProtocolError('Sobre/estado de consulta desconocido: se ha archivado sin asumir éxito. '
                             'Hay que contrastarlo con una respuesta real del tenant.')


def request_logged(session, method, url, directory, filename, **kwargs):
    # No se guardan cabeceras de petición ni objetos Request con el token.
    started = time.monotonic()
    response = session.request(method, url, **kwargs)
    try:
        body = response.json()
    except ValueError:
        body = response.text
    save_json(directory / filename, {'http_status': response.status_code,
              'seconds': round(time.monotonic() - started, 3), 'body': body})
    return response.status_code, body


def probe(start_url, poll_url, token, payload, directory, *, resume=False,
          total_timeout=900, poll_interval=10, http_timeout=45, session=None,
          clock=time.monotonic, sleep=time.sleep, missing_response_grace=60):
    validate_urls(start_url, poll_url)
    if not token.strip():
        raise ValueError('Falta DRUID_WEBHOOK_TOKEN: token de Webhooks, no el login habitual.')
    if min(total_timeout, poll_interval, http_timeout) <= 0:
        raise ValueError('Los intervalos y límites deben ser mayores que cero.')
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    state_path = directory / 'invocacion.json'
    headers = {'Authorization': 'Bearer ' + token.strip(), 'Accept': 'application/json'}
    session = session or requests.Session()
    if resume:
        if state_path.exists():
            state = json.loads(state_path.read_text(encoding='utf-8'))
        else:
            # Recuperar acuses archivados por versiones que solo aceptaban JSON.
            # No se efectúa ningún POST: el ID ya lo emitió Druid.
            ack = json.loads((directory / 'inicio.json').read_text(encoding='utf-8'))
            state = {'invocationId': invocation_id(ack['body'], ack['http_status']),
                     'start_url': start_url, 'poll_url': poll_url,
                     'status': 'pending', 'queries': 0, 'recovered_from_ack': True}
            save_json(state_path, state)
        if state.get('poll_url') != poll_url or state.get('start_url') != start_url:
            raise ValueError('La invocación pertenece a otras URLs; no se inicia otra ejecución.')
    else:
        if state_path.exists() or (directory / 'inicio.json').exists():
            raise ValueError('La carpeta ya tiene un intento de inicio. Usa --reanudar.')
        if not isinstance(payload, dict) or not isinstance(payload.get('Messages'), dict):
            raise ValueError('La entrada debe ser la entidad GPT con Messages, no el sobre PerformOperations.')
        save_json(directory / 'entrada.json', payload)
        # No reintentar automáticamente un POST: si se pierde el acuse, el job
        # podría estar creado. Evitamos duplicar llamadas/cargos al modelo.
        status, body = request_logged(session, 'POST', start_url, directory, 'inicio.json',
            params={'asyncResponse': 'true', 'responseContentType': 'application/json'},
            headers={**headers, 'Content-Type': 'application/json'}, json=payload, timeout=http_timeout)
        state = {'invocationId': invocation_id(body, status), 'start_url': start_url, 'poll_url': poll_url,
                 'status': 'pending', 'queries': 0}
        save_json(state_path, state)
    if state.get('status') == 'completed':
        return directory / 'resultado.json'
    deadline = clock() + total_timeout
    missing_since = None
    while clock() < deadline:
        state['queries'] += 1
        save_json(state_path, state)
        try:
            status, body = request_logged(session, 'GET', poll_url, directory,
                f"consulta_{state['queries']:04d}.json", params={'invocationId': state['invocationId'],
                'responseContentType': 'application/json'}, headers=headers,
                timeout=min(http_timeout, max(0.1, deadline - clock())))
        except (requests.Timeout, requests.ConnectionError):
            print('Consulta interrumpida; se consultará la MISMA invocación.', flush=True)
        else:
            if (status == 404 and isinstance(body, str)
                    and body.strip() == f"No response found for invocationId {state['invocationId']}"):
                # No acredita un job pendiente: solo concede un margen acotado
                # a la disponibilidad del resultado, sin ocultar otros 404.
                now = clock()
                if missing_since is None:
                    missing_since = now
                if now - missing_since >= missing_response_grace:
                    raise AsyncProtocolError('Druid sigue sin devolver resultado para la invocación '
                        f"{state['invocationId']} tras el margen inicial de {missing_response_grace}s. "
                        'Esto no confirma que siga en ejecución. Revisa Connector audit log de la copia '
                        'y los campos RequestBody/ResponseBody de GPT; no se ha repetido el POST. '
                        f'Diagnóstico: {directory}')
                print('Druid aún no encuentra el resultado; se consultará de nuevo durante '
                      'un margen limitado, sin relanzar la integración.', flush=True)
            elif status not in (429, 500, 502, 503, 504):
                if not 200 <= status < 300:
                    raise AsyncProtocolError(f'La consulta devolvió HTTP {status}. Se conserva invocationId.')
                missing_since = None
                result = classify_result(body, status)
                if result is not None:
                    # Reutiliza el rechazo de finish_reason=length y sobres truncados.
                    from oportunidades import extract_druid_response_text
                    text = extract_druid_response_text(result)
                    save_json(directory / 'resultado.json', result)
                    (directory / 'respuesta.md').write_text(text, encoding='utf-8')
                    state['status'] = 'completed'
                    save_json(state_path, state)
                    return directory / 'resultado.json'
        remaining = deadline - clock()
        if remaining > 0:
            sleep(min(poll_interval, remaining))
    raise TimeoutError('Se agotó la espera local. No se cancela ni relanza el trabajo de Druid. '
                       f'Puedes consultar de nuevo con --reanudar "{directory}".')


def main():
    from oportunidades import ROOT, load_env_file
    load_env_file(ROOT / '.env')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entrada', type=Path, help='Entidad GPT JSON. Si se omite, prueba mínima.')
    parser.add_argument('--reanudar', type=Path, help='Carpeta con invocationId ya guardado; no hace POST.')
    parser.add_argument('--preparar', action='store_true', help='Guardar petición sin hacer llamadas.')
    parser.add_argument('--espera', type=float, default=900, help='Espera local máxima en segundos.')
    args = parser.parse_args()
    directory = args.reanudar or (ROOT / 'resumenes' / (datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                + '_PRUEBA-DRUID-ASYNC_' + uuid4().hex[:8]))
    payload = None
    if not args.reanudar:
        if args.entrada:
            payload = json.loads(args.entrada.read_text(encoding='utf-8-sig'))
        else:
            from oportunidades import build_druid_gpt_payload
            payload = build_druid_gpt_payload('Responde exclusivamente PRUEBA_ASYNC_OK.',
                'Prueba de transporte asíncrono, sin documentos ni análisis de licitación.',
                {'tenant_id': '0', 'bot_id': '', 'operation_id': '', 'timeout_seconds': '180'})['Payload']
    if args.preparar:
        if args.reanudar:
            parser.error('--preparar no se combina con --reanudar')
        directory.mkdir(parents=True, exist_ok=False)
        save_json(directory / 'entrada.json', payload)
        print(f'Petición preparada sin conexión: {directory / "entrada.json"}')
        return
    result = probe(os.getenv('DRUID_ASYNC_START_URL', '').strip(), os.getenv('DRUID_ASYNC_POLL_URL', '').strip(),
                   os.getenv('DRUID_WEBHOOK_TOKEN', ''), payload, directory,
                   resume=bool(args.reanudar), total_timeout=args.espera)
    print(f'Respuesta completa recibida: {result}')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, RuntimeError, TimeoutError, OSError, requests.RequestException) as exc:
        # Un requests.HTTPError podría contener URL o detalles internos: no headers.
        print(f'Prueba asíncrona detenida ({type(exc).__name__}): {exc}')
        raise SystemExit(1)
