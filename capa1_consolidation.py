"""Contraste y registro transversal de la extracción documental de capa 1."""
import hashlib
import re
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlsplit
from zipfile import BadZipFile, ZipFile
from xml.etree import ElementTree

from capa1_facts import citation, cite_text, contract_facts, pdf_pages, staff_tables, word_annex_controls
from presales_coverage import UNLOCATED_DETAIL, normalized


ROOT = Path(__file__).resolve().parent
ABSENCE = re.compile(r'\b(?:no consta en la documentaci[oó]n revisada|no localizad[oa] en esta entrega parcial)\b', re.I)
READ_ERROR = re.compile(r'error de lectura|no se pudo (?:leer|extraer)|documento no disponible', re.I)
GENERIC = re.compile(r'^(?:fuente no individualizada|no consta|no localizad[oa]|pendiente|declaraci[oó]n)', re.I)
TOPICS = {
    'volumen anual de negocios': r'volumen (?:anual )?de negocio',
    'patrimonio neto o ratios': r'patrimonio neto|ratios (?:financier|de )',
    'seguro de riesgos profesionales': r'seguro.{0,48}(?:riesgos profesionales|responsabilidad civil)|seguro rc\b',
    'referencias empresariales': r'relaci[oó]n de (?:los )?(?:principales )?servicios|certificados? de buena ejecuci[oó]n|proyectos de referencia',
    'clasificación y ROLECE': r'rolece|clasificaci[oó]n (?:empresarial|del empresari|como contratista)',
    'ENS': r'\bens\b|esquema nacional de seguridad',
    'ISO 20000': r'\biso\s*20000\b',
    'ISO 27001': r'\biso\s*27001\b',
    'Camunda': r'\bcamunda\b',
}


def money(value):
    return Decimal(value.replace('.', '').replace(',', '.'))


