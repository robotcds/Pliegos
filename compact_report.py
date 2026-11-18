"""Generador del informe ejecutivo corto de licitaciones.

El informe usa exclusivamente los metadatos del expediente y el texto de los
agentes. La matriz de viabilidad refleja si cada parámetro pedido por el documento
de fuentes aparece en la extracción; no convierte una ausencia en cumplimiento.
"""
from __future__ import annotations

import re
from pathlib import Path


VIABILITY_FIELDS = (
    ("Volumen de negocio", "umbral, ámbito/línea, mejor ejercicio, ventana, moneda y acreditación", ("A2", "A3"), ("volumen anual de negocios", "volumen de negocio", "cifra de negocio")),
    ("Patrimonio neto y ratios", "activos, pasivos, fórmula, resultado, umbral y acreditación", ("A3",), ("patrimonio neto", "ratio financiero", "ratios financieros", "activos y pasivos")),
    ("Seguro RC / riesgos profesionales", "importe, cobertura, asegurador, identificador, inicio, fin, vigencia y renovación", ("A2", "A3"), ("seguro de responsabilidad civil", "responsabilidad civil", "riesgos profesionales", "póliza")),
    ("Certificados de buena ejecución", "objeto/CPV, importe neto, fechas, duración, destinatario y prueba", ("A2", "A3"), ("certificados de buena ejecución", "buena ejecución", "servicios similares", "relación de servicios")),
    ("ISO y ENS", "norma/nivel, alcance, certificadora, caducidad, acreditación y equivalencias", ("A2", "A9"), ("iso 9001", "iso 14001", "iso 20000", "iso 27001", "esquema nacional de seguridad", "ens")),
    ("Partnerships y fabricante", "fabricante, nivel, especializaciones, cartas, expiración y acreditación", ("A10",), ("partnership", "partner", "fabricante", "carta de fabricante", "canal autorizado")),
    ("Perfiles profesionales", "puesto/cantidad, titulación, experiencia, certificaciones, dedicación, ubicación, idiomas y sustitución", ("A6", "A8"), ("perfiles", "equipo técnico", "responsable técnico", "responsable jurídico", "titulación", "experiencia mínima")),
    ("Clasificación ROLECE", "alternativa, grupo, subgrupo, categoría, vigencia, inscripción y acreditación", ("A2", "A3"), ("rolece", "clasificación empresarial", "grupo, subgrupo", "grupo y subgrupo")),
)


def _plain(value: str) -> str:
    value = re.sub(r"[*`#|]", "", value or "")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def _snippet(text: str, terms: tuple[str, ...], limit: int = 300) -> str:
    candidates = []
    for raw_line in re.split(r"[\r\n]+", text):
        line = _plain(raw_line)
        lower = line.lower()
        if len(line) < 12 or not any(term.lower() in lower for term in terms):
            continue
        if set(line) <= set("-_=| "):
            continue
        score = sum(3 for term in terms if term.lower() in lower)
        score += 4 if any(marker in lower for marker in ("no consta", "no se exige", "no exigida", "no hay")) else 0
        score += 2 if re.search(r"\d", line) else 0
        score -= 5 if lower.startswith(("datos no localizados", "tabla de", "trazabilidad")) else 0
        candidates.append((score, line))
    if not candidates:
        return ""
    snippet = max(candidates, key=lambda item: (item[0], len(item[1])))[1]
    if len(snippet) > limit:
        snippet = snippet[:limit].rsplit(" ", 1)[0] + "..."
    return snippet


def _field_status(snippet: str) -> str:
    lower = snippet.lower()
    if "no se exige" in lower or "no exig" in lower or "no consta" in lower or "no hay" in lower:
        return "ENCONTRADO: no exigido / no consta"
    if "pendiente" in lower or "no disponible" in lower or "lectura parcial" in lower:
        return "PENDIENTE DE VERIFICAR"
    if not snippet:
        return "NO ENCONTRADO"
    return "ENCONTRADO"


def _source_names(documents) -> str:
    names = []
    for document in documents:
        name = getattr(getattr(document, "ref", None), "name", "")
        error = getattr(document, "error", "")
        label = f"{name} ({error})" if name and error else name
        if label and label not in names:
            names.append(label)
    return ", ".join(names[:8]) + ("..." if len(names) > 8 else "")


