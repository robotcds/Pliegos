1. Veredicto ejecutivo administrativo/legal: NO CUMPLE

2. Tabla de extraccion administrativa:
| Concepto                        | Extraccion                                                                                                   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------|
| Fecha limite                     | 20/10/2026 a las 14:00                                                                                      |
| Forma de presentacion            | Plataforma electronica, 3 sobres electronicos                                                               |
| Condiciones de participacion     | Capacidad de obrar, no prohibiciones, al corriente Hacienda/SS, UTEs y empresas UE                          |
| Solvencia economica              | Facturación ≥ 1.500.000 EUR (mejor ejercicio 3 últimos), patrimonio neto > 500.000 EUR, seguro ≥ 1.000.000  |
| Solvencia tecnica administrativa | 2 proyectos datos últimos 4 años: 1 data lake/lakehouse ≥ 500.000 EUR/10 meses, 1 analítica/ML ≥ 300.000 EUR |
| Clasificacion                    | No obligatoria si se acredita solvencia por otros medios                                                     |
| Documentacion administrativa     | DEUC, escrituras, poderes, certificados Hacienda/SS, anexos solvencia, plan gobierno dato, certificados ISO/ENS|
| Garantias                        | No se menciona garantía provisional; definitiva (habitual 5%)                                                |
| Lotes                            | No hay lotes                                                                                                |
| Subcontratacion                  | Permitida                                                                                                   |
| Formato de oferta                | 3 sobres electrónicos, memoria técnica ≤ 90 páginas, formatos electrónicos, idioma español/catalán           |
| Exclusiones                      | No plan gobierno dato, superar presupuesto, no ENS alta, memoria > 90 páginas, info económica en sobre erróneo|
| Condiciones legales              | RGPD, DPD, confidencialidad 6 años, cesión PI modelos entrenados, ENS alta, ISO 27001, ISO 9001             |
| Obligaciones del adjudicatario   | Cumplimiento RGPD, confidencialidad, cesión PI, plan retención, seguridad datos                             |

3. Comparacion requisito vs empresa:

