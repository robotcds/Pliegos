import tempfile
import unittest
import zipfile
from pathlib import Path

import oportunidades as app


class DocxExtractionTests(unittest.TestCase):
    def test_body_table_and_notes_remain_in_reading_order(self):
        ns = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        body = f'''<w:document xmlns:w="{ns}"><w:body>
          <w:p><w:r><w:t>Anexo de condiciones</w:t></w:r></w:p>
          <w:tbl><w:tr><w:tc><w:p><w:r><w:t>Garantia</w:t></w:r></w:p></w:tc>
          <w:tc><w:p><w:r><w:t>5 %</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
          <w:p><w:r><w:t>Plazo:</w:t><w:tab/><w:t>10 dias</w:t><w:br/><w:t>habiles</w:t></w:r></w:p>
        </w:body></w:document>'''
        note = f'<w:footnotes xmlns:w="{ns}"><w:footnote><w:p><w:r><w:t>Excepcion documentada</w:t></w:r></w:p></w:footnote></w:footnotes>'
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'anexos.docx'
            with zipfile.ZipFile(path, 'w') as archive:
                archive.writestr('word/document.xml', body)
                archive.writestr('word/footnotes.xml', note)
            result = app.extract_text(path, 'application/octet-stream')
            self.assertLess(result.index('Garantia'), result.index('5 %'))
            self.assertLess(result.index('5 %'), result.index('Plazo:'))
            self.assertIn('10 dias', result)
            self.assertIn('habiles', result)
            self.assertIn('Excepcion documentada', result)


if __name__ == '__main__':
    unittest.main()
