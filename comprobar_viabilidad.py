"""Prueba reproducible con los prompts reales; --live llama a Druid.

Los resultados esperados no se envían al modelo. No sobreescribe informes existentes.
"""
import argparse
import contextlib
import json
from datetime import datetime
from pathlib import Path

import oportunidades as app


AGENTS = [
    ("profiles", "Solvencia de perfiles", "profiles"),
    ("projects", "Solvencia de proyectos", "solvency"),
    ("economic", "Economico-financiero", "economic_financial"),
    ("admin", "Requisitos administrativos y legales", "admin_legal"),
    ("partners", "Compras / Partners", "purchases_partners"),
    ("service", "Service Design / ITIL", "service_design_itil"),
    ("security", "Seguridad / DPO / ENS", "security_dpo_ens"),
    ("coherence", "Coherencia Documental", "document_coherence"),
    ("risk", "Riesgos y Go/No-Go", "risk_go_no_go"),
]


def user_prompt(prefix, tender, documents, warnings, results, sections):
    build = getattr(app, f"build_{prefix}_prompt")
    if prefix == "purchases_partners":
        return build(tender, documents, warnings, results.get("profiles", "Análisis de perfiles no ejecutado; no presuponer cobertura."))
    if prefix in {"document_coherence", "risk_go_no_go"}:
        return build(tender, sections, documents, warnings)
    return build(tender, documents, warnings)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Ejecuta nueve llamadas reales a Druid.")
    parser.add_argument("--contract", default="OPP-SW-011", help="Expediente del XML que se quiere comprobar.")
    parser.add_argument("--agents", nargs="+", choices=[a[0] for a in AGENTS], help="Agentes que se ejecutarán, en el orden habitual.")
    parser.add_argument("--output", type=Path, help="Carpeta nueva de resultados.")
    parser.add_argument("--reuse-from", type=Path, help="Reutiliza una respuesta previa solo si su prompt completo es idéntico.")
    args = parser.parse_args()
    app.configure_console()
    tender = next(t for t in app.parse_tender_feed(app.DEFAULT_XML) if t.contract_folder_id == args.contract)
    documents, warnings = app.collect_documents(tender)
    if any(d.error or not d.text for d in documents) or not documents:
        raise RuntimeError(f"Caso incompleto: {warnings}")
    print(f"Caso cargado: {tender.contract_folder_id}, opción {tender.number}, {len(documents)} documentos leídos.", flush=True)
    if not args.live:
        print("Validación local correcta. Para probar extracción con IA: python comprobar_viabilidad.py --live")
        return 0
    output = args.output or app.ROOT / "resumenes" / ("prueba_viabilidad_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
    output.mkdir(parents=True, exist_ok=False)
    app.load_env_file(app.ROOT / ".env")
    config = app.get_druid_config()
    missing = [k for k in ("auth_url", "gpt_url", "username", "password", "tenant") if not app.is_real_config_value(config[k])]
    if missing:
        raise RuntimeError("Configuración Druid pendiente: " + ", ".join(missing))
    # Aísla los diagnósticos de error de esta prueba de los informes del usuario.
    def save_test_error(response, exception, system_prompt, user_prompt, payload, attempts):
        path = output / "error_druid.json"
        path.write_text(json.dumps({"status_code": response.status_code if response is not None else None,
                                    "exception_type": type(exception).__name__ if exception else None,
                                    "attempts": attempts}), encoding="utf-8")
        return path
    app.save_druid_error_debug = save_test_error
    token = app.authenticate_druid(config)
    results, sections, status = {}, [], {}
    for key, title, prefix in AGENTS:
        if args.agents and key not in args.agents:
            continue
        print(f"Ejecutando {title}...", flush=True)
        system = getattr(app, f"build_{prefix}_system_prompt")()
        prompt = user_prompt(prefix, tender, documents, warnings, results, sections)
        full_prompt = system + "\n\n" + prompt
        (output / f"{key}.prompt.txt").write_text(full_prompt, encoding="utf-8")
        reuse = False
        if args.reuse_from:
            old_prompt = args.reuse_from / f"{key}.prompt.txt"
            old_response = args.reuse_from / f"{key}.md"
            reuse = old_prompt.exists() and old_response.exists() and old_prompt.read_text(encoding="utf-8") == full_prompt
        if reuse:
            response = old_response.read_text(encoding="utf-8")
            print(f"Prompt idéntico: se reutiliza respuesta de {args.reuse_from}", flush=True)
        else:
            try:
                with (output / f"{key}.log.txt").open("w", encoding="utf-8") as log, contextlib.redirect_stdout(log):
                    call = app.call_purchases_report_with_validation if key == "partners" else app.call_druid_gpt
                    response = call(system, prompt, config, token)
            except Exception as exc:
                status[key] = {"estado": "ERROR", "tipo": type(exc).__name__}
                (output / "estado.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
                raise
        (output / f"{key}.md").write_text(response, encoding="utf-8")
        status[key] = {"estado": "RESPUESTA RECIBIDA",
                       "reutilizada": reuse,
                       "seccion_extraccion": "extracción de viabilidad" in response.lower(),
                       "validacion_semantica": "PENDIENTE DE CONTRASTE CON CASO ESPERADO"}
        results[key] = response
        sections.append((title, response))
        (output / "estado.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Recibido {title}; extracción: {status[key]['seccion_extraccion']}", flush=True)
    print(f"Resultados: {output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
