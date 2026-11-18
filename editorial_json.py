"""Lectura conservadora de JSON editorial, sin completar hechos ni texto cortado."""
import json
import re


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Clave JSON duplicada: ' + key +
                             '. Usa objetos distintos en la lista para conservar ambos contenidos.')
        result[key] = value
    return result


def report_with_premature_closure(text):
    """Recupera secciones completas tras un cierre prematuro, sin reparar valores.

    Solo admite la cabecera conocida del informe, objetos sección JSON íntegros y
    una conclusión íntegra. Entre ellos solo pueden sobrar cierres y comas.
    Cualquier otro contenido, campo nuevo o truncamiento conserva el error.
    """
    decoder = json.JSONDecoder(object_pairs_hook=unique_object)
    header, end = decoder.raw_decode(text)
    if (not isinstance(header, dict)
            or set(header) != {'expediente', 'agentes_revisados', 'introduccion', 'secciones'}
            or not isinstance(header['secciones'], list) or not header['secciones']):
        raise ValueError('No es un informe con cierre prematuro recuperable')
    tail = text[end:]
    while True:
        tail = re.sub(r'^[\s,\]}]*', '', tail)
        if tail.startswith('{'):
            section, end = decoder.raw_decode(tail)
            if (not isinstance(section, dict) or set(section) != {'titulo', 'bloques'}
                    or not isinstance(section['titulo'], str)
                    or not isinstance(section['bloques'], list) or not section['bloques']):
                raise ValueError('Continuación de sección inválida')
            header['secciones'].append(section)
            tail = tail[end:]
            continue
        match = re.match(r'^"conclusion"\s*:\s*', tail)
        if not match:
            raise ValueError('Falta una continuación completa del informe')
        conclusion, end = decoder.raw_decode(tail[match.end():])
        closing = tail[match.end() + end:].strip()
        if (not isinstance(conclusion, list) or not conclusion
                or not all(isinstance(value, str) for value in conclusion)
                or not re.fullmatch(r'[\]}\s]*}', closing)):
            raise ValueError('Conclusión o cierre incompletos')
        header['conclusion'] = conclusion
        return header


def parse_editorial_json(raw):
    text = raw.strip().lstrip('\ufeff')
    text = re.sub(r'^```(?:json)?\s*|\s*```$', '', text)
    try:
        return json.loads(text, object_pairs_hook=unique_object)
    except json.JSONDecodeError:
        pass
    try:
        return report_with_premature_closure(text)
    except (ValueError, TypeError):
        pass
    # Solo se elimina una llave de cierre duplicada cuando la pila exige
    # continuar/cerrar una lista. No se reparan comillas, valores ni truncamientos.
    stack, output = [], []
    quoted = escaped = False
    for index, char in enumerate(text):
        if quoted:
            output.append(char)
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '"':
                quoted = False
            continue
        if char == '"':
            quoted = True
        elif char in '[{':
            stack.append(char)
        elif char in ']}':
            expected = '[' if char == ']' else '{'
            if not stack or stack[-1] != expected:
                previous = ''.join(output).rstrip()
                following = text[index+1:].lstrip()
                if char == '}' and stack and stack[-1] == '[' and previous.endswith('}') and following.startswith((',', ']')):
                    continue
                # Mantener el error original; no adivinar otra estructura.
                return json.loads(text, object_pairs_hook=unique_object)
            stack.pop()
        output.append(char)
    return json.loads(''.join(output), object_pairs_hook=unique_object)
