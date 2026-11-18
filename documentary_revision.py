"""Aplicación explícita de una revisión contrastada a sus documentos originales.

No se selecciona por nombre de licitación ni se inyectan datos entre expedientes.
La revisión se selecciona por CLI o por coincidencia exacta en el catálogo local;
en ambos casos exige coincidencia de los PDF mediante SHA-256.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

from presales_coverage import documentary_requirements


def apply_documentary_revision(payload, revision):
    if (revision.get('schema') != 'oportunidades.revision_preventa.v1'
            or revision.get('identificador_interno') != payload.get('expediente')):
        raise ValueError('La revisión documental no corresponde al expediente de entrada')
    documents = revision.get('documentos', [])
    if not documents:
        raise ValueError('La revisión no identifica documentos contrastados')
    sources = {item['nombre']: item for item in payload.get('documentos_fuente', [])}
    for document in documents:
        source = sources.get(document.get('nombre'))
        if not source:
            raise ValueError('Falta una fuente de la revisión: ' + str(document.get('nombre')))
        path = Path(source.get('ruta_local') or source.get('url', ''))
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != document.get('sha256'):
            raise ValueError('La fuente no coincide con el PDF revisado: ' + document['nombre'])
    records = documentary_requirements(revision)
    if not records:
        raise ValueError('La revisión no contiene requisitos documentales')
    agents = {agent.get('id') for agent in payload.get('agentes', [])}
    if any(record.get('agente_responsable') not in agents for record in records):
        raise ValueError('La revisión asigna un requisito a un agente no presente')
    result = deepcopy(payload)
    result['requisitos_documentales'] = deepcopy(records)
    result['revision_preventa'] = {key: deepcopy(value) for key, value in revision.items()
                                  if key != 'requisitos_documentales'}
    result['revision_preventa']['nota'] = (
        'Contenido corregido mediante revisión local de fuentes, no respuesta automática original. '
        'La extracción automática previa se conserva separada en los diagnósticos de esta ejecución. '
        'Esta revisión cubre las observaciones identificadas, no acredita exhaustividad de todo el expediente.')
    result['expediente_administrativo'] = revision.get('expediente_administrativo', '')
    from oportunidades import markdown_report_to_json
    for agent in result['agentes']:
        own = [record for record in records if record['agente_responsable'] == agent.get('id')]
        if not own:
            if agent.get('id') == 'A1':
                agent['contenido'] = markdown_report_to_json(records[0]['detalle'])
                agent['estado'] = 'revisado_documentalmente'
                agent['origen_contenido'] = 'revision_local_con_fuentes_y_huellas_sha256'
            continue
        text = '\n\n'.join('## ' + record.get('titulo', record['seccion']) + '\n' +
                           record['detalle'] + '\n[' + record['fuente'] + ']' for record in own)
        agent['contenido'] = markdown_report_to_json(text)
        agent['contenido']['requisitos_documentales'] = deepcopy(own)
        agent['estado'] = 'revisado_documentalmente'
        agent['origen_contenido'] = 'revision_local_con_fuentes_y_huellas_sha256'
        agent.pop('puntos_revision', None)
    return result


def matching_documentary_revision(payload, catalog):
    """Reutiliza conocimiento contrastado solo en la misma edición de los PDF."""
    matches = []
    for path in sorted(Path(catalog).glob('*.json')):
        revision = json.loads(path.read_text(encoding='utf-8-sig'))
        if revision.get('identificador_interno') != payload.get('expediente'):
            continue
        try:
            apply_documentary_revision(payload, revision)
        except ValueError:
            continue
        matches.append((path, revision))
    if len(matches) > 1:
        raise ValueError('Varias revisiones coinciden con los documentos: selecciona una explícitamente')
    return matches[0] if matches else None


def save_documentary_revision(original, revision, directory):
    """Preserva respuesta automática y publica por separado JSON corregidos."""
    from oportunidades import safe_filename
    corrected = apply_documentary_revision(original, revision)
    directory = Path(directory)
    archive = directory/'diagnosticos'/'extraccion_automatica_sin_revisar.json'
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_text(json.dumps(original, ensure_ascii=False, indent=2), encoding='utf-8')
    (directory/f'{safe_filename(corrected["expediente"])}_capa1.json').write_text(
        json.dumps(corrected, ensure_ascii=False, indent=2), encoding='utf-8')
    folder = directory/'agentes'
    folder.mkdir(exist_ok=True)
    # Reemplazar también los ficheros individuales con nombre histórico cuando
    # existen; no dejar dos respuestas distintas del mismo agente en agentes/.
    for agent in corrected['agentes']:
        paths = []
        for candidate in folder.glob('*.json'):
            data = json.loads(candidate.read_text(encoding='utf-8'))
            if data.get('id') == agent['id']:
                paths.append(candidate)
        for path in paths or [folder/f'{agent["id"]}_respuesta.json']:
            path.write_text(json.dumps(agent, ensure_ascii=False, indent=2), encoding='utf-8')
    return corrected
