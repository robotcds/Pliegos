import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import oportunidades as app
from capas import LAYER_ONE
from recommendations import generate_recommendations
from revision_points import editorial_payload


def proposal(candidates=None):
    return {'titulo': 'Evaluar candidatura', 'recomendacion': 'Contrastar experiencia de gestión.',
            'fundamento': 'El puesto requiere gestión de proyectos; el inventario declara experiencia.',
            'evidencias': ['Inventario de perfiles y apartado Equipo del informe'],
            'candidatos': candidates or [], 'pendientes': ['Acreditar experiencia sectorial y disponibilidad.']}


class RecommendationsTests(unittest.TestCase):
    def test_candidate_and_fictitious_status(self):
        context = {'empresa_ficticia': {'perfiles': [{'nombre': 'Ana Torres'}]}}
        call = Mock(return_value=json.dumps({'recomendaciones': [proposal(['Ana Torres'])]}))
        result = generate_recommendations('Perfiles y equipo', 'Equipo requerido.', context, {}, 'token', call)
        self.assertEqual(result['estado_recomendaciones'], 'generadas')
        self.assertEqual(result['recomendaciones'][0]['candidatos'], ['Ana Torres'])
        self.assertEqual(result['recomendaciones'][0]['contexto_empresarial'], 'ficticio_no_acreditativo')
        self.assertIn('Ana Torres', call.call_args.args[1])

    def test_invalid_candidate_is_retried_and_diagnosed_without_inventing(self):
        call = Mock(return_value=json.dumps({'recomendaciones': [proposal(['Persona inexistente'])]}))
        result = generate_recommendations('Equipo', 'Texto', {'empresa_ficticia': {}}, {}, 'token', call)
        self.assertEqual(call.call_count, 2)
        self.assertEqual(result['estado_recomendaciones'], 'error')
        self.assertEqual(result['recomendaciones'], [])
        self.assertEqual(len(result['diagnostico_recomendaciones']), 2)

    def test_bad_json_recovered_and_transport_failure_nonfatal(self):
        call = Mock(side_effect=['prosa', '{"recomendaciones":[]}'])
        result = generate_recommendations('Agente', 'Texto', {}, {}, 'token', call)
        self.assertEqual(result['estado_recomendaciones'], 'sin_propuestas')
        self.assertEqual(len(result['diagnostico_recomendaciones']), 1)
        failed = generate_recommendations('Agente', 'Texto', {}, {}, 'token', Mock(side_effect=RuntimeError('offline')))
        self.assertEqual(failed['estado_recomendaciones'], 'error')

    def test_all_twelve_agents_persist_same_recommendations_without_editorial_leak(self):
        processors = ['analyze_economic_financial_with_druid', 'analyze_delivery_operations_with_druid',
                      'analyze_document_coherence_with_druid', 'analyze_risk_go_no_go_with_druid']
        tender = app.parse_tender_feed(app.DEFAULT_XML)[0]
        raw = '## Requisitos\nContenido documental original.'
        response = proposal()
        response['recomendacion'] = 'MARCADOR_RECOMENDACION_EXCLUSIVA_JSON'
        with tempfile.TemporaryDirectory() as folder, contextlib.ExitStack() as stack:
            stack.enter_context(patch('documentary_audit.review_extraction', side_effect=lambda aid, raw, *args: (raw, None)))
            stack.enter_context(patch.object(app, 'ROOT', Path(folder)))
            for fn in [row[3] for row in LAYER_ONE] + processors:
                stack.enter_context(patch.object(app, fn, return_value=raw))
            call = stack.enter_context(patch.object(app, 'call_druid_gpt', return_value=json.dumps({'recomendaciones': [response]})))
            with contextlib.redirect_stdout(io.StringIO()):
                sections = app.run_agent_layers(tender, [], [], {}, 'token', 'todas')
                path = app.save_consolidated_json(tender, [], [], sections)
            payload = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(call.call_count, 12)
            agents = payload['agentes'] + payload['analisis_capa2']
            records = [json.loads(p.read_text(encoding='utf-8')) for p in path.parent.glob('*_respuesta.json')]
            self.assertEqual(len(records), 12)
            for agent in agents:
                record = next(r for r in records if r['nombre'] == agent['nombre'])
                self.assertEqual(record['recomendaciones'], agent['recomendaciones'])
                self.assertEqual(agent['contenido']['salida_original'], raw)
                self.assertEqual(agent['estado_recomendaciones'], 'generadas')
            self.assertNotIn('MARCADOR_RECOMENDACION_EXCLUSIVA_JSON', json.dumps(editorial_payload(payload)))
            self.assertTrue(all(content == raw for _, content in sections))

    def test_contexts_are_specialized(self):
        self.assertIn('perfiles', app.recommendation_company_context('Perfiles y equipo'))
        self.assertIn('finanzas', app.recommendation_company_context('Economico-financiero'))
        self.assertNotIn('perfiles', app.recommendation_company_context('Seguridad y protección de datos'))
