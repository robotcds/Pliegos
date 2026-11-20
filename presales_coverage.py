"""Registro documental y conservación literal de requisitos en el informe legible.

No valida por sí solo que una extracción sea correcta o exhaustiva. Impide perder
hechos ya registrados al redactar, sin usar coincidencias de palabras como prueba.
"""
from copy import deepcopy
import re
import unicodedata


def normalized(value):
    value = unicodedata.normalize('NFKC', str(value)).replace('**', '')
    for original, rendered in [('‑', '-'), ('‐', '-'), ('–', '-'), ('—', '-'),
                               ('≤', '<='), ('≥', '>='), ('≠', '!=')]:
        value = value.replace(original, rendered)
    return re.sub(r'\s+', ' ', value).strip().casefold()


class RegistryFormatError(ValueError):
    """La respuesta está completa pero su registro no puede interpretarse sin adivinar."""


ABSENCE_LABEL = r'(?:[^:;\n]{1,150}:\s*)?'
READING_NOTICE = re.compile(
    r'^' + ABSENCE_LABEL +
    r'(?:NO CONSTA EN LA DOCUMENTACI[ÓO]N REVISADA|NO LOCALIZAD[OA] EN ESTA ENTREGA PARCIAL)\b', re.I)
UNLOCATED_DETAIL = re.compile(r'^' + ABSENCE_LABEL + r'(?:NO CONSTA|NO LOCALIZAD[OA]|PENDIENTE)\b', re.I)


def normalize_registry_rows(rows):
    """Recupera materias omitidas en tablas de registro, nunca fuentes ni hechos.

    Las filas requisito/fuente necesitan una materia previa y una fuente reconocible.
    Un aviso explícito de lectura puede llegar como materia y aviso, con la última
    celda omitida. La fuente queda vacía para conservarlo como diagnóstico.
    """
    if not rows:
        return rows
    names = [normalized(c) for c in rows[0]]
    required = {'materia', 'requisito completo', 'fuente'}
    if not required <= set(names):
        return rows
    if len(names) != 3 or len(set(names)) != 3:
        raise RegistryFormatError('Registro documental con columnas adicionales o repetidas')
    canonical = names == ['materia', 'requisito completo', 'fuente']
    mi, di = names.index('materia'), names.index('requisito completo')
    result, matter = [list(rows[0])], ''
    for index, original in enumerate(rows[1:], 1):
        row = [str(c).strip() for c in original]
        if not any(row):
            continue
        if len(row) == 3 and [normalized(c) for c in row] == names:
            continue  # Cabecera repetida, no un hecho contractual.
        if canonical and len(row) in (1, 3) and row[0] and not any(row[1:]) and re.fullmatch(r'\*\*[^*]+\*\*', row[0]):
            matter = row[0]
            continue  # Encabezado explícito de grupo, conservado en sus filas.
        if canonical and len(row) == 2:
            if row[0] and READING_NOTICE.match(row[1]):
                row.append('')
            else:
                source = row[1]
                identifiable_source = re.search(
                    r'\.(?:pdf|docx?|txt|html?)\b|https?://|\b(?:PCAP|PPT|pliego|anexo)\b|'
                    r'^(?:NO CONSTA|NO LOCALIZAD[OA]|PENDIENTE)', source, re.I)
                if not matter or not row[0] or not source or not identifiable_source:
                    raise RegistryFormatError(f'Fila {index} abreviada sin materia previa o fuente inequívoca')
                row = [matter, row[0], source]
        if len(row) != 3:
            raise RegistryFormatError(f'Fila {index} del registro con {len(row)} celdas; se requieren 3')
        if not row[mi] and row[di] and matter:
            row[mi] = matter
        if row[mi] and row[di]:
            matter = row[mi]
        result.append(row)
    return result


