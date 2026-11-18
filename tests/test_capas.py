import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import oportunidades as app
from capas import LAYER_ONE, LAYER_TWO_CONTEXT
from pypdf import PdfReader


class LayerTests(unittest.TestCase):
    def setUp(self):
        review_mock = patch('documentary_audit.review_extraction', side_effect=lambda aid, raw, *args: (raw, None))
        review_mock.start()
        self.addCleanup(review_mock.stop)
        self.recommendations_mock = patch.object(app, 'generate_recommendations', return_value=app.empty_recommendations())
        self.recommendations_mock.start()
        self.addCleanup(self.recommendations_mock.stop)
        self.tender = app.parse_tender_feed(app.DEFAULT_XML)[0]
        self.documents = [app.ExtractedDocument(
            app.DocumentRef("Pliego", "original.txt", "original.txt"),
            text="MARCADOR_DOCUMENTO_ORIGINAL",
        )]

    def run_mocked_pipeline(self, layer):
        order, processing_inputs = [], []
        processors = [
            "analyze_economic_financial_with_druid", "analyze_delivery_operations_with_druid",
            "analyze_document_coherence_with_druid", "analyze_risk_go_no_go_with_druid",
        ]
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch('documentary_audit.review_extraction', side_effect=lambda aid, raw, *args: (raw, None)))
            directory = Path(stack.enter_context(tempfile.TemporaryDirectory()))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            for aid, _, _, name in LAYER_ONE:
                def extract(*args, aid=aid):
                    order.append(aid)
                    self.assertIs(args[1], self.documents)
                    return f"EXTRACCION_{aid} | original.txt apartado 2"
                stack.enter_context(patch.object(app, name, side_effect=extract))
            for name in processors:
                def process(*args, name=name):
                    order.append(name)
                    docs = args[2] if name in processors[2:] else args[1]
                    processing_inputs.append(docs)
                    if name == processors[1]:
                        self.assertIn("EXTRACCION_A8", args[3])
                        self.assertIn("EXTRACCION_A10", args[4])
                    if name == processors[3]:
                        self.assertIn("Coherencia Documental", [title for title, _ in args[1]])
                    return "ANALISIS " + name
                stack.enter_context(patch.object(app, name, side_effect=process))
            save = stack.enter_context(patch.object(app, "save_summary", return_value=directory / "mock.md"))
            result = app.run_agent_layers(self.tender, self.documents, [], {}, "token", layer)
        return order, processing_inputs, result, save

    def test_layer_one_runs_only_eight_agents_and_uses_separate_outputs(self):
        order, inputs, result, save = self.run_mocked_pipeline("1")
        self.assertEqual(order, ["A1", "A2", "A3", "A4", "A6", "A8", "A9", "A10"])
        self.assertEqual(inputs, [])
        self.assertEqual(len(result), 8)
        self.assertTrue(all(c.kwargs["suffix"].startswith("_capa1") for c in save.call_args_list))

    def test_full_pipeline_separates_raw_sources_from_processing(self):
        order, inputs, result, save = self.run_mocked_pipeline("todas")
        self.assertEqual(order[:8], [row[0] for row in LAYER_ONE])
        self.assertEqual(len(order), 12)
        self.assertEqual(len(result), 12)
        for docs in inputs:
            self.assertEqual(len(docs), 7)
            combined = "\n".join(d.text for d in docs)
            self.assertNotIn("MARCADOR_DOCUMENTO_ORIGINAL", combined)
            self.assertNotIn("EXTRACCION_A1 |", combined)
            for aid in ["A2", "A3", "A4", "A6", "A8", "A9", "A10"]:
                self.assertIn(f"EXTRACCION_{aid} |", combined)
            self.assertIn("original.txt apartado 2", combined)
        self.assertFalse(any(c.kwargs["suffix"].startswith("_capa1") for c in save.call_args_list))

    def test_empty_extraction_stops_before_processing(self):
        with patch.object(app, "summarize_with_druid", return_value=" "), patch.object(
            app, "analyze_economic_financial_with_druid"
        ) as economic, contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(RuntimeError, "A1.*vacía"):
                app.run_agent_layers(self.tender, self.documents, [], {}, "token")
        economic.assert_not_called()

    def test_award_does_not_generate_or_append_simulations(self):
        with patch.object(app, "call_druid_gpt", return_value="Fórmula literal") as call, patch.object(
            app, "append_award_criteria_formula_simulations"
        ) as simulations, patch.object(app, "build_economic_formula_context") as inferred_formulas:
            self.assertEqual(app.analyze_award_criteria_with_druid(
                self.tender, self.documents, [], {}, "token"
            ), "Fórmula literal")
        simulations.assert_not_called()
        inferred_formulas.assert_not_called()
        self.assertNotIn("valores de ejemplo matematicos", call.call_args.args[1])

    def test_extraction_prompts_exclude_internal_dossier_and_cover_missing_domains(self):
        tender = next(t for t in app.parse_tender_feed(app.DEFAULT_XML) if t.contract_folder_id == "OPP-SW-011")
        builders = [app.build_prompt, app.build_profiles_prompt, app.build_solvency_prompt,
                    app.build_admin_legal_prompt, app.build_award_criteria_prompt,
                    app.build_service_design_itil_prompt, app.build_security_dpo_ens_prompt]
        for build in builders:
            prompt = build(tender, self.documents, [])
            self.assertNotIn("FIN-2025-042", prompt)
            self.assertNotIn("DOSSIER INTERNO SINTETICO", prompt)
        partners = app.build_purchases_partners_prompt(tender, self.documents, [], "PERFIL_INTERNO_SECRETO")
        self.assertNotIn("PERFIL_INTERNO_SECRETO", partners)
        summary = app.build_prompt(tender, [], [])
        self.assertIn("máximo 100 palabras", summary)
        self.assertNotIn("Veredicto ejecutivo general", summary)
        solvency = app.build_solvency_prompt(tender, [], []).lower()
        for field in ["volumen de negocio", "patrimonio", "ratios", "seguro", "exenciones", "sectorial"]:
            self.assertIn(field, solvency)
        admin = app.build_admin_legal_prompt(tender, [], []).lower()
        for field in ["presupuesto base", "facturación", "condiciones de pago", "procedimiento"]:
            self.assertIn(field, admin)

    def test_viability_prompts_require_every_source_document_field(self):
        prompts = "\n".join([
            app.build_solvency_prompt(self.tender, self.documents, []),
            app.build_profiles_prompt(self.tender, self.documents, []),
            app.build_admin_legal_prompt(self.tender, self.documents, []),
            app.build_security_dpo_ens_prompt(self.tender, self.documents, []),
            app.build_purchases_partners_prompt(self.tender, self.documents, [], ""),
        ]).lower()
        for field in [
            "volumen anual de negocios", "patrimonio neto", "seguro rc",
            "certificados de buena ejecución", "iso/ens", "partnerships",
            "perfiles", "rolece", "no exigido expresamente",
        ]:
            self.assertIn(field, prompts)

    def test_cli_accepts_layer_and_custom_xml(self):
        with patch("sys.argv", ["oportunidades.py", "--capa", "1", "--xml", "custom.xml"]):
            args = app.parse_args()
        self.assertEqual((args.capa, args.xml), ("1", "custom.xml"))
        self.assertEqual(args.formato, 'age')
        with patch("sys.argv", ["oportunidades.py"]):
            self.assertEqual(app.parse_args().capa, "1")

    def test_one_call_per_extractor_with_full_documents_and_no_fragment_review(self):
        full_text = 'INICIO ' + ('contenido documental ' * 2000) + ' FIN_DOCUMENTO'
        self.documents[0].text = full_text
        with tempfile.TemporaryDirectory() as folder, contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(app, 'ROOT', Path(folder)))
            stack.enter_context(patch.dict('os.environ', {'MAX_PROMPT_DOCUMENT_CHARS': '100'}))
            review = stack.enter_context(patch('documentary_audit.review_extraction'))
            recs = stack.enter_context(patch.object(app, 'generate_recommendations'))
            call = stack.enter_context(patch.object(app, 'call_druid_gpt', return_value='Respuesta directa de prueba.'))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            sections = app.run_agent_layers(self.tender, self.documents, [], {}, 'token', '1')
            self.assertEqual(call.call_count, 8)
            for invocation in call.call_args_list:
                self.assertIn(full_text, invocation.args[1])
            review.assert_not_called()
            recs.assert_not_called()
            self.assertFalse(sections.documentary_reviews)
            for record in sections.processing_records.values():
                self.assertEqual(record['modo'], 'prompt_unico_documentos_completos')
                self.assertFalse(record['documentos'][0]['texto_compactado'])

    def test_exact_capa1_command_saves_all_agents_and_generates_legible_pdf(self):
        config = {key: 'configured' for key in ('auth_url', 'gpt_url', 'username', 'password', 'tenant')}
        report = {'expediente': self.tender.contract_folder_id,
                  'agentes_revisados': [row[0] for row in LAYER_ONE],
                  'introduccion': ['Información del expediente.', 'Resumen de la extracción.'],
                  'secciones': [{'titulo': 'Datos principales', 'bloques': [{'tipo': 'parrafo',
                    'texto': 'Volumen de negocios, patrimonio, ratios, seguro, certificados de buena ejecución, '
                             'ISO, ENS, partnerships, fabricante, perfiles y ROLECE: datos de prueba.'}]}],
                  'conclusion': ['Conclusión de prueba.']}
        with tempfile.TemporaryDirectory() as folder, contextlib.ExitStack() as stack:
            root = Path(folder)
            stack.enter_context(patch.object(app, 'ROOT', root))
            stack.enter_context(patch.object(app, 'configure_console'))
            stack.enter_context(patch.object(app, 'load_env_file'))
            stack.enter_context(patch('sys.argv', ['oportunidades.py', '--capa', '1']))
            stack.enter_context(patch('builtins.input', return_value='1'))
            stack.enter_context(patch.object(app, 'get_druid_config', return_value=config))
            stack.enter_context(patch.object(app, 'authenticate_druid', return_value='token'))
            stack.enter_context(patch.object(app, 'collect_documents', return_value=(self.documents, [])))
            for aid, _, _, function in LAYER_ONE:
                stack.enter_context(patch.object(app, function, return_value=f'EXTRACCION_UNICA_{aid}'))
            call = stack.enter_context(patch.object(app, 'call_druid_gpt', side_effect=[
                json.dumps(report), '{"correcciones":[],"anadidos":[]}']))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            self.assertEqual(app.main(), 0)
            output = next((root / 'resumenes').iterdir())
            prefix = app.safe_filename(self.tender.contract_folder_id)
            payload = json.loads((output / f'{prefix}_capa1.json').read_text(encoding='utf-8'))
            self.assertEqual(len(payload['agentes']), len(LAYER_ONE))
            self.assertEqual(len(list((output / 'agentes').glob('*_respuesta.json'))), len(LAYER_ONE))
            for invocation in call.call_args_list:
                for aid, _, _, _ in LAYER_ONE:
                    self.assertIn(f'EXTRACCION_UNICA_{aid}', invocation.args[1])
            pdf = output / f'{prefix}_resumen_legible.pdf'
            text = '\n'.join(page.extract_text() for page in PdfReader(pdf).pages)
            self.assertIn('RESUMEN DE LICITACIÓN', text)
            self.assertIn('Conclusión operativa', text)
            self.assertEqual(len(list(output.glob('*.pdf'))), 1)
            self.assertEqual(len(list(output.glob('diagnosticos/redaccion/*/redaccion.json'))), 1)

    def test_main_keeps_loading_authentication_and_report_flow_in_both_modes(self):
        report = "\n".join(f"## {title}\nDato documental." for title in app.PURCHASES_REQUIRED_SECTIONS)
        config = {key: "configured" for key in ("auth_url", "gpt_url", "username", "password", "tenant")}
        for layer, count in (("1", 8), ("todas", 12)):
            with self.subTest(layer=layer), tempfile.TemporaryDirectory() as folder, contextlib.ExitStack() as stack:
                stack.enter_context(patch.object(app, "ROOT", Path(folder)))
                stack.enter_context(patch.object(app, "configure_console"))
                stack.enter_context(patch.object(app, "load_env_file"))
                stack.enter_context(patch("sys.argv", ["oportunidades.py", "--capa", layer, "--formato", "ejecutivo"]))
                stack.enter_context(patch("builtins.input", return_value="1"))
                stack.enter_context(patch.object(app, "get_druid_config", return_value=config))
                auth = stack.enter_context(patch.object(app, "authenticate_druid", return_value="token"))
                collect = stack.enter_context(patch.object(app, "collect_documents", return_value=(self.documents, [])))
                call = stack.enter_context(patch.object(app, "call_druid_gpt", return_value=report))
                renderer = stack.enter_context(patch.object(app, "create_age_summary", return_value=Path(folder) / "test.pdf"))
                stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
                self.assertEqual(app.main(), 0)
                auth.assert_called_once_with(config)
                collect.assert_called_once()
                self.assertEqual(call.call_count, count)
                for invocation in call.call_args_list[:8]:
                    self.assertIn("MARCADOR_DOCUMENTO_ORIGINAL", invocation.args[1])
                for invocation in call.call_args_list[8:]:
                    self.assertNotIn("MARCADOR_DOCUMENTO_ORIGINAL", invocation.args[1])
                    self.assertIn(LAYER_TWO_CONTEXT, invocation.args[0])
                run = next((Path(folder) / "resumenes").iterdir())
                outputs = list((run / "agentes").iterdir())
                renderer.assert_called_once()
                self.assertEqual(json.loads((run / "ejecucion.json").read_text(encoding="utf-8"))["estado"], "completada")
                responses = [__import__('json').loads(path.read_text(encoding='utf-8'))
                             for path in outputs if path.name.endswith('_respuesta.json')]
                self.assertEqual({r['id'] for r in responses if 'id' in r}, {row[0] for row in LAYER_ONE})
                self.assertEqual(len(responses), count)
                self.assertTrue(all(r['contenido']['salida_original'] == report for r in responses))
                for path in outputs:
                    if path.name.endswith('_respuesta.json'):
                        response = __import__('json').loads(path.read_text(encoding='utf-8'))
                        expected_layer = 1 if 'id' in response else 2
                        self.assertIn(f'_capa{expected_layer}_', path.name)
                        self.assertEqual(response['capa'], expected_layer)
                        self.assertEqual(path, app.agent_response_path(self.tender, response['nombre'], expected_layer, path.parent))

    def test_extractor_statuses_have_no_opportunity_score(self):
        for aid, title, _, _ in LAYER_ONE:
            status = app.classify_section_status(f"{aid} · {title}", "NO CUMPLE")
            self.assertIsNone(status["score"])

    def test_pdf_keeps_sources_partial_status_and_omits_recommendations(self):
        report = "| Dato | Fuente |\n|---|---|\n| 100 EUR | FUENTE_UNICA apartado 3 |"
        self.documents[0].error = "LECTURA PARCIAL"
        sections = [(f"{aid} · {title}", report) for aid, title, _, _ in LAYER_ONE]
        with tempfile.TemporaryDirectory() as folder, patch.object(app, "ROOT", Path(folder)):
            pdf = app.generate_final_report_pdf(self.tender, sections, self.documents, [], extraction_only=True)
            self.assertIn("_capa1_informe_final.pdf", pdf.name)
            text = "\n".join(p.extract_text() for p in PdfReader(pdf).pages)
        self.assertIn("FUENTE_UNICA", text)
        self.assertIn("LECTURA PARCIAL", text)
        for unwanted in ["Indice de oportunidad", "Importe recomendado", "Foco recomendado", "Semaforo por area"]:
            self.assertNotIn(unwanted, text)

    def test_layer1_json_is_ordered_api_contract_and_preserves_agent_information(self):
        sections = [
            (f"{aid} · {title}", f"## Resumen factual\nDato {aid}.\n\n## Datos no localizados\nNO CONSTA {aid}.\n\n| Requisito | Fuente | Página |\n|---|---|---|\n| Valor | pliego.pdf | 4 |")
            for aid, title, _, _ in LAYER_ONE
        ]
        payload = app.build_layer1_json(self.tender, self.documents, ["aviso"], sections)
        self.assertEqual(payload["schema"], "oportunidades.capa1.v1")
        self.assertEqual([agent["id"] for agent in payload["agentes"]], [row[0] for row in LAYER_ONE])
        self.assertEqual(payload["agentes"][0]["orden"], 1)
        self.assertEqual(payload["agentes"][1]["contenido"]["secciones"][0]["titulo"], "Resumen factual")
        self.assertEqual(payload["agentes"][1]["contenido"]["trazabilidad"][0]["Fuente"], "pliego.pdf")
        self.assertTrue(payload["agentes"][1]["contenido"]["pendientes_y_no_localizados"])
        self.assertIn("Dato A2", payload["agentes"][1]["contenido"]["salida_original"])

    def test_save_layer1_json_is_valid_utf8_json(self):
        sections = [(f"{aid} · {title}", "Información española: 100 €") for aid, title, _, _ in LAYER_ONE]
        with tempfile.TemporaryDirectory() as folder, patch.object(app, "ROOT", Path(folder)):
            path = app.save_layer1_json(self.tender, self.documents, [], sections)
            payload = __import__("json").loads(path.read_text(encoding="utf-8"))
        self.assertEqual(path.name, "OPP-SW-001_capa1.json")
        self.assertEqual(payload["agentes"][0]["contenido"]["salida_original"], "Información española: 100 €")


if __name__ == "__main__":
    unittest.main()
