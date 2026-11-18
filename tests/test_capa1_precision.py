"""Regresiones de cobertura de prompts, persistencia y entrada editorial (sin Druid)."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import oportunidades as app
from age_report import generate_age_report
from capas import LAYER_ONE, LAYER_ONE_DOCUMENT_KEYS


DETAIL = """## Documentación por fase
| Obligación | Fase de acreditación | Plazo | Fuente |
| --- | --- | --- | --- |
| Compromiso de adscripción | Oferta, archivo técnico | Cierre de ofertas | PCAP 8 |
| Prueba de disponibilidad | Requerimiento al propuesto adjudicatario | 7 días hábiles desde notificación | PCAP 12 |
## Costes y continuidad
La cobertura de vacaciones es a cargo del adjudicatario; el número de suplentes NO CONSTA.
La bolsa de 240 horas solo se factura por consumo autorizado; no es ingreso garantizado.
## Discrepancias y pendientes de aclaración
PENDIENTE DE ACLARACION: PPT 4 fija incorporación en 5 días; PCAP 9 fija 10 días para el mismo hito.
"""


class LayerOnePrecisionTests(unittest.TestCase):
    def setUp(self):
        self.tender = app.parse_tender_feed(app.DEFAULT_XML)[0]

    def test_specialist_contract_reaches_system_and_user_prompts(self):
        cases = [
            (app.build_admin_legal_system_prompt, app.build_admin_legal_prompt,
             ['facturar y cobrar', 'propuesto adjudicatario', 'garantía del servicio']),
            (app.build_solvency_system_prompt, app.build_solvency_prompt,
             ['momento de cumplimiento', 'mínimo por referencia']),
            (app.build_award_criteria_system_prompt, app.build_award_criteria_prompt,
             ['número de ofertas', 'grupos empresariales', 'extremos abiertos/cerrados']),
            (app.build_profiles_system_prompt, app.build_profiles_prompt,
             ['bolsa de horas no es', 'vacaciones y bajas', 'solapamientos']),
            (app.build_service_design_itil_system_prompt, app.build_service_design_itil_prompt,
             ['inicio/parada del reloj', 'colaboración con sucesor', 'ventanas de mantenimiento']),
            (app.build_security_dpo_ens_system_prompt, app.build_security_dpo_ens_prompt,
             ['destinatario/canal', 'copias de respaldo', 'certificado de']),
            (app.build_purchases_partners_system_prompt,
             lambda t, d, w: app.build_purchases_partners_prompt(t, d, w, ''),
             ['quién aporta, paga', 'Importe desconocido', 'Ausencia de carta']),
        ]
        for system, user, terms in cases:
            with self.subTest(agent=system.__name__):
                for prompt in (system(), user(self.tender, [], [])):
                    for term in terms:
                        self.assertIn(term, prompt)
                    self.assertIn('no un hecho\n  técnico verificado', prompt)
                    self.assertIn('dos cláusulas', prompt)
                    self.assertIn('DOSSIER DOCUMENTAL COMPLETO PARA PREVENTA', prompt)
                    self.assertIn('EXTRACCIÓN ATÓMICA', prompt)
                    self.assertIn('No hay objetivo de', prompt)
                    self.assertIn('COMPROBACIONES DE A', prompt)
                    self.assertIn('obligación esencial', prompt)
                    self.assertNotIn('decir que no se exige fabricante, canal, partnership ni carta', prompt)
                    self.assertNotIn('Estados permitidos: ENCONTRADO EN EL PLIEGO, NO EXIGIDO/NO CONSTA', prompt)
        self.assertIn('máximo 100 palabras', app.build_system_prompt())
        self.assertIn('momento de cumplir', app.build_system_prompt())

    def test_details_and_real_processing_records_survive_individual_and_consolidated_json(self):
        docs = [app.ExtractedDocument(app.DocumentRef('Pliego', 'PCAP', 'pcap.txt'),
                                      text='Texto contractual. ' * 2000),
                app.ExtractedDocument(app.DocumentRef('Anexo', 'Anexo ausente', ''),
                                      error='Referencia sin URL')]
        warnings = ['Referencia sin URL: Anexo ausente']
        with tempfile.TemporaryDirectory() as folder, contextlib.ExitStack() as stack:
            stack.enter_context(patch('documentary_audit.review_extraction', side_effect=lambda aid, raw, *args: (raw, None)))
            stack.enter_context(patch.object(app, 'ROOT', Path(folder)))
            stack.enter_context(patch.dict('os.environ', {'MAX_PROFILES_PROMPT_DOCUMENT_CHARS': '3000'}))
            stack.enter_context(patch.object(app, 'generate_recommendations', return_value=app.empty_recommendations()))
            for _, _, _, name in LAYER_ONE:
                stack.enter_context(patch.object(app, name, return_value=DETAIL))
            with contextlib.redirect_stdout(io.StringIO()):
                sections = app.run_agent_layers(self.tender, docs, warnings, {}, 'token', '1')
                output = app.save_layer1_json(self.tender, docs, warnings, sections)
            payload = json.loads(output.read_text(encoding='utf-8'))
            for agent in payload['agentes']:
                record = json.loads(app.agent_response_path(
                    self.tender, agent['nombre'], 1, output.parent).read_text(encoding='utf-8'))
                self.assertEqual(record['contenido'], agent['contenido'])
                self.assertEqual(record['registro_procesamiento'], agent['registro_procesamiento'])
                self.assertEqual(record['contenido']['salida_original'], DETAIL)
                rows = record['contenido']['secciones'][0]['tablas'][0]['filas']
                self.assertEqual(rows[1]['Fase de acreditación'], 'Requerimiento al propuesto adjudicatario')
                self.assertIn('7 días hábiles', rows[1]['Plazo'])
                self.assertIn('Discrepancias', record['contenido']['pendientes_y_no_localizados'][1]['titulo'])
                _, expected_index = app.build_documents_prompt_blocks(docs, LAYER_ONE_DOCUMENT_KEYS[agent['id']])
                self.assertEqual(record['registro_procesamiento']['documentos'], expected_index)
                self.assertEqual(record['registro_procesamiento']['avisos'], warnings)
            profiles = next(a for a in payload['agentes'] if a['id'] == 'A8')
            self.assertFalse(profiles['registro_procesamiento']['documentos'][0]['texto_compactado'])
            self.assertEqual(profiles['registro_procesamiento']['documentos'][1]['error'], 'Referencia sin URL')

    def test_old_extraction_has_no_fabricated_processing_record(self):
        payload = app.build_layer1_json(self.tender, [], [], [('A1 · Resumen breve', 'Texto')])
        self.assertTrue(all('registro_procesamiento' not in agent for agent in payload['agentes']))

    def test_editor_and_review_receive_details_without_recommendations(self):
        payload = {'expediente': 'TEST', 'agentes': [{
            'id': 'A2', 'contenido': app.markdown_report_to_json(DETAIL),
            'recomendaciones': [{'recomendacion': 'RECOMENDACION_AJENA_AL_RESUMEN'}],
            'registro_procesamiento': {'origen': 'registro_local_de_esta_extraccion', 'documentos': [], 'avisos': []},
        }]}
        report = {'expediente': 'TEST', 'agentes_revisados': ['A2'],
                  'introduccion': ['Datos documentales.', 'Condiciones del servicio.'],
                  'secciones': [{'titulo': 'Condiciones', 'bloques': [
                      {'tipo': 'parrafo', 'texto': 'Bolsa facturable por consumo autorizado. La cobertura de vacaciones es a cargo del adjudicatario; número de suplentes no localizado.'}]}],
                  'conclusion': ['Discrepancia entre PCAP 9 y PPT 4 pendiente de aclaración.']}
        call = Mock(side_effect=[json.dumps(report), '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as folder, patch('age_report.render_age_pdf') as render:
            generate_age_report(payload, Path(folder)/'summary.pdf', {}, 'token', call)
            render.assert_called_once()
            for invocation in call.call_args_list:
                system, user = invocation.args[:2]
                self.assertIn('errores/omisiones del borrador', system)
                self.assertIn('SÍNTESIS COMPLETA, NO RECORTE DE CONDICIONES', system)
                self.assertIn('BAREMOS COMPLETOS', system)
                self.assertIn('Un encabezado o una palabra coincidente no acreditan cobertura', system)
                self.assertIn('tablas\nde 2-4 columnas', system)
                self.assertIn('7 días hábiles desde notificación', user)
                self.assertIn('bolsa de 240 horas', user)
                self.assertIn('registro_local_de_esta_extraccion', user)
                self.assertNotIn('RECOMENDACION_AJENA_AL_RESUMEN', user)
            saved = next((Path(folder)/'diagnosticos/redaccion').glob('*/entrada_completa.json'))
            self.assertEqual(json.loads(saved.read_text(encoding='utf-8')), payload)


if __name__ == '__main__':
    unittest.main()
