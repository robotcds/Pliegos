"""Datos contractuales contrastables en las fuentes locales de capa 1."""
import re
from collections import defaultdict
from decimal import Decimal
from pathlib import Path
from zipfile import BadZipFile, ZipFile
from xml.etree import ElementTree

from pypdf import PdfReader
from pypdf.errors import PdfReadError


EUROS = r'(\d{1,3}(?:\.\d{3})*,\d{2}|\d+,\d{2})\s*€'
AMOUNTS = {
    'presupuesto_base': r'Importe\s+Presupuesto\s+base\s+de\s+licitaci[oó]n',
    'prorrogas': r'Importe\s+pr[oó]rrogas',
    'modificaciones': r'Importe\s+modificaciones',
    'valor_estimado': r'Valor\s+estimado\s+del\s+contrato',
}
ROOT = Path(__file__).resolve().parent


def flat(text):
    return ' '.join(text.split())


def pdf_pages(documents):
    """Lee únicamente archivos locales que se registraron como extraídos."""
    pages = {}
    for source in documents:
        path = ROOT / (source.get('ruta_local') or '')
        if source.get('estado_lectura') != 'texto_extraido' or path.suffix.lower() != '.pdf' or not path.is_file():
            continue
        try:
            pages[source['nombre']] = [page.extract_text() or '' for page in PdfReader(path).pages]
        except (OSError, ValueError, PdfReadError):
            # El registro previo de extracción permanece disponible. Sin una
            # segunda lectura local, no se certifican citas nuevas.
            continue
    return pages


def citation(document, page=None, section=None):
    return {'documento': document, **({'pagina': page} if page else {}),
            **({'apartado': section} if section else {})}


def cite_text(source):
    fields = [source['documento']]
    if source.get('apartado'):
        fields.append(source['apartado'])
    if source.get('pagina'):
        fields.append(f"p. {source['pagina']}")
    return ', '.join(fields)


def staff_tables(documents, pages):
    """Lee las tablas de equipo actual del anexo técnico conservando su alcance."""
    result = []
    lot_heading = re.compile(r'^\d+\.\s+Lote\s+(\d+)\s*[-–]', re.I)
    section_heading = re.compile(r'^(\d+(?:\.\d+)+)\.\s*(.+)')
    for source in documents:
        name = source['nombre']
        content = pages.get(name, [])
        if not content or not re.fullmatch(r'ANEXO\s+A\.pdf', name, re.I):
            continue
        reader = PdfReader(ROOT / source['ruta_local'])
        lot, section, table, columns = None, '', None, None
        for number, raw in enumerate(content, 1):
            if not table and not re.search(r'^\s*\d+\..*\b(?:Lote\s+\d|L\dS\d|Equipo de trabajo actual)', raw, re.M | re.I):
                continue
            for line in reader.pages[number - 1].extract_text(extraction_mode='layout').splitlines():
                text = line.strip()
                if not text or text.isdigit() or text.startswith('Exp.'):
                    continue
                mark = lot_heading.match(text)
                if mark:
                    lot, section, table, columns = int(mark[1]), '', None, None
                    continue
                heading = section_heading.fullmatch(text)
                if heading:
                    label = heading[2]
                    if re.search(r'\.{5,}\s*\d+$', label):  # índice paginado
                        continue
                    if re.match(r'L\d\.?S\d', label):
                        section = label
                    table, columns = None, None
                    if lot is not None and section and label.casefold() == 'equipo de trabajo actual':
                        code, service = section.split(maxsplit=1)
                        table = {'lote': lot, 'servicio': service, 'codigo_en_encabezado': code,
                                 'fuente': citation(name, number, heading[1]), 'filas': []}
                        result.append(table)
                    continue
                if not table or text.startswith(('Pliego de Prescripciones', 'Contratación mixta', 'administración de servidores,', 'el suministro de licencias,', '151.')):
                    continue
                header = re.search(r'Perfil\s{2,}(?:(Área de conocimiento|Función)\s{2,})?(Técnicos|Colaboradores)\s{2,}(Observaciones)', line)
                if header:
                    columns = (header.start() + 16, header.start(2) - 7, header.start(3) - 7, bool(header[1]))
                    continue
                if not columns:
                    continue
                if text.startswith(('Deberán establecerse guardias', 'Se requiere', 'El equipo de trabajo')):
                    table, columns = None, None
                    continue
                left, middle, right, has_area = columns
                count = next((m for m in re.finditer(r'(?<=\s{2})\d+(?=\s{2}|$)', line)
                              if middle <= m.start() < right), None)
                end = count.start() if count else right
                profile = line[:left].strip() if has_area else line[:end].strip()
                area = line[left:end].strip() if has_area else ''
                notes = line[right:].strip()
                rows = table['filas']
                previous = rows[-1] if rows else None
                if count and (not previous or 'dotacion' in previous) or (
                        profile and (not previous or 'dotacion' in previous and previous['perfil'] and area)):
                    if not profile and not area:
                        continue
                    previous = {'perfil': '', 'area': '', 'observaciones': '', 'paginas': [number]}
                    rows.append(previous)
                if not previous:
                    continue
                for key, value in (('perfil', profile), ('area', area), ('observaciones', notes)):
                    if value:
                        previous[key] = flat(previous[key] + ' ' + value)
                        if number not in previous['paginas']:
                            previous['paginas'].append(number)
                if count:
                    previous['dotacion'] = int(count[0])
                    if number not in previous['paginas']:
                        previous['paginas'].append(number)
    for table in result:
        table['filas'] = [row for row in table['filas'] if row.get('perfil') and 'dotacion' in row]
    return [table for table in result if table['filas']]


