"""Convierte el contrato JSON de capa 1 en un informe DOCX legible."""
from __future__ import annotations

import json
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "resumenes" / "LIC-10484_capa1.json"
OUTPUT = ROOT / "resumenes" / "LIC-10484_capa1_lectura_humana.docx"


def shade(cell, fill: str) -> None:
    properties = cell._tc.get_or_add_tcPr()
    shading = properties.find(qn("w:shd"))
    if shading is None:
        shading = OxmlElement("w:shd")
        properties.append(shading)
    shading.set(qn("w:fill"), fill)


def set_cell_text(cell, value, bold=False, color=None) -> None:
    cell.text = ""
    paragraph = cell.paragraphs[0]
    paragraph.paragraph_format.space_after = Pt(0)
    run = paragraph.add_run(str(value) if value not in (None, "") else "No consta")
    run.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP


def add_table(doc: Document, headers, rows, widths=None) -> None:
    if not rows:
        doc.add_paragraph("No hay datos en este apartado.", style="Caption")
        return
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header = table.rows[0].cells
    for index, value in enumerate(headers):
        set_cell_text(header[index], value, bold=True, color=(255, 255, 255))
        shade(header[index], "17324D")
    for row in rows:
        cells = table.add_row().cells
        values = row if isinstance(row, (list, tuple)) else [row.get(header, "") for header in headers]
        for index, value in enumerate(values):
            set_cell_text(cells[index], value)
            if len(table.rows) % 2 == 0:
                shade(cells[index], "F3F6F8")
    if widths:
        for row in table.rows:
            for index, width in enumerate(widths):
                row.cells[index].width = Inches(width)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_value_table(doc: Document, values: dict) -> None:
    rows = [[key, value if value not in (None, "", [], {}) else "No consta"] for key, value in values.items()]
    add_table(doc, ["Campo", "Valor"], rows, [2.0, 4.8])


def add_text_lines(doc: Document, text: str, bullet=False) -> None:
    if not text:
        doc.add_paragraph("No consta.", style="Caption")
        return
    for raw in str(text).splitlines():
        line = raw.strip()
        if not line:
            continue
        line = re.sub(r"^[-•]\s*", "", line)
        style = "List Bullet" if bullet or raw.lstrip().startswith(("-", "•")) else "Normal"
        doc.add_paragraph(line, style=style)


def add_structured_table(doc: Document, table_data: dict) -> None:
    columns = table_data.get("columnas", [])
    rows = table_data.get("filas", [])
    if not columns:
        return
    add_table(doc, columns, rows)


def configure_document(doc: Document) -> None:
    section = doc.sections[0]
    section.top_margin = Inches(0.65)
    section.bottom_margin = Inches(0.65)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)
    normal = doc.styles["Normal"]
    normal.font.name = "Aptos"
    normal.font.size = Pt(9)
    normal.paragraph_format.space_after = Pt(4)
    for name, size, color in (("Title", 22, "17324D"), ("Heading 1", 16, "17324D"), ("Heading 2", 12, "2D6A9F"), ("Heading 3", 10, "2D6A9F")):
        style = doc.styles[name]
        style.font.name = "Aptos Display" if name == "Title" else "Aptos"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor.from_string(color)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("LIC-10484 | Lectura humana del JSON de capa 1").font.size = Pt(8)


