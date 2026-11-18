# Revisión de la ejecución de LIC-10484

**Resultado: NO VALIDADO.** Se crearon los doce informes Markdown y el PDF de 53
páginas, pero se omitieron documentos esenciales y dos requisitos reales de solvencia.
La salida del usuario selecciona la opción 11, LIC-10484; no es el ensayo sintético
OPP-SW-011 de la opción 12. No procede aplicar aquí el contador de 59 campos de ese
ensayo: hay que contrastar los requisitos de esta licitación.

## Causa principal

El XML contiene diez referencias documentales: un pliego administrativo, un técnico,
siete `cac:AdditionalDocumentReference` y un documento general. El programa procesó
solo tres, tal como indica la salida de consola.

`document_refs()` en `oportunidades.py` recoge `LegalDocumentReference`,
`TechnicalDocumentReference` y `GeneralDocument`, pero omite `AdditionalDocumentReference`.
No es un fallo de descarga del Cuadro de Características: el lector ni siquiera lo
incorporó a la lista de documentos que debía procesar.

Los siete omitidos son:

- LIC10484 PPT Anexo 2.pdf
- LIC10484 PCP CDC Anexo 2.pdf
- LIC10484 PPT Anexo 1.pdf
- LIC10484 PCP CDC Anexo 1.xlsx
- LIC10484 PCP ANEXOS.pdf
- LIC10484 PCP CDC.pdf
- LIC10484 PPT Anexo 3.pdf

Para esta revisión se descargaron y leyeron el Cuadro de Características, el anexo
de ficha de experiencia del equipo y los anexos administrativos. No se modificaron
el programa ni los informes de la ejecución del usuario.

## Contraste con la información requerida

| Parámetro | Resultado del programa | Evidencia contrastada | Evaluación |
|---|---|---|---|
| Volumen anual de negocio | Económico, Coherencia y Go/No-Go dicen NO EXIGIDO | CdC 10.A: no hay exención. CdC 10.C: mínimo 34.440 EUR anuales en consultoría/asesoramiento eléctrico y gasístico, en al menos uno de los tres últimos ejercicios cerrados | FALLO CRÍTICO: omite importe, ámbito y periodo |
| Servicios previos / solvencia técnica | Proyectos afirma que no se exigen referencias ni importes | CdC 10.D: principales servicios similares de los últimos tres años, con importe anual acumulado de al menos 16.072 EUR, sin impuestos indirectos, en el año de mayor ejecución; debe incluir importe, fechas y destinatario público/privado | FALLO CRÍTICO: omite solvencia técnica real; no es un mínimo por contrato individual |
| Empresas de nueva creación | No distingue esta alternativa | CdC 10.E: personal/unidades técnicas, los dos perfiles esenciales y CV para acreditarlos | OMITIDO al faltar el CdC |
| Perfiles y titulaciones | Identifica los dos responsables, sus titulaciones y tres años de experiencia energética | PPT apartado 7, páginas impresas 10–11, páginas PDF 12–13 | CORRECTO en lo principal; falta incorporar la ficha oficial de experiencia del anexo 2 del CdC |
| Datos de las fichas de experiencia | Se centra en título y años | Anexo 2 CdC pide empresas, fechas de inicio/fin, actividad, cargo/tareas, clientes y actividad desarrollada para ellos | INCOMPLETO: anexo no leído |
| Patrimonio / ratios | NO EXIGIDO | En el apartado de solvencia del CdC revisado se exige volumen de negocio, no umbral adicional de patrimonio/ratio | Compatible con el documento revisado; no demuestra la capacidad del modelo para extraer ratios cuando sí existan |
| RC profesional | NO EXIGIDO | CdC 34.A, página PDF 14: no se exige | CONCLUSIÓN CORRECTA, pero el agente citó una sección que no había recibido; su acierto no valida la trazabilidad |
| Clasificación | NO EXIGIDO | CdC 10.B: N/A | CORRECTO, con la misma limitación de fuente omitida en la ejecución |
| ROLECE | Inscripción NO CONSTA | No se aportó certificado de inscripción de la empresa; el PCP describe su uso documental general | Correcto no inventar la inscripción ni su vigencia |
| ISO / ENS | No identifica obligación de esas certificaciones | No se localiza exigencia específica en PCP, PPT y CdC revisados | Compatible con esas fuentes; no debe convertir certificaciones internas genéricas en documentos vigentes |
| Certificaciones internas | Seguridad afirma ISO 27001 y ENS vigentes con «Certificado interno, 2025-2027» | El contexto indica disponibilidad de certificaciones y, para ENS, auditoría superada en 2025 y siguiente planificada en 2027; no aporta un certificado con ese intervalo de vigencia | FALLO: calendario de auditoría no equivale a fecha de validez acreditada |
| Partnerships | Go/No-Go marca «Partnership sectorial» como NO CUMPLE | Los perfiles energéticos pueden requerir contratación o colaboración externa; no se ha identificado un nivel de acreditación de fabricante exigido por el pliego | Debe separar necesidad derivada de personal/partner de un requisito literal de partnership |

