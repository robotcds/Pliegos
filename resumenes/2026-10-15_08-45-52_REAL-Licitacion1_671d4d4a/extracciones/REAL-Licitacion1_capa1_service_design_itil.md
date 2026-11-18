# 1. Resumen factual del servicio requerido

El contrato tiene por objeto la prestación de servicios profesionales para el diseño, desarrollo, puesta en servicio, mantenimiento y evolución tecnológica de un Asistente Virtual (BOT conversacional con IA tradicional y generativa) integrado en el portal Decide Madrid del Ayuntamiento de Madrid. El servicio se ofrece en modalidad SaaS, siendo el adjudicatario responsable de la gestión y operación de todos los elementos de la solución, salvo la infraestructura MultiCloud corporativa (Google Cloud Platform, Microsoft Azure, Amazon AWS) proporcionada por el Ayuntamiento. Incluye panel de control, formación, mantenimiento, monitorización, soporte de primer nivel, evolución tecnológica mediante bolsa de horas, cumplimiento de normativa de IA, seguridad, accesibilidad, transparencia y reversibilidad.

# 2. Alcance y volumetrías

| Dato                                    | Valor/Unidad                | Periodo         | Fuente                                    |
|-----------------------------------------|-----------------------------|-----------------|-------------------------------------------|
| Usuarios registrados Decide Madrid      | 555.318                     | Histórico       | ID_188_3.PDF, p.3                         |
| Debates                                | 8.220                       | Histórico       | ID_188_3.PDF, p.3                         |
| Propuestas                             | 36.124                      | Histórico       | ID_188_3.PDF, p.3                         |
| Consultas públicas                     | 150                         | Histórico       | ID_188_3.PDF, p.3                         |
| Personas atendidas por asistente 2023  | 6.246                       | Año 2023        | ID_188_3.PDF, p.6                         |
| Mensajes intercambiados 2023           | 27.083                      | Año 2023        | ID_188_3.PDF, p.6                         |
| Personas atendidas por asistente 2024  | 4.490                       | Año 2024        | ID_188_3.PDF, p.6                         |
| Mensajes intercambiados 2024           | 46.723                      | Año 2024        | ID_188_3.PDF, p.6                         |
| Personas atendidas por asistente 2025* | 2.552                       | Hasta 30/11/25  | ID_188_3.PDF, p.6                         |
| Mensajes intercambiados 2025*          | 26.784                      | Hasta 30/11/25  | ID_188_3.PDF, p.6                         |
| Capacidad mínima asistente             | 50 conversaciones simultáneas| Durante contrato| ID_188_3.PDF, p.13                        |
| Tráfico mínimo asistente               | 15.000 mensajes/mes         | Durante contrato| ID_188_3.PDF, p.13                        |
| Horario servicio primer nivel atención | 11:00-14:00 días laborables | Durante contrato| ID_188_3.PDF, p.16; ID_188_2.PDF, Anexo I |
| Bolsa de horas evolución tecnológica   | 600 horas (ampliable)       | Vigencia contrato| ID_188_3.PDF, p.17; ID_188_2.PDF, Anexo I |
| Formación                              | 20 horas, máx. 20 asistentes| Contrato        | ID_188_3.PDF, p.16-17                     |
| Plazo ejecución                        | 24 meses (+prórrogas)       | Contrato        | ID_188_2.PDF, Anexo I                     |
| Lugar prestación                       | Dependencias adjudicataria  | Contrato        | ID_188_2.PDF, Anexo I; ID_188_3.PDF, p.52 |

# 3. Modelo de servicio exigido

- Modalidad SaaS: adjudicatario responsable de gestión y operación de todos los elementos de la solución, salvo infraestructura MultiCloud corporativa (Google Cloud Platform, Microsoft Azure, Amazon AWS) proporcionada por el Ayuntamiento. (ID_188_3.PDF, p.1; ID_188_2.PDF, Anexo I)
- Fases: Fase I Implantación (máx. 2 meses), Fase II Operación (resto del contrato). (ID_188_3.PDF, p.8-9)
- Panel de control accesible vía navegador, sin instalación local. (ID_188_3.PDF, p.14)
- Servicio de primer nivel de atención (agente humano) en horario 11:00-14:00 días laborables. (ID_188_3.PDF, p.16)
- Monitorización y supervisión diaria de conversaciones (días laborables). (ID_188_3.PDF, p.15)
- Mantenimiento preventivo, correctivo y evolutivo. (ID_188_3.PDF, p.17)
- Bolsa de horas de evolución tecnológica (600 horas, ampliable por mejora). (ID_188_3.PDF, p.17; ID_188_2.PDF, Anexo I)
- Formación inicial y de actualización. (ID_188_3.PDF, p.16-17)

