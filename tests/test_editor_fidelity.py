import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from age_report import critical_source_lines, fidelity_issues, generate_age_report, validate_report, coverage_issues


class FidelityTests(unittest.TestCase):
    def test_certificate_correct_execution_is_not_a_missing_good_execution_block(self):
        good = 'Certificados de buena ejecución de los servicios previos.'
        correct = ('Certificado de correcta ejecución de los servicios o trabajos realizados, '
                   'expedido o visado por la entidad destinataria [PCAP, Anexo V p.79].')
        for source, present in ((good, correct), (correct, good), (correct, correct)):
            with self.subTest(source=source, present=present):
                self.assertFalse(any('certificados de buena ejecución' in s
                    for s in coverage_issues(self.report(present), self.payload(source))))
        # Una referencia genérica a ejecutar correctamente el servicio no es el documento.
        for source in (good, correct):
            self.assertTrue(any('certificados de buena ejecución' in s
                for s in coverage_issues(self.report('Se exige la correcta ejecución del servicio.'), self.payload(source))))

    def payload(self, text):
        return {'expediente': 'TEST', 'agentes': [{'id': 'A', 'contenido': {'salida_original': text}}]}

    def report(self, text):
        return {'expediente': 'TEST', 'agentes_revisados': ['A'],
                'introduccion': ['Información extraída.', 'Limitaciones documentales.'],
                'secciones': [{'titulo': 'Condiciones', 'bloques': [{'tipo': 'parrafo', 'texto': text}]}],
                'conclusion': ['Resumen de condiciones.']}

    def test_guarantee_state_and_separate_complementary(self):
        payload = self.payload('Garantía provisional | No exigida | PCAP 11.A')
        self.assertTrue(fidelity_issues(self.report('Garantía provisional: no localizada.'), payload))
        self.assertFalse(fidelity_issues(self.report(
            'Garantía provisional: no exigida. Garantía complementaria: no localizada.'), payload))
        self.assertFalse(fidelity_issues(self.report('No se exige garantía provisional.'), payload))

    def test_no_invented_absence_without_source(self):
        payload = self.payload('Garantía provisional: no localizada')
        self.assertFalse(fidelity_issues(self.report('Garantía provisional: no localizada'), payload))

    def test_unrelated_absence_does_not_contaminate_guarantee(self):
        payload = self.payload('Garantía provisional: no exigida')
        report = self.report('Condiciones.')
        report['conclusion'] = ['**NO EXIGIDO:** No se exige garantía provisional.',
                                '**NO LOCALIZADO:** No constan requisitos de hardware.']
        self.assertFalse(fidelity_issues(report, payload))
        report['conclusion'] = ['Resumen.']
        report['secciones'][0]['bloques'] = [{'tipo': 'lista', 'elementos': [
            'No se exige garantía provisional.', 'Seguro RC: no localizado.']}]
        self.assertFalse(fidelity_issues(report, payload))
        report['secciones'][0]['bloques'] = [{'tipo': 'parrafo', 'texto':
            'No se exige garantía provisional. No consta hardware.'}]
        self.assertFalse(fidelity_issues(report, payload))

    def test_guarantee_table_keeps_state_in_same_row(self):
        report = self.report('Condiciones.')
        report['secciones'][0]['bloques'] = [{'tipo': 'tabla', 'columnas': ['Requisito', 'Estado'],
            'filas': [['Garantía provisional', 'No exigida'], ['Hardware', 'No localizado']]}]
        self.assertFalse(fidelity_issues(report, self.payload('Garantía provisional: no exigida')))
        report['secciones'][0]['bloques'][0]['filas'][0][1] = 'No localizada'
        self.assertTrue(fidelity_issues(report, self.payload('Garantía provisional: no exigida')))

    def test_editor_archives_input_and_invalid_raw_response(self):
        payload = self.payload('Fuente única')
        call = Mock(side_effect=['{malformed', json.dumps(self.report('Resumen.')),
                                '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as directory, patch('age_report.render_age_pdf'):
            generate_age_report(payload, Path(directory)/'test.pdf', {}, 'token', call)
            archive = next((Path(directory)/'diagnosticos/redaccion').iterdir())
            read = lambda name: json.loads((archive/name).read_text(encoding='utf-8'))
            self.assertEqual(read('entrada_completa.json'), payload)
            self.assertEqual(read('agente_01.json'), payload['agentes'][0])
            self.assertEqual(read('borrador_1.json')['respuesta_original'], '{malformed')
            self.assertIn('error_json', read('borrador_1.json'))
            self.assertIn('json', read('borrador_2_revision_1.json'))

    def test_global_certainty_is_rejected(self):
        self.assertTrue(fidelity_issues(self.report('La conclusión es de ALTA CERTEZA.'), self.payload('Datos')))

    def test_conflict_keeps_both_versions(self):
        payload = self.payload('Garantía provisional: no exigida (PCAP)\nGarantía provisional: no localizada (PPT)')
        self.assertFalse(fidelity_issues(self.report(
            'Garantía provisional: discrepancia; no exigida según PCAP, no localizada según PPT.'), payload))

    def test_acknowledgement_not_satisfied_by_unrelated_deadline(self):
        payload = self.payload('| Confirmación de solicitud | <24h | PPT p.10 |')
        self.assertTrue(fidelity_issues(self.report('Resolución en 24 horas.'), payload))
        self.assertTrue(fidelity_issues(self.report('Confirmación en 48 horas.'), payload))
        self.assertFalse(fidelity_issues(self.report('Confirmación en menos de 24 horas [PPT p.10].'), payload))
        self.assertIn('<24h', critical_source_lines(payload)[0])

    def test_overlap_and_rolece_effect(self):
        payload = self.payload('No se acumulan periodos de experiencia coincidentes en el tiempo.\n'
                               'ROLECE | Alternativa | Exime documentación | PCP 23.4')
        self.assertEqual(len(fidelity_issues(self.report('Experiencia puntuable; ROLECE no obligatorio.'), payload)), 2)
        self.assertFalse(fidelity_issues(self.report(
            'No se acumulan periodos solapados. ROLECE puede eximir documentación [PCP 23.4].'), payload))

    def test_structured_source_is_also_checked(self):
        payload = self.payload('')
        payload['agentes'][0]['contenido'] = {'filas': [['Garantía provisional', 'No exigida']]}
        self.assertTrue(fidelity_issues(self.report('Garantía provisional: no localizada.'), payload))

    def test_rolece_solvency_absence_does_not_invent_documentary_effect(self):
        payload = self.payload('NO CONSTA EN LA DOCUMENTACION REVISADA: exención de solvencia por ROLECE.')
        self.assertFalse(fidelity_issues(self.report('ROLECE: no consta exención de solvencia.'), payload))

    def test_fidelity_failure_retries_review_only(self):
        payload = self.payload('Garantía provisional: no exigida')
        report = self.report('Garantía provisional: no localizada')
        call = Mock(side_effect=[json.dumps(report), '{"correcciones":[],"anadidos":[]}',
            json.dumps({'correcciones': [{'buscar': 'no localizada', 'reemplazar': 'no exigida'}], 'anadidos': []})])
        with tempfile.TemporaryDirectory() as directory, patch('age_report.render_age_pdf') as render:
            generate_age_report(payload, Path(directory)/'test.pdf', {}, 'token', call)
            self.assertEqual(call.call_count, 3)
            self.assertIn('Control de fidelidad pendiente', call.call_args_list[2].args[1])
            render.assert_called_once()

    def test_failed_fidelity_never_publishes(self):
        payload = self.payload('Garantía provisional: no exigida')
        call = Mock(side_effect=([json.dumps(self.report('Garantía provisional: no localizada'))] +
                    ['{"correcciones":[],"anadidos":[]}'] * 3) * 3)
        with tempfile.TemporaryDirectory() as directory, patch('age_report.render_age_pdf') as render:
            with self.assertRaises(RuntimeError):
                generate_age_report(payload, Path(directory)/'test.pdf', {}, 'token', call)
            render.assert_not_called()

    def test_incomplete_draft_reaches_review_and_keeps_partial_repairs(self):
        payload = self.payload('Patrimonio neto: no localizado.\nCertificados de buena ejecución: no localizados.')
        report = self.report('Condiciones del expediente.')
        additions = lambda text: json.dumps({'correcciones': [], 'anadidos': [
            {'seccion': 'Condiciones', 'bloque': {'tipo': 'parrafo', 'texto': text}}]})
        call = Mock(side_effect=[json.dumps(report), additions('Patrimonio neto: no localizado.'),
                                additions('Certificados de buena ejecución: no localizados.')])
        with tempfile.TemporaryDirectory() as directory, patch('age_report.render_age_pdf') as render:
            generate_age_report(payload, Path(directory)/'test.pdf', {}, 'token', call)
            final = render.call_args.args[0]
            self.assertFalse(coverage_issues(final, payload))
            self.assertEqual(len(final['secciones'][0]['bloques']), 3)
            self.assertEqual(call.call_count, 3)
            first_review = call.call_args_list[1].args[1]
            self.assertIn('bloque requerido: patrimonio', first_review)
            self.assertIn('bloque requerido: certificados', first_review)
            retry = call.call_args_list[2].args[1]
            self.assertIn('Patrimonio neto: no localizado.', retry.split('BORRADOR:\n')[1])
            self.assertNotIn('bloque requerido: patrimonio', retry)

    def test_missing_coverage_still_blocks_publication(self):
        payload = self.payload('Patrimonio neto: no localizado.')
        report = self.report('Condiciones.')
        with self.assertRaises(ValueError):
            validate_report(report, payload)
        validate_report(report, payload, require_coverage=False)
        call = Mock(side_effect=([json.dumps(report)] + ['{"correcciones":[],"anadidos":[]}'] * 3) * 3)
        with tempfile.TemporaryDirectory() as directory, patch('age_report.render_age_pdf') as render:
            with self.assertRaises(RuntimeError):
                generate_age_report(payload, Path(directory)/'test.pdf', {}, 'token', call)
            render.assert_not_called()

    def test_structure_and_identity_still_required_for_draft(self):
        report = self.report('Condiciones.')
        report['expediente'] = 'OTHER'
        with self.assertRaises(ValueError):
            validate_report(report, self.payload('Datos'), require_coverage=False)