def build() -> Path:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    doc = Document()
    configure_document(doc)

    title = doc.add_paragraph(style="Title")
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.add_run("Informe de extracción documental")
    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run(f"{data.get('expediente', 'Sin expediente')} | {data.get('titulo', 'Sin título')}")
    run.bold = True
    run.font.color.rgb = RGBColor(91, 101, 112)
    doc.add_paragraph("Este documento presenta en lenguaje natural toda la información contenida en el JSON de capa 1. Se mantienen los datos, estados, tablas, pendientes, trazabilidad y textos originales de los agentes; únicamente se cambia el formato para facilitar su lectura.")

    doc.add_heading("1. Identificación del expediente", level=1)
    add_value_table(doc, {key: data.get(key, "") for key in ("schema", "version", "capa", "tipo_salida", "expediente", "numero", "titulo", "organo_contratacion")})

    doc.add_heading("2. Metadatos del expediente", level=1)
    add_value_table(doc, data.get("metadatos", {}))

    doc.add_heading("3. Documentos fuente", level=1)
    sources = []
    for item in data.get("documentos_fuente", []):
        sources.append([item.get("orden", ""), item.get("nombre", ""), item.get("tipo", ""), item.get("fuente", ""), item.get("caracteres_extraidos", ""), item.get("estado_lectura", ""), item.get("url", "")])
    add_table(doc, ["Orden", "Documento", "Tipo", "Fuente", "Caracteres", "Estado", "URL"], sources)

    doc.add_heading("4. Avisos de procesamiento", level=1)
    warnings = data.get("avisos_procesamiento", [])
    if warnings:
        for warning in warnings:
            doc.add_paragraph(warning, style="List Bullet")
    else:
        doc.add_paragraph("No constan avisos de procesamiento.")

    agents = data.get("agentes", [])
    doc.add_heading("5. Resultados de los agentes", level=1)
    doc.add_paragraph(f"Se incluyen {len(agents)} agentes en el orden original del JSON.")
    for index, agent in enumerate(agents, start=1):
        if index > 1:
            doc.add_page_break()
        doc.add_heading(f"{agent.get('id', '')} - {agent.get('nombre', '')}", level=1)
        add_value_table(doc, {"Orden": agent.get("orden", ""), "Tipo": agent.get("tipo", ""), "Estado": agent.get("estado", "")})
        content = agent.get("contenido", {})

        doc.add_heading("Resumen", level=2)
        for item in content.get("resumen", []) or []:
            doc.add_paragraph(str(item), style="List Bullet")
        if not content.get("resumen"):
            doc.add_paragraph("No consta resumen estructurado.")

        doc.add_heading("Secciones estructuradas", level=2)
        sections = content.get("secciones", []) or []
        if not sections:
            doc.add_paragraph("No constan secciones estructuradas.")
        for section in sections:
            doc.add_heading(section.get("titulo", "Sección sin título"), level=3)
            for paragraph in section.get("parrafos", []) or []:
                doc.add_paragraph(str(paragraph))
            for element in section.get("elementos", []) or []:
                doc.add_paragraph(str(element), style="List Bullet")
            for structured in section.get("tablas", []) or []:
                doc.add_paragraph("Tabla", style="Heading 3")
                add_structured_table(doc, structured)

        doc.add_heading("Pendientes y datos no localizados", level=2)
        pending = content.get("pendientes_y_no_localizados", []) or []
        if pending:
            for item in pending:
                doc.add_paragraph(str(item), style="List Bullet")
        else:
            doc.add_paragraph("No constan pendientes o datos no localizados.")

        doc.add_heading("Trazabilidad", level=2)
        trace = content.get("trazabilidad", []) or []
        if trace:
            columns = list(trace[0].keys())
            add_table(doc, columns, trace)
        else:
            doc.add_paragraph("No consta trazabilidad estructurada.")

        doc.add_heading("Salida original completa del agente", level=2)
        add_text_lines(doc, content.get("salida_original", ""))

    doc.add_page_break()
    doc.add_heading("6. Contenido completo del JSON", level=1)
    doc.add_paragraph("La información anterior cubre todos los campos de la estructura JSON. Esta sección conserva, además, los valores vacíos de forma explícita para facilitar la comprobación humana.")
    add_value_table(doc, {"Número total de agentes": len(agents), "Número total de documentos fuente": len(data.get("documentos_fuente", [])), "Número total de avisos": len(warnings)})

    doc.save(OUTPUT)
    return OUTPUT


if __name__ == "__main__":
    print(build())