La facturación genérica de una empresa IT no acredita por sí sola los 34.440 EUR de
facturación energética. Lo correcto con los datos internos disponibles sería declarar
esa solvencia sectorial **NO ACREDITADA**, no «NO EXIGIDA» ni «CUMPLE» por usar ventas globales.
Lo mismo ocurre con las referencias IT frente a los servicios eléctricos/gasísticos exigidos.

## Problemas de evidencia y de propagación

El informe económico atribuye los importes corporativos a «Cuentas auditadas» y el
seguro a «Póliza interna». En esta ejecución esos valores provienen de datos ficticios
del programa, sin cuentas ni póliza adjuntas. Además, el dato genérico de RC de un
millón de euros se presenta como límite por siniestro sin que esa modalidad conste.
Las fuentes deben identificarse como datos internos aportados sin documento acreditativo.

Coherencia y Go/No-Go propagan la ausencia ficticia de solvencia económica y referencias.
Aunque el NO-GO final detecta correctamente un problema de perfiles, llega con una
base incompleta: falta incorporar los requisitos económicos y técnicos realmente exigidos.

Compras/Partners genera las tablas de extracción, pero el archivo termina tras ellas
y una explicación de alianzas; no desarrolla el informe completo de compras que se le
solicita. Encontrar algunos campos no garantiza la integridad del resto de secciones.

## PDF y archivos

- Los doce Markdown y el PDF existen y corresponden a la ejecución del usuario.
- El PDF contiene 53 páginas. En su página 25 se reproduce el error «Volumen de
  negocio: NO EXIGIDO». Los importes 34.440 y 16.072 no aparecen en los informes.
- Coherencia se guarda como Markdown y no aparece como capítulo del PDF: el código
  la excluye expresamente mediante `build_client_ready_sections()`. No es un fallo de generación.
- Se inspeccionaron visualmente la página de solvencia del CdC y la página económica
  del informe. No se ha realizado una auditoría visual completa de las 53 páginas.
- No se detectaron identificadores del dossier sintético OPP-SW-011 en estos informes;
  el aislamiento de ese caso se conserva.

## Qué debe corregirse antes de repetir

1. Incluir todas las referencias documentales del XML, también las adicionales, e
   informar del total encontrado, leído, omitido y fallido. Hay un XLSX entre los anexos:
   incluir su referencia no basta si después no puede extraerse su contenido.
2. Cuando un pliego remite al CdC o a un anexo ausente, marcar ese requisito como
   NO EVALUABLE / DOCUMENTO PENDIENTE. No inferir NO EXIGIDO por ausencia de texto.
3. Impedir presentar datos corporativos sin soporte como cuentas auditadas, pólizas o
   certificados leídos. No convertir una próxima auditoría en fecha de caducidad.
4. Reejecutar LIC-10484 y exigir la extracción de CdC 10.C, 10.D y 10.E antes de
   validar los resultados. Para comprobar todos los campos sintéticos del documento
   original, ejecutar además OPP-SW-011, opción 12.

## Archivos de referencia

- Fuente decisiva: `data/docs/b845a8c31a07d69c/LIC10484 PCP CDC.pdf.pdf`,
  página PDF 5 (impresa 4), apartados 10.A–10.E; página PDF 14, apartado 34.A.
- Ficha de experiencia: `data/docs/d530cb0f85103be3/LIC10484 PCP CDC Anexo 2.pdf.pdf`.
- Informes afectados: `LIC-10484_economico_financiero.md`,
  `LIC-10484_solvencia_proyectos.md`, `LIC-10484_coherencia_documental.md`,
  `LIC-10484_riesgos_go_nogo.md` y `LIC-10484_seguridad_dpo_ens.md`.
