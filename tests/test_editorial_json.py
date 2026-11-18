import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import Mock

from age_report import apply_review, generate_age_report, validate_report, expected_editorial_agents, coverage_issues, editorial_source_payload
from editorial_json import parse_editorial_json


class EditorialJsonTests(unittest.TestCase):
    def test_complete_conclusion_after_premature_outer_closure(self):
        header = {key: value for key, value in self.report.items() if key != 'conclusion'}
        raw = json.dumps(header) + ',"conclusion":' + json.dumps(self.report['conclusion']) + '}'
        self.assertEqual(parse_editorial_json(raw), self.report)
        for bad in (raw[:-2], raw + ' trailing prose',
                    raw.replace('"conclusion":', '"unexpected":1,"conclusion":'),
                    raw + ',"conclusion":["Other conclusion"]}'):
            with self.subTest(bad=bad[-60:]), self.assertRaises(ValueError):
                parse_editorial_json(bad)

    def test_exact_displayed_table_row_can_be_corrected_without_fuzzy_matching(self):
        report = deepcopy(self.report)
        row = ['Fecha límite presentación', '17/03/2031 a las 10:00']
        report['secciones'][0]['bloques'] = [{'tipo': 'tabla', 'columnas': ['Dato', 'Valor'], 'filas': [row]}]
        edit = {'correcciones': [{'buscar': ' | '.join(row),
                'reemplazar': 'Fecha límite para solicitudes de participación | 17/03/2031 a las 10:00'}]}
        changed = apply_review(report, edit)
        self.assertEqual(changed['secciones'][0]['bloques'][0]['filas'][0],
                         ['Fecha límite para solicitudes de participación', '17/03/2031 a las 10:00'])
        self.assertEqual(report['secciones'][0]['bloques'][0]['filas'][0], row)
        for replacement in ['Una frase que pierde la fecha', 'Dato | Fecha | Fuente', 'Dato | ']:
            bad = deepcopy(edit)
            bad['correcciones'][0]['reemplazar'] = replacement
            with self.subTest(replacement=replacement), self.assertRaises(ValueError):
                apply_review(report, bad)
        report['secciones'][0]['bloques'][0]['filas'].append(list(row))
        with self.assertRaises(ValueError):
            apply_review(report, edit)

    def test_table_alarm_exposes_actual_cell_ids_in_review(self):
        from age_report import table_rewrite_tasks, fidelity_issues
        payload = {'expediente': 'TEST', 'agentes': [{'id': 'A2', 'contenido': {
            'salida_original': 'Solicitudes de participación hasta 17/03/2031; ofertas por invitación.'}}]}
        report = deepcopy(self.report)
        report['agentes_revisados'] = ['A2']
        report['secciones'][0]['bloques'] = [{'tipo': 'tabla', 'columnas': ['Dato', 'Valor'],
            'filas': [['Fecha límite presentación', '17/03/2031 a las 10:00']]}]
        tasks = table_rewrite_tasks(report, payload)
        self.assertEqual(len(tasks), 1)
        self.assertEqual([c['texto_actual'] for c in tasks[0]['celdas']],
                         ['Fecha límite presentación', '17/03/2031 a las 10:00'])
        edit = {'correcciones_por_id': [{'id': tasks[0]['celdas'][0]['id'],
                  'reemplazar': 'Fecha límite para solicitudes de participación'}]}
        self.assertEqual(fidelity_issues(apply_review(report, edit), payload), [])
        call = Mock(side_effect=[json.dumps(report), json.dumps(edit)])
        with tempfile.TemporaryDirectory() as folder:
            result = generate_age_report(payload, Path(folder) / 'result.pdf', {}, '', call)
            self.assertTrue(result.exists())
        self.assertIn('CORRECCIONES DE TABLAS', call.call_args_list[1].args[1])
        self.assertIn(tasks[0]['celdas'][0]['id'], call.call_args_list[1].args[1])

    def test_id_only_review_does_not_require_unused_empty_operations(self):
        from age_report import editable_report_texts
        identifier = next(iter(editable_report_texts(self.report)))
        changed = apply_review(self.report, {'correcciones_por_id':[
            {'id':identifier, 'reemplazar':'Texto corregido.'}]})
        self.assertEqual(changed['introduccion'][0], 'Texto corregido.')
        for malformed in ({}, {'correcciones_por_id':None}, {'anadidos':'texto'}):
            with self.assertRaises(ValueError):
                apply_review(self.report, malformed)

    def test_turnover_singular_plural_and_annual_variants(self):
        payload = {'agentes': [{'contenido': {'salida_original':
                   'Volumen anual de negocios mínimo: 1.200.000 EUR.'}}]}
        for wording in ('volumen de negocio', 'volumen de negocios', 'volumen anual de negocios',
                        'cifra de negocios', 'cifra anual de negocio'):
            report = deepcopy(self.report)
            report['secciones'][0]['bloques'][0]['texto'] = f'Se exige {wording} de 1.200.000 EUR.'
            self.assertEqual(coverage_issues(report, payload), [], wording)
        self.assertTrue(coverage_issues(self.report, payload))

    def test_singular_turnover_review_finishes_without_extra_retry(self):
        payload = deepcopy(self.payload)
        payload['agentes'][0]['contenido'] = {'salida_original': 'Volumen anual de negocios: 1.200.000 EUR.'}
        edits = {'correcciones': [], 'anadidos': [{'seccion': 'Datos', 'bloque': {
            'tipo': 'parrafo', 'texto': 'Se exige un volumen de negocio de 1.200.000 EUR.'}}]}
        call = Mock(side_effect=[json.dumps(self.report), json.dumps(edits)])
        with tempfile.TemporaryDirectory() as folder:
            generate_age_report(payload, Path(folder)/'report.pdf', {}, 'token', call)
        self.assertEqual(call.call_count, 2)

    def test_full_pipeline_requires_both_layers_and_archives_all_agents(self):
        payload = {'expediente': 'TEST',
                   'agentes': [{'id': i, 'contenido': {}} for i in
                               ['A1', 'A2', 'A3', 'A4', 'A6', 'A8', 'A9', 'A10']],
                   'analisis_capa2': [{'nombre': n, 'contenido': {}} for n in
                                     ['Economico-financiero', 'Delivery / Operacion',
                                      'Coherencia Documental', 'Riesgos y Go/No-Go']]}
        report = deepcopy(self.report)
        report['agentes_revisados'] = expected_editorial_agents(payload)
        self.assertEqual(len(report['agentes_revisados']), 12)
        validate_report(report, payload)
        for ids in [report['agentes_revisados'][:8], report['agentes_revisados'] + ['Inventado']]:
            with self.assertRaisesRegex(ValueError, 'Faltan:.*no reconocidos:'):
                validate_report({**report, 'agentes_revisados': ids}, payload)
        call = Mock(side_effect=[json.dumps(report), '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as folder:
            generate_age_report(payload, Path(folder)/'full.pdf', {}, 'token', call)
            self.assertEqual(len(list(Path(folder).glob('diagnosticos/redaccion/*/agente_*.json'))), 12)
        for invocation in call.call_args_list:
            self.assertIn(json.dumps(report['agentes_revisados'], ensure_ascii=False), invocation.args[0])

    def setUp(self):
        self.payload = {'expediente': 'TEST', 'agentes': [{'id': 'A1', 'contenido': {}}]}
        self.report = {'expediente': 'TEST', 'agentes_revisados': ['A1'],
                       'introduccion': ['Primer párrafo.', 'Segundo párrafo.'],
                       'secciones': [{'titulo': 'Datos', 'bloques': [
                           {'tipo': 'parrafo', 'texto': 'Texto con símbolos } ] y comillas "literales".'}]}],
                       'conclusion': ['Conclusión documentada.']}

    def test_single_section_is_completed_by_review_before_publication(self):
        payload = {'expediente': 'TEST', 'agentes': [
            {'id': aid, 'contenido': 'Texto documental ' * 100} for aid in
            ['A1', 'A2', 'A3', 'A4', 'A6', 'A8', 'A9', 'A10']]}
        short = deepcopy(self.report)
        short['agentes_revisados'] = expected_editorial_agents(payload)
        complete = deepcopy(short)
        complete['secciones'] = [dict(titulo='Materia ' + str(i), bloques=deepcopy(short['secciones'][0]['bloques']))
                                for i in range(6)]
        call = Mock(side_effect=[json.dumps(short), json.dumps({'correcciones': [], 'anadidos': [],
                                'secciones_nuevas': complete['secciones'][1:]})])
        with tempfile.TemporaryDirectory() as folder:
            path = generate_age_report(payload, Path(folder)/'complete.pdf', {}, 'token', call)
            self.assertTrue(path.exists())
        self.assertIn('Desarrolla al menos seis secciones', call.call_args_list[1].args[1])
        self.assertIn('Equipo y continuidad', call.call_args_list[0].args[1])
        self.assertIn('Cierre y transferencia', call.call_args_list[0].args[1])
        self.assertNotIn('RESPUESTA ANTERIOR', call.call_args_list[1].args[1])
        self.assertIn('CONTRATO ESPECÍFICO DE ESTA PASADA', call.call_args_list[1].args[0])
        self.assertEqual(call.call_count, 2)

    def test_premature_report_closures_preserve_all_complete_sections(self):
        report = deepcopy(self.report)
        report['secciones'] *= 3
        header = {key: value for key, value in report.items() if key != 'conclusion'}
        header['secciones'] = report['secciones'][:1]
        malformed = (json.dumps(header) + ', ' + json.dumps(report['secciones'][1]) + ']},' +
                     json.dumps(report['secciones'][2]) + '],"conclusion":' +
                     json.dumps(report['conclusion']) + '}')
        self.assertEqual(parse_editorial_json(malformed), report)
        for bad in [malformed[:-5], malformed + '{"extra":"dato"}',
                    malformed.replace('"conclusion":', '"dato_descartado":1,"conclusion":')]:
            with self.subTest(bad=bad[-60:]), self.assertRaises(ValueError):
                parse_editorial_json(bad)

    def test_partial_report_is_never_published_if_review_does_not_complete_it(self):
        payload = {'expediente': 'TEST', 'agentes': [
            {'id': aid, 'contenido': 'Texto documental ' * 100} for aid in
            ['A1', 'A2', 'A3', 'A4', 'A6', 'A8', 'A9', 'A10']]}
        short = deepcopy(self.report)
        short['agentes_revisados'] = expected_editorial_agents(payload)
        call = Mock(side_effect=[value for _ in range(3) for value in
                               [json.dumps(short)] + ['{"correcciones":[],"anadidos":[]}'] * 3])
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder)/'incomplete.pdf'
            with self.assertRaisesRegex(RuntimeError, 'seis secciones'):
                generate_age_report(payload, target, {}, 'token', call)
            self.assertFalse(target.exists())

    def test_exhausted_prose_reviews_can_recover_with_new_draft(self):
        call = Mock(side_effect=[json.dumps(self.report)] + ['No hay cambios.'] * 3 +
                                [json.dumps(self.report), '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as folder:
            path = generate_age_report(self.payload, Path(folder)/'complete.pdf', {}, 'token', call)
            self.assertTrue(path.exists())
        self.assertIn('Revisión editorial agotada', call.call_args_list[4].args[1])
        self.assertEqual(call.call_count, 6)

    def test_editorial_input_removes_only_exact_reconstructible_copies(self):
        from oportunidades import markdown_report_to_json
        text = '## Pago\nSi se factura en 15 días, pago desde el acta; en otro caso desde factura.\n| Dato | Valor |\n|---|---|\n| Bolsa | Consumo no garantizado |'
        payload = {'expediente': 'TEST', 'agentes': [{'id': 'A2', 'contenido': markdown_report_to_json(text)}]}
        before = deepcopy(payload)
        filtered = editorial_source_payload(payload)
        content = filtered['agentes'][0]['contenido']
        self.assertEqual(content['salida_original'], text)
        self.assertNotIn('secciones', content)
        self.assertTrue(any('Consumo no garantizado' in r['detalle']
                            for r in content['requisitos_documentales']))
        self.assertEqual(payload, before)
        payload['agentes'][0]['contenido']['dato_externo'] = 'Garantía adicional de 12 meses.'
        augmented = editorial_source_payload(payload)['agentes'][0]['contenido']
        for key, value in payload['agentes'][0]['contenido'].items():
            self.assertEqual(augmented[key], value)

    def test_duplicate_json_keys_are_rejected_instead_of_losing_content(self):
        raw = '{"correcciones":[],"anadidos":[{"seccion":"Anormalidad","bloque":{"tipo":"parrafo","texto":"Cinco días"},"seccion":"Garantías","bloque":{"tipo":"parrafo","texto":"Cinco por ciento"}}]}'
        with self.assertRaisesRegex(ValueError, 'Clave JSON duplicada: seccion'):
            parse_editorial_json(raw)

    def test_review_can_target_exact_text_without_fuzzy_replacement(self):
        from age_report import editable_report_texts
        report = deepcopy(self.report)
        report['conclusion'] = [report['introduccion'][0]]
        catalog = editable_report_texts(report)
        target = next(key for key, (path, _) in catalog.items() if path == ['conclusion', 0])
        changed = apply_review(report, {'correcciones': [], 'anadidos': [],
            'correcciones_por_id': [{'id': target, 'reemplazar': 'Conclusión corregida.'}]})
        self.assertEqual(changed['conclusion'], ['Conclusión corregida.'])
        self.assertEqual(changed['introduccion'], report['introduccion'])
        self.assertEqual(report['conclusion'], [report['introduccion'][0]])
        self.assertFalse(any(path[-1] in ('titulo', 'tipo') for path, _ in catalog.values()))

    def test_review_rejects_invalid_or_repeated_text_references(self):
        for changes in [[{'id': 'T9999', 'reemplazar': 'Texto'}],
                        [{'id': 'T0001', 'reemplazar': 'Texto'}] * 2,
                        [{'id': 'T0001', 'reemplazar': ''}], None]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                apply_review(self.report, {'correcciones': [], 'anadidos': [],
                                          'correcciones_por_id': changes})

    def test_review_recovers_from_quote_missing_in_current_draft(self):
        call = Mock(side_effect=[json.dumps(self.report),
            json.dumps({'correcciones': [{'buscar': 'Frase que solo existe en la fuente',
                                        'reemplazar': 'Corrección'}], 'anadidos': []}),
            json.dumps({'correcciones': [], 'anadidos': [], 'correcciones_por_id': [
                {'id': 'T0001', 'reemplazar': 'Primer párrafo corregido con respaldo.'}]})])
        with tempfile.TemporaryDirectory() as folder:
            path = generate_age_report(self.payload, Path(folder)/'complete.pdf', {}, 'token', call)
            saved = json.loads(next(Path(folder).glob('diagnosticos/redaccion/*/redaccion.json')).read_text(encoding='utf-8'))
            self.assertTrue(path.exists())
            self.assertEqual(saved['introduccion'][0], 'Primer párrafo corregido con respaldo.')
        self.assertEqual(call.call_count, 3)
        self.assertIn('TEXTOS EDITABLES DEL BORRADOR ACTUAL', call.call_args_list[2].args[1])
        for index in (1, 2):
            self.assertIn('CONTRATO ESPECÍFICO DE ESTA PASADA', call.call_args_list[index].args[1])
            self.assertTrue(call.call_args_list[index].args[1].rstrip().endswith(
                'El primer carácter de la respuesta debe ser { y el último }; devuelve un solo objeto JSON.'))
        self.assertIn('Frase que solo existe en la fuente', call.call_args_list[2].args[1])
        self.assertNotIn('Contrato de salida para maquetación', call.call_args_list[2].args[0])

    def malformed(self):
        return json.dumps(self.report, ensure_ascii=False).replace('}]}]', '}]}}]')

    def test_duplicate_section_closing_brace_preserves_every_value(self):
        self.assertEqual(parse_editorial_json(self.malformed()), self.report)
        self.assertEqual(parse_editorial_json('```json\n' + self.malformed() + '\n```'), self.report)

    def test_does_not_invent_missing_content_or_accept_multiple_objects(self):
        for raw in ['Texto de introducción.', '{"a": "texto cortado', '{"a":1}{"b":2}']:
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_editorial_json(raw)
        incomplete = deepcopy(self.report)
        incomplete.pop('conclusion')
        with self.assertRaisesRegex(ValueError, 'conclusion'):
            validate_report(parse_editorial_json(json.dumps(incomplete)), self.payload)

    def test_actual_failure_sequence_recovers_then_requires_review(self):
        call = Mock(side_effect=['Texto sin JSON.', self.malformed(),
                                 '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'result.pdf'
            generate_age_report(self.payload, path, {}, 'token', call)
            self.assertTrue(path.exists())
            saved = json.loads(next(Path(folder).glob('diagnosticos/redaccion/*/redaccion.json')).read_text(encoding='utf-8'))
            self.assertEqual(saved['conclusion'], self.report['conclusion'])
            self.assertTrue(list(Path(folder).glob('diagnosticos/redaccion/*/borrador_2_validado.json')))
        self.assertEqual(call.call_count, 3)
        self.assertNotIn('Texto sin JSON.', call.call_args_list[1].args[1])
        self.assertIn('no la uses como plantilla', call.call_args_list[1].args[1])
        self.assertIn('conclusion', call.call_args_list[1].args[1])
        self.assertIn('CONTRATO ESPECÍFICO', call.call_args_list[2].args[0])

    def test_malformed_structure_raises_controlled_validation_error(self):
        mutations = [lambda r: r.update(agentes_revisados=[{}]),
                     lambda r: r['secciones'][0].update(titulo=[]),
                     lambda r: r['secciones'][0].update(bloques=['texto']),
                     lambda r: r['secciones'][0].update(bloques=[{
                         'tipo': 'tabla', 'columnas': ['A', 'B'], 'filas': [None]}])]
        for mutate in mutations:
            report = deepcopy(self.report)
            mutate(report)
            with self.assertRaises(ValueError):
                validate_report(report, self.payload)
        for edits in [{'correcciones': [None], 'anadidos': []},
                      {'correcciones': [], 'anadidos': ['texto']}]:
            with self.assertRaises(ValueError):
                apply_review(deepcopy(self.report), edits)
