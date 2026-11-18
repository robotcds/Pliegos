"""PDF completo y legible construido a partir del contrato JSON de capa 1."""
from __future__ import annotations

import html
from pathlib import Path


def build_human_readable_pdf(payload: dict, path: Path) -> Path:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    navy = HexColor("#17324D")
    blue = HexColor("#2D6A9F")
    pale = HexColor("#F3F6F8")
    gray = HexColor("#5B6570")
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="HRTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=19, leading=23, textColor=navy, alignment=TA_CENTER, spaceAfter=8))
    styles.add(ParagraphStyle(name="HRSubtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=12, textColor=gray, alignment=TA_CENTER, spaceAfter=14))
    styles.add(ParagraphStyle(name="HRH1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=14, leading=17, textColor=navy, spaceBefore=4, spaceAfter=7))
    styles.add(ParagraphStyle(name="HRH2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=blue, spaceBefore=6, spaceAfter=4))
    styles.add(ParagraphStyle(name="HRH3", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=9.2, leading=11, textColor=blue, spaceBefore=5, spaceAfter=3))
    styles.add(ParagraphStyle(name="HRBody", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.8, leading=10, spaceAfter=3))
    styles.add(ParagraphStyle(name="HRSmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=6.8, leading=8.3, textColor=gray, spaceAfter=2))
    styles.add(ParagraphStyle(name="HRCell", parent=styles["BodyText"], fontName="Helvetica", fontSize=6.8, leading=8.2, spaceAfter=0))
    styles.add(ParagraphStyle(name="HRCellHeader", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=6.8, leading=8.2, textColor=colors.white, spaceAfter=0))

    def para(value, style="HRBody"):
        text = html.escape(str(value) if value not in (None, "") else "No consta")
        text = text.replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>").replace("&lt;br/&gt;", "<br/>")
        return Paragraph(text, styles[style])

    def add_table(story, headers, rows, repeat=True):
        if not rows:
            story.append(para("No hay datos en este apartado.", "HRSmall"))
            return
        data = [[para(h, "HRCellHeader") for h in headers]]
        for row in rows:
            values = row if isinstance(row, (list, tuple)) else [row.get(h, "") for h in headers]
            data.append([para(v, "HRCell") for v in values])
        table = Table(data, repeatRows=1 if repeat else 0, hAlign="LEFT")
        commands = [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.3, HexColor("#C9D3DC")),
            ("BACKGROUND", (0, 0), (-1, 0), navy),
            ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]
        for index in range(2, len(data), 2):
            commands.append(("BACKGROUND", (0, index), (-1, index), pale))
        table.setStyle(TableStyle(commands))
        story.extend([table, Spacer(1, 4)])

    def add_lines(story, text, bullet=False):
        if not text:
            story.append(para("No consta.", "HRSmall"))
            return
        for raw in str(text).splitlines():
            line = raw.strip()
            if not line:
                continue
            if bullet or line.startswith(("-", "•")):
                line = "- " + line.lstrip("-• ")
            story.append(para(line))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(HexColor("#D7DEE5"))
        canvas.line(16 * mm, 13 * mm, 194 * mm, 13 * mm)
        canvas.setFont("Helvetica", 6.8)
        canvas.setFillColor(gray)
        canvas.drawString(16 * mm, 8 * mm, "Informe legible de capa 1 | Contenido completo del JSON")
        canvas.drawRightString(194 * mm, 8 * mm, f"Página {doc.page}")
        canvas.restoreState()

    story = [Spacer(1, 8 * mm), para(f"Informe completo de la licitación {payload.get('expediente', '')}", "HRTitle"), para("Traducción en lenguaje natural del contenido completo del fichero JSON, para poder leerse sin conocer JSON.", "HRSubtitle")]
    story.append(para("Este informe conserva los datos estructurados, las tablas, los pendientes, la trazabilidad y la salida original de cada agente. No sustituye a los documentos fuente de la licitación.", "HRBody"))

    story.append(para("1. Datos generales del expediente", "HRH1"))
    general = [["Expediente", payload.get("expediente", "")], ["Número interno", payload.get("numero", "")], ["Título", payload.get("titulo", "")], ["Órgano de contratación", payload.get("organo_contratacion", "")], ["Tipo de salida", payload.get("tipo_salida", "")], ["Esquema / versión", f"{payload.get('schema', '')} (versión {payload.get('version', '')}, capa {payload.get('capa', '')})"]]
    add_table(story, ["Campo", "Valor"], general)

    story.append(para("2. Metadatos del expediente", "HRH1"))
    add_table(story, ["Campo", "Valor"], [[key, value] for key, value in payload.get("metadatos", {}).items()])

    story.append(para("Criterios de adjudicación del XML", "HRH2"))
    add_lines(story, "\n".join(payload.get("metadatos", {}).get("criterios_adjudicacion_xml", [])), bullet=True)
    story.append(para("Requisitos generales del XML", "HRH2"))
    add_lines(story, "\n".join(payload.get("metadatos", {}).get("requisitos_xml", [])), bullet=True)
    story.append(para("Condiciones especiales de ejecución del XML", "HRH2"))
    conditions = payload.get("metadatos", {}).get("condiciones_ejecucion_xml", [])
    add_lines(story, "\n".join(conditions) if conditions else "No se listan condiciones especiales en el XML de origen.")

    story.append(para("3. Documentos fuente analizados", "HRH1"))
    docs = payload.get("documentos_fuente", [])
    add_table(story, ["Orden", "Nombre", "Tipo", "Fuente", "Caracteres", "Estado"], [[d.get("orden", ""), d.get("nombre", ""), d.get("tipo", ""), d.get("fuente", ""), d.get("caracteres_extraidos", ""), d.get("estado_lectura", "")] for d in docs])
    story.append(para("URLs de descarga", "HRH2"))
    for doc in docs:
        story.append(para(f"{doc.get('orden', '')}. {doc.get('nombre', '')}: {doc.get('url', '')}", "HRSmall"))

    story.append(para("4. Avisos de procesamiento", "HRH1"))
    add_lines(story, "\n".join(payload.get("avisos_procesamiento", [])) or "No constan avisos de procesamiento.", bullet=True)

    agents = payload.get("agentes", [])
    story.append(para("5. Análisis por agentes", "HRH1"))
    story.append(para(f"El expediente ha sido analizado por {len(agents)} agentes especializados. Cada uno aporta resumen, secciones, datos pendientes, trazabilidad y salida original.", "HRBody"))
    for number, agent in enumerate(agents, start=1):
        story.append(PageBreak())
        story.append(para(f"Agente {number} - {agent.get('id', '')}: {agent.get('nombre', '')}", "HRH1"))
        add_table(story, ["Campo", "Valor"], [["Orden", agent.get("orden", "")], ["Tipo", agent.get("tipo", "")], ["Estado", agent.get("estado", "")]])
        content = agent.get("contenido", {})
        story.append(para("Resumen", "HRH2"))
        add_lines(story, "\n".join(str(value) for value in content.get("resumen", []) or []), bullet=True)
        story.append(para("Secciones", "HRH2"))
        for section_number, section in enumerate(content.get("secciones", []) or [], start=1):
            story.append(para(f"{agent.get('id', '')}.{section_number} - {section.get('titulo', 'Sección sin título')}", "HRH3"))
            add_lines(story, "\n".join(str(value) for value in section.get("parrafos", []) or []))
            add_lines(story, "\n".join(str(value) for value in section.get("elementos", []) or []), bullet=True)
            for table_number, table_data in enumerate(section.get("tablas", []) or [], start=1):
                story.append(para(f"Tabla {table_number}", "HRH3"))
                add_table(story, table_data.get("columnas", []), table_data.get("filas", []))
        story.append(para("Pendientes y datos no localizados", "HRH2"))
        add_lines(story, "\n".join(str(value) for value in content.get("pendientes_y_no_localizados", []) or []) or "No constan pendientes o datos no localizados.", bullet=True)
        story.append(para("Trazabilidad", "HRH2"))
        trace = content.get("trazabilidad", []) or []
        if trace:
            add_table(story, list(trace[0].keys()), trace)
        else:
            story.append(para("No consta trazabilidad estructurada.", "HRSmall"))
        story.append(para("Salida original completa del agente", "HRH2"))
        add_lines(story, content.get("salida_original", ""))

    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=16 * mm, leftMargin=16 * mm, topMargin=14 * mm, bottomMargin=18 * mm, title=f"Informe legible - {payload.get('expediente', '')}", author="Oportunidades Pliegos")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return path
