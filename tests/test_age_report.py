import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock
from unittest.mock import patch
from pypdf import PdfReader
from age_report import apply_review, generate_age_report, render_age_pdf, validate_report, group_conclusion


class AgeTests(unittest.TestCase):
    def test_conclusion_groups_repeated_labels_and_preserves_text(self):
        paragraphs = ['**NO EXIGIDO EXPRESAMENTE:** Primer punto.',
                      '**NO LOCALIZADO:** Otro estado.',
                      'NO EXIGIDO: Segundo punto.',
                      '**PUNTO RELEVANTE:** A. **PUNTO RELEVANTE:** B.']
        groups = group_conclusion(paragraphs)
        self.assertEqual(list(groups), ['NO EXIGIDO EXPRESAMENTE', 'NO LOCALIZADO', 'PUNTO RELEVANTE'])
        self.assertEqual(groups['NO EXIGIDO EXPRESAMENTE'], ['Primer punto.', 'Segundo punto.'])
        self.assertEqual(groups['PUNTO RELEVANTE'], ['A.', 'B.'])
        self.assertEqual(group_conclusion(['Texto sin etiqueta.']), {'Síntesis': ['Texto sin etiqueta.']})

    def test_pdf_conclusion_prints_each_heading_once(self):
        self.report['conclusion'] = ['**NO EXIGIDO EXPRESAMENTE:** Primer punto.',
                                    '**NO EXIGIDO EXPRESAMENTE:** Segundo punto.']
        with tempfile.TemporaryDirectory() as directory:
            path = render_age_pdf(self.report, Path(directory)/'test.pdf', self.payload)
            text = '\n'.join(p.extract_text() for p in PdfReader(path).pages)
            self.assertEqual(text.count('NO EXIGIDO EXPRESAMENTE:'), 1)
            self.assertIn('Primer punto.', text)
            self.assertIn('Segundo punto.', text)

    def test_existing_json_runs_editor_without_extraction(self):
        import oportunidades as app
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)/'source.json'
            source.write_text(json.dumps(self.payload), encoding='utf-8')
            self._check_existing_json(app, source)

    def _check_existing_json(self, app, source):
        with patch('sys.argv', ['oportunidades.py', '--desde-json', str(source)]), \
             patch.object(app, 'ROOT', source.parent), patch.object(app, 'load_env_file'), patch.object(app, 'get_druid_config', return_value={}), \
             patch.object(app, 'authenticate_druid', return_value='token'), \
             patch.object(app, 'create_age_summary', return_value=Path('summary.pdf')) as editor, \
             patch.object(app, 'collect_documents') as collect, patch.object(app, 'run_agent_layers') as extract:
            self.assertEqual(app.main(), 0)
            editor.assert_called_once()
            self.assertEqual(editor.call_args.args[0]['expediente'], 'TEST-AGE')
            collect.assert_not_called()
            extract.assert_not_called()

    def setUp(self):
        self.payload = {'expediente': 'TEST-AGE', 'agentes': [{'id': 'NUEVO', 'contenido': 'fuente única'}],
                        'avisos_procesamiento': ['Anexo técnico no leído'], 'documentos_fuente': []}
        self.report = {'expediente': 'TEST-AGE', 'agentes_revisados': ['NUEVO'],
                       'introduccion': ['He revisado el expediente TEST-AGE.', 'Existen limitaciones de lectura.'],
                       'secciones': [{'titulo': 'Datos principales', 'bloques': [
                           {'tipo': 'tabla', 'columnas': ['Dato', 'Valor'],
                            'filas': [['Presupuesto', '**1.000 EUR**'], ['Fórmula', 'P = 45 x (PMIN / PO)']]}]}],
                       'conclusion': ['**NO LOCALIZADO:** el anexo técnico.']}

    def test_pdf_structure_and_warnings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = render_age_pdf(self.report, Path(directory)/'test.pdf', self.payload)
            reader = PdfReader(path)
            text = '\n'.join(p.extract_text() for p in reader.pages)
            self.assertTrue(text.lstrip('0123456789\n ').startswith('RESUMEN DE LICITACIÓN'))
            self.assertNotIn('PREGUNTA', text)
            self.assertNotIn('C2 - RESTRINGIDO', text)
            self.assertIn('Anexo técnico no leído', text)
            self.assertIn('1. Datos principales', text)
            self.assertIn('Conclusión operativa', text)
            self.assertEqual(tuple(reader.pages[0].mediabox)[2:], (612, 792))

    def test_reject_wrong_case_and_missing_agent(self):
        with self.assertRaises(ValueError):
            validate_report(dict(self.report, expediente='OTHER'), self.payload)
        with self.assertRaises(ValueError):
            validate_report(dict(self.report, agentes_revisados=[]), self.payload)

    def test_conclusion_as_last_section_is_preserved(self):
        conclusion = self.report.pop('conclusion')
        self.report['secciones'].append({'titulo': 'Conclusión operativa', 'bloques': [
            {'tipo': 'lista', 'elementos': conclusion}]})
        result = validate_report(self.report, self.payload)
        self.assertEqual(result['conclusion'], conclusion)
        self.assertEqual(len(result['secciones']), 1)
        self.assertNotIn('conclusion', self.report)
        self.assertEqual(validate_report(result, self.payload), result)

    def test_missing_and_conflicting_conclusions_are_rejected(self):
        missing = dict(self.report)
        missing.pop('conclusion')
        with self.assertRaises(ValueError):
            validate_report(missing, self.payload)
        self.report['secciones'].append({'titulo': 'Conclusión operativa', 'bloques': [
            {'tipo': 'parrafo', 'texto': 'Otra conclusión diferente'}]})
        with self.assertRaises(ValueError):
            validate_report(self.report, self.payload)

    def test_lists_and_inline_warnings(self):
        self.report['secciones'][0]['bloques'].append({'tipo': 'lista', 'elementos': ['Primera tarea', 'Segunda tarea']})
        self.report['conclusion'] = ['**PUNTO RELEVANTE:** Revisar anexo. AVISO DE PROCESAMIENTO: Anexo técnico no leído']
        with tempfile.TemporaryDirectory() as directory:
            path = render_age_pdf(self.report, Path(directory)/'test.pdf', self.payload)
            text = '\n'.join(p.extract_text() for p in PdfReader(path).pages)
            self.assertIn('Primera tarea', text)
            self.assertEqual(text.count('AVISO DE PROCESAMIENTO:'), 1)

    def test_narrow_tables_only(self):
        block = self.report['secciones'][0]['bloques'][0]
        block['columnas'] = ['A', 'B', 'C', 'D', 'E']
        block['filas'] = [['1'] * 5]
        with self.assertRaises(ValueError):
            validate_report(self.report, self.payload)

    def test_response_times_are_not_a_reserved_heading(self):
        self.report['secciones'][0]['titulo'] = 'Plazos de respuesta y entrega'
        validate_report(self.report, self.payload)
        self.report['secciones'][0]['titulo'] = 'PREGUNTA'
        with self.assertRaises(ValueError):
            validate_report(self.report, self.payload)

    def test_review_preserves_structure_and_adds_missing_detail(self):
        reviewed = apply_review(self.report, {'correcciones': [{'buscar': '1.000 EUR', 'reemplazar': '2.000 EUR'}],
                                            'anadidos': [{'seccion': 'Datos principales', 'bloque': {'tipo': 'parrafo', 'texto': 'Plazo documentado.'}}]})
        self.assertEqual(len(reviewed['secciones']), 1)
        self.assertEqual(reviewed['secciones'][0]['bloques'][0]['filas'][0][1], '**2.000 EUR**')
        self.assertEqual(reviewed['secciones'][0]['bloques'][-1]['texto'], 'Plazo documentado.')
        self.assertEqual(reviewed['conclusion'], self.report['conclusion'])
        with self.assertRaises(ValueError):
            apply_review(self.report, {'correcciones': [{'buscar': 'inexistente', 'reemplazar': 'otro'}], 'anadidos': []})

    def test_retry_preserves_entire_json(self):
        call = Mock(side_effect=['incomplete', json.dumps(self.report), '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as directory:
            generate_age_report(self.payload, Path(directory)/'test.pdf', {}, 'token', call)
        self.assertEqual(call.call_count, 3)
        for invocation in call.call_args_list:
            self.assertIn(json.dumps(self.payload, ensure_ascii=False, indent=2), invocation.args[1])

    def test_bad_review_retries_review_without_regenerating_draft(self):
        call = Mock(side_effect=[json.dumps(self.report),
                               '{"correcciones":[{"buscar":"No existe","reemplazar":"Otro"}],"anadidos":[]}',
                               '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as directory:
            generate_age_report(self.payload, Path(directory)/'test.pdf', {}, 'token', call)
        self.assertEqual(call.call_count, 3)
        self.assertIn('CONTRATO ESPECÍFICO', call.call_args_list[2].args[0])
        self.assertIn('No existe', call.call_args_list[2].args[1])

    def test_invalid_report_does_not_overwrite_existing_pdf(self):
        call = Mock(return_value='{}')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'test.pdf'
            render_age_pdf(self.report, path, self.payload)
            before = path.read_bytes()
            with self.assertRaises(RuntimeError):
                generate_age_report(self.payload, path, {}, 'token', call)
            self.assertEqual(path.read_bytes(), before)

    def test_three_unreadable_drafts_recover_all_agents_without_more_ai_calls(self):
        payload = {'expediente': 'RECOVERY', 'agentes': [
            {'id': f'A{i}', 'contenido': {'salida_original':
                f'# Materia {i}\nObligación única del agente {i}.\n\n'
                '| Perfil | Cantidad | Horas | Condición | Fuente |\n'
                '|---|---|---|---|---|\n'
                f'| Técnico {i} | 2 | 480 | Dato final {i} | Anexo {i} |'}}
            for i in range(1, 7)]}
        call = Mock(side_effect=['Texto sin JSON', '{"introduccion":["cortado"],',
                                 '{"secciones":[{"titulo":"Ficha"},'])
        with tempfile.TemporaryDirectory() as directory:
            path = generate_age_report(payload, Path(directory)/'recovered.pdf', {}, '', call)
            text = '\n'.join(p.extract_text() for p in PdfReader(path).pages)
            self.assertIn('REVISIÓN EDITORIAL PENDIENTE', text)
            for i in range(1, 7):
                self.assertIn(f'Obligación única del agente {i}', text)
                self.assertIn(f'Dato final {i}', text)
                self.assertIn(f'Anexo {i}', text)
            meta = json.loads(next(Path(directory).glob('diagnosticos/redaccion/*/composicion.json')).read_text(encoding='utf-8'))
            self.assertTrue(meta['revision_editorial_pendiente'])
            self.assertEqual(call.call_count, 3)

    def test_well_formed_but_invalid_reports_never_activate_recovery(self):
        payload = {'expediente': 'NO-RECOVERY', 'agentes': [
            {'id': f'A{i}', 'contenido': {'salida_original': '# Materia\nContenido'}}
            for i in range(1, 7)]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'report.pdf'
            with self.assertRaises(RuntimeError):
                generate_age_report(payload, path, {}, '', Mock(return_value='{}'))
            self.assertFalse(path.exists())
            self.assertFalse(list(Path(directory).glob('diagnosticos/redaccion/*/composicion.json')))
