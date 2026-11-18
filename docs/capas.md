# Extracción y procesamiento del pliego

## Ejecución

`python oportunidades.py --capa 1` ejecuta A1 y los siete extractores. Mantiene el
menú de XML/Examples, autenticación, lectura, seguimiento de enlaces, configuración,
reintentos y salida Markdown/PDF. `--xml` funciona igual en ambos modos.

`python oportunidades.py` o `--capa todas` ejecuta primero la capa 1 y después los
cuatro agentes de procesamiento. No existe un modo de capa 2 independiente que
reutilice informes antiguos: cada ejecución completa obtiene extracciones nuevas.

La selección de agentes está en `capas.py`; la orquestación, en `run_agent_layers`.
Las llamadas a Druid y los constructores de prompts existentes siguen siendo los
responsables de cada especialidad. No se duplican los prompts en otro flujo.

## Responsabilidades y cobertura

| Agente | Información que extrae |
|---|---|
| A1 · Referencia inicial | Máximo 100 palabras y 5 viñetas: expediente/órgano, objeto, presupuesto, duración y plazo; ausencias/lectura parcial relevantes. El límite se solicita en el prompt. |
| A2 · Administrativo-legal | Procedimiento, plazos, lotes, documentación, presentación, garantías, obligaciones, presupuesto sin/con IVA, valor estimado, precios unitarios, pagos, facturación, aceptación, modificaciones, penalizaciones y exclusiones expresas. |
| A3 · Requisitos de solvencia de la empresa | Solvencia económica y técnica, ventas globales/sectoriales y periodos, patrimonio, ratios, seguros, experiencia, referencias/CBE, certificados, clasificación, alternativas, exenciones y acreditación. |
| A4 · Criterios de adjudicación | Criterios y subcriterios, puntos y pesos documentados, fórmulas y variables, umbrales, topes, redondeos, mejoras y condiciones/documentación para obtener puntos. |
| A6 · Requisitos del servicio | Alcance, actividades, volúmenes, horarios, SLA/KPI, procesos, herramientas, implantación, operación, transición, continuidad y reversibilidad. |
| A8 · Perfiles y equipo | Equipo mínimo, funciones, cantidades, dedicaciones, titulaciones, experiencia, certificaciones, adscripción, acreditación y sustituciones. |
| A9 · Seguridad y protección de datos | ENS, privacidad, medidas, alojamiento/cloud, transferencias, subencargados, incidentes, auditoría, conservación, borrado y cadena de suministro. |
| A10 · Compras, proveedores y colaboradores | Suministros, licencias, fabricantes, equivalencias, acreditaciones de partner, terceros, responsabilidades de aportación, subcontratación, logística, soporte y garantías. |

Cada extractor conserva documento, página/apartado identificable, literal breve,
valor, unidad/moneda, lote, periodo, hito, tipo y acreditación. Separa requisitos
obligatorios, puntuables, condiciones de ejecución e información descriptiva.
Señala contradicciones y documentos ausentes/parciales; no inventa una resolución.
Una ausencia se expresa como NO CONSTA, nunca como NO EXIGIDO por silencio.

## Resultado de la revisión de prompts

Los siete agentes ya contenían reglas objetivas, tanto en sistema como en usuario
y en la ampliación `viabilidad.py`. No recibían el dossier interno sintético en sus
prompts de extracción. Se han corregido estos puntos:

- A1 pedía veredicto y recomendación y recibía contexto interno: ahora solo orienta.
- A3 se centraba en proyectos/CBE; la solvencia económica quedaba en Económico-financiero.
  A3 cubre ahora ambos tipos de solvencia y sus medios de acreditación.
- A2 no pedía expresamente todo el presupuesto y los pagos: ahora lo hace.
- A4 permitía cálculos y añadía simulaciones locales después de Druid: ahora solo
  transcribe datos y reglas. Los cálculos de Económico-financiero siguen en capa 2.
- El orden intercalaba procesamiento y extracción: ahora hay una frontera explícita.
- El PDF de capa 1 conserva fuentes y estados de lectura y carece de dashboard de
  oportunidad. Los Markdown/PDF de este modo usan `_capa1` para distinguirlos del completo.

## Capa 2

Económico-financiero y Delivery / Operación procesan las siete extracciones. Coherencia
Documental recibe además esos análisis; Riesgos / Go-No-Go recibe la consolidación.
Los informes se pasan como documentos derivados identificados como capa 1, conservando
sus referencias originales. Los procesadores también reciben metadatos y avisos.
No reciben el texto original de los pliegos desde el flujo principal.

El contrato de sistema exige distinguir hechos, cálculos, hipótesis, evidencia interna
y recomendaciones. Los extractores no emiten veredictos de empresa: los procesadores
no deben presuponerlos. Las listas internas `INVENTED_*` siguen siendo ficticias y no
acreditan cumplimiento. No se han añadido conexiones a ERP, RRHH u otros sistemas.

## ¿Es suficiente para analizar el pliego?

El reparto cubre los ámbitos documentales necesarios para analizar las exigencias
del expediente. No permite garantizar por sí solo que una ejecución haya extraído
todos los requisitos ni decidir si una empresa debe presentarse.

La suficiencia de cada extracción depende de disponer de pliegos, CDC, anexos,
rectificaciones y aclaraciones aplicables, leerlos sin pérdidas y conservar cifras,
fórmulas, condiciones y fuentes. El lector existente puede encontrar documentos
ilegibles, formatos no soportados o límites de caracteres; los avisos deben mantenerse.
Las citas y la cobertura de documentos no equivalen a una auditoría de exhaustividad.

La viabilidad empresarial requiere, además, evidencia real de solvencia, personal,
certificados, costes, proveedores y capacidades. La capa 2 debe mantener como no
acreditado/no evaluable lo que carezca de prueba suficiente.

## Comprobación

`python -m unittest discover -s tests -v` verifica selección y orden, frontera de
entrada de la capa 2, aislamiento del dossier interno, supresión de simulaciones en
A4, cobertura de los nuevos campos, separación de archivos y trazabilidad del PDF.
Son pruebas locales con Druid simulado: comprueban el programa y los prompts, no la
calidad o exhaustividad de una respuesta real del modelo.

## Contrato JSON para la web

El modo `--capa 1` genera `<expediente>_capa1.json` junto al PDF. Es un JSON UTF-8
con `ensure_ascii=false`, válido para devolverlo como `application/json`. La raíz
contiene:

```json
{
  "schema": "oportunidades.capa1.v1",
  "version": 1,
  "capa": 1,
  "tipo_salida": "extraccion_documental",
  "expediente": "LIC-10484",
  "metadatos": {},
  "documentos_fuente": [],
  "avisos_procesamiento": [],
  "agentes": []
}
```

`agentes` siempre conserva el orden A1, A2, A3, A4, A6, A8, A9 y A10. Cada elemento
incluye un mini JSON con `contenido.resumen`, `contenido.secciones`,
`contenido.pendientes_y_no_localizados`, `contenido.trazabilidad` y
`contenido.salida_original`. Las secciones y las tablas se normalizan desde la
respuesta del agente; la salida original se conserva para que ningún dato se pierda
si el frontend necesita mostrar el informe tal como fue generado.
