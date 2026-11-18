# Cobertura documental de preventa — 14/10/2026

La capa 1 extrae hechos y reglas de los documentos. Conserva condiciones, excepciones,
fases, unidades y fuentes en los JSON; el redactor los integra en el formato AGE
existente, con prosa, subapartados, listas, tablas de 2–4 columnas y conclusión operativa.

## Responsables de los puntos solicitados

| Materia | Responsable principal | Detalle que se debe conservar |
|---|---|---|
| Fases y documentación | A2 Administrativo-legal; A3 en solvencia | Participación, oferta, requerimiento, adjudicación, formalización y ejecución; sujeto, sobre, documento/compromiso, momento de cumplimiento y acreditación, plazo y evento inicial |
| Exenciones y obligaciones | Todos; A2/A3/A10 según materia | Diferenciar exención de documento, ausencia de evidencia y obligación material; literal y alcance de cada exención |
| Clasificación contractual | A2; especialistas en su ámbito | Condición especial, obligación esencial y otra obligación contractual; clasificación literal y consecuencias, sin equipararlas |
| Importes y reglas económicas | A2 | PBL, IVA, valor estimado, lotes, anualidades, prórrogas, modificaciones, precios unitarios, bolsas, límites y gastos incluidos |
| Facturación y cobro | A2 | Unidad/hito facturable, consumo autorizado, conformidad, evidencia, calendario, pago, retenciones y conceptos sin ingreso garantizado |
| Criterios y puntos | A4 Adjudicación | Subcriterios, fórmulas, variables, baremos completos, extremos, topes, redondeo, mínimos, desempates y acreditación |
| Ofertas anormalmente bajas | A4; A2 en trámite | Parámetros y casos según número de ofertas, grupos, bases y exclusiones; requerimiento, justificación, cómputo del plazo y consecuencias |
| Garantías | A2; A6 para garantía del servicio | Garantías económicas: base, importe, constitución, reposición y devolución; garantía del servicio: duración, inicio, cobertura y correcciones |
| Equipo | A8 Perfiles | Personas, puestos, perfiles, dedicación, horas y capacidad adicional separados; experiencia específica, conocimientos, pruebas y adscripción |
| Incorporación y sustitución | A8; A6 en transición | Hitos, plazos, autorización, equivalencia, preaviso, transferencia y solapamiento |
| Ausencias y continuidad | A8 y A6 | Vacaciones, bajas, refuerzos y cobertura obligatoria, medios y costes expresamente atribuidos; sin dimensionar ni valorar costes no documentados |
| Horarios y disponibilidad | A6 Servicio | Atención habitual, calendario, presencialidad, guardias, ventanas, emergencias y cobertura adicional |
| Alcance técnico y operativo | A6 | Plataformas, integraciones, herramientas, tareas, volúmenes, dependencias y entregables con aceptación |
| Medios y costes del adjudicatario | A10 Compras; A2/A6 en condiciones económicas/operativas | Licencias, infraestructura, herramientas y equipos; quién aporta, paga, mantiene, renueva y transfiere; medios del cliente separados |
| Fabricantes y proveedores | A10 | Obligación material, acreditación/carta, nivel, canal, vigencia, soporte y responsabilidad; no extrapolar una exención documental |
| SLA y consecuencias | A6; A2 en régimen contractual | Definición, umbral, reloj, acuse/respuesta/resolución, medición, penalización, base, límites y resolución, con relación documental explícita |
| Seguridad y datos | A9 Seguridad | Medidas, roles, incidentes, destinatarios, comunicaciones, plazos, evidencias, auditorías y responsabilidades concretas |
| Cierre y transferencia | A6; A9 datos; A10 activos/licencias | Documentación, activos, conocimiento, sucesor, continuidad, aceptación, devolución/borrado, plazos y costes atribuidos |
| Discrepancias internas | Cada especialista; redactor en consolidación | Dos cláusulas/valores y fuentes, ámbito y efecto; pendiente de aclaración, sin resolver por suposición |
| Errores del resumen | Redactor y revisión editorial | Corregir contra el JSON; no convertir errores del borrador o desacuerdos entre agentes en contradicciones probadas del pliego |
| Limitaciones del procesamiento | Registro local y todos los agentes | Atribuir avisos al registro disponible; no afirmar que una lectura de PDF verifica JSON, enlaces u OCR de una ejecución anterior |

A1 sigue siendo una referencia de máximo 100 palabras y cinco viñetas; no sustituye
el detalle de los siete especialistas ni el resumen final.

## Cambios y causa identificada