def duration_months(value, unit):
    return int(value) * (12 if unit.lower().startswith(('año', 'year', 'ann')) else 1)


def word_annex_controls(documents):
    """Contrasta marcas de solvencia y la jerarquía de puntos en anexos Word."""
    from oportunidades import extract_text

    result = {'solvencia': [], 'adjudicacion': []}
    for item in documents:
        path = ROOT / (item.get('ruta_local') or '')
        if item.get('estado_lectura') != 'texto_extraido' or path.suffix.lower() != '.docx' or not path.is_file():
            continue
        name = item['nombre']
        try:
            text = extract_text(path, '')
        except (OSError, ValueError, BadZipFile, ElementTree.ParseError, KeyError):
            continue
        solvency = re.search(r'(?ms)^Anexo IV\.1\s*\n.*?(?=^Anexo IV\.2\s*$)', text)
        if solvency:
            for label, section, pattern in (
                ('Volumen de negocio', '4.1', r'^☒ Referido al año de mayor volumen[^\n]*dos veces el valor anual medio[^\n]+'),
                ('Patrimonio neto o ratios', '4.1', r'^☐ Patrimonio neto[^\n]+'),
                ('Seguro de riesgos profesionales', '4.1', r'^☒ Justificante de la existencia de un seguro[^\n]+'),
                ('Importe anual de los servicios acreditados', '4.2.1', r'^b\) Requisito mínimo:[^\n]*70\s*%[^\n]+'),
                ('Experiencia de migración', '4.2.1', r'^☒ Relación de tres[^\n]*migración tecnológica[^\n]+'),
                ('Experiencia en arquitecturas híbridas', '4.2.1', r'^☒ Relación de tres[^\n]*arquitecturas[^\n]+'),
                ('Experiencia en virtualización', '4.2.1', r'^☒ Relación de tres[^\n]*UDS Virtual Cable[^\n]+'),
                ('Profesionales certificados Camunda', '4.2.2', r'^Títulos o acreditaciones académicos o profesionales exigidos:[^\n]*Camunda[^\n]+'),
            ):
                match = re.search(pattern, solvency[0], re.M | re.I)
                if match:
                    result['solvencia'].append({'campo': label, 'cita': match[0],
                        'fuente': citation(name, section=f'Anexo IV.1, {section}'),
                        'estado': 'casilla_no_marcada' if match[0].startswith('☐') else 'localizado'})
        award = re.search(r'(?ms)^Anexo XI\s*\n.*?(?=^Anexo XII\s*$)', text)
        if not award:
            continue
        blocks = re.split(r'(?m)^\[Lote-(\d+)\]\s*-\s*Criterios sometidos a (juicio de valor|fórmulas automáticas)\s*\((\d+) puntos\)\s*$', award[0])
        for i in range(1, len(blocks), 4):
            lot, mode, cap, block = blocks[i:i + 4]
            if mode == 'juicio de valor':
                headings = r'^PJV (\d+)\s*\n([^\n]+)\nHasta (\d+)\b'
            else:
                headings = r'^()((?:1\. )?Importe total de [^\n]+|Número de implantaciones[^\n]+|Reducción de plazos de implantación)(?:\n\([^\n]+\))?\nHasta (\d+)\b'
            subcriteria = [{'criterio': flat(label), 'puntos': int(points), **({'codigo': 'PJV ' + code} if code else {})}
                           for code, label, points in re.findall(headings, block, re.M)]
            if not subcriteria:
                continue
            score = sum(row['puntos'] for row in subcriteria)
            control = {'lote': int(lot), 'bloque': mode, 'maximo': int(cap), 'subcriterios': subcriteria,
                       'suma': score, 'coincide': score == int(cap),
                       'fuente': citation(name, section=f'Anexo XI, Lote {lot}, {mode}')}
            text_scales = re.findall(r'(?m)^(?:\d+ puntos?: |Metodología de cálculo: |Límite de puntuación: |Inadmisibilidad de cifras intermedias: )[^\n]+', block)
            if mode == 'fórmulas automáticas' and text_scales:
                control['baremo_pf_2_1'] = text_scales
            result['adjudicacion'].append(control)
        try:
            with ZipFile(path) as archive:
                xml = ElementTree.fromstring(archive.read('word/document.xml'))
            math = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
            word = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
            for paragraph in xml.iter(word + 'p'):
                expressions = list(paragraph.iter(math + 'oMath'))
                for equation, power in zip(expressions, expressions[1:]):
                    fraction = equation.find(math + 'f')
                    if fraction is None:
                        continue
                    literal = ''.join(t.text or '' for t in equation.iter(math + 't')).replace(' ', '')
                    exponent = ''.join(t.text or '' for t in power.iter(math + 't'))
                    vertical = power.find('.//' + word + 'vertAlign')
                    if (re.fullmatch(r'PEx=Pmax[.·×]\(Om[ií]nOi\)', literal) and exponent == 'n'
                            and vertical is not None and vertical.get(word + 'val') == 'superscript'
                            and re.search(r'(?m)^N:\s*0,5$', award[0])):
                        result['formula'] = {'valor': 'Pmax × (Omin / Oi)^0,5',
                            'fuente': citation(name, section='Anexo XI, subcriterios económicos')}
                        break
                if 'formula' in result:
                    break
        except (OSError, ValueError, BadZipFile, ElementTree.ParseError, KeyError):
            continue
    return result


