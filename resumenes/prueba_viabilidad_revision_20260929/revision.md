# Revisión de extracción de viabilidad

Se incorporaron los requisitos del documento del usuario a los doce agentes y se
probó la extracción con Druid sobre OPP-SW-011. El caso aparece en la **opción 12**
del menú; LIC-10484 conserva la 11 y las licitaciones de Examples pasan a la 13.

**Resultado: cobertura amplia, con observaciones; no validación completa sin reservas.**
El control textual encuentra **58 de 59 comprobaciones**. El campo pendiente es el
nombre completo del nivel de partner: Compras escribe «Microsoft Solutions Partner
(Azure)» y omite «Infrastructure». Esto conserva la familia tecnológica, pero pierde
precisión en una acreditación exigida y debe corregirse/confirmarse al revisar la oferta.
La presencia de un valor no garantiza que todas las conclusiones del informe sean correctas.

## Qué se añadió

Se conservaron las instrucciones anteriores. `viabilidad.py` añade requisitos por
especialidad, estados de evidencia y tablas de extracción. Las fuentes del documento
se tratan como ubicaciones previstas, sin simular consultas a ERP, CRM, SharePoint,
RRHH o ROLECE. El documento no especificaba los métodos de acceso a esas fuentes.

El caso nuevo tiene un PCAP, un PPT y un dossier interno separado. Toda la información
es ficticia. El dossier solo se incluye en los prompts de OPP-SW-011 y no altera los
perfiles ni la situación corporativa de otras oportunidades.

## Evidencia de la prueba

Se obtuvieron respuestas reales de siete especialistas, Coherencia y Go/No-Go.
Esta carpeta reúne las respuestas de la revisión final. Cinco respuestas se reutilizaron
de la ejecución anterior porque el prompt completo era idéntico; Económico, Compras,
Coherencia y Go/No-Go se ejecutaron de nuevo tras los últimos ajustes. Los prompts y
respuestas se conservan por agente; los resultados esperados nunca se enviaron al modelo.

| Ámbito | Resultado observado | Respuesta |
|---|---|---|
| Ventas | Se extraen ventas globales e IT de 2023, 2024 y 2025. Detecta mejor IT de 1.180.000 EUR y déficit de 20.000 EUR | economic.md |
| Patrimonio y ratios | Extrae 410.000 EUR de patrimonio, activo corriente 720.000, pasivo 480.000 y liquidez 1,50 frente a mínimo 1,20 | economic.md |
| RC | Extrae póliza, asegurador, titular, actividad, millón por siniestro, dos millones agregado y fechas. Distingue CUMPLE AL CIERRE de NO ACREDITADO EJECUCIÓN por falta de renovación para 2027 | economic.md |
| CBE | Extrae objeto, tecnologías, cliente, CPV 72262000, inicio/fin y 465.000 EUR netos ejecutados de REF-001. Para REF-002 identifica ausencia de CBE, emisor y neto certificado | projects.md |
| Perfiles | Separa 6 años empresa / 10 sector de Ana y 4 / 7 de Sofia; extrae títulos, experiencia relevante, emisores e identificadores. Detecta PMP vencido al cierre y AWS sin vigencia acreditada | profiles.md |
| ISO 9001 y 14001 | Extrae titular, alcance, emisor, identificador y caducidad. Detecta fecha vencida de ISO 14001; la etiqueta del estado requiere revisión | admin.md |
| ISO 20000 | Identifica ausencia de certificado y deja titular, alcance, emisor y caducidad como NO CONSTA | service.md |
| ISO 27001 y ENS | Extrae emisor, titular, alcance, caducidad y nivel ENS; detecta que no cubren producción | security.md |
| Partnerships | Separa indirect reseller propio del partner externo, especialización caducada, fechas y compromiso ausente. Omite «Infrastructure» en el nombre del nivel | partners.md |
| ROLECE | Distingue inscripción aportada, actualización pendiente y falta de clasificación. Reconoce V/2/3 como alternativa que sustituye ventas y CBE | admin.md |
| Coherencia | Detecta discrepancias entre estados y corrige la lectura de cobertura RC y certificados fuera de alcance | coherence.md |
| Go/No-Go | Emite NO-GO y conserva los bloqueos de solvencia, CBE, seguro, certificados y personal | risk.md |

