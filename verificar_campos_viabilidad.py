"""Contrasta presencia de datos esperados en respuestas, nunca en los prompts.

Este control de cobertura no sustituye la revisión semántica de filas/veredictos.
Los patrones esperados NO se importan ni se envían desde la aplicación a Druid.
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path


EXPECTED = {
    "economic": {
        "Ventas globales 2023": [r"920[. ]?000"],
        "Ventas globales 2024": [r"1[. ]?350[. ]?000"],
        "Ventas globales 2025": [r"1[. ]?680[. ]?000"],
        "Ventas IT 2023": [r"610[. ]?000"],
        "Ventas IT 2024": [r"980[. ]?000"],
        "Ventas IT 2025": [r"1[. ]?180[. ]?000"],
        "Ejercicios de referencia": [r"2023", r"2024", r"2025"],
        "Brecha de ventas": [r"20[. ]?000", r"no cumple"],
        "Patrimonio": [r"410[. ]?000", r"350[. ]?000"],
        "Componentes de liquidez": [r"720[. ]?000", r"480[. ]?000"],
        "Ratio y umbral": [r"1[,.]50?\b", r"1[,.]20?\b"],
        "Fuente financiera": [r"fin-2025-042", r"ca-2025"],
        "Poliza y asegurador": [r"rc-it-2026-031", r"aseguradora ficticia peninsular"],
        "Limites de cobertura RC": [r"1[. ]?000[. ]?000", r"2[. ]?000[. ]?000", r"siniestro", r"agregado"],
        "Actividad asegurada": [r"desarrollo", r"operacion"],
        "Vigencia y renovacion RC": [r"01/01/2026", r"31/12/2026", r"2027", r"renovacion"],
    },
    "projects": {
        "Objeto y tecnologias": [r"portal", r"react", r"java", r"postgresql"],
        "Importe neto certificado": [r"465[. ]?000"],
        "Inicio y fin REF-001": [r"01/02/2024", r"30/04/2025"],
        "Adjudicador REF-001": [r"ayuntamiento ficticio de sierra capital"],
        "CPV": [r"72262000"],
        "Certificado y emisor": [r"cbe-ref-001", r"publico", r"ejecucion"],
        "Ventana y minimo": [r"30/10/2023", r"30/10/2026", r"350[. ]?000"],
        "Ausencia de segundo CBE": [r"ref-002", r"no acreditado|no consta|falta", r"comercial"],
    },
    "profiles": {
        "Titulaciones": [r"ingeniera informatica"],
        "Antiguedad y sector separados": [r"empresa", r"sector", r"\b6\b", r"\b10\b", r"\b4\b", r"\b7\b"],
        "Experiencia relevante": [r"\b8\b", r"backend"],
        "PMP, emisor e identificador": [r"pmp-at-0921", r"pmi"],
        "PMP caducado al cierre": [r"30/09/2026", r"30/10/2026", r"no cumple"],
        "AWS sin vigencia acreditada": [r"aws-sm-0422", r"aws", r"no acreditado", r"fecha"],
        "Fuente RRHH": [r"rh-2026-09", r"meta4"],
    },
    "admin": {
        "ISO 9001 identificador y emisor": [r"q-901-114", r"certificadora ficticia iberia"],
        "ISO 9001 alcance y fecha": [r"operacion", r"31/12/2027"],
        "ISO 14001 identificador y emisor": [r"m-140-208", r"certificadora ficticia ambiental"],
        "ISO 14001 alcance y fecha": [r"instalaciones madrid", r"30/06/2026"],
        "Titular": [r"sermicro software ficticio"],
        "Inscripcion ROLECE y fecha": [r"rol-2026-0915", r"15/09/2026"],
        "Clasificacion alternativa": [r"grupo v|v/2/3", r"categoria 3|v/2/3", r"alternativa|no obligatoria"],
        "Sustitucion limitada a ventas y CBE": [r"sustituye|sustituir", r"ventas|volumen", r"cbe"],
        "Actualizacion ROLECE pendiente": [r"ausencia de variaciones"],
    },
    "partners": {
        "Nivel propio del licitador": [r"indirect reseller"],
        "Titular del nivel externo": [r"cloud partner ficticio"],
        "Nivel Microsoft exigido": [r"solutions partner", r"infrastructure", r"azure"],
        "Especializacion": [r"azure vmware solution"],
        "Fechas nivel y especializacion": [r"31/03/2027", r"31/08/2026"],
        "Evidencia de alianza": [r"ali-027", r"fab-2026-09"],
        "Compromiso pendiente": [r"compromiso", r"no consta|no acreditado|falta|ausente"],
    },
    "security": {
        "Titular": [r"sermicro software ficticio"],
        "ISO 27001 identificador y emisor": [r"s-270-317", r"certificadora ficticia seguridad"],
        "ISO 27001 caducidad": [r"31/12/2027"],
        "ENS categoria e identificador": [r"media", r"ens-m-044"],
        "ENS emisor y caducidad": [r"auditora ficticia ens", r"31/12/2026"],
        "Alcance inadecuado": [r"desarrollo", r"produccion", r"no cumple"],
        "Fuente Compliance": [r"cal-2026-09"],
    },
    "service": {
        "ISO 20000 ausente": [r"iso 20000", r"no acreditado|no disponible|no consta"],
        "Campos sin evidencia": [r"titular", r"alcance", r"emisor", r"caducidad", r"no consta"],
        "Equivalencia no aportada": [r"equivalen", r"no consta"],
    },
    "coherence": {
        "Conserva brechas de viabilidad": [r"1[. ]?180[. ]?000", r"cbe", r"pmp", r"produccion", r"rolece"],
    },
    "risk": {
        "Decision condicionada por incumplimientos": [r"no.go", r"solvencia", r"certific"],
    },
}


def normalize(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text.lower()) if not unicodedata.combining(c))


def audit(folder):
    checks = []
    for agent, fields in EXPECTED.items():
        file = folder / f"{agent}.md"
        response = normalize(file.read_text(encoding="utf-8")) if file.exists() else ""
        for name, patterns in fields.items():
            missing = [pattern for pattern in patterns if not re.search(pattern, response)]
            checks.append({"agente": agent, "campo": name, "presente": not missing, "patrones_ausentes": missing})
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    checks = audit(args.folder)
    if not args.folder.is_dir():
        parser.error("La carpeta de respuestas no existe")
    (args.folder / "cobertura_campos.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
    passed = sum(c["presente"] for c in checks)
    print(f"Cobertura textual: {passed}/{len(checks)} comprobaciones. Requiere revisión semántica.")
    for check in checks:
        if not check["presente"]:
            print(f"REVISAR {check['agente']}: {check['campo']}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
