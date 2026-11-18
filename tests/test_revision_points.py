import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import oportunidades as app
from age_report import generate_age_report
from capas import LAYER_ONE
from revision_points import editorial_payload, extract_review_points, collect_review_points


class ReviewPointsTests(unittest.TestCase):
    def setUp(self):
        review_mock = patch('documentary_audit.review_extraction', side_effect=lambda aid, raw, *args: (raw, None))
        review_mock.start()
        self.addCleanup(review_mock.stop)

        mock = patch.object(app, 'generate_recommendations', return_value=app.empty_recommendations())
        mock.start()
        self.addCleanup(mock.stop)
    def test_at_most_five_groups_preserve_all_details_and_prioritize(self):
        content = '''## Revisión
- No consta plazo de sustitución del personal.
- No consta horario del equipo.
- Coste de licencias pendiente de validar.
- No consta fórmula de puntuación.
- No consta solvencia mínima.
- No consta plazo de notificación de brechas de seguridad.
- Documento ausente: anexo de condiciones adicionales.
- No consta idioma de las comunicaciones.'''
        raw = collect_review_points(content)
        grouped = extract_review_points(content)
        self.assertLessEqual(len(grouped), 5)
        self.assertEqual(sum(len(p['subpuntos']) for p in grouped), len(raw))
        self.assertEqual(grouped[0]['subpuntos'][0]['tipo'], 'verificacion_documental')
        self.assertEqual({p['evidencia'] for p in raw},
                         {s['evidencia'] for g in grouped for s in g['subpuntos']})
        self.assertTrue(any(len(p['subpuntos']) > 1 for p in grouped))
        self.assertEqual(extract_review_points('Sin pendientes.'), [])
        self.assertEqual(grouped, extract_review_points(content))

    def test_mixed_case_headings_preserve_distinct_unknowns(self):
        points = collect_review_points('''6. Identidad, accesos y privilegios
NO CONSTA EN LA DOCUMENTACION REVISADA
7. Vulnerabilidades, parcheado y desarrollo seguro
NO CONSTA EN LA DOCUMENTACION REVISADA
12. Datos no localizados o ambiguos
- No se exige DPO ni se define un canal de contacto.
Ambigüedades y datos no localizados
- Coste pendiente de validar.''')
        self.assertEqual(len(points), 4)
        self.assertEqual(points[0]['seccion'], 'Identidad, accesos y privilegios')
        self.assertEqual(points[1]['seccion'], 'Vulnerabilidades, parcheado y desarrollo seguro')
        self.assertIn('canal de contacto', points[2]['detalle'])

    def test_second_layer_individuals_match_consolidated(self):
        from contextlib import ExitStack, redirect_stdout
        import io
        tender = app.parse_tender_feed(app.DEFAULT_XML)[0]
        functions = ['analyze_economic_financial_with_druid', 'analyze_delivery_operations_with_druid',
                     'analyze_document_coherence_with_druid', 'analyze_risk_go_no_go_with_druid']
        with tempfile.TemporaryDirectory() as folder, patch.object(app, 'ROOT', Path(folder)):
            with ExitStack() as stack, redirect_stdout(io.StringIO()):
                for function in [row[3] for row in LAYER_ONE] + functions:
                    stack.enter_context(patch.object(app, function, return_value='## Costes\n- Coste no acreditado.'))
                sections = app.run_agent_layers(tender, [], [], {}, 'token', 'todas')
                path = app.save_consolidated_json(tender, [], [], sections)
            payload = json.loads(path.read_text(encoding='utf-8'))
            singles = [json.loads(p.read_text(encoding='utf-8'))
                       for p in path.parent.glob('*_respuesta.json')]
            self.assertEqual(len(singles), 12)
            self.assertEqual(len(payload['analisis_capa2']), 4)
            for agent in payload['analisis_capa2']:
                saved = next(a for a in singles if a['nombre'] == agent['nombre'])
                self.assertEqual(saved['puntos_revision'], agent['puntos_revision'])
                self.assertEqual(saved['contenido'], agent['contenido'])
                self.assertEqual(agent['puntos_revision'][0]['tipo'], 'dato_no_concretado')
            filtered = editorial_payload(payload)
            self.assertTrue(all('puntos_revision' not in a for a in filtered['analisis_capa2']))
            self.assertEqual(filtered['analisis_capa2'][0]['contenido'], payload['analisis_capa2'][0]['contenido'])

    def test_unknowns_in_bullets_tables_and_numbered_sections_keep_context(self):
        result = collect_review_points('''1. DATOS PENDIENTES
- No consta plazo de sustitución. PPT p. 11.
| Requisito | Vigencia | Fuente |
|---|---|---|
| Certificado | NO CONSTA | PCAP 4 |
2. SEGURIDAD
NO CONSTA EN LA DOCUMENTACION REVISADA
3. REVERSIBILIDAD
NO CONSTA EN LA DOCUMENTACION REVISADA''')
        self.assertEqual(len(result), 4)
        self.assertIn('Certificado', result[1]['detalle'])
        self.assertIn('PCAP 4', result[1]['evidencia'])
        self.assertEqual(result[3]['seccion'], 'REVERSIBILIDAD')

    def test_explicit_exemption_and_negative_discrepancy_are_not_pending(self):
        self.assertEqual(collect_review_points(
            '- Garantía provisional: no exigida.\n- No se detectan contradicciones.'), [])
        points = collect_review_points('- Seguro: NO EXIGIDO/NO CONSTA EN EL PLIEGO')
        self.assertEqual(points[0]['tipo'], 'estado_ambiguo')

    def test_partial_sources_and_duplicate_bullets(self):
        points = collect_review_points('- Documento ausente: anexo 2.\n- Documento ausente: anexo 2.')
        self.assertEqual(len(points), 1)
        self.assertEqual(points[0]['tipo'], 'verificacion_documental')
        points = collect_review_points('## Costes\nNO ACREDITADO\n## Viabilidad\nNO EVALUABLE')
        self.assertEqual(len(points), 2)

    def test_all_agents_get_field_in_consolidated_and_individual_json(self):
        tender = app.parse_tender_feed(app.DEFAULT_XML)[0]
        with tempfile.TemporaryDirectory() as folder, patch.object(app, 'ROOT', Path(folder)):
            from contextlib import ExitStack, redirect_stdout
            import io
            with ExitStack() as stack, redirect_stdout(io.StringIO()):
                for _, _, _, function in LAYER_ONE:
                    stack.enter_context(patch.object(app, function, return_value='- No consta plazo.'))
                sections = app.run_agent_layers(tender, [], [], {}, 'token', '1')
            payload = app.build_layer1_json(tender, [], [], sections)
            singles = list((Path(folder) / 'resumenes').glob('*_respuesta.json'))
            self.assertEqual(len(singles), 8)
            for path in singles:
                self.assertTrue(json.loads(path.read_text(encoding='utf-8'))['puntos_revision'])
            self.assertTrue(all(a['puntos_revision'] for a in payload['agentes']))

    def test_review_metadata_is_never_sent_to_editor_even_on_retry(self):
        payload = {'expediente': 'TEST', 'agentes': [{'id': 'A1',
                   'contenido': {'salida_original': 'Texto original.'},
                   'puntos_revision': [{'detalle': 'MARCADOR_SOLO_JSON'}]}]}
        payload['analisis_capa2'] = [{'nombre': 'Economico-financiero',
            'contenido': {'salida_original': 'Costes originales.'},
            'puntos_revision': [{'detalle': 'MARCADOR_CAPA2_SOLO_JSON'}]}]
        filtered = editorial_payload(payload)
        self.assertNotIn('puntos_revision', filtered['agentes'][0])
        self.assertIn('puntos_revision', payload['agentes'][0])
        call = Mock(return_value='{}')
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(RuntimeError):
                generate_age_report(payload, Path(folder) / 'test.pdf', {}, 'token', call)
            archive = next(Path(folder).glob('diagnosticos/redaccion/*/entrada_completa.json'))
            self.assertEqual(json.loads(archive.read_text(encoding='utf-8')), payload)
        for invocation in call.call_args_list:
            self.assertNotIn('MARCADOR_SOLO_JSON', invocation.args[1])
            self.assertNotIn('MARCADOR_CAPA2_SOLO_JSON', invocation.args[1])
            self.assertIn('Costes originales.', invocation.args[1])
            self.assertIn('Texto original.', invocation.args[1])