def document_inventory(documents, pages):
    inventory = []
    for item in documents:
        name = item['nombre']
        path = ROOT / (item.get('ruta_local') or '')
        info = {'id': f"F{item.get('orden', len(inventory) + 1):02d}", 'nombre': name,
                'formato_original': Path(name).suffix.lower(), 'estado_lectura': item.get('estado_lectura'),
                'caracteres_extraidos': item.get('caracteres_extraidos')}
        if item.get('estado_lectura') == 'texto_extraido' and path.is_file():
            info['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
            info['formato_leido'] = path.suffix.lower()
            if path.resolve().is_relative_to(ROOT):
                relative = path.resolve().relative_to(ROOT).as_posix()
                info['ruta_relativa'] = relative
                item['ruta_local'] = relative
            if name in pages:
                info['paginas'] = len(pages[name])
            elif path.suffix.lower() == '.xlsx':
                from openpyxl import load_workbook
                try:
                    workbook = load_workbook(path, read_only=True)
                    try:
                        info['hojas'] = workbook.sheetnames
                    finally:
                        workbook.close()
                except (OSError, ValueError, BadZipFile, KeyError):
                    pass
            elif path.suffix.lower() == '.docx':
                try:
                    with ZipFile(path) as archive:
                        xml = ElementTree.fromstring(archive.read('docProps/app.xml'))
                    count = xml.findtext('{*}Pages')
                    if count and count.isdigit() and int(count) > 0:
                        info['paginas_declaradas'] = int(count)
                except (OSError, ElementTree.ParseError, BadZipFile, KeyError):
                    pass
        inventory.append(info)
    return inventory


def filtered_link_audit(payload, documents):
    """Reconstruye el filtro de enlaces con las copias de lectura, sin abrir URLs."""
    from oportunidades import (DocumentRef, ExtractedDocument, content_type_for_path,
                              extract_text, linked_urls_from_document, should_follow_document_link)

    warnings = ' '.join(payload.get('avisos_procesamiento', []))
    count = re.search(r'Se omitieron (\d+) enlaces internos', warnings)
    if not count:
        return None
    urls, unavailable = [], []
    for item in documents:
        path = ROOT / (item.get('ruta_local') or '')
        if item.get('estado_lectura') != 'texto_extraido' or not path.is_file():
            unavailable.append(item['nombre'])
            continue
        content_type = content_type_for_path(path)
        try:
            document = ExtractedDocument(DocumentRef(item.get('tipo', ''), item['nombre'], item.get('url', '')),
                                         path, content_type, extract_text(path, content_type))
            urls.extend({'documento': item['nombre'], 'url': url, 'dominio': urlsplit(url).hostname}
                        for url in linked_urls_from_document(document) if not should_follow_document_link(url))
        except (OSError, ValueError, BadZipFile, ElementTree.ParseError, KeyError):
            unavailable.append(item['nombre'])
    complete = not unavailable and len(urls) == int(count[1])
    return {'estado': 'recuento_reproducido' if complete else 'reconstruccion_parcial',
            'recuento_procesamiento': int(count[1]), 'recuento_reconstruido': len(urls),
            'dominios': dict(Counter(row['dominio'] for row in urls)), 'enlaces': urls,
            'fuentes_sin_contraste': unavailable}


def lot_scope(text, matter):
    explicit = re.findall(r'\blotes?\s*(\d+(?:\s*(?:,|y|e|/)\s*\d+)*)', matter, re.I)
    if not explicit:
        explicit = re.findall(r'\blotes?\s*(\d+(?:\s*(?:,|y|e|/)\s*\d+)*)', text, re.I)
    return tuple(sorted({int(number) for scope in explicit for number in re.findall(r'\d+', scope)}))


def source_references(source, documents):
    """Acepta el localizador citado, separando las referencias genéricas."""
    result = []
    for part in source.split(';'):
        ref = part.strip(' []')
        if GENERIC.match(ref) or re.search(r'\brevisi[oó]n (?:completa|parcial)\b', ref, re.I):
            continue
        for name in documents:
            if name.casefold() not in ref.casefold():
                continue
            location = re.sub(re.escape(name), '', ref, flags=re.I)
            page = re.search(r'\b(?:p[aá]gs?\.?|p[aá]ginas?|p\.)\s*(\d+(?:\s*[-–,y]\s*\d+)*)', location, re.I)
            section = re.search(r'\b(?:anexo\s+[IVXLCDM]+(?:\.\d+)?|(?:apartado|cl[aá]usula)\s+[\w.]+'
                                r'|hoja\s+[^,;]+|criterios de adjudicaci[oó]n\s+lotes?\s+\d+(?:\s*[,y]\s*\d+)*)\b',
                                location, re.I)
            if page or section:
                result.append(citation(name, page[1].strip() if page else None, section[0].strip(' ,.') if section else None))
    return result


def literal_reference(detail, pages):
    # El encabezado antepuesto por las fichas no pertenece a la cita.
    text = re.sub(r'\s*\[[^\n]*\]\s*$', '', detail).strip()
    variants = [text, text.split(': ', 1)[-1]]
    matches = {}
    for phrase in variants:
        needle = normalized(phrase).strip(' .')
        if len(needle.split()) < 8:
            continue
        for name, raw_pages in pages.items():
            for page, text in raw_pages:
                if needle in text:
                    matches[(name, page)] = citation(name, page)
    return list(matches.values()) if len(matches) == 1 else []


def count_original_registry(agents):
    rows = [r for a in agents if isinstance(a.get('contenido'), dict)
            for r in a['contenido'].get('requisitos_documentales', [])]
    notices = sum(row.get('es_requisito_contractual') is False for row in rows)
    keys = {(normalized(row['detalle']), normalized(row['fuente']))
            for row in rows if row.get('es_requisito_contractual') is not False}
    return {'registros_extraccion': len(rows), 'avisos_excluidos_criterio_anterior': notices,
            'duplicados_criterio_anterior': len(rows) - notices - len(keys),
            'registro_consolidado_criterio_anterior': len(keys)}


def documentary_type(detail):
    for kind, pattern in (
        ('entorno_actual', r'equipo (?:de trabajo )?actual|plantilla actual|dotaci[oó]n (?:actual|hist[oó]rica)|referencia orientativa'),
        ('alternativa_de_acreditacion', r'podr[aá] acreditar|alternativa de acreditaci[oó]n|tambi[eé]n se entender[aá] cumplido'),
        ('prohibicion', r'\bno se (?:admiten?|permite|autoriza)\b|\bqueda prohibid'),
        ('obligacion', r'\b(?:deber[aá]n?|se exige|es obligatori[oa]|se requiere)\b'),
        ('condicion', r'\b(?:siempre que|en caso de|cuando proceda|a condici[oó]n de)\b'),
    ):
        if re.search(pattern, detail, re.I):
            return kind
    return 'dato_documental'


def documentary_phase(detail, matter):
    for phase, pattern in (
        ('propuesto_como_adjudicatario', r'\b(?:propuesto como adjudicatario|mejor (?:oferta|clasificado)|antes de la adjudicaci[oó]n)\b'),
        ('presentacion_de_oferta', r'\b(?:con (?:su|la) oferta|sobre [123ABC]|presentaci[oó]n de ofertas)\b'),
        ('ejecucion', r'\b(?:durante la ejecuci[oó]n|en (?:la )?fase de (?:ejecuci[oó]n|operaci[oó]n))\b'),
    ):
        if re.search(pattern, matter + ' ' + detail, re.I):
            return phase
    return 'sin_fase_individualizada'


def claim_text(detail, documents, matter):
    detail = re.sub(r'\s*\[([^\[\]\n]+)\]\s*$',
                    lambda match: '' if source_references(match[1], documents) else match[0], detail)
    prefix = matter.strip() + ': '
    if detail.casefold().startswith(prefix.casefold()):
        detail = detail[len(prefix):]
    return normalized(detail)


def numeric_checks(facts, records):
    results = []
    lots = facts['lotes']
    for concept, item in facts['importes_totales'].items():
        for tax in ('sin_iva', 'con_iva'):
            parts = [lot.get('importes', {}).get(concept, {}).get(tax) for lot in lots]
            if tax in item and parts and all(parts):
                calculated = sum(map(money, parts))
                expected = money(item[tax])
                results.append({'campo': f'{concept} {tax}', 'suma_por_lotes_eur': str(calculated),
                                'total_eur': str(expected), 'coincide': calculated == expected,
                                'fuente': item['fuente']})
    for record in records:
        text = record['detalle']
        score = re.match(r'Criterios sometidos a (juicio de valor|f[oó]rmulas autom[aá]ticas)\s*'
                         r'\(m[aá]x\.\s*(\d+) puntos\):', text, re.I)
        parts = re.findall(r'\bhasta\s+(\d+)\s+puntos\b', text, re.I) if score else []
        if len(parts) > 1 and 'A4' in record['agentes']:
            summed = sum(map(int, parts))
            results.append({'campo': score[1], 'lotes': record['lotes'], 'parciales': list(map(int, parts)),
                            'suma': summed, 'total_declarado': int(score[2]), 'coincide': summed == int(score[2]),
                            'referencias': record['referencias']})
    return results


def consolidate_layer1(payload):
    if (payload.get('capa') != 1 or not payload.get('documentos_fuente') or payload.get('revision_preventa')
            or payload.get('analisis_capa2')):
        return payload
    agents, documents = payload.get('agentes', []), payload['documentos_fuente']
    pages = pdf_pages(documents)
    index = {name: [(i, normalized(text)) for i, text in enumerate(content, 1)] for name, content in pages.items()}
    inventory = document_inventory(documents, pages)
    facts = contract_facts(payload, pages)
    staff = staff_tables(documents, pages)
    annexes = word_annex_controls(documents)
    names = [item['nombre'] for item in documents]
    unread = [item['nombre'] for item in documents if item.get('estado_lectura') != 'texto_extraido']
    counts = count_original_registry(agents)
    records, findings, hints, branch_counts = {}, [], defaultdict(list), Counter()
    for agent in agents:
        aid = agent['id']
        content = agent.get('contenido', {})
        if not isinstance(content, dict):
            continue
        chunks = re.split(r'(?m)^## Entrega (\d+)\s*$', content.get('salida_original', ''))
        deliveries = [(int(chunks[i]), chunks[i+1]) for i in range(1, len(chunks), 2)]
        trace = content.setdefault('trazabilidad', [])
        seen = {(normalized(t.get('Requisito completo', '')), normalized(t.get('Fuente', ''))) for t in trace}
        if aid == 'A8':
            for table in staff:
                for item in table['filas']:
                    source = {**table['fuente'], 'pagina': ', '.join(map(str, item['paginas']))}
                    detail = f"{item['perfil']} · {item['area'] or table['servicio']} · {item['dotacion']} en el equipo actual"
                    origin = cite_text(source)
                    key = (normalized(detail), normalized(origin))
                    if key not in seen:
                        trace.append({'Materia': f"Lote {table['lote']} · {table['servicio']}",
                                      'Requisito completo': detail, 'Fuente': origin})
                        seen.add(key)
        for row in content.get('requisitos_documentales', []):
            detail, matter, source = row['detalle'], row['seccion'], row['fuente']
            lots = lot_scope(detail, row.get('titulo', '') + ' ' + matter)
            topics = [topic for topic, pattern in TOPICS.items() if re.search(pattern, matter + ' ' + detail, re.I)]
            origin = {'agente': aid, 'registro': row.get('id'), 'materia': matter, 'fuente_original': source}
            matching = [number for number, text in deliveries if detail in text]
            if len(matching) == 1:
                origin['entrega'] = matching[0]
            refs = source_references(source, names)
            if not refs and GENERIC.match(source) and not ABSENCE.search(detail):
                refs = literal_reference(detail, index)
            missing = bool(UNLOCATED_DETAIL.match(detail) or ABSENCE.search(detail))
            if (row.get('es_requisito_contractual') is False or UNLOCATED_DETAIL.match(detail)
                    or missing and not refs or ABSENCE.match(detail)):
                findings.append({**origin, 'detalle': detail, 'lotes': lots, 'temas': topics,
                                 'parcial': 'entrega parcial' in detail.casefold()})
                branch_counts['avisos_separados'] += 1
                continue
            services = tuple(sorted(set(re.findall(r'\bL\d+\.?S\d+(?:\.\d+)?\b', matter + ' ' + detail, re.I))))
            phase = documentary_phase(detail, matter)
            key = (claim_text(detail, names, matter), lots, services, phase)
            common = records.setdefault(key, {'id': f'C{len(records)+1:05d}', 'detalle': detail,
                'lotes': lots, 'subservicios': services, 'fase': phase, 'agentes': [], 'origenes': [],
                'referencias': [], 'materias': [],
                'tipo_documental': documentary_type(detail)})
            common['origenes'].append(origin)
            if aid not in common['agentes']:
                common['agentes'].append(aid)
            if matter not in common['materias']:
                common['materias'].append(matter)
            for ref in refs:
                if ref not in common['referencias']:
                    common['referencias'].append(ref)
            if refs:
                branch_counts[f'{aid}_con_localizador'] += 1
                trace_source = '; '.join(map(cite_text, refs))
                if aid == 'A8' and (normalized(detail), normalized(trace_source)) not in seen:
                    trace.append({'Materia': matter, 'Requisito completo': detail, 'Fuente': trace_source})
                    seen.add((normalized(detail), normalized(trace_source)))
                if not missing and not re.match(r'Ver\b', detail, re.I):
                    for topic in topics:
                        match = (common['id'], origin.get('entrega'))
                        if match not in hints[(aid, topic, lots)]:
                            hints[(aid, topic, lots)].append(match)
    unchecked = next((entry for entry in annexes['solvencia'] if entry['estado'] == 'casilla_no_marcada'
                      and entry['campo'] == 'Patrimonio neto o ratios'), None)
    for item in findings:
        matches = [hints[(item['agente'], topic, item['lotes'])] for topic in item['temas']]
        qualifiers = re.search(r'momento exacto|exenci[oó]n|excepciones|patrimonio|ratios|variant|similar|equivalen|'
                               r'n[uú]mero m[ií]nimo|experiencia individual|\bISO\b|\bENS\b|\bmoneda\b|cadena de',
                               item['detalle'], re.I)
        if (unchecked and item['agente'] == 'A3' and not item['lotes']
                and re.search(r'ning[uú]n requisito obligatorio de patrimonio neto ni ratios entre activos y pasivos\.?$', item['detalle'], re.I)):
            item['estado'] = 'localizado'
            item['resultado_contraste'] = 'La casilla de ese medio de solvencia figura sin marcar en el apartado citado.'
            item['referencias_directas'] = [unchecked['fuente']]
        elif item['agente'] == 'A3' and matches and all(matches) and not qualifiers:
            entry = item.get('entrega')
            other = entry is not None and all(any(number is not None and entry != number for _, number in group)
                                              for group in matches)
            item['estado'] = 'localizado_en_otra_entrega' if other else 'localizado'
            item['referencias_registro'] = list(dict.fromkeys(ref for group in matches for ref, _ in group))
        elif READ_ERROR.search(item['detalle']) or unread and item['fuente_original'] in unread:
            item['estado'] = 'pendiente_error_lectura'
        else:
            # Un inventario legible y varias entregas no acreditan una búsqueda
            # exhaustiva de cada condición de un aviso.
            item['estado'] = 'pendiente_de_contraste'
            if matches:
                item['referencias_relacionadas'] = list(dict.fromkeys(ref for group in matches for ref, _ in group))
            if 'ENS' in item['temas'] and facts.get('seguridad') and not item['lotes']:
                item['referencias_directas'] = [entry['fuente'] for entry in facts['seguridad']]
    for record in records.values():
        record['estado'] = 'localizado' if record['referencias'] else 'pendiente_de_trazabilidad'
    payload['consolidacion_documental'] = {
        'datos_contractuales': facts, 'inventario_fuentes': inventory,
        'registros': list(records.values()), 'avisos_por_entrega': findings,
        'equipo_actual_por_subservicio': staff,
        'contrastes_anexos_word': annexes,
        'pendientes_lectura': unread, 'controles_numericos': numeric_checks(facts, records.values()),
        'recuento': {**counts, **branch_counts, 'registros_unicos': len(records),
                    'registros_sin_localizador': sum(not r['referencias'] for r in records.values()),
                    'duplicados_dentro_de_agente': sum(len(r['origenes']) - len(r['agentes']) for r in records.values()),
                    'duplicados_entre_agentes': sum(len(r['agentes']) - 1 for r in records.values()),
                    'avisos_por_estado': dict(Counter(item['estado'] for item in findings))},
    }
    link_audit = filtered_link_audit(payload, documents)
    if link_audit:
        payload['consolidacion_documental']['auditoria_enlaces_filtrados'] = link_audit
    return payload


def report_sections(report, payload):
    """Inserta datos contrastados y pendientes directamente desde el JSON."""
    data = payload.get('consolidacion_documental')
    if not data:
        return report
    facts = data['datos_contractuales']

    def paragraph(text):
        return {'tipo': 'parrafo', 'texto': text}

    def heading(text):
        return {'tipo': 'subtitulo', 'texto': text}

    def table(columns, rows):
        return {'tipo': 'tabla', 'columnas': columns, 'filas': rows}

    identifiers = []
    for key, label in (('organo_xml', 'Órgano según ficha XML'), ('organo_pcap', 'Órgano marcado en el PCAP')):
        entry = facts.get(key)
        if entry:
            identifiers.append([label, entry['valor'] + ' [' + cite_text(entry['fuente']) + ']'])
    deadline = facts.get('presentacion')
    if deadline:
        identifiers.append(['Fecha y hora de presentación según XML', deadline['valor'] + ' [Ficha XML del expediente]'])
        if deadline.get('regla_pcap'):
            clause = deadline['regla_pcap']
            identifiers.append(['Regla de presentación en el PCAP',
                               clause['valor'] + ' [' + cite_text(clause['fuente']) + ']'])
    durations = []
    duration_sources = []
    for item in facts['lotes']:
        term = item.get('duracion')
        if term:
            durations.append([str(item['lote']), str(term['inicial_meses']),
                              f"{term['numero_prorrogas']} × {term['meses_por_prorroga']}" if term['numero_prorrogas'] else '0',
                              str(term['maximo_meses'])])
            source = citation(item['fuente']['documento'], item['fuente'].get('pagina'))
            if source not in duration_sources:
                duration_sources.append(source)
    labels = {'presupuesto_base': 'Presupuesto base de licitación', 'valor_estimado': 'Valor estimado',
              'prorrogas': 'Prórrogas', 'modificaciones': 'Modificaciones'}
    money_rows = [[labels[key], *(value.get(tax, '') + (' €' if value.get(tax) else '') for tax in ('sin_iva', 'con_iva')),
                   cite_text(value['fuente'])] for key, value in facts['importes_totales'].items()]
    amounts = []
    if money_rows:
        amounts.append(table(['Concepto', 'Sin IVA', 'Con IVA', 'Fuente'], money_rows))
        lot_amounts = []
        for item in facts['lotes']:
            for key, value in item.get('importes', {}).items():
                lot_amounts.append([str(item['lote']), labels[key], value['sin_iva'] + ' €',
                                    value['con_iva'] + ' €' if value.get('con_iva') else ''])
        if lot_amounts:
            sources = list(dict.fromkeys(cite_text(citation(item['fuente']['documento'], item['fuente'].get('pagina')))
                                        for item in facts['lotes'] if item.get('importes')))
            amounts.extend([heading('Importes por lote'), paragraph('Fuentes: ' + '; '.join(sources)),
                            table(['Lote', 'Concepto', 'Sin IVA', 'Con IVA'], lot_amounts)])
    if identifiers or durations:
        blocks = [paragraph(payload['titulo'])] if payload.get('titulo') else []
        if identifiers:
            blocks.append(table(['Dato', 'Valor y fuente'], identifiers))
        if durations:
            blocks.extend([heading('Vigencia y prórrogas por lote'),
                           paragraph('Fuentes: ' + '; '.join(map(cite_text, duration_sources))),
                           table(['Lote', 'Inicial (meses)', 'Prórrogas × meses', 'Máximo (meses)'], durations),
                           paragraph('El máximo se calcula suponiendo que se ejercitan todas las prórrogas indicadas.')])
        title = 'Identificación, objeto y vigencia'
        report['secciones'] = [{'titulo': title, 'bloques': blocks},
                               *[s for s in report['secciones'] if s['titulo'] != title]]
        opening = [f"Resumen documental de la extracción del expediente **{payload['expediente']}**."]
        if durations:
            opening.append('La duración y las prórrogas se muestran por lote. El máximo se calcula a partir del plazo inicial y de las prórrogas previstas en el PCAP.')
        if deadline:
            opening.append('La ficha XML indica como plazo de presentación **' + deadline['valor'] +
                           '**. La fecha debe contrastarse con el anuncio al que remite el PCAP cuando proceda.')
        if len(opening) < 2:
            opening.append('Las tablas identifican el origen de los datos disponibles.')
        report['introduccion'] = opening
    if amounts:
        title = 'Presupuesto, facturación y garantías'
        section = next((s for s in report['secciones'] if s['titulo'] == title), None)
        if section:
            # Las cifras se generan desde el JSON contrastado. Las demás
            # materias hacen su recorrido editorial habitual.
            cut = next((i for i, block in enumerate(section['bloques'])
                        if block['tipo'] == 'subtitulo' and re.search(r'factur|cobro|garant', block['texto'], re.I)), None)
            rest = section['bloques'][cut:] if cut is not None else [
                block for block in section['bloques'] if block['tipo'] == 'parrafo'
                and re.search(r'facturaci[oó]n|garant[ií]a|cobro', block['texto'], re.I)
                and not re.search(r'presupuesto base|valor estimado', block['texto'], re.I)]
            section['bloques'] = [*amounts, *rest]
        else:
            report['secciones'].insert(1, {'titulo': title, 'bloques': amounts})
    if facts.get('seguridad'):
        title = 'Seguridad y protección de datos'
        section = next((s for s in report['secciones'] if s['titulo'] == title), None)
        if section is None:
            section = {'titulo': title, 'bloques': []}
            report['secciones'].append(section)
        blocks = []
        for entry in facts['seguridad']:
            blocks.append(paragraph(f"El PPT exige al licitador acreditar {entry['campo']} {entry['valor']}. "
                                    + cite_text(entry['fuente']) + '.'))
            proof = entry.get('acreditacion')
            if proof:
                blocks.append(paragraph(proof['valor'] + '. ' + cite_text(proof['fuente']) + '.'))
        section['bloques'] = [*blocks, *(block for block in section['bloques'] if block['tipo'] != 'parrafo'
                            or not re.search(r'categor[ií]a ENS|\bENS\s+(?:de\s+)?(?:Nivel )?Alto\b', block['texto'], re.I))]
    staff = data.get('equipo_actual_por_subservicio', [])
    if staff:
        title = 'Perfiles, equipo y continuidad'
        section = next((s for s in report['secciones'] if s['titulo'] == title), None)
        if section is None:
            section = {'titulo': title, 'bloques': []}
            report['secciones'].append(section)
        verified = [heading('Dotaciones del equipo actual por lote y subservicio'),
                    paragraph('El anexo describe una dedicación parcial. Una persona puede cubrir varias áreas. Las cifras corresponden al equipo actual.')]
        for team in staff:
            pages = list(dict.fromkeys(page for row in team['filas'] for page in row['paginas']))
            source = {**team['fuente'], 'pagina': ', '.join(map(str, pages))}
            verified.extend([heading(f"Lote {team['lote']} · {team['servicio']}"),
                             paragraph(cite_text(source)),
                             table(['Perfil', 'Área de conocimiento o función', 'Equipo actual'],
                                   [[row['perfil'], row['area'] or '—', str(row['dotacion'])] for row in team['filas']])])
        # Las tablas anteriores de personal pueden mezclar cifras actuales y
        # condiciones de ejecución. Las obligaciones citadas siguen visibles.
        rest = [block for block in section['bloques'] if block['tipo'] == 'parrafo'
                and not re.search(r'dotaci[oó]n|plantilla actual|equipo (?:de trabajo )?actual|hasta\s+\d+\s+personas', block['texto'], re.I)]
        section['bloques'] = [*rest, *verified]
    annex_controls = data.get('contrastes_anexos_word', {})
    award = annex_controls.get('adjudicacion', [])
    envelopes = facts.get('regla_sobres')
    if envelopes:
        title = 'Fases del procedimiento y presentación'
        section = next((s for s in report['secciones'] if s['titulo'] == title), None)
        if section is None:
            section = {'titulo': title, 'bloques': []}
            report['secciones'].append(section)
        section['bloques'].insert(0, paragraph(envelopes['valor'] + ' ' + cite_text(envelopes['fuente']) + '.'))
    if award:
        title = 'Criterios de adjudicación y mejoras'
        section = next((s for s in report['secciones'] if s['titulo'] == title), None)
        if section is None:
            section = {'titulo': title, 'bloques': []}
            report['secciones'].append(section)
        by_lot = defaultdict(dict)
        for item in award:
            by_lot[item['lote']][item['bloque']] = item['maximo']
        verified = [paragraph(cite_text(citation(award[0]['fuente']['documento'], section='Anexo XI'))),
                    table(['Lote', 'Juicio de valor', 'Fórmulas', 'Total publicado por bloques'],
                          [[str(lot), str(blocks.get('juicio de valor', '—')),
                            str(blocks.get('fórmulas automáticas', '—')), str(sum(blocks.values()))]
                           for lot, blocks in sorted(by_lot.items())])]
        for item in award:
            label = f"Lote {item['lote']} · {item['bloque']}"
            verified.extend([heading(label), table(['Criterio', 'Puntos máximos'],
                [[row['criterio'], str(row['puntos'])] for row in item['subcriterios']])])
            if not item['coincide']:
                verified.append(paragraph(f"El desglose leído suma {item['suma']} puntos. El máximo del bloque es {item['maximo']}."))
            if item.get('baremo_pf_2_1'):
                verified.append({'tipo': 'lista', 'elementos': item['baremo_pf_2_1']})
        formula = annex_controls.get('formula')
        if formula:
            verified.extend([heading('Fórmula económica'), paragraph(formula['valor'] +
                '. Pmax es la puntuación máxima del subcriterio, Omin la menor oferta y Oi la oferta evaluada. Los importes se calculan sin IVA.')])
        distinct = [block for block in section['bloques'] if block['tipo'] == 'parrafo'
                    and re.search(r'desempate|mejoras|variantes', block['texto'], re.I)
                    and not re.search(r'f[oó]rmula|\d+\s*puntos', block['texto'], re.I)]
        section['bloques'] = [*verified, *distinct]
    outstanding = []
    for compared in facts['contrastes']:
        if compared['estado'] != 'coincidente':
            for value in compared['valores']:
                outstanding.append([compared['campo'], value['valor'], cite_text(value['fuente'])])
    limitations = [paragraph('El registro de lectura acredita extracción técnica. La cobertura de cláusulas, tablas y celdas se comprueba por sus referencias concretas.')]
    if outstanding:
        limitations.insert(0, table(['Campo', 'Valor o alcance', 'Fuente'], outstanding))
    if data['pendientes_lectura']:
        limitations.append(paragraph('Pendientes por lectura: ' + ', '.join(data['pendientes_lectura']) + '.'))
    review = Counter((item['agente'], topic) for item in data['avisos_por_entrega']
                     if item['estado'] in ('no_localizado', 'pendiente_error_lectura', 'pendiente_de_contraste')
                     for topic in item['temas'])
    if review:
        limitations.append(paragraph('El JSON conserva avisos de búsqueda con detalles pendientes de contraste, '
                                     'incluidos los que ya tienen evidencia sobre parte de la consulta.'))
    if data['recuento']['registros_sin_localizador']:
        limitations.append(paragraph(f"El JSON identifica {data['recuento']['registros_sin_localizador']} registros con localización pendiente."))
    if data.get('auditoria_enlaces_filtrados'):
        links = data['auditoria_enlaces_filtrados']
        limitations.append(paragraph(f"Enlaces filtrados durante la lectura: {links['recuento_procesamiento']}. "
                                     f"La reconstrucción local encontró {links['recuento_reconstruido']} y sus dominios figuran en el JSON."))
    annexes = facts['prelacion_documental']
    if annexes:
        section = next((s for s in report['secciones'] if s['titulo'] == 'Alcance, actividades y entregables'), None)
        if section:
            section['bloques'][:0] = [paragraph(entry['valor'] + ' [' + cite_text(entry['fuente']) + ']') for entry in annexes]
    title = 'Discrepancias y datos pendientes'
    report['secciones'] = [*[s for s in report['secciones'] if s['titulo'] != title], {'titulo': title, 'bloques': limitations}]
    if outstanding:
        report['conclusion'] = [line for line in report['conclusion']
                               if not re.search(r'sin discrepancias|documentaci[oó]n revisada es coherente|no se han (?:detectado|identificado) discrepancias|m[aá]xim[oa].{0,30}mes', line, re.I)]
        report['conclusion'].append('Las diferencias de alcance y de identificación se mantienen con la referencia de cada fuente. El órgano marcado en el PCAP y el valor de la ficha XML se muestran por separado cuando discrepan.')
    return report
