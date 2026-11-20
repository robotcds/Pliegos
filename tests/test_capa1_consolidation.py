import unittest
from unittest.mock import patch

from capa1_consolidation import consolidate_layer1
from capa1_facts import contract_facts
from editorial_deliveries import prepare_editorial_report


class Capa1ConsolidationTests(unittest.TestCase):
    def test_lot_schedule_amounts_and_conflicting_office_reach_editorial_report(self):
        pcap = 'PCAP expediente.pdf'
        page = '''Lote 1 Impuestos excluidos Impuestos incluidos
Importe Presupuesto base de licitación 1.000,00 € 1.210,00 €
Duración del contrato (sin prórrogas) 2 años
Número de prórrogas 3
Duración de las prórrogas 12 meses
Lote 2 Impuestos excluidos Impuestos incluidos
Duración del contrato (sin prórrogas) 42 meses
Número de prórrogas 1
Duración de las prórrogas 12 meses
A.1 Órgano de contratación ☐ Primera unidad ☒ Segunda unidad B. Objeto del contrato'''
        payload = {'expediente': 'DEMO', 'organo_contratacion': 'Primera unidad', 'titulo': 'Servicio TIC',
                   'metadatos': {'plazo_presentacion': '2026-11-30+01:00 14:00:00.000'}, 'agentes': []}
        facts = contract_facts(payload, {pcap: [page]})
        self.assertEqual([lot['duracion']['maximo_meses'] for lot in facts['lotes']], [60, 54])
        self.assertEqual(facts['lotes'][0]['importes']['presupuesto_base']['con_iva'], '1.210,00')
        self.assertEqual(facts['presentacion']['valor'], '30/11/2026 a las 14:00 (UTC+01:00)')
        self.assertEqual(facts['contrastes'][0]['estado'], 'contradictorio')
        payload['consolidacion_documental'] = {'datos_contractuales': facts, 'avisos_por_entrega': [],
                                             'pendientes_lectura': [], 'recuento': {'registros_sin_localizador': 0}}
        report = prepare_editorial_report({'expediente': 'DEMO', 'agentes_revisados': [],
            'introduccion': ['Ficha', 'Resumen'], 'conclusion': ['Documentación revisada es coherente.'],
            'secciones': []}, payload)
        self.assertIn(['2', '42', '1 × 12', '54'], report['secciones'][0]['bloques'][-2]['filas'])
        self.assertNotIn('coherente', ' '.join(report['conclusion']))

    def test_duplicates_and_partial_solvent_notices_keep_origins(self):
        pcap = 'PCAP expediente.pdf'
        requirement = 'Se exige un volumen anual de negocios de dos veces el valor anual medio.'
        pending = 'NO LOCALIZADO EN ESTA ENTREGA PARCIAL el requisito de volumen anual de negocios.'
        qualified = 'NO LOCALIZADO EN ESTA ENTREGA PARCIAL el momento exacto del certificado ENS.'
        def row(record, detail, matter, reference):
            return {'id': record, 'detalle': detail, 'seccion': matter, 'fuente': reference}

        rows = [row('1', pending, 'Lote 1', 'fuente no individualizada'),
                row('2', qualified, 'Lote 1', 'fuente no individualizada'),
                row('3', requirement, 'Lote 1', f'{pcap}, p. 4'),
                row('4', requirement, 'Lote 2', f'{pcap}, p. 5')]
        payload = {'capa': 1, 'documentos_fuente': [{'nombre': pcap, 'estado_lectura': 'texto_extraido'}],
                   'agentes': [{'id': 'A3', 'contenido': {'requisitos_documentales': rows,
                        'salida_original': f'## Entrega 1\n{pending}\n## Entrega 2\n{requirement}'}},
                               {'id': 'A2', 'contenido': {'requisitos_documentales': [
                                   row('1', requirement, 'Lote 1', f'{pcap}, p. 6')]}}]}
        with patch('capa1_consolidation.pdf_pages', return_value={}):
            registry = consolidate_layer1(payload)['consolidacion_documental']
        self.assertEqual(len(registry['registros']), 2)
        self.assertEqual(len(registry['registros'][0]['referencias']), 2)
        self.assertEqual(registry['recuento']['duplicados_entre_agentes'], 1)
        self.assertEqual(registry['avisos_por_entrega'][0]['estado'], 'localizado_en_otra_entrega')
        self.assertEqual(registry['avisos_por_entrega'][1]['estado'], 'pendiente_de_contraste')