def records_from_sections(sections):
    records = []
    for section in sections:
        for table in section.get('tablas', []):
            columns = {normalized(name): name for name in table.get('columnas', [])}
            if not {'materia', 'requisito completo', 'fuente'} <= columns.keys():
                continue
            for row in table.get('filas', []):
                values = [row.get(columns[name], '').strip()
                          for name in ('materia', 'requisito completo', 'fuente')]
                diagnostic_only = bool(re.match(r'^No se han (?:identificado|detectado|localizado) '
                                                r'(?:discrepancias|contradicciones)\b', values[1], re.I))
                if diagnostic_only and not values[2]:
                    values[2] = 'Declaración no contrastada del extractor; no acredita ausencia de contradicciones en los pliegos.'
                if values[0] and not values[2] and UNLOCATED_DETAIL.match(values[1]):
                    # Una ausencia declarada no tiene por qué tener una cláusula
                    # localizable. No inventarla ni tratarla como exención.
                    values[0] = 'Datos no localizados y límites de lectura'
                    values[2] = 'Declaración de ausencia del extractor; no acredita una exención contractual.'
                    diagnostic_only = True
                if not all(values):
                    raise RegistryFormatError('Registro documental sin materia, requisito o fuente')
                records.append(dict(id=f'R{len(records)+1:04d}', seccion=values[0],
                                    detalle=values[1], fuente=values[2], origen='extraccion_agente',
                                    **({'es_requisito_contractual': False} if diagnostic_only else {})))
    return records


AGENT_MATTERS = {
    'A2': 'Procedimiento, economía y obligaciones', 'A3': 'Solvencia y acreditación',
    'A4': 'Valoración y preparación de la oferta', 'A6': 'Alcance y ejecución del servicio',
    'A8': 'Equipo y continuidad', 'A9': 'Seguridad y protección de datos',
    'A10': 'Medios, licencias y proveedores',
}


def complete_extracted_records(content, agent):
    """Conserva también hechos de tablas/párrafos omitidos del registro del modelo.

    Es normalización de la extracción, no lectura del pliego ni validación semántica.
    No puede recuperar requisitos que el modelo nunca extrajo.
    """
    if agent not in AGENT_MATTERS or not isinstance(content, dict):
        return []
    records = deepcopy(content.get('requisitos_documentales', []))
    if content.get('registro_completo_estructura'):
        return records
    if not content.get('secciones') and content.get('salida_original'):
        from oportunidades import markdown_report_to_json
        content = {**markdown_report_to_json(content['salida_original']), **content}
    known = [normalized(r.get('detalle', '')) for r in records]
    for record in records:
        record.setdefault('agente_responsable', agent)

    def append(detail, source, heading):
        detail = str(detail).strip()
        if not detail or detail in ('---', '--'):
            return
        # En fichas de equipo, una condición idéntica puede corresponder a
        # perfiles diferentes. Conservar su encabezado evita deduplicarlos
        # indebidamente o presentar experiencia/horas sin identificar el perfil.
        if agent == 'A8' and heading and normalized(heading) not in normalized(detail):
            detail = str(heading).strip() + ': ' + detail
        key = normalized(detail)
        if any(key == old for old in known):
            return
        refs = re.findall(r'\[[^\[\]\n]*\.(?:pdf|docx?|xlsx?)\b[^\[\]\n]*\]|'
                          r'\([^()\n]*\.(?:pdf|docx?|xlsx?)\b[^()\n]*\)', detail, re.I)
        source = str(source or (refs[-1].strip('[]()') if refs else '')).strip()
        records.append(dict(id=f'{agent}-S{len(records)+1:04d}',
            seccion=AGENT_MATTERS[agent], titulo=re.sub(r'^\d+[.)]\s*', '', heading),
            detalle=detail, fuente=source or 'Fuente no individualizada en la extracción; pendiente de verificación.',
            agente_responsable=agent, origen='estructura_extraida_sin_validacion_semantica',
            cita_individualizada=bool(source)))
        known.append(key)

    for section in content.get('secciones', []):
        heading = str(section.get('titulo', ''))
        label = normalized(heading)
        # Resumen y trazabilidad repiten los mismos hechos; el registro explícito
        # ya se conserva. No descartar secciones sustantivas por carecer de registro.
        if any(x in label for x in ('registro documental', 'resumen factual',
                                    'documentos revisados', 'trazabilidad', 'fuentes para proyecto')):
            continue
        for text in section.get('parrafos', []) + section.get('elementos', []):
            if re.match(r'^\s*\(?ver (?:tabla|registro|secci[oó]n)', str(text), re.I):
                continue
            append(text, '', heading)
        for table in section.get('tablas', []):
            columns = table.get('columnas', [])
            if {'materia', 'requisito completo', 'fuente'} <= {normalized(c) for c in columns}:
                continue
            for row in table.get('filas', []):
                if not isinstance(row, dict):
                    row = dict(zip(columns, row))
                source_cols = [col for col in columns if normalized(col) in
                               ('fuente', 'documento/apartado', 'documento y apartado/página')]
                source = '; '.join(str(row.get(col, '')) for col in source_cols)
                detail = '; '.join(f'{col}: {row.get(col, "")}' for col in columns
                                   if col not in source_cols)
                append(detail, source, heading)
    return records


