import json
import tempfile
import unittest
from pathlib import Path

from pypdf import PdfReader

from age_report import generate_age_report
from oportunidades import DruidCallError, markdown_report_to_json


class EditorialDeliveriesTests(unittest.TestCase):
    def test_bounded_thematic_summary_survives_timeout_and_reuses_checkpoints(self):
        original = ('| Materia | Requisito completo | Fuente |\n|---|---|---|\n'
                    '| Entrega | Entregar el documento en siete días hábiles. | PCAP.pdf p.3 |\n'
                    '| Entrega | Registro técnico que solo debe quedar en el JSON. | PCAP.pdf p.3 |\n')
        content = markdown_report_to_json(original)
        content['salida_original'] += '\n' + ('Contexto del documento. ' * 2400)
        payload = {'expediente': 'TEST', 'titulo': 'Servicio de ejemplo', 'capa': '1', 'agentes': [
            {'id': 'A2', 'nombre': 'Admin', 'contenido': content,
             'registro_procesamiento': {'modo': 'entregas_guardadas'}}]}
        calls = []
        leaf = 0
        fail_format = True

        def call(system, user, config, token):
            nonlocal leaf
            calls.append((system, user))
            self.assertTrue(config['_delivery_managed'])
            if 'resumen temático COMPLETO' in system:
                raise DruidCallError('timeout', status_code=504)
            if 'FRAGMENTO ACTUAL:' in user:
                if fail_format:
                    return 'Respuesta incompleta.'
                fragment = user.split('\nCONTEXTO ANTERIOR', 1)[0]
                self.assertLess(len(fragment), 6200)
                if len(fragment) > 5000:
                    raise DruidCallError('timeout', status_code=504)
                leaf += 1
                subject = 'tramites_de_presentacion' if leaf % 2 == 0 else 'presentacion'
                return json.dumps({'anotaciones': {subject: [
                    f'PCAP.pdf p.3, nota {leaf}: ' + 'Contexto documental. ' * 40,
                    'Entregar el documento en siete días hábiles. [PCAP.pdf p.3]',
                ]}})
            if 'en una síntesis' in system:
                return 'Entregar el documento en siete días hábiles. [PCAP.pdf p.3]'
            if 'única sección' in system:
                if 'BORRADOR:' not in user and len(user) > 6500:
                    raise DruidCallError('timeout de sección', status_code=504)
                if 'BORRADOR:' in user:
                    return 'La revisión se entregó como texto libre.'
                return json.dumps({'fuentes': 'PCAP.pdf p.3', 'bloques': [
                    {'tipo': 'parrafo', 'texto': 'Entregar el documento en siete días hábiles.'},
                ], 'sintesis': 'Plazo de entrega documentado en el PCAP.'})
            self.assertIn('Apertura y cierre', user)
            return json.dumps({'introduccion': ['Presentación.', 'Alcance.'], 'conclusion': ['Verificar la entrega.']})

        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            path = directory / 'report.pdf'
            config = {'_editorial_delivery_chars': 6000}
            with self.assertRaises(ValueError):
                generate_age_report(payload, path, config, 'token', call)
            self.assertFalse(path.exists())
            fail_format = False
            self.assertEqual(generate_age_report(payload, path, config, 'token', call), path)
            editor = directory / 'entregas' / 'redaccion' / 'resumen_tematico'
            archived = json.loads((editor / 'entrada_completa.json').read_text(encoding='utf-8'))
            self.assertEqual(archived, payload)
            self.assertTrue(any('Ronda 2' in user for _, user in calls))
            self.assertTrue(any('CONTEXTO ANTERIOR' in user for _, user in calls))
            self.assertTrue(any('BORRADOR:' in user for _, user in calls))
            self.assertTrue(any('en una síntesis' in system for system, _ in calls))
            self.assertTrue(list((editor / 'anotaciones').glob('entrega_*.1.json')))
            pages = PdfReader(path).pages
            self.assertEqual(len(pages), 2)
            self.assertIn('Servicio de ejemplo', pages[0].extract_text())
            body = pages[1].extract_text()
            self.assertEqual(body.count('1. Fases del procedimiento y presentación'), 1)
            self.assertEqual(body.count('Entregar el documento en siete días hábiles.'), 1)
            self.assertIn('Fuentes: PCAP.pdf p.3', body)
            self.assertIn('Revisión editorial pendiente', body)
            self.assertNotIn('Registro técnico que solo debe quedar en el JSON.', body)
            coverage = json.loads((directory / 'comprobacion_cobertura.json').read_text(encoding='utf-8'))
            self.assertEqual(coverage['estado'], 'RESUMEN_EDITORIAL')
            self.assertEqual(len(coverage['avisos_editoriales']), 1)
            self.assertEqual(coverage['registros'], 2)
            count = len(calls)
            generate_age_report(payload, path, config, 'token', call)
            self.assertEqual(len(calls), count)

    def test_normal_generation_tabulates_profiles_when_druid_returns_prose(self):
        profiles = (
            'En el Lote 1 (Infraestructura), el equipo actual tiene dedicación parcial: '
            'Linux (4 técnicos); Active Directory (2). '
            'En el Lote 2, se describen áreas de soporte y comunicaciones. '
            'Estas cifras corresponden al equipo actual y no se presentan como mínimos obligatorios.'
        )
        payload = {'expediente': 'PERFILES', 'agentes': [
            {'id': 'A8', 'contenido': {'salida_original': profiles + '\n' + 'Datos de referencia. ' * 2600}},
        ]}

        def call(system, user, config, token):
            if 'resumen temático COMPLETO' in system:
                raise DruidCallError('timeout', status_code=504)
            if 'FRAGMENTO ACTUAL:' in user:
                return json.dumps({'anotaciones': {'equipo': [profiles]}})
            if 'una única sección' in system:
                self.assertIn('una fila por área, tecnología o perfil', system)
                return json.dumps({'fuentes': 'PPT p. 20', 'sintesis': 'Perfiles por lote.', 'bloques': [
                    {'tipo': 'subtitulo', 'texto': 'Perfiles técnicos y áreas de conocimiento por lote'},
                    {'tipo': 'parrafo', 'texto': profiles},
                    {'tipo': 'lista', 'elementos': ['Lote 1: Administración', 'Lote 2: Soporte al usuario']},
                    {'tipo': 'tabla', 'columnas': ['Lote', 'Perfil', 'Cantidad', 'Titulación', 'Disponibilidad'],
                     'filas': [['Lote 1', 'Técnico', '4', 'Técnico superior', 'Parcial']]},
                    {'tipo': 'tabla', 'columnas': ['Lote/Área', 'Perfil', 'Dotación actual'],
                     'filas': [['Lote 1 - Sistemas', 'Técnico', '4'], ['Lote 2 - CAU', 'Operador', '2']]},
                ]})
            return json.dumps({'introduccion': ['Presentación.', 'Alcance.'], 'conclusion': ['Equipo por lote.']})

        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            path = generate_age_report(payload, directory / 'report.pdf', {}, 'token', call)
            editor = directory / 'entregas' / 'redaccion' / 'resumen_tematico'
            report = json.loads((editor / 'informe.json').read_text(encoding='utf-8'))
            blocks = report['secciones'][0]['bloques']
            tables = [block for block in blocks if block['tipo'] == 'tabla']
            self.assertEqual(tables[0]['filas'], [['Linux', '4 técnicos'], ['Active Directory', '2']])
            self.assertEqual(tables[1]['filas'], [['Lote 1', 'Administración'], ['Lote 2', 'Soporte al usuario']])
            self.assertEqual(tables[2]['filas'], [['Lote 1', 'Técnico', '4', 'Técnico superior']])
            self.assertEqual(tables[3]['filas'], [['Lote 1', 'Parcial']])
            self.assertEqual(tables[4]['filas'], [['Sistemas', 'Técnico', '4']])
            self.assertEqual(tables[5]['filas'], [['CAU', 'Operador', '2']])
            self.assertTrue(any(b.get('texto') == 'Lote 1 · Infraestructura' for b in blocks))
            self.assertTrue(any(b.get('texto') == 'Lote 2' for b in blocks))
            self.assertTrue(any(b.get('texto', '').startswith('Estas cifras corresponden') for b in blocks))
            text = ' '.join(page.extract_text() for page in PdfReader(path).pages)
            self.assertIn('Área o tecnología', text)
            self.assertIn('mínimos obligatorios', text)

    def test_large_editorial_report_can_finish_in_one_full_call(self):
        first = 'INICIO ' + 'Información del expediente. ' * 2100
        second = 'ÚLTIMO DATO DEL EXPEDIENTE'
        payload = {'expediente': 'COMPLETO', 'agentes': [
            {'id': 'A1', 'contenido': first}, {'id': 'A8', 'contenido': second},
        ]}
        calls = []

        def call(system, user, config, token):
            calls.append((system, user))
            self.assertIn('resumen temático COMPLETO', system)
            self.assertTrue(config['_delivery_managed'])
            self.assertIn(first, user)
            self.assertIn(second, user)
            return json.dumps({
                'titulo_corto': 'Servicio documental',
                'introduccion': ['Objeto del servicio.', 'Alcance del servicio.'],
                'conclusion': ['Equipo documentado.'],
                'secciones': [{'materia': 'equipo', 'fuentes': 'PPT p. 20', 'bloques': [
                    {'tipo': 'tabla', 'columnas': ['Perfil', 'Dotación'], 'filas': [['Técnico', '4']]},
                ]}],
            })

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'summary.pdf'
            for _ in range(2):
                self.assertEqual(generate_age_report(payload, path, {}, '', call), path)
            self.assertEqual(len(calls), 1)
            directory = path.parent / 'entregas' / 'redaccion' / 'resumen_tematico'
            mode = json.loads((directory / 'composicion.json').read_text(encoding='utf-8'))['modo']
            self.assertEqual(mode, 'resumen_tematico_completo')
            self.assertFalse((directory / 'anotaciones').exists())


if __name__ == '__main__':
    unittest.main()