def read_lot_table(document, pages):
    candidates = defaultdict(list)
    for number, page in enumerate(pages, 1):
        rows = re.split(r'(?im)^\s*Lote\s+(\d+)\s+Impuestos\s+excluidos\s+Impuestos\s+incluidos\s*$', page)
        for index in range(1, len(rows), 2):
            lot, body = rows[index], flat(rows[index + 1])
            initial = re.search(r'Duraci[oó]n del contrato\s*\(sin pr[oó]rrogas\)\s*(\d+)\s*(mes(?:es)?|años?)', body, re.I)
            renewals = re.search(r'N[uú]mero de pr[oó]rrogas\s*(\d+)', body, re.I)
            term = re.search(r'Duraci[oó]n de las pr[oó]rrogas\s*(\d+)\s*(mes(?:es)?|años?)', body, re.I)
            source = citation(document, number, f'Cuadro de importes del lote {lot}')
            item = {'lote': int(lot), 'fuente': source}
            if initial and renewals and (term or int(renewals[1]) == 0):
                months = duration_months(*initial.groups())
                count = int(renewals[1])
                per_term = duration_months(*term.groups()) if term else 0
                item['duracion'] = {'inicial_meses': months, 'numero_prorrogas': count,
                                    'meses_por_prorroga': per_term, 'maximo_meses': months + count * per_term,
                                    'maximo_derivado': True}
            amounts = {}
            for key, label in AMOUNTS.items():
                pair = re.search(label + r'\s*' + EUROS + r'(?:\s*' + EUROS + r')?', body, re.I)
                if pair:
                    amounts[key] = {'sin_iva': pair[1], **({'con_iva': pair[2]} if pair[2] else {})}
            if amounts:
                item['importes'] = amounts
            if len(item) > 2:
                candidates[int(lot)].append(item)
    return [items[0] for _, items in sorted(candidates.items())
            if all({k: v for k, v in item.items() if k != 'fuente'} ==
                   {k: v for k, v in items[0].items() if k != 'fuente'} for item in items)]


