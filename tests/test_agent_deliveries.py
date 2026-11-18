import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from agent_deliveries import run_deliveries, slices, merge_outputs
from oportunidades import DocumentRef, ExtractedDocument, DruidCallError


class DeliveriesTests(unittest.TestCase):
    def test_dedup_keeps_distinct_sources_and_conflicting_values(self):
        header = '| Materia | Requisito completo | Fuente |\n|---|---|---|\n'
        row = '| Plazo | 10 días | PCAP.pdf p.3 |'
        result, count = merge_outputs([header + row, header + row + '\n'
            '| Plazo | 10 días | PPT.pdf p.4 |\n| Plazo | 15 días | PCAP.pdf p.3 |'])
        self.assertEqual(count, 1)
        self.assertEqual(result.count(row), 1)
        self.assertIn('PPT.pdf p.4', result)
        self.assertIn('15 días', result)

    def doc(self, text):
        return ExtractedDocument(DocumentRef('Pliego', 'PCAP.pdf', 'local.pdf'), text=text)

    def test_slices_cover_all_characters_with_bounded_overlap(self):
        text = ('apartado con datos\n' * 400)
        spans = list(slices(text, 2000))
        self.assertEqual(spans[0][0], 0)
        self.assertEqual(spans[-1][1], len(text))
        for a, b in spans:
            self.assertLessEqual(b - a, 2000)
        for (_, end), (start, _) in zip(spans, spans[1:]):
            self.assertLessEqual(start, end)

    def test_resume_only_pending_and_context_is_restored(self):
        with tempfile.TemporaryDirectory() as folder:
            calls = []
            docs = [self.doc('A' * 2500), self.doc('B' * 2500)]
            def first(batch, partial, previous):
                calls.append(batch[0].text[0])
                if calls[-1] == 'B':
                    raise DruidCallError('auth', status_code=401)
                return 'Entrega A completa'
            with self.assertRaises(DruidCallError):
                run_deliveries(docs, first, folder, {'agent': 'A2'}, size=4000, minimum=1000)
            def resumed(batch, partial, previous):
                self.assertEqual(batch[0].text[0], 'B')
                self.assertEqual(previous, 'Entrega A completa')
                return 'Entrega B completa'
            output = run_deliveries(docs, resumed, folder, {'agent': 'A2'}, size=4000, minimum=1000)
            self.assertIn('Entrega A completa', output)
            self.assertIn('Entrega B completa', output)

    def test_timeout_splits_only_failed_part_and_never_caches_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            calls = []
            def invoke(batch, partial, previous):
                length = sum(len(d.text) for d in batch)
                calls.append(length)
                if length > 2100:
                    raise DruidCallError('504', status_code=504)
                return f'Completada {length}'
            docs = [self.doc('X' * 3900)]
            result = run_deliveries(docs, invoke, folder, {'agent': 'A2'}, size=4000, minimum=1000)
            count = len(calls)
            resumed = run_deliveries(docs, invoke, folder, {'agent': 'A2'}, size=4000, minimum=1000)
            self.assertEqual(result, resumed)
            self.assertEqual(len(calls), count)
            self.assertEqual(calls[0], 3900)
            self.assertTrue(all(n <= 2100 for n in calls[1:]))

    def test_changed_sources_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            run_deliveries([self.doc('antes')], lambda *a: 'ok', folder, {'agent': 'A2'}, size=4000, minimum=1000)
            with self.assertRaisesRegex(ValueError, 'han cambiado'):
                run_deliveries([self.doc('despues')], lambda *a: 'wrong', folder, {'agent': 'A2'}, size=4000, minimum=1000)

    def test_non_timeout_error_does_not_split(self):
        with tempfile.TemporaryDirectory() as folder:
            def fail(*args):
                raise DruidCallError('forbidden', status_code=403)
            with self.assertRaises(DruidCallError):
                run_deliveries([self.doc('X' * 3900)], fail, folder, {'agent': 'A2'}, size=4000, minimum=1000)
            self.assertEqual(len(list(Path(folder).glob('entrega_*.json'))), 1)

    @patch('agent_deliveries.time.sleep')
    def test_minimum_timeout_stops_without_publishing_result(self, sleep):
        with tempfile.TemporaryDirectory() as folder:
            def fail(*args):
                raise DruidCallError('timeout', timed_out=True)
            with self.assertRaisesRegex(RuntimeError, 'tamaño mínimo'):
                run_deliveries([self.doc('X' * 900)], fail, folder, {'agent': 'A2'}, size=4000, minimum=1000)
            self.assertFalse((Path(folder) / 'resultado.json').exists())
            self.assertEqual(sleep.call_count, 2)

    @patch('agent_deliveries.time.sleep')
    def test_minimum_transient_timeout_recovers_and_is_cached(self, sleep):
        with tempfile.TemporaryDirectory() as folder:
            calls = []
            def invoke(batch, partial, previous):
                calls.append((batch[0].text, partial, previous))
                if len(calls) < 3:
                    raise DruidCallError('gateway', status_code=504)
                return 'Entrega recuperada'
            docs = [self.doc('X' * 900)]
            result = run_deliveries(docs, invoke, folder, {'agent': 'A6'}, size=4000, minimum=1000)
            self.assertEqual(result, 'Entrega recuperada')
            self.assertEqual(calls, [calls[0]] * 3)
            run_deliveries(docs, invoke, folder, {'agent': 'A6'}, size=4000, minimum=1000)
            self.assertEqual(len(calls), 3)
            self.assertEqual([call.args[0] for call in sleep.call_args_list], [5, 10])


if __name__ == '__main__':
    unittest.main()
