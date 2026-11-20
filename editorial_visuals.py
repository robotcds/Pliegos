"""Presentación de datos comparables en el resumen de preventa."""
import re


VISUAL_GUIDANCE = (
    'Usa tablas para comparar datos con campos comunes presentes en las fuentes: '
    'lotes, importes, plazos, hitos, sobres, dotaciones, baremos o penalizaciones. '
    'Pon una fila por elemento, con unidades en los encabezados cuando sean comunes. '
    'Si hacen falta más de cuatro columnas, reparte los campos en tablas con la misma columna de identificación. '
    'Cuando el contenido sea una enumeración de actividades o condiciones, usa subtítulos '
    'o listas breves. Explica excepciones y relaciones complejas en párrafos junto a la tabla. '
    'Conserva el alcance y la fuente, y evita duplicar en prosa los mismos datos de la tabla.'
)

TEAM_GUIDANCE = (
    'Si las notas detallan perfiles técnicos o áreas de conocimiento, dedica un subapartado '
    '«Perfiles técnicos y áreas de conocimiento por lote». Dentro, coloca un subtítulo por '
    'cada lote documentado y una tabla con una fila por área, tecnología o perfil. Usa columnas '
    '«Área o perfil», «Tecnologías o conocimientos» y «Dotación» solo cuando haya datos para '
    'cada columna. Si solo constan áreas sin cifras, usa una lista breve por lote. Distingue '
    'el equipo actual de los mínimos exigidos y deja la dedicación, guardias o disponibilidad '
    'junto al lote o perfil al que correspondan. No infieras cantidades ni añadas lotes.'
)


LOT_SPAN = re.compile(r'(?:^|(?<=[.!?])\s+|\n)(?:(?:en|para)\s+(?:el\s+)?)?(lote\s+\d+[a-z]?)\b', re.I)
PROFILE_HEADING = re.compile(r'perfil(?:es)?.*t[eé]cnic|conocimiento', re.I)
SHARED_NOTE = re.compile(r'(?<=[.!?])\s+(?=(?:Estas cifras|Estos datos|Las cifras anteriores|En todos los lotes)\b)', re.I)
AREA_COUNT = re.compile(r'(?P<area>.+?)\s+\((?P<count>\d+(?:\s+(?:t[eé]cnicos?|personas?|recursos?))?)\)')
LOT_ITEM = re.compile(r'(lote\s+\d+[a-z]?)\s*:\s*(\S.*)', re.I | re.S)
LOT_AREA = re.compile(r'(lote\s+\d+[a-z]?)\s*(?:[-–—·:/]\s*(.+))?', re.I)


def table(columns, rows):
    return {'tipo': 'tabla', 'columnas': columns, 'filas': rows}


def narrow_tables(blocks):
    """Reparte las columnas de tablas anchas sin eliminar datos ni combinarlos."""
    result = []
    for block in blocks:
        if not isinstance(block, dict) or block.get('tipo') != 'tabla':
            result.append(block)
            continue
        columns, rows = block.get('columnas'), block.get('filas')
        if (not isinstance(columns, list) or len(columns) <= 4 or not isinstance(rows, list)
                or any(not isinstance(row, list) or len(row) != len(columns) for row in rows)):
            result.append(block)
            continue
        for start in range(1, len(columns), 3):
            result.append(table([columns[0], *columns[start:start + 3]],
                                [[row[0], *row[start:start + 3]] for row in rows]))
    return result


def profile_blocks(text):
    """Da formato a lotes y recuentos explícitos sin inferir campos."""
    content, *notes = SHARED_NOTE.split(text.strip(), maxsplit=1)
    matches = list(LOT_SPAN.finditer(content))
    if not matches or matches[0].start() != 0:
        return None

    blocks = []
    has_counts = False
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        detail = content[match.end():end].strip(' ,:')
        if not detail:
            return None
        title = match.group(1).capitalize()
        hint = re.match(r'^\(([^)]+)\)\s*,?\s*', detail)
        if hint:
            title += ' · ' + hint.group(1)
            detail = detail[hint.end():]
        blocks.append({'tipo': 'subtitulo', 'texto': title})

        if not detail:
            return None
        context, separator, entries = detail.partition(':')
        counts = [AREA_COUNT.fullmatch(item.strip()) for item in entries.rstrip('.').split(';')]
        if separator and len(counts) >= 2 and all(counts) and any(' ' in entry['count'] for entry in counts):
            has_counts = True
            context = context.strip()
            blocks.extend([
                {'tipo': 'parrafo', 'texto': context[:1].upper() + context[1:] + '.'},
                table(['Área o tecnología', 'Dotación indicada'],
                      [[entry['area'], entry['count']] for entry in counts]),
            ])
        else:
            blocks.append({'tipo': 'parrafo', 'texto': detail[:1].upper() + detail[1:]})

    if len(matches) == 1 and not has_counts:
        return None
    blocks.extend({'tipo': 'parrafo', 'texto': note} for note in notes)
    return blocks


def team_tables_by_lot(block):
    columns = block['columnas']
    if len(columns) < 3 or not re.search(r'\blote\b', columns[0], re.I):
        return None
    groups = {}
    for row in block['filas']:
        match = LOT_AREA.fullmatch(row[0].strip())
        if not match:
            return None
        lot, area = match.groups()
        groups.setdefault(lot.capitalize(), []).append([area or '', *row[1:]])
    if len(groups) < 2:
        return None

    result = []
    for lot, rows in groups.items():
        result.append({'tipo': 'subtitulo', 'texto': lot})
        if any(row[0] for row in rows):
            result.append(table(['Área', *columns[1:]], rows))
        else:
            result.append(table(columns[1:], [row[1:] for row in rows]))
    return result


def visual_blocks(blocks, *, team=False):
    """Convierte comparativas que llegan en prosa o listas con etiquetas explícitas."""
    result = []
    profiles = team
    for block in blocks:
        if block['tipo'] == 'subtitulo':
            profiles = bool(PROFILE_HEADING.search(block['texto']))
        elif block['tipo'] == 'parrafo' and profiles:
            formatted = profile_blocks(block['texto'])
            if formatted:
                result.extend(formatted)
                continue
        elif block['tipo'] == 'lista' and len(block['elementos']) >= 2:
            lots = [LOT_ITEM.fullmatch(item.strip()) for item in block['elementos']]
            if all(lots) and len({lot[1].casefold() for lot in lots}) == len(lots):
                result.append(table(['Lote', 'Detalle'], [[lot[1].capitalize(), lot[2]] for lot in lots]))
                continue
        elif block['tipo'] == 'tabla' and team:
            formatted = team_tables_by_lot(block)
            if formatted:
                result.extend(formatted)
                continue
        result.append(block)
    return result