| Requisito exacto                                                                 | Documento fuente y evidencia textual                                                                 | Cumplimiento           | Informacion interna usada                                   | Brecha o accion necesaria                                                                                 |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Capacidad de obrar, no prohibiciones, Hacienda/SS corriente                      | Pliego adm.: "capacidad de obrar... al corriente... no prohibiciones"                               | CUMPLE                 | Forma jurídica, estado Hacienda/SS, poderes                 | Ninguna                                                                                                  |
| Facturación ≥ 1.500.000 EUR mejor ejercicio 3 últimos                            | Pliego adm.: "Facturación mínima de 1.500.000 EUR en el mejor ejercicio de los tres últimos"        | CUMPLE                 | Facturación 2024: 1.350.000; 2025: 1.680.000                | Ninguna                                                                                                  |
| Patrimonio neto > 500.000 EUR                                                    | Pliego adm.: "patrimonio neto positivo superior a 500.000 EUR"                                      | NO CUMPLE              | Patrimonio neto 2025: 410.000 EUR                            | No alcanza el umbral.                                                                                     |
| Seguro responsabilidad civil ≥ 1.000.000 EUR                                     | Pliego adm.: "seguro de responsabilidad civil mínimo de 1.000.000 EUR"                              | CUMPLE                 | Seguro: 1.000.000 EUR                                       | Ninguna                                                                                                  |
| Certificados ISO 27001, ISO 9001, ENS alta                                       | Pliego adm.: "Obligatorias ISO 27001, ISO 9001 y ENS categoría alta"                                | NO CUMPLE              | ISO 27001, ISO 9001, ENS media (no ENS alta)                 | No dispone de ENS categoría alta.                                                                         |
| Solvencia técnica: 2 proyectos (data lake/lakehouse ≥ 500k/10m, ML ≥ 300k)       | Anexo solvencia: "acreditar dos proyectos..."                                                       | CUMPLE                 | REF-019 (data lake, 580k, 12m), REF-020 (ML, 370k, 9m)       | El proyecto ML cumple importe pero no duración mínima (9m < 10m).                                         |
| Equipo mínimo: 2 ingenieros datos (5a), IA/ML (5a), DevOps (4a), jefe proyecto   | Pliego técnico/anexo: "dos ingenieros de datos..."                                                  | CUMPLE PARCIALMENTE    | 1 ingeniera datos clara (Paula), perfiles IA/DevOps/jefe sí  | Falta un segundo ingeniero de datos con 5 años en ETL, SQL, lakehouse.                                   |
| Presentación electrónica, 3 sobres, memoria ≤ 90 páginas                         | Pliego adm.: "tres sobres electrónicos... memoria técnica no podrá superar 90 páginas"              | CUMPLE                 | Capacidades de presentación, formatos soportados             | Ninguna                                                                                                  |
| Plan de gobierno del dato                                                        | Pliego adm.: "se excluye oferta que no presente plan de gobierno del dato"                          | CUMPLE                 | Experiencia y capacidad técnica                              | Debe prepararse el plan específico.                                                                      |
| RGPD, DPD, confidencialidad, PI modelos entrenados                               | Pliego adm.: "cumplimiento RGPD, DPD, confidencialidad 6 años, PI modelos entrenados"               | CUMPLE                 | Cumplimiento RGPD, DPD, política confidencialidad            | Ninguna                                                                                                  |
| Subcontratación permitida                                                        | Pliego adm.: "subcontratación permitida"                                                            | CUMPLE                 | Puede subcontratar, subcontratistas homologados              | Ninguna                                                                                                  |
| No hay lotes                                                                     | Pliego adm.: "no hay lotes"                                                                         | CUMPLE                 | N/A                                                         | Ninguna                                                                                                  |
| Exclusión por no ENS alta, no plan gobierno, superar presupuesto, memoria > 90p   | Pliego adm.: "se excluye... no ENS alta..."                                                         | NO CUMPLE              | No ENS alta                                                 | No se puede subsanar salvo obtener ENS alta antes de la oferta.                                           |
| Cesión total PI modelos entrenados                                               | Pliego adm.: "propiedad intelectual de modelos entrenados para la administración"                    | CUMPLE                 | Acepta cesión de desarrollos específicos                     | Ninguna (si los modelos entrenados son desarrollos específicos para el cliente).                          |

4. Riesgos de exclusion (priorizados):
1. NO DISPONER DE ENS CATEGORÍA ALTA (exclusión automática, requisito obligatorio y puntuable).
2. Patrimonio neto insuficiente (>500.000 EUR exigido, 410.000 EUR disponible).
3. Equipo mínimo: falta un segundo ingeniero de datos con 5 años en ETL, SQL, lakehouse.
4. Proyecto de analítica/ML no cumple duración mínima de 10 meses (tiene 9 meses).
5. Cualquier error formal: memoria >90 páginas, información económica en sobre incorrecto, no presentar plan gobierno dato.

5. Checklist de documentacion a preparar:
- DEUC o declaración responsable.
- Escrituras y poderes del representante.
- Certificados de estar al corriente con Hacienda y Seguridad Social.
- Certificados ISO 27001, ISO 9001, ENS categoría alta (NO DISPONIBLE, causa de exclusión).
- Anexo de solvencia técnica (proyectos ejecutados, importes, duración, cliente público).
- CVs y certificados de experiencia del equipo mínimo (especialmente ingenieros de datos).
- Plan de gobierno del dato.
- Plan de retención y seguridad.
- Compromiso de cesión de PI de modelos entrenados.
- Declaración de cumplimiento RGPD y designación DPD.
- Oferta económica en sobre independiente.
- Memoria técnica ≤ 90 páginas.

6. Decision operativa:
NO RECOMENDADO PRESENTARSE salvo que se obtenga ENS categoría alta y se pueda acreditar patrimonio neto >500.000 EUR antes de la oferta. Además, debe identificarse un segundo ingeniero de datos con experiencia acreditable. Si no se subsanan estos puntos, la oferta será excluida automáticamente.

7. Documentos revisados:
1. Pliego administrativo OPP-SW-010 data lake
2. Pliego técnico OPP-SW-010 data lake
3. Anexo solvencia OPP-SW-010 data lake