import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace

import oportunidades as app
from viabilidad import build_viability_fixture_context
from verificar_campos_viabilidad import audit


class ViabilidadTests(unittest.TestCase):
    def test_incomplete_purchases_report_retries_and_rejects_second_failure(self):
        with patch.object(app, "call_druid_gpt", return_value="Solo extracción de viabilidad") as call:
            with self.assertRaisesRegex(RuntimeError, "Informe de Compras incompleto"):
                app.call_purchases_report_with_validation("system", "prompt", {}, "token")
            self.assertEqual(call.call_count, 2)

    def test_complete_purchases_report_is_returned_without_retry(self):
        report = "\n".join(f"## {title}\nContenido." for title in app.PURCHASES_REQUIRED_SECTIONS)
        with patch.object(app, "call_druid_gpt", return_value=report) as call:
            self.assertEqual(app.call_purchases_report_with_validation("system", "prompt", {}, "token"), report)
            self.assertEqual(call.call_count, 1)

    def test_real_xml_includes_cdc_and_all_seven_additional_documents(self):
        tender = next(t for t in app.parse_tender_feed(app.DEFAULT_XML) if t.contract_folder_id == "LIC-10484")
        self.assertEqual(len(tender.documents), 10)
        self.assertEqual(sum(d.kind == "Documento adicional / anexo" for d in tender.documents), 7)
        self.assertIn("LIC10484 PCP CDC.pdf", [d.name for d in tender.documents])
        self.assertTrue(any(d.name.endswith(".xlsx") for d in tender.documents))

    def test_exhausted_budget_keeps_unread_documents_in_agent_index(self):
        refs = [app.DocumentRef("Anexo", name, name) for name in ("first.txt", "cdc.txt")]
        tender = SimpleNamespace(documents=refs, contract_folder_id="TEST")
        with patch.dict(app.os.environ, {"MAX_DOCUMENT_CHARS": "4"}), patch.object(
            app, "is_examples_tender", return_value=False
        ), patch.object(app, "host_allowed", return_value=True), patch.object(
            app, "download_and_extract", return_value=app.ExtractedDocument(refs[0], text="abcdefgh")
        ):
            documents, warnings = app.collect_documents(tender)
        self.assertEqual(len(documents), 2)
        self.assertIn("PARCIAL", documents[0].error)
        self.assertIn("MAX_DOCUMENT_CHARS", documents[1].error)
        blocks, index = app.build_documents_prompt_blocks(documents, "PROFILES")
        self.assertTrue(all(item["error"] for item in index))
        self.assertIn("cdc.txt", blocks[1])
        self.assertTrue(warnings)

    def test_xlsx_preserves_sheet_coordinates_and_labels_uncomputed_formula(self):
        cells = [SimpleNamespace(value="Importe", coordinate="A1", data_type="s"),
                 SimpleNamespace(value="=SUM(B2:B3)", coordinate="B1", data_type="f")]
        sheet = SimpleNamespace(title="Oferta", iter_rows=lambda: [cells])
        book = SimpleNamespace(worksheets=[sheet], close=lambda: None)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "anexo.xlsx.bin"
            path.write_bytes(b"mock")
            with patch("openpyxl.load_workbook", return_value=book):
                result = app.extract_text(path, "application/octet-stream")
        self.assertIn("HOJA: Oferta", result)
        self.assertIn("A1: Importe", result)
        self.assertIn("B1: FORMULA (resultado no calculado): =SUM(B2:B3)", result)

    def test_unsupported_format_is_an_explicit_failure(self):
        with self.assertRaisesRegex(ValueError, "sin extractor"):
            app.extract_text(Path("anexo.doc"), "application/msword")

    def test_fixture_is_loaded_and_selectable_without_hiding_real_tenders(self):
        tenders = app.parse_tender_feed(app.DEFAULT_XML)
        tender = next(t for t in tenders if t.contract_folder_id == "OPP-SW-011")
        with patch("builtins.input", return_value=str(tender.number)):
            self.assertIs(app.ask_for_tender(tenders), tender)
        with patch("builtins.input", return_value=str(len(tenders) + 1)), patch.object(
            app, "ask_for_examples_tender", return_value="examples"
        ):
            self.assertEqual(app.ask_for_tender(tenders), "examples")
        docs, warnings = app.collect_documents(tender)
        self.assertEqual(warnings, [])
        self.assertEqual(len(docs), 2)
        self.assertTrue(all(d.text and not d.error for d in docs))

    def test_synthetic_internal_evidence_does_not_leak_into_other_tenders(self):
        for tender in app.parse_tender_feed(app.DEFAULT_XML):
            if tender.contract_folder_id == "OPP-SW-011":
                self.assertIn("FIN-2025-042", build_viability_fixture_context(tender.contract_folder_id))
            else:
                self.assertNotIn("FIN-2025-042", build_viability_fixture_context(tender.contract_folder_id))
                self.assertIn("NO APORTADOS", build_viability_fixture_context(tender.contract_folder_id))
                self.assertNotIn("FIN-2025-042", app.build_profiles_prompt(tender, [], []))

    def test_audit_does_not_count_expected_values_in_prompts_as_model_output(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            (path / "economic.prompt.txt").write_text("920000 1350000 1680000 610000 980000 1180000", encoding="utf-8")
            self.assertFalse(any(check["presente"] for check in audit(path)))
            (path / "economic.md").write_text("Ventas 2023: 920.000 EUR", encoding="utf-8")
            checks = audit(path)
            present = [c["campo"] for c in checks if c["presente"]]
            self.assertEqual(present, ["Ventas globales 2023"])

if __name__ == "__main__":
    unittest.main()