# 4. Procesos y actividades

| Proceso/actividad                        | Expreso en pliego | Exigencia descrita                                                                 | Fuente                  |
|------------------------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------|
| Gestión de incidencias                   | ITIL NO CITADO    | Mantenimiento correctivo, soporte técnico, resolución de incidencias                | ID_188_3.PDF, p.17      |
| Monitorización y supervisión             | ITIL NO CITADO    | Monitorización diaria de conversaciones, revisión de calidad y mejora continua      | ID_188_3.PDF, p.15      |
| Gestión de cambios/evolución tecnológica | ITIL NO CITADO    | Bolsa de horas para proyectos de evolución tecnológica                              | ID_188_3.PDF, p.17      |
| Transferencia de conocimiento            | ITIL NO CITADO    | Actividades de transferencia de conocimiento al final del contrato                  | ID_188_3.PDF, p.9       |
| Formación a usuarios                     | ITIL NO CITADO    | Formación inicial y de actualización al personal DGPC                              | ID_188_3.PDF, p.16-17   |
| Gestión documental y reporting           | ITIL NO CITADO    | Entrega de documentación técnica, informes mensuales, informe final de proyecto     | ID_188_3.PDF, p.9,11,41 |
| Gestión de datos y reversibilidad        | ITIL NO CITADO    | Entrega y borrado seguro de datos, bases de datos, modelos, logs, etc. al cierre    | ID_188_3.PDF, p.9,40-41 |
| Supervisión humana de IA                 | ITIL NO CITADO    | Supervisión humana de las respuestas del asistente virtual                         | ID_188_3.PDF, p.15,38   |

# 5. SLA/KPI/penalizaciones

| Servicio/Actividad                | Prioridad | Respuesta/Resolución | Horario/Objetivo                  | Penalización                        | Fuente                        |
|-----------------------------------|-----------|---------------------|-----------------------------------|-------------------------------------|-------------------------------|
| Fase implantación                 | N/A       | 2 meses máx.        | Desde inicio contrato             | Penalidad por incumplimiento        | ID_188_3.PDF, p.8-9; ID_188_2.PDF, Anexo I |
| Disponibilidad asistente virtual   | N/A       | 24x7x365            | 24x7x365 (excepto mantenimientos) | Penalidad si indisponibilidad >48h  | ID_188_3.PDF, p.13,76         |
| Indisponibilidad >48h             | Grave     | N/A                 | N/A                               | 5% precio contrato (grave)          | ID_188_2.PDF, Anexo I, p.76   |
| Indisponibilidad >5 días          | Muy grave | N/A                 | N/A                               | 10% precio contrato (muy grave)     | ID_188_2.PDF, Anexo I, p.77   |
| Retraso en implantación >1 semana | Grave     | N/A                 | N/A                               | 5% precio contrato                  | ID_188_2.PDF, Anexo I, p.76   |
| Retraso en implantación >2 semanas| Muy grave | N/A                 | N/A                               | 10% precio contrato                 | ID_188_2.PDF, Anexo I, p.77   |
| Monitorización y supervisión      | N/A       | Diaria (laborables) | Días laborables                   | Penalidad por incumplimiento        | ID_188_3.PDF, p.15; ID_188_2.PDF, Anexo I |
| Servicio primer nivel atención    | N/A       | 11:00-14:00         | Días laborables                   | Penalidad por incumplimiento        | ID_188_3.PDF, p.16; ID_188_2.PDF, Anexo I |
| Informe de impacto de género      | N/A       | Antes fin contrato  | N/A                               | 5% precio contrato                  | ID_188_2.PDF, Anexo I, p.78   |
| Cumplimiento condiciones sociales | N/A       | N/A                 | N/A                               | 5% precio contrato                  | ID_188_2.PDF, Anexo I, p.78   |

# 6. Organización y roles exigidos

| Rol/Perfil                        | Nº Personas | Titulación mínima                | Experiencia mínima                                      | Fuente                  |
|-----------------------------------|-------------|-------------------------------|--------------------------------------------------------|-------------------------|
| Jefe/a de Proyecto                | 2           | Universitaria grado/equiv.     | 5 años dir. proyectos administración electrónica; 3 años asistentes virtuales | ID_188_3.PDF, p.25-26 |
| Técnico/a experto/a nube          | 1           | Universitaria grado/equiv.     | 3 años funciones perfil; 2 años asistentes virtuales    | ID_188_3.PDF, p.25-26   |
| Analista programador              | 1           | Universitaria grado/equiv.     | 3 años funciones perfil; 2 años asistentes virtuales    | ID_188_3.PDF, p.25-26   |
| Experto en IA y análisis de datos  | 1           | Universitaria grado/equiv.     | 3 años funciones perfil; 2 años asistentes virtuales    | ID_188_3.PDF, p.25-26   |
| Lingüista computacional           | 1           | Universitaria grado/equiv.     | 3 años funciones perfil; 2 años asistentes virtuales    | ID_188_3.PDF, p.25-26   |
| Agente primer nivel atención      | 2           | Educación Secundaria           | 3 años atención ciudadanía en castellano                | ID_188_3.PDF, p.25-26   |
| Consultor evolución tecnológica   | 1           | Universitaria grado/equiv.     | 5 años funciones perfil; 3 años análisis proyectos administración electrónica; 3 años asistentes virtuales | ID_188_3.PDF, p.25-26 |

