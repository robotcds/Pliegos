import contextlib
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import oportunidades as app


REJECTED = b'<html><title>Request Rejected</title>The requested URL was rejected.</html>'


class DownloadValidationTests(unittest.TestCase):
    def test_http_200_rejection_is_not_cached_or_read(self):
        ref = app.DocumentRef('Pliego administrativo', 'pliego.pdf', 'https://example.org/doc')
        response = Mock(content=REJECTED, headers={'content-type': 'text/html'})
        with tempfile.TemporaryDirectory() as directory, patch.object(app, 'DOCS_DIR', Path(directory)), patch.object(app.requests, 'get', return_value=response):
            result = app.download_and_extract(ref)
            self.assertFalse(result.text)
            self.assertIn('Descarga rechazada', result.error)
            self.assertFalse(list(Path(directory).rglob('metadata.json')))

    def test_cached_rejection_is_retried_and_replaced_by_valid_response(self):
        ref = app.DocumentRef('Pliego administrativo', 'pliego.pdf', 'https://example.org/doc')
        response = Mock(content=b'%PDF-1.7\nfixture', headers={'content-type': 'application/pdf'})
        with tempfile.TemporaryDirectory() as directory, patch.object(app, 'DOCS_DIR', Path(directory)), patch.object(app.requests, 'get', return_value=response) as get, patch.object(app, 'extract_text', return_value='Texto del PDF'):
            folder = Path(directory) / hashlib.sha256(ref.url.encode()).hexdigest()[:16]
            folder.mkdir()
            cached = folder / 'rejected.html'
            cached.write_bytes(REJECTED)
            (folder / 'metadata.json').write_text(json.dumps({'path': str(cached), 'content_type': 'text/html'}))
            result = app.download_and_extract(ref)
            get.assert_called_once()
            self.assertEqual(result.text, 'Texto del PDF')
            self.assertEqual(result.path.read_bytes(), response.content)

    def test_html_instead_of_pdf_is_rejected_but_detail_page_is_allowed(self):
        content = b'<html><body>Login</body></html>'
        with self.assertRaisesRegex(ValueError, 'PDF valido'):
            app.validate_document_response(content, 'text/html', app.DocumentRef('Pliego', 'p.pdf', 'https://example.org/doc'))
        app.validate_document_response(content, 'text/html', app.DocumentRef('Detalle', 'Detalle', 'https://example.org/detail'))

    def test_no_readable_pliego_stops_before_authentication_and_agents(self):
        tender = app.parse_tender_feed(app.DEFAULT_XML)[0]
        documents = [app.ExtractedDocument(tender.documents[0], error='Descarga rechazada'),
                     app.ExtractedDocument(app.DocumentRef('Documento adicional', 'Detalle', 'https://example.org/detail'), text='Ficha del anuncio')]
        config = {key: 'configured' for key in ('auth_url', 'gpt_url', 'username', 'password', 'tenant')}
        with contextlib.ExitStack() as stack:
            for name in ('configure_console', 'load_env_file', 'begin_run'):
                stack.enter_context(patch.object(app, name))
            stack.enter_context(patch('sys.argv', ['oportunidades.py', '--capa', '1']))
            stack.enter_context(patch.object(app, 'ask_for_tender', return_value=tender))
            stack.enter_context(patch.object(app, 'get_druid_config', return_value=config))
            stack.enter_context(patch.object(app, 'collect_documents', return_value=(documents, [])))
            auth = stack.enter_context(patch.object(app, 'authenticate_druid'))
            agents = stack.enter_context(patch.object(app, 'run_agent_layers'))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            self.assertEqual(app.main(), 3)
            auth.assert_not_called()
            agents.assert_not_called()


if __name__ == '__main__':
    unittest.main()