Había instrucciones incompatibles con la precisión requerida: el estado combinado
`NO EXIGIDO/NO CONSTA` y una instrucción que podía generalizar la inexistencia de
fabricante/canal/partnership/carta. Se han separado los estados y limitado las
exenciones al objeto, fase y alcance documentados. Otras materias ya figuraban en los
prompts, pero sin exigir todos sus subcampos, condiciones y relaciones.

`capa1_requirements.py` centraliza la precisión transversal y la cobertura específica.
`viabilidad.py` la incorpora a los prompts de sistema y de usuario de los siete
especialistas; A1 recibe las reglas transversales. `age_report.py` incorpora la misma
cobertura al borrador, a la revisión y a sus reintentos, junto con el prompt editable
`docs/prompt_resumen_age.md`.

La capa 1 ejecuta un único prompt por agente con el texto documental completo.
No llama a la revisión por materias de `documentary_audit.py`, ni selecciona fragmentos
para los extractores. Los límites `MAX_*_PROMPT_DOCUMENT_CHARS` no compactan capa 1.
Los requisitos de precisión y cobertura se conservan dentro del prompt de cada agente.
Las salidas se guardan directamente en los JSON individuales y en el JSON de capa 1,
con el índice de documentos y avisos reales de lectura. No se añade `revision_documental`
a las nuevas extracciones ni se presentan como contrastadas por un segundo agente.

En `--capa 1` no se hacen llamadas separadas de recomendaciones. El redactor final
recibe el JSON completo y mantiene sus controles de formato y cobertura. Los reintentos
técnicos de Druid permanecen; no son una división del análisis en fragmentos.

## Fuera de capa 1

- Calcular coste real, rentabilidad, margen, tesorería o precio recomendado.
- Dimensionar suplentes, FTE, turnos y recursos adicionales a partir de la cobertura.
- Valorar salarios, licencias, proveedores o contingencias sin importe documental.
- Proponer personas/proveedores, estrategia de puntos o decisión Go/No-Go.
- Resolver jurídicamente contradicciones sin aclaración documental o comprobar
  capacidades empresariales sin evidencia interna real.

La capa 1 sí recoge todas las obligaciones y reglas contractuales necesarias para
esos análisis posteriores. Una obligación de continuidad sin número de suplentes
debe conservarse como tal, con dimensionamiento e importe no especificados.

## Validación y uso

`python -m unittest discover -s tests -v` comprueba integración, citas y referencias,
estados, discrepancias, conservación de condiciones en el resumen, recuperación
editorial y rechazo sin sobrescribir PDF anteriores. Druid está simulado en la batería:
no acredita calidad semántica ni exhaustividad de una ejecución real. Las pruebas
reales se archivan por separado y no sustituyen la revisión del expediente completo.

Los informes guardados anteriormente no se regeneran con este cambio. Para extraer
los campos que faltaban hay que volver a ejecutar `python oportunidades.py --capa 1`
y seleccionar el expediente. `--desde-json` aplica la nueva revisión editorial, pero
no recupera hechos que nunca se extrajeron en el JSON de origen.


## Dossier completo para preventa

Cada prompt de especialista incorpora `PRESALES_EXTRACTION` y las comprobaciones de
su especialidad en `PRESALES_CHECKS`. Se exige lectura de todos los documentos,
extracción de reglas con condiciones completas, listas finitas completas, comparación
de tablas/desarrollos y separación de ausencia, parámetro no especificado y remisión.
No se fija un objetivo de brevedad para los especialistas. A1 conserva su función
orientativa; no sustituye el desarrollo de los otros siete agentes.

El redactor y su revisión reciben `EDITORIAL_PRESALES`: todo hecho relevante debe
quedar desarrollado en el cuerpo, con tablas de hasta cuatro columnas y sin límite
objetivo de páginas. No se añaden pasadas de extracción ni se fragmentan documentos.
El coste de llamadas no se usa como criterio para recortar el detalle solicitado.
Esto refuerza instrucciones; no convierte la validación formal en verificación
semántica completa. Las salidas existentes no cambian sin una nueva ejecución.


## Recuperación del redactor final

Una ficha de una sola sección para una extracción amplia vuelve al redactor completo;
no pasa a una revisión de cambios puntuales. Si tres revisiones editoriales no producen
un resultado válido, se solicita un nuevo borrador dentro del límite de tres borradores.
El PDF solo se publica cuando supera los controles.

`entrada_completa.json` conserva el JSON original y `entrada_editorial.json` registra
exactamente lo enviado al modelo. Cada salida original se envía íntegra una sola vez
cuando los campos estructurados son una copia que el parser local reconstruye exactamente.
Si esos campos contienen datos adicionales o provienen de otro esquema, se conservan.
Esto no divide la extracción en fragmentos ni omite requisitos.