- Sustituciones: plazo 7 días para presentar sustituto, con acreditación de requisitos. (ID_188_3.PDF, p.28)
- Cobertura de ausencias, vacaciones, bajas: obligación expresa. (ID_188_3.PDF, p.23)
- Idioma: castellano. (ID_188_3.PDF, p.9,13,16)
- Certificaciones: NO CONSTA EN LA DOCUMENTACION REVISADA.

# 7. Gobierno y reporting exigidos

- Responsable del contrato (Ayuntamiento): supervisión, control, validación, aceptación, reuniones, informes. (ID_188_3.PDF, p.10)
- Interlocutor único de la empresa (IE): coordinación técnica, comunicación con DGPC, suplente obligatorio. (ID_188_3.PDF, p.10)
- Reuniones de seguimiento: mensuales o superior, con actas e informes. (ID_188_3.PDF, p.11)
- Informe mensual de seguimiento: incidencias, funciones, mantenimiento, horas, etc. (ID_188_3.PDF, p.11)
- Informes adicionales a requerimiento. (ID_188_3.PDF, p.11)
- Informe final de proyecto: hitos, lecciones aprendidas, recomendaciones. (ID_188_3.PDF, p.9)
- Informe de impacto de género antes de fin de contrato. (ID_188_3.PDF, p.52)

# 8. Herramientas ITSM, CMDB, monitorización e integraciones exigidas

- Panel de control (cuadro de mando): acceso web, métricas, trazabilidad, informes, exportación, análisis, supervisión, encuestas, gestión agentes, mínimo 5 usuarios DGPC. (ID_188_3.PDF, p.14-15)
- Integración con buscador Decide Madrid y portal (script JS). (ID_188_3.PDF, p.6,13)
- Monitorización: diaria, con logs, trazas, integración con herramientas de observabilidad IAM si se requiere. (ID_188_3.PDF, p.15,31)
- CMDB: los sistemas desplegados deben figurar en la CMDB corporativa de IAM. (ID_188_3.PDF, p.33)
- Infraestructura: despliegue en MultiCloud (Azure, GCP, AWS) bajo gobierno IAM. (ID_188_3.PDF, p.29-34)
- Integración con Plataforma del Dato y MAIA (IA municipal). (ID_188_3.PDF, p.42-44)
- API para datos reutilizables, formatos abiertos, metadatos. (ID_188_3.PDF, p.22,56)

# 9. Transición, continuidad y reversibilidad exigidas

- Fase de implantación: máx. 2 meses, con validación y aceptación por DGPC/IAM. (ID_188_3.PDF, p.8-9)
- Transferencia de conocimiento: últimos 2 meses del contrato, actividades y documentación. (ID_188_3.PDF, p.9)
- Entrega de información generada: productos, modelos, código, datos, logs, encuestas, etc. (ID_188_3.PDF, p.9,40-41)
- Borrado seguro de datos y certificado de destrucción al cierre. (ID_188_3.PDF, p.9,40-41)
- Entrega de bases de datos, modelos, documentación, serie histórica, formato abierto y reutilizable. (ID_188_3.PDF, p.41,56)
- Continuidad: obligación de cobertura de ausencias, vacaciones, bajas. (ID_188_3.PDF, p.23)
- Reversibilidad: entrega de todos los activos, datos, documentación, logs, etc. (ID_188_3.PDF, p.9,40-41)

# 10. Automatización, self-service y gestión del conocimiento

- Automatización/self-service: El asistente virtual debe permitir interacción 24x7x365, integración con buscador, respuestas automáticas, panel de control con generación de informes y exportación. (ID_188_3.PDF, p.13-15)
- Gestión del conocimiento: BBDD de respuestas, logs, trazabilidad, panel de control, documentación técnica, manuales, formación. (ID_188_3.PDF, p.14-15,9,16-17)

# 11. Datos no localizados o ambiguos en la documentación