def contract_facts(payload, pages):
    source_name = next((name for name in pages if re.match(r'PCAP\b', name, re.I)), None)
    facts = {'lotes': [], 'importes_totales': {}, 'contrastes': [], 'prelacion_documental': [], 'seguridad': []}
    meta = payload.get('metadatos', {})
    xml = citation('Ficha XML del expediente')
    if meta.get('enlace_detalle'):
        xml['url'] = meta['enlace_detalle']
    if payload.get('organo_contratacion'):
        facts['organo_xml'] = {'valor': payload['organo_contratacion'], 'fuente': xml}
    raw_date = meta.get('plazo_presentacion', '')
    if raw_date:
        date = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})([+-]\d{2}:\d{2})?\s+(\d{2}:\d{2})(?::\d{2}(?:\.\d+)?)?', raw_date)
        display = f'{date[3]}/{date[2]}/{date[1]} a las {date[5]}' if date else raw_date
        if date and date[4]:
            display += f' (UTC{date[4]})'
        facts['presentacion'] = {'valor': display, 'valor_original': raw_date, 'fuente': xml,
                                 'fase': 'Presentación según el campo de plazo de la ficha XML'}
    if source_name:
        facts['lotes'] = read_lot_table(source_name, pages[source_name])
        for number, page in enumerate(pages[source_name], 1):
            text = flat(page)
            office = re.search(r'A\.1\s+[ÓO]rgano de contrataci[oó]n\s+(.*?)(?=\s+B\.\s+Objeto del contrato)', text, re.I)
            if office:
                selected = re.findall(r'☒\s*([^☐☒]+)', office[1])
                if len(selected) == 1:
                    name = re.sub(r'\s*\(\s*Perfil de contratante\s*\)\s*$', '', selected[0], flags=re.I).strip()
                    facts['organo_pcap'] = {'valor': name, 'fuente': citation(source_name, number, 'A.1')}
            ve = re.search(r'C\.1\s+Valor estimado del contrato\s*:\s*' + EUROS, text, re.I)
            if ve:
                facts['importes_totales']['valor_estimado'] = {'sin_iva': ve[1], 'fuente': citation(source_name, number, 'C.1')}
            if re.search(r'C\.2\s+Presupuesto base de licitaci[oó]n', text, re.I):
                base = re.search(r'Importe sin IVA:\s*' + EUROS + r'\s*-\s*Importe con IVA:\s*' + EUROS, text, re.I)
                if base:
                    facts['importes_totales']['presupuesto_base'] = {'sin_iva': base[1], 'con_iva': base[2],
                                                                      'fuente': citation(source_name, number, 'C.2')}
                changes = re.search(r'El importe de las modificaciones[^\d]{1,100}' + EUROS +
                                    r',\s*impuestos excluidos,\s*\(' + EUROS + r',', text, re.I)
                if changes:
                    facts['importes_totales']['modificaciones'] = {'sin_iva': changes[1], 'con_iva': changes[2],
                                                                    'fuente': citation(source_name, number, 'C.2')}
            deadline = re.search(r'antes de las\s+catorce horas del d[ií]a que se se[ñn]ale en la publicaci[oó]n del anuncio', text, re.I)
            if deadline and 'presentacion' in facts:
                facts['presentacion']['regla_pcap'] = {
                    'valor': 'Antes de las 14:00 del día señalado en el anuncio de licitación',
                    'fuente': citation(source_name, number, '11.3')}
            envelopes = re.search(r'Si no se incluyeran en la licitaci[oó]n criter\s*ios sometidos a un juicio de valor, se presentar[aá]n [uú]nicamente dos sobres', text, re.I)
            if envelopes:
                facts['regla_sobres'] = {'valor': 'Cuando se aplican criterios de juicio de valor se presentan tres sobres. En su ausencia se presentan dos.',
                                        'fuente': citation(source_name, number, '11.1')}
        lots = facts['lotes']
        if lots and all({'sin_iva', 'con_iva'} <= lot.get('importes', {}).get('prorrogas', {}).keys() for lot in lots):
            expected = re.search(r'Se prev[eé]n\s+(tres|dos|\d+)\s+lotes', flat(' '.join(pages[source_name])), re.I)
            if expected and {'tres': '3', 'dos': '2'}.get(expected[1].lower(), expected[1]) == str(len(lots)):
                values = {}
                for key in ('sin_iva', 'con_iva'):
                    total = sum(Decimal(lot['importes']['prorrogas'][key].replace('.', '').replace(',', '.'))
                                for lot in lots)
                    values[key] = f'{total:,.2f}'.translate(str.maketrans(',.', '.,'))
                facts['importes_totales']['prorrogas'] = {**values, 'derivado': True,
                    'fuente': citation(source_name, section='Suma de los importes de prórrogas de los cuadros por lote')}
    if 'organo_xml' in facts and 'organo_pcap' in facts and facts['organo_xml']['valor'].casefold() != facts['organo_pcap']['valor'].casefold():
        facts['contrastes'].append({'campo': 'Órgano de contratación', 'estado': 'contradictorio',
                                    'valores': [facts['organo_xml'], facts['organo_pcap']]})
    duration = re.fullmatch(r'(\d+)\s+(MON|ANN|meses|años)', meta.get('duracion', ''), re.I)
    if duration and facts['lotes']:
        values = {item['duracion']['inicial_meses'] for item in facts['lotes'] if 'duracion' in item}
        if values and values != {duration_months(*duration.groups())}:
            facts['contrastes'].append({'campo': 'Duración', 'estado': 'alcance_distinto',
                'valores': [{'valor': f'{duration_months(*duration.groups())} meses sin desglose por lote', 'fuente': xml},
                            {'valor': 'Duración inicial y prórrogas diferenciadas en el PCAP', 'fuente': facts['lotes'][0]['fuente']}]})
    for key, concept, tax in (('importe_estimado', 'valor_estimado', 'sin_iva'),
                               ('importe_total', 'presupuesto_base', 'con_iva')):
        value = re.fullmatch(r'(\d+(?:\.\d+)?)\s*EUR', meta.get(key, ''), re.I)
        entry = facts['importes_totales'].get(concept, {})
        if value and entry.get(tax):
            equal = Decimal(value[1]) == Decimal(entry[tax].replace('.', '').replace(',', '.'))
            facts['contrastes'].append({'campo': 'Valor estimado' if key == 'importe_estimado' else 'Importe total XML / PBL con IVA',
                'estado': 'coincidente' if equal else 'discrepancia_pendiente_de_contraste',
                'valores': [{'valor': meta[key], 'fuente': xml},
                            {'valor': entry[tax] + ' €', 'fuente': entry['fuente']}]})
    for name, content in pages.items():
        if re.match(r'PPT\b', name, re.I):
            for page, raw in enumerate(content, 1):
                heading = re.search(r'\b(\d+)\.\s+Esquema nacional de seguridad\b', flat(raw), re.I)
                required = re.search(r'El licitador deber[aá] acreditar que dispone de un sistema de gesti[oó]n de seguridad de la informaci[oó]n certificado en el Nivel Alto del Esquema Nacional de Seguridad', flat(raw), re.I)
                if required:
                    section = f'{heading[1]}. Esquema nacional de seguridad' if heading else None
                    entry = {'campo': 'ENS', 'valor': 'Nivel Alto', 'fase': 'Acreditación del licitador',
                             'fuente': citation(name, page, section)}
                    proof = r'El licitador aportar[aá] el correspondiente Certificado de Conformidad vigente, expedido por una entidad de certificaci[oó]n acreditada por la Entidad Nacional de Acreditaci[oó]n'
                    for offset, proof_page in enumerate(content[page - 1:page + 1]):
                        if re.search(proof, flat(proof_page), re.I):
                            entry['acreditacion'] = {'valor': 'Certificado de Conformidad vigente de una entidad acreditada por ENAC',
                                                     'fuente': citation(name, page + offset, section)}
                            break
                    facts['seguridad'].append(entry)
        if re.fullmatch(r'ANEXO\s+A\.pdf', name, re.I):
            for page, text in enumerate(content, 1):
                if re.search(r'En caso de diferencias.*(?:Prescripciones T[eé]cnicas).*prevalecer[aá] siempre\s+este anexo', flat(text), re.I):
                    facts['prelacion_documental'].append({
                        'valor': 'El Anexo A prevalece sobre el PPT en caso de diferencia. El PPT lo complementa en lo compatible.',
                        'fuente': citation(name, page, '1.1 Introducción')})
    return facts