## Correcciones comprobadas durante la iteración

La primera versión omitía ventas de dos ejercicios, mezclaba candidatos con perfiles
plenamente acreditados y posponía información al final. Se exigieron fichas por campo
y se colocó la extracción antes del desarrollo del informe. Después se exigió distinguir
vigencia al cierre y cobertura completa de ejecución: la respuesta final de Económico
ya indica que el seguro no acredita todo el periodo contractual.

Las tablas repetidas reducían el espacio destinado al contenido original. Se limitaron
las fichas de Compras a partnerships y se redujo la consolidación a una matriz breve.
La respuesta final de Compras desarrolla sus secciones 1–17, sin anunciar una continuación;
Coherencia y Go/No-Go también desarrollan sus informes.

## Observaciones que impiden una validación sin reservas

1. **Nivel de fabricante incompleto.** Falta «Infrastructure» en Compras, aunque consta
   en el pliego y dossier. El control de cobertura lo marca como pendiente y no se
   ha relajado para convertir la abreviación en un acierto.
2. **Estados no siempre uniformes.** ISO 14001 está caducada en el caso, pero algunas
   respuestas usan «PENDIENTE VALIDACIÓN» o «NO ACREDITADO». Debe distinguirse el hecho
   probado de caducidad de la eventual aportación de una renovación futura.
3. **Precisión de las fuentes.** Proyectos atribuye al CBE algunas tecnologías que
   están en la ficha comercial general (por ejemplo WCAG), pero no en la transcripción
   del CBE. Los datos existen en el contexto; su atribución documental no es exacta.
4. **Conclusiones más fuertes que la evidencia.** Go/No-Go afirma imposibilidad de
   subsanar antes del cierre sin disponer de plazos reales de obtención de documentos.
   Lo acreditado es la situación actual y los requisitos pendientes. La recomendación
   NO-GO es compatible con el caso, pero esa predicción temporal exige revisión.

No se alteraron las respuestas del modelo para ocultar estas observaciones. Tampoco
se certifica la precisión de todos los cálculos de precios/márgenes o de los restantes
análisis anteriores: la prueba está centrada en los nuevos campos de viabilidad.

## Control de requisito no exigido

Se realizó otra llamada real a Compras con OPP-SW-005, cuyo pliego dice que no exige
partner de fabricante. La respuesta lo marca **NO EXIGIDO**, sin convertirlo en
condición de admisión. No recibió el dossier OPP-SW-011. El informe de este control
está en `../prueba_viabilidad_no_exigido_20260929/partners.md`.
La respuesta vincula también experiencia Microsoft valorable con certificación;
esa equiparación no queda demostrada por el pliego y no se valida en este control.

## Comprobaciones locales y reproducción

Las tres pruebas locales pasan: selección del caso/Examples, aislamiento del dossier
y comprobación de que el auditor analiza respuestas, no los prompts. Compilación
Python y revisión de espacios del diff correctas.

```powershell
python -m unittest discover -s tests -v
python comprobar_viabilidad.py
python comprobar_viabilidad.py --live
python verificar_campos_viabilidad.py resumenes/prueba_viabilidad_revision_20260929
```

El último comando devuelve código 1 por el campo incompleto indicado, y guarda
`cobertura_campos.json`. `estado.json` registra ejecución y revisión; no confundir
«RESPUESTA RECIBIDA» con validación semántica superada. Para una nueva ejecución se
crea otra carpeta, sin reemplazar los resultados de esta revisión.