def ensure_extracted_records(payload):
    """Contrato común para JSON nuevos y antiguos; no aplica revisiones de un caso."""
    payload = deepcopy(payload)
    if payload.get('revision_preventa'):
        return payload
    controls = []
    for agent in payload.get('agentes', []):
        aid, content = agent.get('id'), agent.get('contenido', {})
        if aid not in AGENT_MATTERS or not isinstance(content, dict):
            continue
        records = complete_extracted_records(content, aid)
        if not records:
            continue
        content['requisitos_documentales'] = records
        content['registro_completo_estructura'] = True
        controls.append(dict(agente=aid, registros=len(records),
            registros_adicionales_desde_estructura=sum(
                r.get('origen') == 'estructura_extraida_sin_validacion_semantica' for r in records),
            alcance='Conservación de hechos extraídos; no certifica exhaustividad ni exactitud.'))
    if controls:
        payload['control_cobertura_agentes'] = controls
    return payload


def documentary_requirements(payload):
    candidates = list(payload.get('requisitos_documentales', []))
    for agent in payload.get('agentes', []):
        content = agent.get('contenido', {})
        if isinstance(content, dict):
            candidates.extend(complete_extracted_records(content, agent.get('id'))
                              if agent.get('id') in AGENT_MATTERS and not payload.get('revision_preventa') else
                              content.get('requisitos_documentales', []))
    records, seen = [], set()
    for record in candidates:
        if (not isinstance(record, dict) or any(not isinstance(record.get(key), str)
                or not record[key].strip() for key in ('seccion', 'detalle', 'fuente'))):
            raise ValueError('Requisito documental inválido: faltan detalle, materia o fuente')
        if record.get('es_requisito_contractual') is False:
            continue
        key = (normalized(record['detalle']), normalized(record['fuente']))
        if key not in seen:
            records.append(record)
            seen.add(key)
    return records


def body_text(report):
    def strings(value):
        if isinstance(value, str):
            yield value
        elif isinstance(value, list):
            for item in value:
                yield from strings(item)
        elif isinstance(value, dict):
            for key, item in value.items():
                if key not in ('titulo', 'tipo'):
                    yield from strings(item)
    return normalized('\n'.join(strings(report.get('secciones', []))))


def integrate_requirements(report, payload):
    """Completa por materias el cuerpo; no oculta omisiones en una conclusión/anexo."""
    report = deepcopy(report)
    # Una revisión explícita puede aportar un cuerpo ya contrastado y redactado.
    # En ese modo el modelo solo redacta la apertura/cierre: no vuelve a condensar
    # ni duplica los párrafos profesionales del registro en otros apartados.
    if payload.get('revision_preventa', {}).get('composicion_editorial') == 'registro_contrastado':
        report['secciones'] = []
        revision = payload['revision_preventa']
        for origin, destination in [('introduccion_editorial', 'introduccion'),
                                    ('conclusion_editorial', 'conclusion')]:
            if origin in revision:
                paragraphs = revision[origin]
                if (not isinstance(paragraphs, list) or not paragraphs
                        or not all(isinstance(value, str) and value.strip() for value in paragraphs)):
                    raise ValueError('Texto editorial contrastado inválido: ' + origin)
                report[destination] = deepcopy(paragraphs)
    for record in documentary_requirements(payload):
        text = body_text(report)
        if normalized(record['detalle']) in text and normalized(record['fuente']) in text:
            continue
        title = record['seccion'].strip()
        subheading = record.get('titulo', '')
        if ': ' in title:
            title, suffix = title.split(': ', 1)
            subheading = subheading or suffix
        section = next((item for item in report['secciones']
                        if normalized(item['titulo']) == normalized(title)), None)
        if section is None:
            section = {'titulo': title, 'bloques': []}
            report['secciones'].append(section)
        if subheading:
            section['bloques'].append({'tipo': 'subtitulo', 'texto': subheading})
        if record.get('tabla'):
            section['bloques'].append(deepcopy(record['tabla']))
        section['bloques'].extend([
            {'tipo': 'parrafo', 'texto': record['detalle']},
            {'tipo': 'parrafo', 'texto': '[' + record['fuente'] + ']'},
        ])
    return report


