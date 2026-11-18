import json
import tempfile
import unittest
from pathlib import Path
from run_outputs import begin_run, resume_run, output_directory, output_session, execution_id

class RunOutputsTests(unittest.TestCase):
    def test_resume_keeps_id_and_rejects_other_tender(self):
        with tempfile.TemporaryDirectory() as tmp:
            with output_session():
                directory = begin_run(Path(tmp), 'TEST', '1')
                identifier = execution_id()
            with output_session():
                resume_run(directory, 'TEST', '1')
                self.assertEqual(execution_id(), identifier)
                self.assertEqual(output_directory(Path(tmp)), directory.resolve())
            with self.assertRaises(ValueError):
                resume_run(directory, 'OTHER', '1')

    def test_same_tender_runs_are_isolated_and_inventory_is_saved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            runs = []
            for _ in range(2):
                with output_session():
                    directory = begin_run(root, "2026/TEST", "1")
                    runs.append(directory)
                    self.assertEqual(output_directory(root), directory)
                    (output_directory(root, "agentes") / "A1.json").write_text("{}")
                    identifier = execution_id()
                metadata = json.loads((directory / "ejecucion.json").read_text())
                self.assertEqual(metadata["id"], identifier)
                self.assertEqual(metadata["estado"], "completada")
                self.assertEqual(len(metadata["archivos"]), 1)
            self.assertNotEqual(*runs)
            self.assertEqual(output_directory(root), root / "resumenes")

    def test_failure_keeps_evidence_and_resets_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(ValueError):
                with output_session():
                    directory = begin_run(root, "TEST", "1")
                    (directory / "entrada.json").write_text("{}")
                    raise ValueError("secret must not be persisted")
            metadata = json.loads((directory / "ejecucion.json").read_text())
            self.assertEqual(metadata["estado"], "fallida")
            self.assertEqual(metadata["error_tipo"], "ValueError")
            self.assertNotIn("secret", str(metadata))
            self.assertTrue((directory / "entrada.json").exists())
            self.assertEqual(output_directory(root), root / "resumenes")
