"""Durable, bounded agent work. A failed HTTP request never counts as progress."""
from dataclasses import replace, asdict
from pathlib import Path
import hashlib
import json
import re
import time


VERSION = 1


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     default=str).encode()).hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


def retryable(exc):
    # Do not split authentication, permission, configuration or arbitrary failures.
    return getattr(exc, 'status_code', None) in (504,) or getattr(exc, 'timed_out', False)


def slices(text, size, overlap=500):
    """Half-open character spans; every input character belongs to at least one span."""
    if size < 1000:
        raise ValueError('El tamaño de entrega debe ser al menos 1000 caracteres')
    overlap = min(overlap, size // 10)
    start = 0
    while start < len(text):
        end = min(len(text), start + size)
        if end < len(text):
            boundary = text.rfind('\n', start + size // 2, end)
            if boundary > start:
                end = boundary + 1
        yield start, end
        if end == len(text):
            break
        start = end - overlap


def split_documents(documents, size):
    result = []
    for doc in documents:
        if not doc.text:
            continue
        for start, end in slices(doc.text, size):
            pages = list(re.finditer(r'\[Pagina PDF \d+\]', doc.text[:start]))
            page_context = pages[-1].group() + '\n' if pages else ''
            source = f'{doc.ref.source}; caracteres {start}:{end} de {len(doc.text)}'
            result.append([replace(doc, ref=replace(doc.ref, source=source),
                                   text=page_context + doc.text[start:end])])
    return result


def merge_outputs(outputs):
    """Only identical registry rows (including their source) can be deduplicated."""
    seen = set()
    removed = 0
    blocks = []
    for index, output in enumerate(outputs, 1):
        registry = False
        lines = []
        for line in output.splitlines():
            cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
            if len(cells) == 3 and [s.lower() for s in cells] == ['materia', 'requisito completo', 'fuente']:
                registry = True
            elif registry and not line.lstrip().startswith('|'):
                registry = False
            elif registry and len(cells) == 3 and all(cells) and not all(re.fullmatch(r'[: -]+', s) for s in cells):
                key = tuple(cells)
                if key in seen:
                    removed += 1
                    continue
                seen.add(key)
            lines.append(line)
        blocks.append(f'## Entrega {index}\n\n' + '\n'.join(lines))
    return '\n\n'.join(blocks), removed


def run_deliveries(documents, invoke, directory, signature, *, size=50000,
                   minimum=6000, validate=None, consolidate=None):
    """invoke(batch, partial, previous) must return a complete response or raise.

    Successful leaves are preserved verbatim. Consolidation is an additional view,
    never a replacement of those leaves (except the intentionally brief A1).
    """
    if minimum < 1000 or size < minimum * 2:
        raise ValueError('DELIVERY_CHARS debe ser >= 2 * DELIVERY_MIN_CHARS (mínimo 1000)')
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    identity = digest({'version': VERSION, 'signature': signature, 'size': size,
                       'minimum': minimum, 'documents': [asdict(d) for d in documents]})
    manifest = directory / 'plan.json'
    if manifest.exists():
        state = json.loads(manifest.read_text(encoding='utf-8'))
        if state['identity'] != identity:
            raise ValueError('Los documentos, instrucciones o configuración han cambiado. '
                             'Inicia una ejecución nueva; no se mezclarán entregas anteriores.')
    else:
        state = {'identity': identity, 'estado': 'pendiente', 'version': VERSION,
                 'documentos': [{'nombre': d.ref.name, 'caracteres': len(d.text),
                                 'sha256': digest(d.text)} for d in documents]}
        save(manifest, state)

    def work(batch, key, partial, previous='', depth=0):
        target = directory / (key + '.json')
        request_hash = digest({'documents': [asdict(d) for d in batch], 'previous': previous,
                               'partial': partial, 'identity': identity})
        if target.exists():
            record = json.loads(target.read_text(encoding='utf-8'))
            if record['request_hash'] != request_hash:
                raise ValueError('El contexto de una entrega guardada ha cambiado')
            if record['estado'] == 'completada':
                print(f'  Entrega {key}: recuperada del disco', flush=True)
                return [record['respuesta']]
            split = record['estado'] == 'dividida'
        else:
            split = False
        record = {'request_hash': request_hash, 'estado': 'pendiente',
                  'fuentes': [{'nombre': d.ref.name, 'origen': d.ref.source,
                               'caracteres': len(d.text)} for d in batch]}
        length = max((len(d.text) for d in batch), default=0)
        terminal = depth >= 8 or (len(batch) == 1 and length <= minimum)
        if not split:
            save(target, record)
            print(f'  Entrega {key}: {sum(len(d.text) for d in batch)} caracteres', flush=True)
            try:
                # At the smallest leaf a transient gateway timeout must not
                # immediately discard the run. Keep retries bounded and retain
                # exactly the same context, including on a resumed run.
                for attempt in range(3 if terminal else 1):
                    try:
                        result = invoke(batch, partial, previous)
                        break
                    except Exception as exc:
                        if not retryable(exc) or not terminal or attempt == 2:
                            raise
                        delay = 5 * (attempt + 1)
                        record.update(estado='reintentando', intentos=attempt + 1,
                                      error_tipo=type(exc).__name__)
                        save(target, record)
                        print(f'  Entrega {key}: timeout; reintento {attempt + 2}/3 '
                              f'en {delay} segundos', flush=True)
                        time.sleep(delay)
                if not isinstance(result, str) or not result.strip():
                    raise RuntimeError(f"{signature.get('agent', 'Agente')}: entrega vacía; no se guarda como completada")
                if validate:
                    validate(result)
                record.update(estado='completada', respuesta=result)
                save(target, record)
                return [result]
            except Exception as exc:
                record.update(estado='fallida', error_tipo=type(exc).__name__)
                save(target, record)
                if not retryable(exc):
                    raise
        if terminal:
            raise RuntimeError(f'La entrega {key} sigue agotando el tiempo con el tamaño mínimo. '
                               f'Progreso conservado en {directory}; revisa Druid y usa --reanudar.')
        new_size = max(minimum, min(size, length // 2))
        children = split_documents(batch, new_size)
        record.update(estado='dividida', partes=len(children))
        save(target, record)
        outputs = []
        for index, child in enumerate(children, 1):
            context = outputs[-1][-2500:] if outputs else previous
            outputs.extend(work(child, f'{key}.{index}', True, context, depth + 1))
        return outputs

    total = sum(len(d.text) for d in documents)
    batches = split_documents(documents, size) if total > size else [documents]
    outputs = []
    for index, batch in enumerate(batches, 1):
        previous = outputs[-1][-2500:] if outputs else ''
        outputs.extend(work(batch, f'entrega_{index:04d}', len(batches) > 1, previous))
    if not outputs:
        raise ValueError('No hay texto para procesar')
    combined, duplicates = (outputs[0], 0) if len(outputs) == 1 else merge_outputs(outputs)
    if consolidate and len(outputs) > 1:
        def synthesize(group, final, depth=0):
            key = digest({'identity': identity, 'group': group, 'final': final})
            path = directory / ('sintesis_' + key + '.json')
            stored = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
            if stored.get('respuesta'):
                return stored['respuesta']
            try:
                value = consolidate(group, final)
                if not value.strip():
                    raise ValueError('Síntesis vacía')
            except Exception as exc:
                save(path, {'key': key, 'estado': 'fallida', 'error_tipo': type(exc).__name__})
                if not retryable(exc) or depth >= 8 or len(group) <= minimum:
                    raise
                halves = [group[a:b] for a, b in slices(group, max(1000, len(group) // 2), overlap=0)]
                partials = [synthesize(part, False, depth + 1) for part in halves]
                merged = '\n\n'.join(partials)
                if len(merged) >= len(group):
                    raise RuntimeError('La síntesis no reduce el contexto tras timeout; progreso guardado') from exc
                value = synthesize(merged, final, depth + 1)
            save(path, {'key': key, 'estado': 'completada', 'respuesta': value})
            return value

        # Bounded reduction with durable checkpoints, including the final synthesis.
        nodes = list(outputs)
        for level in range(10):
            text = '\n\n'.join(nodes)
            groups = [text[a:b] for a, b in slices(text, size, overlap=0)]
            reduced = []
            for index, group in enumerate(groups):
                value = synthesize(group, len(groups) == 1)
                reduced.append(value)
            if len(groups) == 1:
                combined = consolidate_result(reduced[0], combined, signature.get('agent') == 'A1')
                break
            if sum(map(len, reduced)) >= len(text):
                raise RuntimeError('La síntesis no reduce el contexto; entregas conservadas para reanudar')
            nodes = reduced
        else:
            raise RuntimeError('No se pudo consolidar dentro del límite; entregas conservadas')
    state.update(estado='completada', entregas_completadas=len(outputs),
                 filas_duplicadas_exactas=duplicates,
                 alcance='Cobertura de texto procesado; no certifica exhaustividad semántica')
    save(manifest, state)
    save(directory / 'resultado.json', {'identity': identity, 'respuesta': combined})
    return combined


def consolidate_result(summary, combined, brief):
    return summary if brief else '# Síntesis global\n\n' + summary + '\n\n# Entregas conservadas\n\n' + combined
