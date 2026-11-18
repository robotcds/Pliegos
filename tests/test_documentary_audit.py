import contextlib
import io
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import Mock, patch

import oportunidades as app
from documentary_audit import TOPICS, CONFLICT_CHECKS, validate_audit, review_extraction, editorial_record_issues, fragment_sources, select_fragments, resolve_evidence, check_criterion_labels, temporal_bounds, validate_all_records
from age_report import apply_review, coverage_issues, render_age_pdf
from capas import LAYER_ONE


SOURCE = ('Se facturará por trimestres vencidos. El pago será de 30 días naturales desde '
          'el acta si la factura se presenta en 15 días; en otro caso desde su presentación. '
          'No se exige garantía provisional. El equipo se valorará con máximo 5 puntos. '
          'El equipo de soporte tendrá un máximo de 6 puntos.')


class DocumentaryAuditTests(unittest.TestCase):
    def setUp(self):
        self.docs = [app.ExtractedDocument(app.DocumentRef('Pliego', 'PCP', ''), text=SOURCE)]
        self.audit = {'registros': [dict(id=f'A2-{i}', tema=topic, estado='NO_LOCALIZADO',
                                        detalle='No se ha localizado detalle de ' + topic + '.', evidencias=[])
                                   for i, topic in enumerate(TOPICS['A2'], 1)]}

    def fact(self, detail, quote, state='CONSTA'):
        self.audit['registros'][0].update(estado=state, detalle=detail, evidencias=[
            {'documento': 1, 'ubicacion': 'Cláusula económica', 'literal': quote}])

    def test_citations_accept_layout_whitespace_not_invented_numbers(self):
        self.fact('Facturación trimestral.', 'Se facturará por\ntrimestres vencidos.')
        validate_audit(self.audit, 'A2', self.docs)
        self.audit['registros'][0]['evidencias'][0]['literal'] = 'Se facturará por meses vencidos.'
        with self.assertRaisesRegex(ValueError, 'no localizada'):
            validate_audit(self.audit, 'A2', self.docs)

    def test_retry_locates_exemption_in_different_fragment(self):
        docs = [app.ExtractedDocument(app.DocumentRef('PCP', 'PCP', ''), text=
            '[Pagina PDF 1]\nNo se exige la constitución de garantía provisional en este procedimiento.\n'
            '[Pagina PDF 2]\nLa garantía definitiva será del cinco por ciento del importe adjudicado.')]
        fragments = fragment_sources(docs)
        keys = list(fragments)
        wrong = {'registros': [{'id': 'A2-1', 'tema': 'economia', 'estado': 'CONSTA',
                 'detalle': 'Garantía provisional: no se exige.', 'evidencias': [{'fragmento': keys[1]}]}]}
        corrected = deepcopy(wrong)
        corrected['registros'][0]['evidencias'] = [{'fragmento': keys[0]}]
        call = Mock(side_effect=[json.dumps(wrong), json.dumps(corrected)])
        with tempfile.TemporaryDirectory() as directory:
            _, result = review_extraction('A2', '', docs, [], {}, 'token', call,
                                          Path(directory)/'audit', topics=['economia'])
            feedback = call.call_args_list[1].args[1]
            self.assertIn('Registro A2-1', feedback)
            self.assertIn('Detalle rechazado: Garantía provisional: no se exige.', feedback)
            self.assertIn(keys[0] + ':', feedback)
            self.assertIn('No se exige la constitución de garantía provisional', feedback)
            self.assertIn('no añadas registros sobre reparación', feedback)
            self.assertEqual(result['registros'][0]['evidencias'][0]['fragmento'], keys[0])
            self.assertTrue((Path(directory)/'audit/economia_validacion_1.txt').exists())
        # El control debe seguir rechazando el mismo hecho cuando falta su respaldo.
        wrong['registros'][0]['evidencias'] = [resolve_evidence({'fragmento': keys[1]}, fragments)]
        with self.assertRaisesRegex(ValueError, 'exención'):
            validate_all_records(wrong, 'A2', docs, ['economia'])

    def test_missing_topic_is_rejected(self):
        self.audit['registros'].pop()
        with self.assertRaisesRegex(ValueError, 'Cobertura'):
            validate_audit(self.audit, 'A2', self.docs)

    def test_exemption_requires_express_clause(self):
        self.fact('No se exige garantía provisional.', 'No se exige garantía provisional.', 'EXENCION_EXPRESA')
        validate_audit(self.audit, 'A2', self.docs)
        self.audit['registros'][0]['evidencias'][0]['literal'] = 'Se facturará por trimestres vencidos.'
        with self.assertRaisesRegex(ValueError, 'Exención'):
            validate_audit(self.audit, 'A2', self.docs)

    def test_absence_cannot_be_exemption_even_if_disguised_as_fact(self):
        for state in ['NO_LOCALIZADO', 'CONSTA']:
            self.fact('No se exige clasificación.', 'Se facturará por trimestres vencidos.', state)
            with self.assertRaisesRegex(ValueError, 'exención'):
                validate_audit(self.audit, 'A2', self.docs)

    def test_obligation_classification_requires_literal(self):
        self.fact('La facturación es una obligación esencial.', 'Se facturará por trimestres vencidos.')
        with self.assertRaisesRegex(ValueError, 'Clasificación'):
            validate_audit(self.audit, 'A2', self.docs)

    def test_contractual_categories_are_not_interchangeable(self):
        for claimed, actual in [
            ('Condición especial de ejecución', 'obligación esencial'),
            ('Obligación esencial', 'condición especial de ejecución')]:
            clause = 'La confidencialidad constituye una ' + actual + ' del contrato.'
            self.docs[0].text = clause
            self.fact(claimed + ': cumplir la confidencialidad.', clause)
            with self.assertRaisesRegex(ValueError, 'Clasificación contractual'):
                validate_audit(self.audit, 'A2', self.docs)
        clause = 'La confidencialidad constituye una obligación\nesencial del contrato.'
        self.docs[0].text = clause
        self.fact('Obligación esencial: cumplir la confidencialidad.', clause)
        validate_audit(self.audit, 'A2', self.docs)

    def test_classification_retry_keeps_obligation_and_resolution_consequence(self):
        clause = 'El incumplimiento de los requisitos de seguridad faculta a resolver el contrato.'
        docs = [app.ExtractedDocument(app.DocumentRef('PCP', 'PCP', ''), text=clause)]
        wrong = {'registros': [{'id': 'A2-1', 'tema': 'clasificacion_obligaciones', 'estado': 'CONSTA',
                 'detalle': 'Condición especial de ejecución: ' + clause,
                 'evidencias': [{'fragmento': 'D1-F1'}]}]}
        corrected = deepcopy(wrong)
        corrected['registros'][0]['detalle'] = 'Obligación contractual: ' + clause
        call = Mock(side_effect=[json.dumps(wrong), json.dumps(corrected)])
        with tempfile.TemporaryDirectory() as directory:
            _, result = review_extraction('A2', '', docs, [], {}, 'token', call,
                Path(directory)/'audit', topics=['clasificacion_obligaciones'])
        feedback = call.call_args_list[1].args[1]
        self.assertIn('CORRECCIÓN ESPECÍFICA DE CLASIFICACIÓN', feedback)
        self.assertIn('no borres obligaciones', feedback)
        self.assertEqual(result['registros'][0]['estado'], 'CONSTA')
        self.assertIn('resolver el contrato', result['registros'][0]['detalle'])

    def test_minimum_experience_cannot_be_rewritten_as_less_than(self):
        clause = 'Titulación y experiencia mínima \nde 3 años en servicios afines.'
        self.docs[0].text += ' ' + clause
        self.fact('Cero puntos con menos de 3 años de experiencia.', clause)
        with self.assertRaisesRegex(ValueError, 'invertidos'):
            validate_audit(self.audit, 'A2', self.docs)
        self.audit['registros'][0]['detalle'] = 'La fila indica experiencia mínima de 3 años.'
        validate_audit(self.audit, 'A2', self.docs)

    def test_documentary_exemption_can_be_part_of_a_sourced_procedural_rule(self):
        clause = 'La documentación se aportará al requerimiento y no con carácter previo.'
        self.docs[0].text += ' ' + clause
        self.fact('No se exige presentación previa; se aporta al requerimiento.', clause)
        validate_audit(self.audit, 'A2', self.docs)

    def test_temporal_comparisons_preserve_negation_and_pdf_whitespace(self):
        self.assertEqual(temporal_bounds('no superior a 3 meses'), temporal_bounds('máximo de 3 meses'))
        self.assertEqual(temporal_bounds('no inferior a 1 mes'), temporal_bounds('mínimo de 1 mes'))
        self.assertEqual(temporal_bounds('más de\n7 años'), temporal_bounds('>7 años'))

    def test_feedback_reports_multiple_independent_errors_together(self):
        self.audit['registros'][0].update(estado='CONSTA', evidencias=[])
        self.audit['registros'][1].update(estado='DISCREPANCIA', evidencias=[])
        with self.assertRaises(ValueError) as caught:
            validate_all_records(self.audit, 'A2', self.docs, TOPICS['A2'])
        self.assertIn('afirmación necesita evidencia', str(caught.exception))
        self.assertIn('dos cláusulas', str(caught.exception))

    def test_conflict_requires_two_distinct_located_clauses(self):
        self.fact('Máximos 5 y 6: pendiente de aclaración.', 'El equipo se valorará con máximo 5 puntos.', 'DISCREPANCIA')
        record = self.audit['registros'][0]
        with self.assertRaisesRegex(ValueError, 'dos cláusulas'):
            validate_audit(self.audit, 'A2', self.docs)
        record['evidencias'].append(deepcopy(record['evidencias'][0]))
        with self.assertRaisesRegex(ValueError, 'idénticas'):
            validate_audit(self.audit, 'A2', self.docs)
        record['evidencias'][1]['literal'] = 'El equipo de soporte tendrá un máximo de 6 puntos.'
        validate_audit(self.audit, 'A2', self.docs)

    def test_retry_corrects_quotes_and_preserves_original_for_diagnosis(self):
        count = 0
        def reply(system, user, *args):
            nonlocal count
            count += 1
            if count == 1:
                return '{"registros":[]}'
            topic = user.split('TEMA UNICO: ')[1].split('\n')[0]
            records = [deepcopy(r) for r in self.audit['registros'] if r['tema'] == topic]
            if topic == 'discrepancias':
                records = [dict(records[0], comprobacion=c) for c in CONFLICT_CHECKS['A2']]
            return json.dumps({'registros': records})
        call = Mock(side_effect=reply)
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / 'review'
            result, audit = review_extraction('A2', 'BORRADOR ERRONEO', self.docs, [], {}, 'token', call, archive)
            self.assertNotIn('BORRADOR ERRONEO', result)
            self.assertIn('BORRADOR ERRONEO', (archive / 'entrada.json').read_text(encoding='utf-8'))
            self.assertEqual(len(audit['fuentes']), 1)
            self.assertTrue((archive / 'economia_respuesta_2.txt').exists())
            self.assertIn(SOURCE, call.call_args_list[0].args[1])

    def test_invalid_review_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            call = Mock(return_value='{"registros":[]}')
            with self.assertRaisesRegex(RuntimeError, 'no validada'):
                review_extraction('A2', 'Texto anterior', self.docs, [], {}, 'token', call, Path(directory)/'review')
            self.assertEqual(call.call_count, 3)

    def test_fragment_reference_is_resolved_from_source_not_model_quote(self):
        def reply(system, user, *args):
            topic = user.split('TEMA UNICO: ')[1].split('\n')[0]
            r = next(deepcopy(r) for r in self.audit['registros'] if r['tema'] == topic)
            if topic == 'economia':
                r.update(estado='CONSTA', detalle='Se facturará por trimestres vencidos.',
                         evidencias=[{'fragmento': 'D1-F1', 'literal': 'TEXTO INVENTADO'}])
            records = [dict(r, comprobacion=c) for c in CONFLICT_CHECKS['A2']] if topic == 'discrepancias' else [r]
            return json.dumps({'registros': records})
        with tempfile.TemporaryDirectory() as directory:
            _, result = review_extraction('A2', 'Borrador', self.docs, [], {}, 'token', Mock(side_effect=reply), Path(directory)/'review')
            self.assertEqual(result['registros'][0]['evidencias'][0]['literal'], SOURCE)
            self.assertIn('busqueda_lexica', result['busquedas'][0]['metodo'])

    def test_unknown_fragment_is_rejected(self):
        r = deepcopy(self.audit['registros'][0])
        r.update(estado='CONSTA', evidencias=[{'fragmento': 'D99-F1'}])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RuntimeError, 'fragmento no enviado'):
                review_extraction('A2', '', self.docs, [], {}, 'token',
                                  Mock(return_value=json.dumps({'registros': [r]})), Path(directory)/'review')

    def test_two_conflicting_clauses_can_share_a_fragment(self):
        selected = fragment_sources(self.docs)
        first = resolve_evidence({'fragmento': 'D1-F1', 'cita': 'El equipo se valorará con máximo 5 puntos.'}, selected)
        second = resolve_evidence({'fragmento': 'D1-F1', 'cita': 'El equipo de soporte tendrá un máximo de 6 puntos.'}, selected)
        self.fact('Máximos incompatibles, pendiente de aclaración.', SOURCE, 'DISCREPANCIA')
        self.audit['registros'][0]['evidencias'] = [first, second]
        validate_audit(self.audit, 'A2', self.docs)
        with self.assertRaisesRegex(ValueError, 'no localizada'):
            resolve_evidence({'fragmento': 'D1-F1', 'cita': 'El equipo tendrá máximo 7 puntos.'}, selected)

    def test_ellipsis_recovers_actual_source_span_only_between_exact_unique_anchors(self):
        selected = fragment_sources(self.docs)
        recovered = resolve_evidence({'fragmento': 'D1-F1', 'cita':
            'Se facturará por trimestres vencidos. ... No se exige garantía provisional.'}, selected)
        self.assertIn('si la factura se presenta en 15 días', recovered['literal'])
        self.assertNotIn('...', recovered['literal'])
        with self.assertRaises(ValueError):
            resolve_evidence({'fragmento': 'D1-F1', 'cita':
                'Se facturará por meses vencidos. ... No se exige garantía provisional.'}, selected)

    def test_fragment_selection_preserves_pages_and_table_neighbours(self):
        docs = [app.ExtractedDocument(app.DocumentRef('Pliego', 'PCP', ''), text=
                '[Pagina PDF 1]\nAntecedentes generales.\n[Pagina PDF 2]\nPuntuación máxima 40 puntos.\n'
                '[Pagina PDF 3]\nTabla continuación: total 60.\n[Pagina PDF 4]\nOtro contenido.')]
        selected = select_fragments(fragment_sources(docs), 'A4', 'criterios_subcriterios')
        self.assertTrue(any(e['ubicacion'] == 'Página PDF 3' for e in selected.values()))
        self.assertTrue(any('total 60' in e['literal'] for e in selected.values()))

    def test_short_trailing_footer_is_merged_not_offered_as_evidence(self):
        self.docs[0].text = '[Pagina PDF 1]\n' + ('Una línea de contenido contractual.\n' * 65) + '1\n'
        fragments = fragment_sources(self.docs)
        self.assertTrue(all(len(e['literal'].strip()) >= 20 for e in fragments.values()))
        self.assertEqual(''.join(e['literal'] for e in fragments.values()), self.docs[0].text)

    def test_general_score_split_does_not_cover_source_criterion_labels(self):
        selected = {'D1-F1': {'literal': 'B.1 Calidad 15 puntos. B.2 Equipo 10 puntos.'}}
        partial = {'registros': [{'detalle': 'Oferta técnica 60 puntos y precio 40.'}]}
        with self.assertRaisesRegex(ValueError, 'B.1, B.2'):
            check_criterion_labels(partial, selected, 'criterios_subcriterios')
        partial['registros'][0]['detalle'] = 'B.1 Calidad 15 puntos; B.2 Equipo 10 puntos.'
        check_criterion_labels(partial, selected, 'criterios_subcriterios')

    def test_editor_must_preserve_payment_condition_not_only_keywords(self):
        detail = 'Pago a 30 días desde el acta si se factura en 15 días; después, desde la presentación.'
        payload = {'expediente': 'TEST', 'agentes': [{'id': 'A2', 'revision_documental': {
            'registros': [{'id': 'A2-1', 'detalle': detail}]}}]}
        report = {'expediente': 'TEST', 'agentes_revisados': ['A2'], 'introduccion': ['Objeto.', 'Condiciones.'],
                  'secciones': [{'titulo': 'Economía', 'bloques': [{'tipo': 'parrafo', 'texto': 'Pago a 30 días.'}]}],
                  'conclusion': [detail]}
        self.assertTrue(editorial_record_issues(report, payload))
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / 'report.pdf'
            pdf.write_bytes(b'PREVIOUS')
            with self.assertRaises(ValueError):
                render_age_pdf(report, pdf, payload)
            self.assertEqual(pdf.read_bytes(), b'PREVIOUS')
        report['secciones'][0]['bloques'][0]['texto'] = detail
        self.assertFalse(editorial_record_issues(report, payload))

    def test_review_can_add_sections_without_mutating_draft(self):
        draft = {'secciones': [{'titulo': 'Datos', 'bloques': [{'tipo': 'parrafo', 'texto': 'Objeto.'}]}]}
        edits = {'correcciones': [], 'anadidos': [], 'secciones_nuevas': [
            {'titulo': 'Pago', 'bloques': [{'tipo': 'parrafo', 'texto': 'Regla completa.'}]}]}
        revised = apply_review(draft, edits)
        self.assertEqual(len(revised['secciones']), 2)
        self.assertEqual(len(draft['secciones']), 1)
        with self.assertRaisesRegex(ValueError, 'duplicada'):
            apply_review(revised, edits)

    def test_layer_one_preserves_direct_response_without_fragment_review(self):
        tender = app.parse_tender_feed(app.DEFAULT_XML)[0]
        with tempfile.TemporaryDirectory() as directory, contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(app, 'ROOT', Path(directory)))
            for _, _, _, function in LAYER_ONE:
                stack.enter_context(patch.object(app, function, return_value='BORRADOR'))
            review = stack.enter_context(patch('documentary_audit.review_extraction', return_value=('CORREGIDO', self.audit)))
            recs = stack.enter_context(patch.object(app, 'generate_recommendations', return_value=app.empty_recommendations()))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            sections = app.run_agent_layers(tender, self.docs, [], {}, 'token', '1')
            payload = app.build_layer1_json(tender, self.docs, [], sections)
            review.assert_not_called()
            recs.assert_not_called()
            for a in payload['agentes']:
                path = app.agent_response_path(tender, a['nombre'], 1, Path(directory)/'resumenes')
                saved = json.loads(path.read_text(encoding='utf-8'))
                self.assertNotIn('revision_documental', saved)
                self.assertNotIn('revision_documental', a)
                self.assertEqual(saved['ejecucion'], payload['ejecucion'])
                self.assertEqual(a['ejecucion'], payload['ejecucion'])
                self.assertEqual(a['contenido']['salida_original'], 'BORRADOR')

    def test_original_short_report_regression_when_local_artifacts_available(self):
        root = Path(__file__).resolve().parents[1] / 'resumenes'
        source = root / '2026-03993_capa1.json'
        report = root / '2026-03993_resumen_legible.redaccion.json'
        if not source.exists() or not report.exists():
            self.skipTest('Artefactos locales de auditoría no distribuidos con el código')
        issues = coverage_issues(json.loads(report.read_text(encoding='utf-8')),
                                 json.loads(source.read_text(encoding='utf-8')))
        self.assertTrue(any('facturación' in x for x in issues))
        self.assertTrue(any('garantía definitiva' in x for x in issues))
        self.assertTrue(any('secciones' in x for x in issues))


if __name__ == '__main__':
    unittest.main()