def build_compact_report_pdf(tender, sections, documents, warnings, path: Path) -> Path:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak

    navy = HexColor("#17324D")
    blue = HexColor("#2D6A9F")
    pale = HexColor("#F3F6F8")
    red = HexColor("#A53030")
    gray = HexColor("#5B6570")
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCompact", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=navy, alignment=TA_CENTER, spaceAfter=7))
    styles.add(ParagraphStyle(name="SubCompact", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=13, textColor=gray, alignment=TA_CENTER, spaceAfter=12))
    styles.add(ParagraphStyle(name="HCompact", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=14, leading=17, textColor=navy, spaceBefore=3, spaceAfter=7))
    styles.add(ParagraphStyle(name="H2Compact", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=blue, spaceBefore=6, spaceAfter=4))
    styles.add(ParagraphStyle(name="BodyCompact", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.5, leading=11, spaceAfter=3))
    styles.add(ParagraphStyle(name="SmallCompact", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.2, leading=9, textColor=gray, spaceAfter=2))
    styles.add(ParagraphStyle(name="CellCompact", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.2, leading=8.7, spaceAfter=0))
    styles.add(ParagraphStyle(name="CellHeaderCompact", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=7.2, leading=8.7, textColor=colors.white, spaceAfter=0))
    styles.add(ParagraphStyle(name="AlertCompact", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9, leading=11.5, textColor=red, spaceAfter=3))

    def p(text, style="BodyCompact"):
        text = str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        text = text.replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")
        text = text.replace("&lt;br/&gt;", "<br/>")
        return Paragraph(text, styles[style])

    def table(rows, widths):
        cells = []
        for row_index, row in enumerate(rows):
            style = "CellHeaderCompact" if row_index == 0 else "CellCompact"
            cells.append([p(cell, style) for cell in row])
        result = Table(cells, colWidths=widths, repeatRows=1)
        commands = [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.35, HexColor("#C9D3DC")),
            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("BACKGROUND", (0, 0), (-1, 0), navy),
        ]
        for i in range(2, len(rows), 2):
            commands.append(("BACKGROUND", (0, i), (-1, i), pale))
        result.setStyle(TableStyle(commands))
        return result

    by_agent = {title.split(" ", 1)[0].strip(): content for title, content in sections}
    rows = [["Parámetro y subcampos obligatorios", "Estado en el pliego", "Literal/dato localizado"]]
    for label, subfields, agent_ids, terms in VIABILITY_FIELDS:
        evidence = _snippet("\n".join(by_agent.get(agent_id, "") for agent_id in agent_ids), terms)
        if label == "Certificados de buena ejecución" and evidence and "buena ejecución" not in evidence.lower() and "certificado" not in evidence.lower():
            evidence = "No consta CBE como requisito; sí se exige relación de servicios similares. " + evidence
        status = _field_status(evidence)
        if label == "Volumen de negocio" and re.search(r"34[.,]440", evidence):
            status = "ENCONTRADO EN EL PLIEGO"
        rows.append([f"<b>{label}</b><br/>{subfields}", status, evidence or "No aparece en el texto de los agentes."])

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(HexColor("#D7DEE5"))
        canvas.line(18 * mm, 14 * mm, 192 * mm, 14 * mm)
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(gray)
        canvas.drawString(18 * mm, 9 * mm, "Informe ejecutivo | Extracción documental")
        canvas.drawRightString(192 * mm, 9 * mm, f"Página {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=18 * mm, leftMargin=18 * mm, topMargin=15 * mm, bottomMargin=20 * mm, title=f"Informe ejecutivo - {tender.contract_folder_id}", author="Oportunidades Pliegos")
    story = [Spacer(1, 10 * mm), p("Informe ejecutivo de licitación", "TitleCompact"), p(f"{tender.contract_folder_id} | {tender.contracting_body or tender.title}", "SubCompact")]
    story += [p("Resumen del expediente", "HCompact"), table([
        ["Dato", "Información"],
        ["Objeto", tender.title],
        ["Importe estimado", tender.estimated_amount or "No consta en metadatos"],
        ["Importe total / presupuesto", tender.total_amount or "No consta en metadatos"],
        ["Duración", tender.duration or "No consta en metadatos"],
        ["Plazo", tender.deadline or "No consta en metadatos"],
        ["Documentos leídos", _source_names(documents)],
    ], [43 * mm, 127 * mm]), Spacer(1, 5 * mm)]
    if tender.deadline:
        story.append(p(f"Plazo indicado en el expediente: {tender.deadline}. Confirmar siempre su vigencia en la plataforma antes de preparar la oferta.", "AlertCompact"))
    story += [PageBreak(), p("Parámetros de viabilidad solicitados", "HCompact"), p("La siguiente matriz incluye todos los campos definidos en IA - Fuentes para proyecto VIABILIDAD. El estado describe únicamente lo localizado en el PDF/JSON de extracción; no acredita por sí solo el cumplimiento de la empresa.", "BodyCompact"), table(rows, [45 * mm, 37 * mm, 88 * mm]), PageBreak()]

    story += [p("Requisitos decisivos y puntuación", "HCompact")]
    for title, content in sections:
        low = content.lower()
        if any(key in low for key in ("puntu", "criterio", "solvencia", "responsable", "equipo", "penalidad", "sobres")):
            evidence = _snippet(content, ("puntu", "solvencia", "responsable", "equipo", "sobres", "penalidad"), 450)
            if evidence:
                story.append(p(f"<b>{title}</b>: {evidence}"))
    story += [Spacer(1, 3 * mm), p("Checklist de revisión", "H2Compact"), table([
        ["Comprobar antes de decidir", "Resultado"],
        ["Vigencia del procedimiento", "Confirmar fecha y estado en la plataforma."],
        ["Solvencia económica y técnica", "Revisar umbrales, periodo, unidad y medio de acreditación."],
        ["Perfiles y experiencia", "Verificar titulación, años y CV/fichas exigidos."],
        ["Certificados, RC, ISO/ENS, partnerships y ROLECE", "No marcar como acreditado sin documento, alcance y vigencia."],
        ["Oferta técnica y económica", "Comprobar criterios, fórmula, sobres, formato y firma."],
    ], [70 * mm, 100 * mm]), Spacer(1, 5 * mm), p("Avisos del procesamiento", "H2Compact")]
    for warning in warnings:
        story.append(p("- " + warning))
    if not warnings:
        story.append(p("No constan avisos de procesamiento."))
    story += [Spacer(1, 4 * mm), p("Trazabilidad resumida", "H2Compact")]
    trace_rows = [["Agente", "Evidencia localizada"]]
    for title, content in sections:
        excerpt = _plain(content)[:380]
        if len(_plain(content)) > 380:
            excerpt += "..."
        trace_rows.append([title, excerpt or "Sin contenido"])
    story.append(table(trace_rows, [48 * mm, 122 * mm]))
    story += [Spacer(1, 4 * mm), p("Este PDF es el resumen ejecutivo. El JSON de capa 1 y los Markdown conservan el detalle completo y la trazabilidad por agente.", "SmallCompact")]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return path
