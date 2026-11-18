import hashlib
import json
import re
import shutil
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from pypdf import PdfReader
from oportunidades import markdown_report_to_json, empty_document_reason, ExtractedDocument, DocumentRef
import oportunidades as app
from age_report import editorial_source_payload, generate_age_report, render_age_pdf, fidelity_issues
from documentary_revision import apply_documentary_revision, matching_documentary_revision, save_documentary_revision
from presales_coverage import (documentary_requirements, integrate_requirements,
                              normalized, requirement_issues, check_pdf_requirements,
                              ensure_extracted_records)


class PresalesCoverageTests(unittest.TestCase):
    def test_summary_exemption_is_rewritten_by_id_without_weakening_fidelity_or_losing_body(self):
        from age_report import summary_rewrite_tasks
        report = json.loads(json.dumps(self.report))
        bad = 'No se exige hardware ni carta de fabricante. El proveedor aporta portátil.'
        report['introduccion'].append(bad)
        report['conclusion'] = ['**NO EXIGIDO EXPRESAMENTE:** No se exige software ni SLA de fabricante.']
        report = integrate_requirements(report, self.payload)
        tasks = summary_rewrite_tasks(report)
        self.assertEqual(len(tasks), 2)
        self.assertTrue(fidelity_issues(report, self.payload))
        edits = {'correcciones':[], 'anadidos':[], 'correcciones_por_id':[
            {'id':task['id'], 'reemplazar':'**PUNTO RELEVANTE:** Solo se factura el consumo autorizado.'}
            for task in tasks]}
        call = Mock(side_effect=[json.dumps(report), json.dumps(edits)])
        with tempfile.TemporaryDirectory() as folder:
            generate_age_report(self.payload, Path(folder)/'resumen.pdf', {}, 'token', call)
            saved = json.loads(next(Path(folder).glob('diagnosticos/redaccion/*/redaccion.json')).read_text(encoding='utf8'))
            self.assertEqual(fidelity_issues(saved, self.payload), [])
            self.assertEqual(requirement_issues(saved, self.payload), [])
        review_prompt = call.call_args_list[1].args[1]
        self.assertIn('REESCRITURAS OBLIGATORIAS', review_prompt)
        for task in tasks:
            self.assertIn(task['id'], review_prompt)
        self.assertIn('No basta con matizarlas', review_prompt)

    def test_identical_conditions_on_different_profiles_keep_both_profile_names(self):
        raw = ('# Administrador Alfa\n- Experiencia mínima de 3 años. [PPT.pdf, página 8]\n'
               '# Administrador Beta\n- Experiencia mínima de 3 años. [PPT.pdf, página 8]')
        records = documentary_requirements({'agentes':[{'id':'A8', 'contenido':markdown_report_to_json(raw)}]})
        self.assertEqual(len(records), 2)
        self.assertIn('Administrador Alfa', records[0]['detalle'])
        self.assertIn('Administrador Beta', records[1]['detalle'])

    def test_profile_facts_in_cards_are_preserved_in_json_and_report_body(self):
        raw = ('# Administrador de plataforma\n'
               '- Experiencia mínima de 4 años en automatización. [PPT.pdf, página 8]\n'
               '- Dedicación de 850 horas en 19 meses. [PPT.pdf, página 9]\n'
               '# Sustituciones\n- Traspaso de 11 días con el sustituto. [PPT.pdf, página 10]')
        payload = ensure_extracted_records({'expediente':'PRUEBA', 'agentes':[
            {'id':'A8','contenido':markdown_report_to_json(raw)}]})
        records = documentary_requirements(payload)
        self.assertEqual(len(records), 3)
        for record in records:
            self.assertNotIn('pendiente de verificación', record['fuente'])
        report = integrate_requirements({'expediente':'PRUEBA', 'secciones':[]}, payload)
        self.assertEqual(requirement_issues(report, payload), [])

    def test_length_finish_reason_rejects_even_parseable_output_and_regenerates_full_input(self):
        first = Mock(ok=True, status_code=200)
        first.json.return_value = {'DataSource': {'finish_reason':'length', 'ChatResponse':'Texto aparentemente completo'}}
        second = Mock(ok=True, status_code=200)
        second.json.return_value = {'DataSource': {'finish_reason':'stop', 'ChatResponse':'Registro completo'}}
        with self.assertRaises(app.DruidOutputLimitError):
            app.extract_druid_response_text(first.json())
        cfg = {'timeout_seconds':'10', 'max_retries':'2', 'gpt_url':'https://druid.invalid',
               'tenant_id':'1', 'bot_id':'test', 'operation_id':'test'}
        sent = []
        def post(*args, **kwargs):
            sent.append(json.loads(json.dumps(kwargs['json'])))
            return first if len(sent)==1 else second
        with tempfile.TemporaryDirectory() as folder, \
                patch.object(app, 'output_directory', return_value=Path(folder)), \
                patch.object(app.requests, 'post', side_effect=post):
            result = app.call_druid_gpt('Sistema perfiles', 'DOCUMENTOS COMPLETOS SIN RECORTAR', cfg, 'test-token')
        self.assertEqual(result, 'Registro completo')
        for payload in sent:
            self.assertEqual(payload['Payload']['Messages']['items'][1]['Content'], 'DOCUMENTOS COMPLETOS SIN RECORTAR')
        self.assertIn('CONTROL DE REGENERACIÓN', sent[1]['Payload']['Messages']['items'][0]['Content'])

    def test_profiles_scope_does_not_require_transversal_company_inventory(self):
        prompt = app.build_profiles_system_prompt()
        self.assertNotIn('REQUISITOS OBLIGATORIOS DEL DOCUMENTO IA - FUENTES', prompt)
        for term in ['CONTROL DE ALCANCE Y FINALIZACIÓN DE A8', 'horas y periodos',
                     'sustitución', 'CV, títulos, vínculo', 'TERMINA la respuesta']:
            self.assertIn(term, prompt)

    def test_unverified_no_discrepancy_statement_is_diagnostic_not_contractual(self):
        raw = ('# Registro documental de preventa\n| Materia | Requisito completo | Fuente |\n'
               '|---|---|---|\n| Equipo | Se requieren 850 horas. | Ejemplo.pdf, p. 8 |\n'
               '| Discrepancias | No se han identificado discrepancias en la documentación revisada. | |')
        parsed = markdown_report_to_json(raw)
        records = documentary_requirements({'agentes':[{'id':'A2','contenido':parsed}]})
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]['detalle'], 'Se requieren 850 horas.')
        self.assertFalse(parsed['requisitos_documentales'][1]['es_requisito_contractual'])
        self.assertIn('no acredita ausencia', parsed['requisitos_documentales'][1]['fuente'])
        self.assertTrue(any(x.get('estado')=='DECLARACION_DEL_EXTRACTOR_NO_CONTRASTADA'
                            for x in parsed['pendientes_y_no_localizados']))
        with self.assertRaises(ValueError):
            markdown_report_to_json(raw.replace('No se han identificado discrepancias en la documentación revisada.',
                                               'Se exigen otras 900 horas.'))

    def test_complete_response_envelope_with_literal_newlines_preserves_text(self):
        raw = '{"Response":"Primera línea\nSegunda línea\tcon tabulación"}'
        self.assertEqual(app.unwrap_druid_text(raw), 'Primera línea\nSegunda línea\tcon tabulación')
        with self.assertRaises(ValueError):
            app.unwrap_druid_text(raw[:-2])

    def test_bad_chat_response_does_not_hide_complete_structured_tool_result(self):
        data = {'DataSource': {'ChatResponse': '{"Response":"cortado', 'responseJSON': {'tool_calls': [
            {'function': {'arguments': json.dumps({'Response':'Extracción íntegra con su fuente.'})}}]}}}
        self.assertEqual(app.extract_druid_response_text(data), 'Extracción íntegra con su fuente.')
        data['DataSource']['responseJSON']['tool_calls'] = []
        with self.assertRaises(ValueError):
            app.extract_druid_response_text(data)

    def test_rejected_response_is_archived_before_final_failure(self):
        raw = {'ChatResponse':'{"Response":"cortado'}
        response = Mock(ok=True, status_code=200)
        response.json.return_value = raw
        cfg = {'timeout_seconds':'10', 'max_retries':'1', 'gpt_url':'https://druid.invalid'}
        with tempfile.TemporaryDirectory() as folder, \
                patch.object(app, 'output_directory', return_value=Path(folder)), \
                patch.object(app, 'build_druid_gpt_payload', return_value={}), \
                patch.object(app.requests, 'post', return_value=response):
            with self.assertRaisesRegex(RuntimeError, 'Respuesta íntegra guardada'):
                app.call_druid_gpt('sistema', 'documentos completos', cfg, 'test-token')
            saved = json.loads(next(Path(folder).glob('druid/respuesta_rechazada_*.json')).read_text(encoding='utf8'))
            self.assertEqual(saved['respuesta_api'], raw)
            self.assertEqual(saved['intento'], 1)

    def test_login_credentials_use_code_constants_and_keep_url_and_tenant_configuration(self):
        with patch.dict(app.os.environ, {'DRUID_USERNAME':'otro_usuario', 'DRUID_PASSWORD':'otra_clave',
                                        'DRUID_AUTH_URL':'https://druid.invalid/login', 'DRUID_TENANT':'tenant-prueba'}), \
                patch.object(app, 'DRUID_USERNAME_FALLBACK', 'usuario_codigo'), \
                patch.object(app, 'DRUID_PASSWORD_FALLBACK', 'clave_codigo'):
            config = app.get_druid_config()
        self.assertEqual(config['username'], 'usuario_codigo')
        self.assertEqual(config['password'], 'clave_codigo')
        self.assertEqual(config['auth_url'], 'https://druid.invalid/login')
        self.assertEqual(config['tenant'], 'tenant-prueba')

    def test_gateway_failure_diagnostic_preserves_attempt_timing(self):
        response = Mock(status_code=504, url='https://druid.invalid', text='')
        history = [{'intento':1, 'status_code':504, 'segundos':120.0,
                    'timeout_operacion':360, 'timeout_http':390}]
        with tempfile.TemporaryDirectory() as folder, patch.object(app, 'output_directory', return_value=Path(folder)):
            file = app.save_druid_error_debug(response, None, 'sistema', 'pliego', {}, 1, history)
            saved = json.loads(file.read_text(encoding='utf8'))
        self.assertEqual(saved['intentos'], history)
        self.assertEqual(saved['status_code'], 504)
        self.assertNotIn('Authorization', saved)

    def test_druid_request_contains_one_copy_of_each_prompt(self):
        cfg = {'tenant_id':'1', 'bot_id':'test', 'operation_id':'test', 'timeout_seconds':'180'}
        payload = app.build_druid_gpt_payload('SISTEMA-ÚNICO', 'DOCUMENTOS-ÍNTEGROS', cfg)
        encoded = json.dumps(payload, ensure_ascii=False)
        self.assertEqual(encoded.count('SISTEMA-ÚNICO'), 1)
        self.assertEqual(encoded.count('DOCUMENTOS-ÍNTEGROS'), 1)
        self.assertNotIn('MessagesJSON', payload['Payload'])
        self.assertEqual(payload['Payload']['Messages']['items'][1]['Content'], 'DOCUMENTOS-ÍNTEGROS')

    def test_gateway_timeout_increases_druid_and_http_timeouts_without_splitting(self):
        first = Mock(ok=False, status_code=504, text='', headers={})
        second = Mock(ok=True, status_code=200)
        second.json.return_value = {'ChatResponse': 'Respuesta completa'}
        sent = []
        def post(*args, **kwargs):
            sent.append((dict(kwargs['json']), kwargs['timeout']))
            return first if len(sent) == 1 else second
        cfg = {'timeout_seconds': '180', 'max_retries': '2', 'gpt_url': 'https://druid.invalid'}
        with patch.object(app, 'build_druid_gpt_payload', return_value={'full': 'documentos íntegros'}), \
                patch.object(app.requests, 'post', side_effect=post), patch.object(app.time, 'sleep'):
            self.assertEqual(app.call_druid_gpt('sistema', 'documentos íntegros', cfg, 'test-token'), 'Respuesta completa')
        self.assertEqual([p['TimeoutInSeconds'] for p, _ in sent], [180, 360])
        self.assertEqual([t for _, t in sent], [210, 390])
        self.assertEqual([p['full'] for p, _ in sent], ['documentos íntegros'] * 2)

    def test_numeric_index_does_not_duplicate_full_pages_or_remove_original_documents(self):
        from capa1_requirements import numeric_source_index
        text = '[Pagina PDF 1]\nRecursos durante 19 meses: 850 horas\n' + ('Contexto contractual sin cifras.\n' * 300)
        ref = DocumentRef('PPT', 'Ejemplo.pdf', '', 'Prueba')
        document = ExtractedDocument(ref=ref, text=text)
        index = numeric_source_index([document], 'profiles')
        self.assertIn('850 horas', index)
        self.assertLess(len(index), len(text) // 2)
        full, metadata = app.build_documents_prompt_blocks([document], 'PROFILES')
        self.assertIn(text, full[0])
        self.assertFalse(metadata[0]['texto_compactado'])
        web_text = 'Recursos durante 19 meses con 850 horas: ' + ('contenido web ' * 3000)
        document.text = web_text
        self.assertLess(len(numeric_source_index([document], 'profiles')), 1500)
        self.assertIn(web_text, app.build_documents_prompt_blocks([document], 'PROFILES')[0][0])

    def test_editorial_summary_cannot_turn_absent_supplier_letter_into_global_exemption(self):
        report = {'introduccion': [], 'conclusion': ['No se exige hardware, software ni SLA de fabricante.'], 'secciones': []}
        self.assertTrue(any('exención general' in x for x in fidelity_issues(report, {'agentes': []})))
        report['conclusion'] = ['El proveedor aporta portátil y licencias; no se ha localizado una carta nominal de fabricante.']
        self.assertFalse(fidelity_issues(report, {'agentes': []}))

    def test_incomplete_druid_envelope_retries_same_complete_request(self):
        first = Mock(ok=True)
        first.json.return_value = {'ChatResponse': '{"Response":"cortado'}
        second = Mock(ok=True)
        second.json.return_value = {'ChatResponse': '{"Response":"Texto completo"}'}
        cfg = {'timeout_seconds': '10', 'max_retries': '2', 'gpt_url': 'https://druid.invalid'}
        with tempfile.TemporaryDirectory() as folder, \
                patch.object(app, 'output_directory', return_value=Path(folder)), \
                patch.object(app, 'build_druid_gpt_payload', return_value={'full': 'documents'}), \
                patch.object(app.requests, 'post', side_effect=[first, second]) as post:
            result = app.call_druid_gpt('sistema', 'documentos completos', cfg, 'test-token')
        self.assertEqual(result, 'Texto completo')
        self.assertEqual(post.call_count, 2)
        self.assertEqual(post.call_args_list[0], post.call_args_list[1])

    def test_druid_response_envelope_does_not_hide_registry_rows(self):
        raw = ('# Registro documental de preventa\n| Materia | Requisito completo | Fuente |\n'
               '|---|---|---|\n| Equipo | Se requieren 850 horas en 19 meses. | Ejemplo.pdf p. 8 |')
        envelope = json.dumps({'Response': raw}, ensure_ascii=False)
        parsed = markdown_report_to_json(envelope)
        self.assertEqual(parsed['salida_original'], envelope)
        self.assertEqual(len(parsed['requisitos_documentales']), 1)
        self.assertEqual(parsed['requisitos_documentales'][0]['detalle'], 'Se requieren 850 horas en 19 meses.')
        self.assertEqual(app.extract_druid_response_text({'ChatResponse': envelope}), raw)
        broken = envelope[:-4]
        with self.assertRaises(ValueError):
            app.unwrap_druid_text(broken)

    def test_absence_without_clause_is_not_fabricated_as_a_source(self):
        raw = ('# Registro documental de preventa\n| Materia | Requisito completo | Fuente |\n'
               '|---|---|---|\n| Logística | NO CONSTA un almacén específico. | |')
        record = markdown_report_to_json(raw)['requisitos_documentales'][0]
        self.assertIn('no acredita una exención', record['fuente'])
        self.assertEqual(record['seccion'], 'Datos no localizados y límites de lectura')
        labelled = markdown_report_to_json(raw.replace('NO CONSTA un almacén específico.', 'Almacén: NO CONSTA EN LA DOCUMENTACION REVISADA'))
        self.assertIn('no acredita una exención', labelled['requisitos_documentales'][0]['fuente'])
        with self.assertRaises(ValueError):
            markdown_report_to_json(raw.replace('NO CONSTA un almacén específico.', 'Se exige un almacén.'))

    def test_pdf_aligned_rows_preserve_label_value_pairing_on_non_contract_fixture(self):
        from reportlab.pdfgen import canvas
        from oportunidades import aligned_numeric_rows
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder)/'table.pdf'
            c = canvas.Canvas(str(file))
            # Orden de escritura por columnas, distinto del orden de lectura.
            for y, amount in [(700, '230'), (650, '570'), (600, '910')]:
                c.drawString(300, y, amount)
            for y, name in [(700, 'Perfil Alfa'), (650, 'Perfil Beta'), (600, 'Perfil Gamma')]:
                c.drawString(60, y, name)
            c.save()
            text = aligned_numeric_rows(PdfReader(file).pages[0])
            for name, number in [('Alfa','230'),('Beta','570'),('Gamma','910')]:
                self.assertIn(f'Perfil {name} | {number}', text)

    def test_participation_date_cannot_be_published_as_generic_offer_deadline(self):
        payload = {'agentes': [{'id':'A2','contenido': {'salida_original':
            'Solicitudes de participación hasta 17/03/2031; ofertas posteriores por invitación.'}}]}
        report = {'introduccion': [], 'conclusion': [], 'secciones': [
            {'titulo':'Datos','bloques':[{'tipo':'tabla','columnas':['Dato','Valor'],
                'filas':[['Fecha límite presentación','17/03/2031']]}]}]}
        self.assertTrue(any('fase de la fecha' in x for x in fidelity_issues(report, payload)))
        report['secciones'][0]['bloques'][0]['filas'][0][0] = 'Fecha límite de solicitudes de participación'
        self.assertFalse(any('fase de la fecha' in x for x in fidelity_issues(report, payload)))

    def test_multiline_registry_formula_preserves_branches_and_source(self):
        raw = ('# Registro documental de preventa\n| Materia | Requisito completo | Fuente |\n'
               '|---|---|---|\n| Precio | Fórmula por tramos:\n'
               '- Si D > 7: P = D * 3\n- Si D <= 7: P = 0\n'
               'D en puntos porcentuales. | PCAP.pdf, p. 17 |\n')
        record = markdown_report_to_json(raw)['requisitos_documentales'][0]
        self.assertIn('D > 7', record['detalle'])
        self.assertIn('D <= 7', record['detalle'])
        self.assertEqual(record['fuente'], 'PCAP.pdf, p. 17')
        self.assertEqual(markdown_report_to_json(raw)['salida_original'], raw)
        with self.assertRaises(ValueError):
            markdown_report_to_json(raw.rsplit(' | PCAP', 1)[0])

    def test_unregistered_service_team_and_security_facts_cannot_disappear(self):
        payload = {'expediente': 'UNRELATED-TENDER', 'agentes': [
            {'id': 'A6', 'contenido': markdown_report_to_json(
                '# Niveles de servicio\n| Servicio | Respuesta | Resolución | Objetivo | Fuente |\n'
                '|---|---|---|---|---|\n| Servicio Delta | 17 minutos | 9 horas | 98,7% | PPT.pdf, p. 8 |')},
            {'id': 'A8', 'contenido': markdown_report_to_json(
                '# Dedicación\nTres recursos compartidos, 850 horas durante 19 meses. (PPT.pdf, p. 9)')},
            {'id': 'A9', 'contenido': markdown_report_to_json(
                '# Incidentes\nNotificar en 11 horas desde conocimiento. (PPT.pdf, p. 10)')},
        ]}
        enriched = ensure_extracted_records(payload)
        self.assertEqual(ensure_extracted_records(enriched), enriched)
        self.assertEqual(len(enriched['control_cobertura_agentes']), 3)
        records = documentary_requirements(enriched)
        self.assertEqual({r['agente_responsable'] for r in records}, {'A6','A8','A9'})
        compact = editorial_source_payload(enriched)
        self.assertEqual(documentary_requirements(compact), records)
        report = {**self.report, 'expediente': payload['expediente'],
                  'agentes_revisados': ['A6','A8','A9']}
        report = integrate_requirements(report, compact)
        self.assertEqual(requirement_issues(report, enriched), [])
        with tempfile.TemporaryDirectory() as folder:
            pdf = render_age_pdf(report, Path(folder)/'different.pdf', enriched)
            text = '\n'.join(p.extract_text() for p in PdfReader(pdf).pages)
            for detail in ['17 minutos','9 horas','98,7%','850 horas','19 meses','11 horas']:
                self.assertIn(detail, text)

    def test_explicit_registry_does_not_hide_a_second_table(self):
        content = markdown_report_to_json(
            '# Registro documental de preventa\n| Materia | Requisito completo | Fuente |\n'
            '|---|---|---|\n| Equipo | Equipo dedicado. | PCAP.pdf, p. 1 |\n'
            '# Sustitución\nAviso de sustitución en 13 días. (PPT.pdf, p. 2)')
        records = documentary_requirements({'agentes':[{'id':'A8','contenido':content}]})
        self.assertEqual(len(records), 2)
        self.assertTrue(any('13 días' in r['detalle'] for r in records))

    def setUp(self):
        self.record = dict(id='R1', seccion='Facturación',
            detalle='Solo se factura el consumo autorizado; el 25 % es gratuito en cada factura.',
            fuente='PCAP, página PDF 61')
        self.payload = {'expediente': 'TEST', 'agentes': [{'id': 'A2', 'contenido': {}}],
                        'requisitos_documentales': [self.record]}
        self.report = dict(expediente='TEST', agentes_revisados=['A2'],
            introduccion=['Oportunidad.', 'Condiciones.'],
            secciones=[{'titulo': 'Facturación', 'bloques': [{'tipo': 'parrafo', 'texto': 'Hay facturación.'}]}],
            conclusion=['Cierre.'])

    def test_registry_round_trip_to_agent_and_editorial_json(self):
        raw = ('## Registro documental de preventa\n| Materia | Requisito completo | Fuente |\n'
               '|---|---|---|\n| Facturación | '+self.record['detalle']+' | '+self.record['fuente']+' |')
        content = markdown_report_to_json(raw)
        payload = {'agentes': [{'id': 'A2', 'contenido': content}]}
        self.assertEqual(documentary_requirements(payload)[0]['detalle'], self.record['detalle'])
        self.assertEqual(documentary_requirements(editorial_source_payload(payload)),
                         documentary_requirements(payload))
        self.assertEqual(content['salida_original'], raw)

    def test_introduction_and_heading_cannot_fake_body_coverage(self):
        self.report['introduccion'].append(self.record['detalle'])
        self.report['secciones'][0]['titulo'] = self.record['detalle']
        self.assertTrue(requirement_issues(self.report, self.payload))
        result = integrate_requirements(self.report, self.payload)
        self.assertEqual(requirement_issues(result, self.payload), [])
        self.assertEqual(integrate_requirements(result, self.payload), result)

    def test_duplicates_deduplicate_only_when_detail_and_source_match(self):
        self.payload['agentes'][0]['contenido']['requisitos_documentales'] = [self.record]
        self.assertEqual(len(documentary_requirements(self.payload)), 1)
        self.payload['agentes'][0]['contenido']['requisitos_documentales'] = [
            {**self.record, 'detalle': 'Otra condición, con la misma fuente.'}]
        self.assertEqual(len(documentary_requirements(self.payload)), 2)

    def test_explicit_review_body_does_not_duplicate_model_paraphrases(self):
        self.payload['revision_preventa'] = {'composicion_editorial': 'registro_contrastado'}
        result = integrate_requirements(self.report, self.payload)
        self.assertNotIn('Hay facturación.', str(result))
        self.assertEqual(requirement_issues(result, self.payload), [])
        self.assertEqual(integrate_requirements(result, self.payload), result)

    def test_invalid_record_is_rejected(self):
        self.payload['requisitos_documentales'] = [{**self.record, 'fuente': ''}]
        with self.assertRaises(ValueError):
            documentary_requirements(self.payload)

    def test_actual_pdf_without_required_detail_fails_even_if_json_has_it(self):
        root = Path(__file__).resolve().parents[1]
        report = integrate_requirements(self.report, self.payload)
        with self.assertRaisesRegex(ValueError, 'no se publica'):
            check_pdf_requirements(report, self.payload, root/'Examples/Licitacion1/ID_188_1.PDF')

    def test_pdf_url_layout_matching_does_not_ignore_numeric_differences(self):
        from presales_coverage import pdf_literal_span
        expected = 'Perfil: https://example.invalid/path/AbCd1234!/'
        rendered = 'prefacio perfil: https://example.invalid/path/ab cd1234!/ final'
        start, end, method = pdf_literal_span(normalized(expected), rendered)
        self.assertGreaterEqual(start, 0)
        self.assertEqual(method, 'url_partida_por_maquetacion')
        self.assertIn('ab cd1234', rendered[start:end])
        self.assertEqual(pdf_literal_span('importe 1200 €', 'importe 12 00 €')[0], -1)
        self.assertEqual(pdf_literal_span('importe 1200 €', 'importe 1201 €')[0], -1)
        self.assertEqual(pdf_literal_span(normalized(expected), rendered.replace('1234','1235'))[0], -1)

    def test_pdf_only_verification_failure_can_be_reported_but_missing_body_still_blocks(self):
        root = Path(__file__).resolve().parents[1]
        report = integrate_requirements(self.report, self.payload)
        actual_other_pdf = root/'Examples/Licitacion1/ID_188_1.PDF'
        coverage = check_pdf_requirements(report, self.payload, actual_other_pdf, allow_pdf_warnings=True)
        self.assertEqual(coverage['estado'], 'CON_AVISOS')
        self.assertEqual(coverage['registros_completos'], 0)
        self.assertTrue(all(w['revision_manual_requerida'] for w in coverage['avisos']))
        with self.assertRaisesRegex(ValueError, 'no se publica'):
            check_pdf_requirements(self.report, self.payload, actual_other_pdf, allow_pdf_warnings=True)

    def test_long_url_warning_is_in_coverage_report_and_end_of_pdf(self):
        payload = {'expediente': 'URL-TEST', 'agentes': [{'id': 'A2', 'contenido': {
            'requisitos_documentales': [{'id': 'R0001', 'seccion': 'Perfil',
                'detalle': 'Perfil: https://example.invalid/' + 'AbCd1234' * 25 + '/',
                'fuente': 'PCAP.pdf, p.9'}]}}]}
        report = integrate_requirements({'expediente': 'URL-TEST', 'agentes_revisados': ['A2'],
            'introduccion': ['Referencia documental.', 'Datos del expediente.'],
            'secciones': [], 'conclusion': ['Consultar las condiciones documentadas.']}, payload)
        with tempfile.TemporaryDirectory() as directory:
            pdf = render_age_pdf(report, Path(directory)/'url.pdf', payload)
            coverage = json.loads((Path(directory)/'comprobacion_cobertura.json').read_text(encoding='utf8'))
            self.assertEqual(coverage['estado'], 'CON_AVISOS')
            self.assertEqual(coverage['avisos'][0]['tipo'], 'URL_PARTIDA_EN_PDF')
            self.assertEqual(coverage['registros_completos'], 1)
            self.assertEqual(coverage['registros_pendientes_revision'], 0)
            text = '\n'.join(page.extract_text() or '' for page in PdfReader(pdf).pages)
            self.assertIn('AVISOS DE VALIDACIÓN DEL PDF', text)
            self.assertIn('URL_PARTIDA_EN_PDF', text)
            self.assertGreater(text.index('AVISOS DE VALIDACIÓN DEL PDF'), text.index('Conclusión operativa'))
            self.assertEqual(report['validacion_pdf']['estado'], 'CON_AVISOS')

    def test_warning_metadata_is_saved_in_consolidated_json(self):
        from run_outputs import begin_run, output_session
        coverage = {'estado': 'CON_AVISOS', 'avisos': [{'tipo': 'COBERTURA_PDF_NO_CONFIRMADA'}],
                    'registros_pendientes_revision': 1, 'registros': 3, 'registros_completos': 2}
        def generated(payload, path, *args):
            path.write_bytes(b'test')
            (path.parent/'comprobacion_cobertura.json').write_text(json.dumps(coverage), encoding='utf8')
            return path
        with tempfile.TemporaryDirectory() as directory, output_session():
            root = Path(directory)
            run = begin_run(root, 'TEST', 'test')
            payload = {'expediente': 'TEST', 'agentes': []}
            with patch.object(app, 'ROOT', root), patch('age_report.generate_age_report', side_effect=generated):
                app.create_age_summary(payload, {}, '')
            saved = json.loads((run/'TEST_capa1.json').read_text(encoding='utf8'))
            self.assertEqual(saved['validacion_resumen_pdf'], coverage)

    def test_failed_pdf_content_check_does_not_replace_existing_output(self):
        report = integrate_requirements(self.report, self.payload)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/'summary.pdf'
            target.write_bytes(b'existing output')
            with patch('age_report.check_pdf_requirements', side_effect=ValueError('PDF incompleto')):
                with self.assertRaisesRegex(ValueError, 'PDF incompleto'):
                    render_age_pdf(report, target, self.payload)
            self.assertEqual(target.read_bytes(), b'existing output')
            self.assertFalse(target.with_suffix('.tmp.pdf').exists())

    def test_web_empty_text_does_not_diagnose_ocr(self):
        doc = ExtractedDocument(DocumentRef('Enlace', 'TED', 'https://example.invalid'),
                                content_type='text/html')
        message = empty_document_reason(doc)
        self.assertIn('HTTP', message)
        self.assertIn('No se ha diagnosticado', message)
        self.assertNotIn('pendiente de lectura/OCR', message)

    def test_ted_uses_official_pdf_only_for_expected_host_and_notice_path(self):
        url = 'https://ted.europa.eu/es/notice/-/detail/147409-2026'
        self.assertEqual(app.ted_document_url(url), 'https://ted.europa.eu/es/notice/147409-2026/pdf')
        for other in ['https://example.com/es/notice/-/detail/147409-2026',
                      'https://ted.europa.eu/es/notice/147409-2026/pdf',
                      'https://ted.europa.eu/es/notice/-/detail/not-a-notice']:
            self.assertEqual(app.ted_document_url(other), other)

    def test_ted_does_not_reuse_empty_html_cache_for_pdf_export(self):
        ref = DocumentRef('TED', '147409-2026', 'https://ted.europa.eu/es/notice/-/detail/147409-2026')
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)/hashlib.sha256(ref.url.encode()).hexdigest()[:16]
            folder.mkdir()
            cached = folder/'old.html'
            cached.write_text('<html><body></body></html>', encoding='utf-8')
            (folder/'metadata.json').write_text(json.dumps({'path':str(cached), 'content_type':'text/html'}))
            response = Mock(headers={'content-type':'application/pdf'}, content=b'%PDF-test')
            with patch.object(app, 'DOCS_DIR', Path(directory)), \
                 patch.object(app.requests, 'get', return_value=response) as request, \
                 patch.object(app, 'extract_text', return_value='Texto del anuncio'):
                result = app.download_and_extract(ref)
            self.assertEqual(result.text, 'Texto del anuncio')
            self.assertTrue(request.call_args.args[0].endswith('/147409-2026/pdf'))
            metadata = json.loads((folder/'metadata.json').read_text(encoding='utf-8'))
            self.assertEqual(metadata['url'], ref.url)
            self.assertTrue(metadata['download_url'].endswith('/pdf'))

    def test_review_requires_matching_case_and_source_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)/'doc.pdf'
            source.write_bytes(b'original')
            self.payload['documentos_fuente'] = [{'nombre': 'doc.pdf', 'url': str(source)}]
            revision = dict(schema='oportunidades.revision_preventa.v1', identificador_interno='TEST',
                documentos=[{'nombre': 'doc.pdf', 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()}],
                requisitos_documentales=[{**self.record, 'agente_responsable': 'A2'}])
            catalog = Path(directory)/'catalog'
            catalog.mkdir()
            (catalog/'review.json').write_text(json.dumps(revision), encoding='utf-8')
            self.assertEqual(matching_documentary_revision(self.payload, catalog)[1], revision)
            result = apply_documentary_revision(self.payload, revision)
            self.assertEqual(result['agentes'][0]['estado'], 'revisado_documentalmente')
            self.assertNotIn('revision_preventa', self.payload)
            source.write_bytes(b'other edition')
            self.assertIsNone(matching_documentary_revision(self.payload, catalog))
            with self.assertRaisesRegex(ValueError, 'no coincide'):
                apply_documentary_revision(self.payload, revision)
            revision['identificador_interno'] = 'OTHER'
            with self.assertRaisesRegex(ValueError, 'expediente'):
                apply_documentary_revision(self.payload, revision)

    def test_saved_review_keeps_original_and_replaces_historical_individual_file(self):
        root = Path(__file__).resolve().parents[1]
        revision = json.loads((root/'docs/auditorias/licitacion1_revision.json').read_text(encoding='utf-8'))
        payload = dict(expediente='REAL-Licitacion1', agentes=[{'id': aid, 'contenido': {}}
            for aid in ['A1','A2','A3','A4','A6','A8','A9','A10']],
            documentos_fuente=[{'nombre': item['nombre'], 'url': str(root/'Examples/Licitacion1'/item['nombre'])}
                               for item in revision['documentos']])
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder/'agentes').mkdir()
            historical = folder/'agentes'/'administrativo_legal_respuesta.json'
            historical.write_text(json.dumps(payload['agentes'][1]), encoding='utf-8')
            corrected = save_documentary_revision(payload, revision, folder)
            original = json.loads((folder/'diagnosticos/extraccion_automatica_sin_revisar.json').read_text(encoding='utf-8'))
            self.assertEqual(original, payload)
            self.assertEqual(json.loads(historical.read_text(encoding='utf-8')), corrected['agentes'][1])
            self.assertEqual(len(list((folder/'agentes').glob('*.json'))), 8)
            self.assertEqual(corrected['agentes'][0]['estado'], 'revisado_documentalmente')

    def test_all_reviewed_licitacion1_observations_survive_json_and_pdf_body(self):
        root = Path(__file__).resolve().parents[1]
        revision = json.loads((root/'docs/auditorias/licitacion1_revision.json').read_text(encoding='utf-8'))
        observations = {obs for record in revision['requisitos_documentales'] for obs in record['observaciones']}
        self.assertEqual(observations, {f'E{i:02d}' for i in range(1,16)} | {f'F{i:02d}' for i in range(1,53)})
        payload = dict(expediente='REAL-Licitacion1', agentes=[{'id': aid, 'contenido': {}}
            for aid in ['A1','A2','A3','A4','A6','A8','A9','A10']],
            documentos_fuente=[{'nombre': item['nombre'], 'url': str(root/'Examples/Licitacion1'/item['nombre']),
                                'estado_lectura': 'texto_extraido'}
                               for item in revision['documentos']])
        payload = apply_documentary_revision(payload, revision)
        report = {**self.report, 'expediente': payload['expediente'],
                  'agentes_revisados': [agent['id'] for agent in payload['agentes']]}
        call = Mock(side_effect=[json.dumps(report), '{"correcciones":[],"anadidos":[]}'])
        with tempfile.TemporaryDirectory() as directory:
            result = generate_age_report(payload, Path(directory)/'full.pdf', {}, 'token', call)
            saved = json.loads(next(Path(directory).glob('diagnosticos/redaccion/*/redaccion.json')).read_text(encoding='utf-8'))
            self.assertEqual(requirement_issues(saved, payload), [])
            # Un párrafo puede continuar en otra página; la numeración de pie
            # no forma parte de su contenido contractual.
            text = normalized('\n'.join(re.sub(r'(?m)^\s*\d+\s*$', '', page.extract_text())
                                        for page in PdfReader(result).pages))
            for record in documentary_requirements(payload):
                self.assertIn(normalized(record['detalle']), text, record['id'])
            self.assertIn('150.234,97', text)
            self.assertIn('mcp', text)
            self.assertIn('power bi pro', text)
            self.assertIn('1,53', text)
            call.assert_not_called()
            self.assertNotIn('no consta exigencia expresa de clasificación, cpv', text)
            self.assertIn('constitución en quince días desde notificación', text)

    def test_october_feedback_has_locatable_evidence_and_separate_responsibilities(self):
        root = Path(__file__).resolve().parents[1]
        revision = json.loads((root/'docs/auditorias/licitacion1_revision.json').read_text(encoding='utf-8'))
        expected = {'F45':'A6', 'F46':'A2', 'F47':'A9', 'F48':'A4',
                    'F49':'A6', 'F50':'A9', 'F51':'A2', 'F52':'A2'}
        for observation, agent in expected.items():
            matches = [record for record in revision['requisitos_documentales']
                       if observation in record['observaciones']]
            self.assertEqual(len(matches), 1, observation)
            record = matches[0]
            self.assertEqual(record['agente_responsable'], agent)
            for evidence in record['evidencias']:
                text = PdfReader(root/'Examples/Licitacion1'/evidence['documento']).pages[evidence['pagina_pdf']-1].extract_text()
                self.assertEqual(hashlib.sha256(text.encode()).hexdigest(), evidence['sha256_texto'])
                self.assertIn(normalized(evidence['extracto_literal']), normalized(text))
        from capa1_requirements import extraction_requirements, editorial_requirements
        for agent, phrase in [('service','videotutorial'), ('admin','acuse de recibo'),
                              ('security','subsistencia'), ('award','puntuación propia')]:
            self.assertIn(phrase, extraction_requirements(agent))
        for phrase in ['videotutorial','evento de cómputo','puntuaciones independientes']:
            self.assertIn(phrase, editorial_requirements())
        for agent, phrase in [('service','modalidad'), ('service','SaaS'),
                              ('partners','SaaS'), ('security','datos sintéticos'),
                              ('admin','obligatoriedad'), ('admin','intereses')]:
            self.assertIn(phrase, extraction_requirements(agent))
        for phrase in ['SaaS', 'propiedad', 'obligatoriedad', 'aprobación de conformidad']:
            self.assertIn(phrase.lower(), editorial_requirements().lower())
        social = next(record for record in revision['requisitos_documentales']
                      if 'F39' in record['observaciones'])
        self.assertIn('siete días naturales', social['detalle'])
        self.assertNotIn('en plazo previsto', social['detalle'])

    def test_normal_layer_one_applies_only_the_matching_source_revision(self):
        root = Path(__file__).resolve().parents[1]
        tender = app.tender_from_examples_folder(root/'Examples/Licitacion1')
        documents = [app.download_and_extract(ref) for ref in tender.documents]
        sections = app.AgentSections()
        for aid, title, _, _ in app.LAYER_ONE:
            sections.append((aid+' · '+title, 'SALIDA AUTOMÁTICA SIN REVISAR.'))
        config = {key: 'configured' for key in ['auth_url','gpt_url','username','password','tenant']}
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            catalog = folder/'docs/auditorias'
            catalog.mkdir(parents=True)
            shutil.copyfile(root/'docs/auditorias/licitacion1_revision.json', catalog/'revision.json')
            with patch('sys.argv', ['oportunidades.py','--capa','1']), \
                 patch.object(app,'ROOT',folder), patch.object(app,'load_env_file'), \
                 patch.object(app,'configure_console'), patch.object(app,'parse_tender_feed',return_value=[tender]), \
                 patch.object(app,'ask_for_tender',return_value=tender), \
                 patch.object(app,'collect_documents',return_value=(documents,[])), \
                 patch.object(app,'get_druid_config',return_value=config), \
                 patch.object(app,'authenticate_druid',return_value='token'), \
                 patch.object(app,'run_agent_layers',return_value=sections), \
                 patch.object(app,'call_druid_gpt') as redactor:
                self.assertEqual(app.main(),0)
            redactor.assert_not_called()
            run = next((folder/'resumenes').iterdir())
            result = json.loads((run/'REAL-Licitacion1_capa1.json').read_text(encoding='utf-8'))
            self.assertEqual(len(documentary_requirements(result)),69)
            self.assertEqual(len(list((run/'agentes').glob('*.json'))),8)
            self.assertIn('SALIDA AUTOMÁTICA SIN REVISAR',
                          (run/'diagnosticos/extraccion_automatica_sin_revisar.json').read_text(encoding='utf-8'))
            pdf = next(run.glob('*_resumen_legible.pdf'))
            self.assertIn('150.234,97', '\n'.join(p.extract_text() for p in PdfReader(pdf).pages))


if __name__ == '__main__':
    unittest.main()
