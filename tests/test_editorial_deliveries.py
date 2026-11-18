import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from editorial_deliveries import generate_editorial_deliveries
from oportunidades import markdown_report_to_json


class EditorialDeliveriesTests(unittest.TestCase):
    def test_bounded_drafts_reviews_and_resume_preserve_registry(self):
        original = ('| Materia | Requisito completo | Fuente |\n|---|---|---|\n'
                    '| Entrega | Entregar el documento en siete días. | PCAP.pdf p.3 |\n')
        content = markdown_report_to_json(original)
        content['salida_original'] += '\n' + ('Contexto del documento. ' * 400)
        payload = {'expediente': 'TEST', 'agentes': [{'id': 'A2', 'nombre': 'Admin', 'contenido': content}]}
        calls = []
        def call(system, user, config, token):
            calls.append((system, user))
            if 'apertura y cierre' in system:
                return json.dumps({'introduccion': ['Presentación.', 'Alcance.'], 'conclusion': ['Verificar requisitos.']})
            return json.dumps({'secciones': [{'titulo': 'Entregables', 'bloques': [
                {'tipo': 'parrafo', 'texto': 'Entregar el documento en siete días. [PCAP.pdf p.3]'}]}],
                'resumen': 'Entregar el documento en siete días. [PCAP.pdf p.3]'})
        with tempfile.TemporaryDirectory() as folder, patch('age_report.render_age_pdf') as render:
            path = Path(folder) / 'report.pdf'
            render.return_value = path
            result = generate_editorial_deliveries(payload, path, {'_editorial_delivery_chars': 6000}, 'token', call)
            self.assertEqual(result, path)
            self.assertTrue(any('BORRADOR:' in user for _, user in calls))
            report = render.call_args.args[0]
            self.assertIn('siete días', json.dumps(report, ensure_ascii=False))
            count = len(calls)
            generate_editorial_deliveries(payload, path, {'_editorial_delivery_chars': 6000}, 'token', call)
            self.assertEqual(len(calls), count)
            self.assertTrue((Path(folder) / 'entregas/redaccion/entrada_completa.json').exists())


if __name__ == '__main__':
    unittest.main()
