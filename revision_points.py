"""Pendientes explícitos de cada extracción; metadatos exclusivos del JSON.

No infiere obligaciones ni compara pliegos: conserva la evidencia del agente.
Una lista vacía no acredita una revisión exhaustiva.
"""
import re
import unicodedata
from copy import deepcopy


def normalized(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn').lower()


def collect_review_points(content):
    points, seen = [], set()
    section, headers = 'Contenido inicial', []
    lines = content.splitlines()
    for index, raw in enumerate(lines):
        line = raw.strip()
        if not line:
            continue
        heading = re.match(r'^#{1,6}\s+(.+)', line)
        numbered = re.match(r'^\d+[.)]\s+(.+)', line)
        # Los títulos numerados pueden estar en minúsculas. No confundirlos
        # con elementos numerados que ya expresan una ausencia o un estado.
        numbered_heading = (numbered and ':' not in numbered[1]
                            and not re.search(r'no consta|no se |pendiente de|no acreditado|no evaluable', normalized(numbered[1]))
                            and not numbered[1].endswith('.'))
        bare_heading = re.fullmatch(r'(?:datos no localizados(?: o ambiguos)?|ambiguedades y datos no localizados)', normalized(line))
        if heading or numbered_heading or bare_heading:
            section = (heading or numbered)[1] if heading or numbered_heading else line
            headers = []
            continue
        if line.isupper() and '|' not in line and ':' not in line and len(line) > 12:
            if not re.search(r'no consta|no disponible|no localizado|no acreditado|no evaluable|pendiente de', normalized(line)):
                section, headers = line, []
                continue
        if '|' in line:
            cells = [v.strip() for v in line.strip('|').split('|')]
            if all(re.fullmatch(r':?-{3,}:?', c.replace(' ', '')) for c in cells):
                continue
            next_line = lines[index + 1].strip() if index + 1 < len(lines) else ''
            if re.fullmatch(r'[|:\s-]+', next_line) and '-' in next_line:
                headers = cells
                continue
            detail = ('; '.join(f'{headers[i] if i < len(headers) else i+1}: {v}'
                                for i, v in enumerate(cells)) if headers else line)
        else:
            headers = []
            detail = re.sub(r'^(?:[-*•]|\d+[.)])\s+', '', line)
        value = normalized(detail)
        if re.search(r'no exigid[oa].*[/].*no consta', value):
            kind = 'estado_ambiguo'
        elif re.search(r'lectura parcial|documento (?:ausente|no disponible|no leido)|pendiente de (?:lectura|verificacion)', value):
            kind = 'verificacion_documental'
        elif re.search(r'\b(?:contradiccion|discrepancia|ambigu[oa]|inconsistencia)\b', value) and not re.search(r'(?:sin|no (?:hay|existen|se detectan|se identifican)) (?:\w+ )?(?:contradiccion|discrepancia|ambig)', value):
            kind = 'ambiguedad_o_discrepancia'
        elif re.search(r'no consta|(?:no|ni) se (?:han? )?(?:localiza|identifica|define|especifica|detalla|concreta)|no localizado|no calculable|no verificable|no acreditado|no evaluable|pendiente de (?:confirmar|concretar|validar|verificacion|acreditar)', value):
            kind = 'dato_no_concretado'
        else:
            continue
        key = (normalized(section), re.sub(r'\s+', ' ', value))
        if key in seen:
            continue
        seen.add(key)
        points.append({'id': f'REV-{len(points)+1:03d}', 'tipo': kind,
                       'estado': 'pendiente_de_revision', 'seccion': section,
                       'detalle': detail, 'evidencia': line,
                       'origen': 'salida_del_agente'})
    return points


def review_priority(point):
    """Orden orientativo por impacto contractual; no es un veredicto jurídico."""
    value = normalized(point['detalle'] + ' ' + point['seccion'])
    if point['tipo'] == 'verificacion_documental':
        return 100
    if point['tipo'] == 'ambiguedad_o_discrepancia':
        return 95
    if re.search(r'exclusion|admision|solvencia|obligatorio|resolucion del contrato', value):
        return 90
    if re.search(r'coste|precio|importe|pago|factura|rentabilidad|margen|penal|garantia|puntu|baremo', value):
        return 80
    if re.search(r'seguridad|incidente|brecha|personal|equipo|sustitucion|continuidad|plazo|sla', value):
        return 70
    return 40


def review_topic(point):
    value = normalized(point['detalle'])
    # Priorizar la materia del dato; utilizar el apartado solo para textos genéricos.
    if len(value.split()) < 10:
        value += ' ' + normalized(point['seccion'])
    if re.search(r'\bens\b|\biso\b|seguridad|privacidad|datos personales|\bdpo\b|cifrado|acceso|vulnerab|brecha|borrado|confidencial|logging|siem', value):
        return 'Seguridad, certificaciones y protección de datos'
    if re.search(r'solvencia|admision|exclusion|rolece|clasificacion|acredita|documentacion administrativa|patrimonio|seguro|partnership|fabricante', value):
        return 'Admisión, solvencia y acreditaciones'
    if re.search(r'coste|precio|importe|pago|factura|rentabilidad|margen|penal|garantia|puntu|baremo|oferta economica|descuento|redondeo', value):
        return 'Condiciones económicas y adjudicación'
    if re.search(r'servicio|equipo|personal|perfil|jornada|horario|sustitucion|continuidad|plazo|sla|soporte|transicion|reversibilidad|herramienta|licencia|suministro|logistica|subcontrat', value):
        return 'Equipo, medios y ejecución del servicio'
    return 'Documentación y otras condiciones pendientes'


def extract_review_points(content):
    """Hasta cinco bloques priorizados, sin perder las evidencias agrupadas."""
    groups = {}
    for point in collect_review_points(content):
        groups.setdefault(review_topic(point), []).append(point)
    ordered = sorted(groups.items(), key=lambda item: max(map(review_priority, item[1])), reverse=True)
    result = []
    for index, (topic, members) in enumerate(ordered, 1):
        members = sorted(members, key=review_priority, reverse=True)
        # Conservar detalle y evidencia en cada subpunto, sin repetirlos en la cabecera.
        subpoints = [{**p, 'id': f'REV-{index:03d}.{i:02d}'} for i, p in enumerate(members, 1)]
        result.append({'id': f'REV-{index:03d}', 'tipo': members[0]['tipo'],
                       'estado': 'pendiente_de_revision', 'titulo': topic,
                       'prioridad': 'alta' if review_priority(members[0]) >= 80 else 'media',
                       'detalle': f'Revisar {topic.lower()}: {len(members)} aspectos pendientes.',
                       'origen': 'salida_del_agente', 'subpuntos': subpoints})
    return result


def editorial_payload(payload):
    """Excluye solo los nuevos metadatos; mantiene íntegra la extracción previa."""
    result = deepcopy(payload)
    for agent in result.get('agentes', []) + result.get('analisis_capa2', []):
        agent.pop('puntos_revision', None)
        for key in ('recomendaciones', 'estado_recomendaciones', 'aviso_recomendaciones', 'diagnostico_recomendaciones'):
            agent.pop(key, None)
    return result
