import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import oportunidades as app
from presales_coverage import RegistryFormatError, normalize_registry_rows


HEADER = '| Materia | Requisito completo | Fuente |\n|---|---|---|\n'


class RegistryNormalizationTests(unittest.TestCase):
    def test_grouped_short_rows_preserve_all_details_and_sources(self):
        raw = HEADER + ('| **Economía** | Tope de 825 € sin IVA. | PCAP Alfa.pdf, p.4 |\n'
              '| Se factura por hitos, sin mínimo garantizado. | PCAP Alfa.pdf, p.8 |\n'
              '|\n| **Equipo** |\n'
              '| Dos perfiles, con dedicación diferente. | PPT Beta.pdf, p.11 |\n'
              '| | Sustitución en siete días laborables. | PPT Beta.pdf, p.12 |\n')
        content = app.markdown_report_to_json(raw)
        records = content['requisitos_documentales']
        self.assertEqual(len(records), 4)
        self.assertEqual([r['seccion'] for r in records], ['**Economía**'] * 2 + ['**Equipo**'] * 2)
        self.assertEqual(records[1]['detalle'], 'Se factura por hitos, sin mínimo garantizado.')
        self.assertEqual(records[1]['fuente'], 'PCAP Alfa.pdf, p.8')
        self.assertEqual(records[3]['fuente'], 'PPT Beta.pdf, p.12')
        self.assertEqual(content['salida_original'], raw)

    def test_no_source_or_unanchored_matter_is_guessed(self):
        bad = [HEADER + '| Hecho sin materia. | PCAP.pdf p.1 |',
               HEADER + '| Economía | Primer hecho. | PCAP.pdf p.1 |\n| Otro hecho. | Texto sin aspecto de fuente |',
               HEADER + '| Economía | Hecho sin fuente. | |',
               HEADER + '| Economía | Hecho. | PCAP.pdf p.1 | Extra que no puede descartarse |']
        for raw in bad:
            with self.subTest(raw=raw), self.assertRaises(RegistryFormatError):
                app.markdown_report_to_json(raw)

    def test_matter_does_not_leak_to_next_table(self):
        raw = HEADER + '| Equipo | Perfil uno. | PPT.pdf p.1 |\n\n# Otro bloque\n' + HEADER + '| Perfil dos. | PPT.pdf p.2 |'
        with self.assertRaises(RegistryFormatError):
            app.markdown_report_to_json(raw)

    def test_complete_records_with_different_column_order_and_generic_tables(self):
        rows = [['Fuente', 'Materia', 'Requisito completo'], ['PPT.pdf p.3', 'Equipo', 'Perfil experto.']]
        self.assertEqual(normalize_registry_rows(rows), rows)
        other = [['Concepto', 'Valor'], ['Precio', '27 €']]
        self.assertEqual(normalize_registry_rows(other), other)
        self.assertEqual(app.markdown_report_to_json(HEADER + '| Pago | No consta plazo. | |')['requisitos_documentales'][0]['detalle'], 'No consta plazo.')

    def test_retry_preserves_rejected_answer_and_uses_full_original_documents(self):
        tender = app.parse_tender_feed(app.DEFAULT_XML)[0]
        documents = [app.ExtractedDocument(app.DocumentRef('Pliego', 'original.pdf', '', ''), text='TEXTO_INTEGRO')]
        bad = HEADER + '| Equipo | Perfil sin fuente. | |'
        good = HEADER + '| Equipo | Perfil con fuente. | original.pdf p.3 |'
        for outputs, should_fail in (([bad, good], False), ([bad] * 3, True)):
            with self.subTest(should_fail=should_fail), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                calls = []
                def extract(t, docs, warnings, config, token):
                    self.assertIs(docs, documents)
                    calls.append(config)
                    return outputs[len(calls) - 1]
                with patch.object(app, 'LAYER_ONE', [('A2', 'Admin', '_admin', 'extract_test')]), \
                     patch.object(app, 'extract_test', side_effect=extract, create=True), \
                     patch.object(app, 'output_directory', return_value=root), \
                     patch.object(app, 'save_summary', return_value=root/'raw.md'), \
                     contextlib.redirect_stdout(io.StringIO()):
                    if should_fail:
                        with self.assertRaisesRegex(RuntimeError, 'ambiguo tras 3 intentos'):
                            app.run_agent_layers(tender, documents, [], {}, 'token', '1')
                    else:
                        result = app.run_agent_layers(tender, documents, [], {}, 'token', '1')
                        self.assertEqual(result[0][1], good)
                archived = list(root.rglob('formato_rechazado_*.json'))
                self.assertEqual(len(archived), 3 if should_fail else 1)
                self.assertEqual(json.loads(archived[0].read_text(encoding='utf8'))['respuesta_original'], bad)
                self.assertIn('_registry_recovery_error', calls[1])
                self.assertNotIn('_registry_recovery_error', calls[0])

    def test_recovery_instruction_does_not_replace_or_fragment_input(self):
        response = Mock(ok=True)
        response.json.return_value = {'DataSource': {'ChatResponse': 'Extracción completa.'}}
        config = {'timeout_seconds': '180', 'tenant_id': '0', 'bot_id': 'bot', 'operation_id': 'operation',
                  'gpt_url': 'https://example.invalid', '_registry_recovery_error': 'Fila ambigua'}
        with patch.object(app.requests, 'post', return_value=response) as post, contextlib.redirect_stdout(io.StringIO()):
            app.call_druid_gpt('PROMPT_ORIGINAL', 'DOCUMENTOS_COMPLETOS', config, 'token')
        messages = post.call_args.kwargs['json']['Payload']['Messages']['items']
        self.assertTrue(messages[0]['Content'].startswith('PROMPT_ORIGINAL'))
        self.assertIn('REGENERACIÓN POR FORMATO', messages[0]['Content'])
        self.assertEqual(messages[1]['Content'], 'DOCUMENTOS_COMPLETOS')


if __name__ == '__main__':
    unittest.main()