def requirement_issues(report, payload):
    text = body_text(report)
    return [f"Falta el requisito documental completo: {record.get('id', record['seccion'])}"
            for record in documentary_requirements(payload)
            if normalized(record['detalle']) not in text or normalized(record['fuente']) not in text]


def pdf_literal_span(detail, text):
    """Solo tolera espacios insertados DENTRO de una URL, no cambios de cifras."""
    index = text.find(detail)
    if index >= 0:
        return index, index + len(detail), 'literal'
    parts = re.split(r'(https?://\S+)', detail)
    if len(parts) == 1:
        return -1, -1, ''
    pattern = ''.join(r'\s*'.join(re.escape(c) for c in part)
                      if re.match(r'^https?://', part) else re.escape(part) for part in parts)
    match = re.search(pattern, text)
    return (match.start(), match.end(), 'url_partida_por_maquetacion') if match else (-1, -1, '')


def check_pdf_requirements(report, payload, pdf_path, *, allow_pdf_warnings=False):
    """Comprueba el PDF temporal antes de publicarlo; no solo el borrador JSON."""
    from pypdf import PdfReader
    records = documentary_requirements(payload)
    if not records:
        return None
    reader = PdfReader(pdf_path)
    pages = [normalized(re.sub(r'(?m)^\s*\d+\s*$', '', page.extract_text() or ''))
             for page in reader.pages]
    text = ' '.join(pages)
    body = body_text(report)
    checks, warnings = [], []
    offsets, offset = [], 0
    for number, page in enumerate(pages, 1):
        offsets.append((offset, offset+len(page), number))
        offset += len(page)+1
    for record in records:
        detail, source = normalized(record['detalle']), normalized(record['fuente'])
        index, end_index, match_type = pdf_literal_span(detail, text)
        in_body = detail in body and source in body
        in_pdf = index >= 0 and source in text
        checks.append(dict(registro=record.get('id', ''), observaciones=record.get('observaciones', []),
            agente=record.get('agente_responsable', ''), apartado=record['seccion'], fuente=record['fuente'],
            en_json=True, en_cuerpo=in_body, en_pdf=in_pdf, metodo_localizacion=match_type,
            paginas_pdf=[number for begin,end,number in offsets
                         if index >= 0 and begin < end_index and end > index]))
        if in_body and (not in_pdf or match_type == 'url_partida_por_maquetacion'):
            warnings.append(dict(tipo='COBERTURA_PDF_NO_CONFIRMADA' if not in_pdf else 'URL_PARTIDA_EN_PDF',
                agente=record.get('agente_responsable', ''), registro=record.get('id', ''),
                apartado=record['seccion'], fuente=record['fuente'], detalle=record['detalle'],
                revision_manual_requerida=not in_pdf,
                mensaje=('El texto y la fuente están en el JSON y en el cuerpo del informe, pero '
                         'no se ha confirmado su coincidencia completa en el texto extraído del PDF. '
                         'No acredita ausencia física: requiere comprobación visual antes de utilizarlo.'
                         if not in_pdf else
                         'La URL está localizada en el PDF con saltos de línea de maquetación. '
                         'Se ha comprobado conservando todos sus caracteres y permitiendo únicamente '
                         'espacios dentro de la URL; no se han modificado sus datos.')))
    missing_body = [f"{c['agente']}/{c['registro']}" for c in checks if not c['en_cuerpo']]
    missing_pdf = [f"{c['agente']}/{c['registro']}" for c in checks if not c['en_pdf']]
    if missing_body or (missing_pdf and not allow_pdf_warnings):
        raise ValueError('El PDF omite requisitos registrados; no se publica: ' + ', '.join(missing_body or missing_pdf))
    observations = {obs for check in checks for obs in check['observaciones']}
    return dict(registros=len(checks), observaciones=len(observations), paginas=len(pages),
                apartados=len(report['secciones']),
                registros_completos=sum(c['en_cuerpo'] and c['en_pdf'] for c in checks),
                estado='CON_AVISOS' if warnings else 'COMPLETO', avisos=warnings,
                registros_pendientes_revision=sum(w['revision_manual_requerida'] for w in warnings),
                alcance='Cobertura literal de requisitos registrados en JSON, cuerpo y PDF. '
                        'No certifica que la extracción sea exhaustiva ni sustituye contraste semántico con fuentes.',
                comprobaciones=checks)