- No consta exigencia de certificaciones técnicas específicas para el personal.
- No consta exigencia de idiomas adicionales al castellano.
- No consta detalle de niveles N2/N3 ni Service Desk estructurado según ITIL.
- No consta exigencia expresa de herramientas ITSM comerciales ni de procesos ITIL denominados como tales.
- No consta detalle de RTO/RPO, ni de mecanismos de alta disponibilidad específicos.
- No consta exigencia de reporting automatizado salvo el panel de control y exportación de informes.
- No consta exigencia de integración con sistemas externos distintos a los mencionados (portal, buscador, MAIA, Plataforma del Dato).

# 12. Documentos revisados

1. ID_188_1.PDF (Documento licitación real)
2. ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares y Anexos)
3. ID_188_3.PDF (Pliego de Prescripciones Técnicas)
4. poc (Documento enlazado, detalle licitación, texto extraído)
5. poc (Documento enlazado, perfil contratante, texto extraído)
6. poc (Documento enlazado, perfil contratante, texto extraído)
7. 147409-2026 (Documento enlazado, sin texto extraíble; pendiente de lectura/OCR)
8. perfilContratante (Documento enlazado, texto extraído)

# 13. Discrepancias y pendientes de aclaración

- Documento 7 (147409-2026) pendiente de lectura/OCR: no se ha podido verificar si contiene condiciones adicionales o diferentes.
- No se han identificado discrepancias internas en la documentación revisada.

# 14. Tabla de trazabilidad

| Requisito/dato                        | Tipo                        | Valor/condición                                      | Documento     | Página/apartado         | Estado de lectura         |
|---------------------------------------|-----------------------------|-----------------------------------------------------|---------------|------------------------|--------------------------|
| Usuarios registrados Decide Madrid    | Volumetría                  | 555.318                                              | ID_188_3.PDF  | p.3                    | Leído                    |
| Capacidad mínima asistente            | Requisito técnico           | 50 conversaciones simultáneas                        | ID_188_3.PDF  | p.13                   | Leído                    |
| Tráfico mínimo asistente              | Requisito técnico           | 15.000 mensajes/mes                                  | ID_188_3.PDF  | p.13                   | Leído                    |
| Horario primer nivel atención         | Requisito de servicio       | 11:00-14:00 días laborables                          | ID_188_3.PDF  | p.16                   | Leído                    |
| Bolsa de horas evolución tecnológica  | Requisito de servicio       | 600 horas (ampliable)                                | ID_188_3.PDF  | p.17                   | Leído                    |
| Fase implantación                     | SLA                         | Máx. 2 meses                                         | ID_188_3.PDF  | p.8-9                  | Leído                    |
| Disponibilidad asistente virtual      | SLA                         | 24x7x365                                             | ID_188_3.PDF  | p.13                   | Leído                    |
| Indisponibilidad >48h                 | Penalización                | 5% precio contrato                                   | ID_188_2.PDF  | Anexo I, p.76          | Leído                    |
| Indisponibilidad >5 días              | Penalización                | 10% precio contrato                                  | ID_188_2.PDF  | Anexo I, p.77          | Leído                    |
| Jefe/a de Proyecto                    | Perfil obligatorio          | 2 personas, titulación universitaria, experiencia    | ID_188_3.PDF  | p.25-26                | Leído                    |
| Panel de control                      | Herramienta                 | Acceso web, métricas, informes, gestión agentes      | ID_188_3.PDF  | p.14-15                | Leído                    |
| CMDB                                  | Herramienta                 | Obligación de registrar sistemas en CMDB IAM         | ID_188_3.PDF  | p.33                   | Leído                    |
| Transferencia de conocimiento         | Requisito de cierre         | Últimos 2 meses, actividades y documentación         | ID_188_3.PDF  | p.9                    | Leído                    |
| Borrado seguro de datos               | Requisito de cierre         | Certificado de destrucción                           | ID_188_3.PDF  | p.9,40-41              | Leído                    |
| Automatización/self-service           | Requisito funcional         | Interacción 24x7x365, panel de control, informes     | ID_188_3.PDF  | p.13-15                | Leído                    |
| Certificaciones técnicas              | NO CONSTA                  | NO CONSTA EN LA DOCUMENTACION REVISADA              | N/A           | N/A                    | N/A                      |
| Niveles N2/N3, Service Desk ITIL      | NO CONSTA                  | NO CONSTA EN LA DOCUMENTACION REVISADA              | N/A           | N/A                    | N/A                      |
| Herramientas ITSM comerciales         | NO CONSTA                  | NO CONSTA EN LA DOCUMENTACION REVISADA              | N/A           | N/A                    | N/A                      |
| Documento 7 (147409-2026)             | Pendiente de verificación   | Sin texto extraíble; pendiente de lectura/OCR        | 147409-2026   | N/A                    | No leído                 |