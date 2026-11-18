# 1. Resumen factual del servicio requerido

El contrato exige la provisión de una solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para la operación ferroviaria de RENFE-Operadora. Incluye acceso web seguro, módulos de simulación de incendios e inundaciones, visualización geoespacial, integración de datos meteorológicos y geográficos, generación de alertas y boletines, soporte y mantenimiento, asistencia técnica especializada, formación, documentación, integración con sistemas corporativos y cumplimiento de estrictos requisitos de seguridad, continuidad y reversibilidad.

# 2. Alcance y volumetrías

| Dato                                    | Valor/Unidad                        | Periodo         | Fuente                                    |
|-----------------------------------------|-------------------------------------|-----------------|-------------------------------------------|
| Usuarios nominativos mínimos            | 15                                  | Vigencia contrato| ANEXO I, p.4                              |
| Ampliación usuarios                     | Paquetes adicionales                | Vigencia contrato| ANEXO I, p.4                              |
| Acceso                                 | Web seguro, navegadores soportados  | Vigencia contrato| ANEXO I, p.4                              |
| Módulos incluidos                      | Inteligencia meteorológica, visualización geoespacial, simulación incendios, simulación inundaciones | Vigencia contrato| ANEXO I, p.4                              |
| Perfiles de usuario                     | Administración, operación, análisis, consulta | Vigencia contrato| ANEXO I, p.4                              |
| Duración del servicio                   | 24 meses                            | 2 años          | PCP, p.22; ANEXO I, p.21                  |
| Horario de soporte                      | 8h/día, 7 días/semana               | Vigencia contrato| ANEXO I, p.16                              |
| Bolsa de horas                          | 350 UT/año (acumulable)             | Anual           | ANEXO I, p.19                              |
| Formación inicial                       | 2 jornadas remotas mínimo           | Inicio           | ANEXO I, p.20                              |
| Informes de servicio                    | Mensual                             | Operación        | ANEXO I, p.19-20                           |

# 3. Modelo de servicio exigido

- Solución SaaS accesible por web, sin despliegue de infraestructura física en RENFE.
- Incluye alojamiento, operación, actualización, mantenimiento y soporte.
- Soporte y mantenimiento: atención de incidencias técnicas y funcionales, consultas de uso, problemas de datos y solicitudes de configuración.
- Centro de soporte accesible por portal de solicitudes, correo electrónico y atención telefónica para incidencias urgentes.
- Asistencia técnica especializada multidisciplinar (meteorología, GIS, datos, cloud, riesgos naturales).
- Bolsa de horas para soporte especializado, desarrollos adaptativos, integraciones, formación adicional y análisis complejos.
- Formación inicial y continua, documentación actualizada y materiales grabados.

# 4. Procesos y actividades

| Proceso/actividad                                      | Expreso en pliego | Exigencia descrita                                                                                 | Fuente                |
|--------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------|-----------------------|
| Gestión de incidencias y soporte                       | ITIL NO CITADO    | Atención de incidencias técnicas y funcionales, consultas, problemas de datos, solicitudes         | ANEXO I, p.16         |
| Gestión de alertas y avisos                            | ITIL NO CITADO    | Configuración, envío, registro, exportación de alertas y avisos                                    | ANEXO I, p.10-11      |
| Gestión de usuarios y perfiles                         | ITIL NO CITADO    | Administración de usuarios, perfiles diferenciados, integración con sistema de identidad           | ANEXO I, p.4, 14, 31  |
| Integración de datos y sistemas                        | ITIL NO CITADO    | APIs documentadas, servicios geoespaciales, integración con sistemas corporativos                 | ANEXO I, p.14-15      |
| Monitorización y trazabilidad                          | ITIL NO CITADO    | Registro, auditoría, trazabilidad de eventos, logs, integración con SIEM de Renfe                 | ANEXO I, p.27, 36     |
| Gestión de cambios y evolución                         | ITIL NO CITADO    | Gestión formal de cambios de alcance y evolución de requisitos                                    | ANEXO I, p.22         |
| Gestión de continuidad y contingencia                  | ITIL NO CITADO    | Planes de contingencia, crisis, continuidad, salida programada y sobrevenida                      | ANEXO I, p.38-39      |
| Gestión de vulnerabilidades y parches                  | ITIL NO CITADO    | Proceso formal de gestión de vulnerabilidades y parcheado                                         | ANEXO I, p.35         |
| Gestión de la seguridad y cumplimiento normativo       | ITIL NO CITADO    | Cumplimiento ENS, RGPD, LOPDGDD, análisis de riesgos, roles de seguridad, acuerdos de confidencialidad | ANEXO I, p.23-39  |
| Gestión de la formación y transferencia de conocimiento| ITIL NO CITADO    | Plan de formación, materiales, sesiones periódicas, documentación actualizada                     | ANEXO I, p.20-21      |
| Gestión de la reversibilidad y devolución de datos     | ITIL NO CITADO    | Plan de salida, devolución/destrucción de información, certificado de supresión                   | ANEXO I, p.39         |

# 5. SLA/KPI/penalizaciones

| Servicio         | Prioridad | Respuesta/Resolución | Horario           | Objetivo/Definición                  | Penalización                                                                 | Fuente                |
|------------------|----------|---------------------|-------------------|--------------------------------------|------------------------------------------------------------------------------|-----------------------|
| Soporte          | Crítica  | No especificado     | 8h/día, 7d/semana | Indisponibilidad total, funciones esenciales | 2% importe contrato por superación tiempo respuesta/restauración comprometido | PCP, p.29             |
| Soporte          | Alta     | No especificado     | 8h/día, 7d/semana | Degradación grave, fallo esencial    | 1,5% importe contrato por superación tiempo respuesta/restauración           | PCP, p.29             |
| Soporte          | Media    | No especificado     | 8h/día, 7d/semana | Funcionamiento parcial, error menor  | 1% (media), 0,5% (media) importe contrato por superación tiempo respuesta/restauración | PCP, p.29     |
| Soporte          | Baja     | No especificado     | 8h/día, 7d/semana | Consulta, defecto menor, mejora      | NO CONSTA EN LA DOCUMENTACION REVISADA                                       | PCP, p.29             |
| Calidad servicio | N/A      | N/A                 | N/A               | Falta de calidad manifiesta          | Hasta 10% importe total contrato                                             | PCP, p.30             |
| Equipo           | N/A      | N/A                 | N/A               | Cambio no autorizado, falta de conocimientos | 5.000 € por incumplimiento                                            | PCP, p.30             |
| Reuniones        | N/A      | N/A                 | N/A               | Incomparecencia a reuniones          | Hasta 1% importe total contrato                                              | PCP, p.30             |
| Oferta técnica   | N/A      | N/A                 | N/A               | Incumplimiento oferta técnica        | Hasta 2.000 € por incumplimiento                                             | PCP, p.30             |
| Seguridad/confid.| N/A      | N/A                 | N/A               | Incumplimiento obligaciones seguridad/confidencialidad | Hasta 20% importe total contrato                              | PCP, p.30             |
| Ética/cumplimiento| N/A     | N/A                 | N/A               | Incumplimiento obligaciones esenciales| Hasta 10% (máx. 20%) o resolución contrato                                   | PCP, p.31             |
| Seguridad ciber  | N/A      | N/A                 | N/A               | Incumplimiento entrega doc. ciberseguridad | Hasta 10% importe contrato                                            | PCP, p.31             |
| ENS              | N/A      | N/A                 | N/A               | Falta de certificación ENS           | Hasta 10% importe contrato                                                   | PCP, p.31             |
| POC Seguridad    | N/A      | N/A                 | N/A               | No notificación formal POC Seguridad | 1.000 €/mes de retraso, 1.000 €/24h sin respuesta                            | PCP, p.31             |

Nota: Los tiempos concretos de respuesta y restauración se recogerán en el acuerdo de nivel de servicio aprobado para el contrato (ANEXO I, p.16). NO CONSTA el detalle de los valores objetivo en la documentación revisada.

# 6. Organización y roles exigidos

- Project Manager (Responsable del servicio): titulación universitaria oficial (preferente Ingeniería, Informática, Telecomunicaciones, Física, Matemáticas, Geografía, Ciencias Ambientales o equivalente), mínimo 3 años experiencia en proyectos análogos. (ANEXO I, p.17)
- Especialista en meteorología y predicción: titulación universitaria en Física, Meteorología, Ciencias Atmosféricas, Matemáticas, Ciencias Ambientales o equivalente, formación en meteorología y predicción numérica. (ANEXO I, p.18)
- Especialista en algoritmos de predicción a corto plazo: titulación universitaria en Física, Meteorología, Ciencias Atmosféricas, Matemáticas, Ingeniería o equivalente, formación en meteorología y predicción numérica. (ANEXO I, p.18)
- Especialista en software, datos e integraciones: titulación universitaria en Informática, Telecomunicaciones, Ingeniería, Matemáticas, Ciencia de Datos o equivalente. (ANEXO I, p.18)
- Especialista en riesgos naturales: titulación universitaria en Ingeniería de Montes, Forestal, Caminos, Civil, Hidrología, Geología, Geografía, Ciencias Ambientales o equivalente, formación en incendios o inundaciones. (ANEXO I, p.18)
- Equipo multidisciplinar, experiencia conjunta mínima 4 años en proyectos análogos. (ANEXO I, p.17)
- Adscripción estable durante toda la vigencia del contrato, cambios solo por fuerza mayor. (ANEXO I, p.18)
- Formación inicial y continua para usuarios de RENFE. (ANEXO I, p.20-21)
- Idioma: castellano. (PCP, p.7; ANEXO I, p.21)

# 7. Gobierno y reporting exigidos

- Designación de responsable del servicio por el adjudicatario. (ANEXO I, p.22)
- Reuniones de seguimiento con periodicidad establecida por RENFE. (ANEXO I, p.22)
- Cuadro de acciones, responsables, fechas objetivo, riesgos y decisiones. (ANEXO I, p.22)
- Gestión formal de cambios y evolución de requisitos. (ANEXO I, p.22)
- Escalado de incidencias, riesgos de continuidad y desviaciones relevantes. (ANEXO I, p.22)
- Revisión periódica de indicadores, calidad del dato, uso de la solución y oportunidades de mejora. (ANEXO I, p.22)
- Informes mensuales de servicio: disponibilidad, incidencias, consultas, tiempos de atención, problemas recurrentes, cambios, bolsa de horas, análisis de causa raíz, riesgos y propuestas de mejora. (ANEXO I, p.19-20)

# 8. Herramientas ITSM, CMDB, monitorización e integraciones exigidas

- Portal de solicitudes para soporte. (ANEXO I, p.16)
- Integración con sistema corporativo de identidad (autenticación, SSO). (ANEXO I, p.14, 31)
- APIs documentadas para consulta de predicciones, observaciones, alertas, informes y simulaciones. (ANEXO I, p.15)
- Servicios geoespaciales normalizados para publicación y consumo de mapas, entidades y teselas. (ANEXO I, p.15)
- Intercambio de ficheros mediante canales seguros y formatos estructurados. (ANEXO I, p.15)
- Integración con herramientas corporativas de operación, analítica, comunicación o gestión de incidencias cuando RENFE lo solicite. (ANEXO I, p.15)
- Mecanismos de autenticación de sistemas, control de cuota, registro de llamadas y tratamiento de errores. (ANEXO I, p.15)
- Registro, auditoría y trazabilidad de eventos, logs, integración con SIEM de Renfe. (ANEXO I, p.27, 36)
- Monitorización de la infraestructura para detectar incidencias e incidentes en formato 24x7. (ANEXO I, p.37)
- Inventario actualizado de equipos, software y activos. (ANEXO I, p.33)
- NO CONSTA mención expresa a herramienta ITSM o CMDB comercial específica.

# 9. Transición, continuidad y reversibilidad exigidas

- Servicio estándar disponible desde el inicio de la prestación. (ANEXO I, p.21)
- Configuración, personalización, carga de datos, integración de red ferroviaria y puesta en marcha completa en máximo 3 meses desde que RENFE facilite información y accesos. (ANEXO I, p.21)
- Reunión inicial, inventario de datos e integraciones, configuración de usuarios, carga de capas, definición de alertas prioritarias, pruebas, formación y aceptación del servicio. (ANEXO I, p.21)
- Garantía técnica durante toda la vigencia: disponibilidad, corrección de defectos, funcionamiento de integraciones, actualización de datos y conservación de configuraciones. (ANEXO I, p.21-22)
- Plan de devolución, exportación de datos, entrega documental y certificado de supresión cuando proceda al finalizar el contrato. (ANEXO I, p.22)
- Planes de contingencia, crisis, continuidad de negocio, salida programada y sobrevenida, devolución/destrucción de información, certificado de destrucción. (ANEXO I, p.38-39)
- Mecanismos de respaldo de la información, restauración, pruebas de restauración. (ANEXO I, p.38)
- Propuesta de identificación de competencias básicas para reanudar control directo en caso extremo. (ANEXO I, p.38)

# 10. Automatización, self-service y gestión del conocimiento

- Automatización: generación y envío automático de boletines y alertas, exportación automática de informes. (ANEXO I, p.11, 14)
- Portal de solicitudes para soporte (self-service). (ANEXO I, p.16)
- Documentación de usuario y técnica accesible durante toda la vigencia. (ANEXO I, p.4, 21)
- Videoteca o materiales grabados para formación y consulta. (ANEXO I, p.21)
- Sesiones periódicas sobre nuevas funcionalidades y casos de uso. (ANEXO I, p.21)

# 11. Datos no localizados o ambiguos en la documentación

- NO CONSTA detalle de los tiempos objetivo de respuesta y resolución para cada prioridad de incidencia (remitido a acuerdo de nivel de servicio posterior). (ANEXO I, p.16)
- NO CONSTA mención expresa a herramientas ITSM o CMDB comerciales concretas.
- NO CONSTA detalle de la frecuencia de reuniones de seguimiento (queda a establecer por RENFE).
- NO CONSTA detalle de la cantidad de sesiones de formación continua más allá del mínimo inicial.
- NO CONSTA detalle de la volumetría de datos, número de incidencias esperadas, ni dimensionamiento de equipo.
- NO CONSTA mención a idiomas adicionales al castellano.
- NO CONSTA mención a soporte fuera del horario mínimo exigido (8h/día, 7d/semana).

# 12. Documentos revisados

1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393 .pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Documento enlazado, Plataforma de Contratación)
7. poc (Documento enlazado, Perfil de Contratante)
8. poc (Documento enlazado, Perfil de Contratante)

# Tabla de trazabilidad

| Requisito/dato                                 | Tipo                        | Valor/condición                                                                 | Documento                  | Página/apartado         | Estado de lectura |
|------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|----------------------------|-------------------------|-------------------|
| Usuarios nominativos mínimos                   | Obligación contractual      | 15 usuarios nominativos mínimo, ampliable                                        | ANEXO I 2026 03393 .pdf    | p.4                     | Leído             |
| Horario de soporte                             | Obligación contractual      | 8h/día, 7 días/semana                                                            | ANEXO I 2026 03393 .pdf    | p.16                    | Leído             |
| Bolsa de horas                                 | Obligación contractual      | 350 UT/año, acumulable                                                           | ANEXO I 2026 03393 .pdf    | p.19                    | Leído             |
| Project Manager                                | Obligación contractual      | Titulación universitaria, 3 años experiencia                                     | ANEXO I 2026 03393 .pdf    | p.17                    | Leído             |
| Especialistas multidisciplinares               | Obligación contractual      | Meteorología, predicción, software, datos, riesgos naturales                     | ANEXO I 2026 03393 .pdf    | p.18                    | Leído             |
| Informes mensuales                             | Obligación contractual      | Disponibilidad, incidencias, cambios, bolsa de horas, análisis causa raíz         | ANEXO I 2026 03393 .pdf    | p.19-20                 | Leído             |
| Plan de formación inicial                      | Obligación contractual      | 2 jornadas remotas mínimo                                                        | ANEXO I 2026 03393 .pdf    | p.20                    | Leído             |
| Documentación de usuario y técnica             | Obligación contractual      | Accesible durante toda la vigencia                                               | ANEXO I 2026 03393 .pdf    | p.4, 21                 | Leído             |
| Integración con sistemas corporativos          | Obligación contractual      | APIs, servicios geoespaciales, autenticación, SSO                                | ANEXO I 2026 03393 .pdf    | p.14-15, 31             | Leído             |
| Monitorización 24x7                            | Obligación contractual      | Monitorización de infraestructura para incidencias e incidentes                  | ANEXO I 2026 03393 .pdf    | p.37                    | Leído             |
| Planes de contingencia, continuidad, salida    | Obligación contractual      | Planes de contingencia, crisis, continuidad, salida programada y sobrevenida     | ANEXO I 2026 03393 .pdf    | p.38-39                 | Leído             |
| Penalizaciones por SLA                         | Penalización                | 2%/1,5%/1%/0,5% según prioridad y superación tiempos respuesta/restauración      | PCP 2026 03993.pdf         | p.29                    | Leído             |
| Penalización por falta de calidad              | Penalización                | Hasta 10% importe total contrato                                                 | PCP 2026 03993.pdf         | p.30                    | Leído             |
| Penalización por incumplimiento equipo         | Penalización                | 5.000 € por incumplimiento                                                       | PCP 2026 03993.pdf         | p.30                    | Leído             |
| Penalización por incumplimiento seguridad      | Penalización                | Hasta 20% importe total contrato                                                 | PCP 2026 03993.pdf         | p.30                    | Leído             |
| Automatización de alertas y boletines          | Obligación contractual      | Generación y envío automático                                                    | ANEXO I 2026 03393 .pdf    | p.11, 14                | Leído             |
| Portal de solicitudes (self-service)           | Obligación contractual      | Acceso a soporte                                                                 | ANEXO I 2026 03393 .pdf    | p.16                    | Leído             |
| Videoteca/materiales grabados                  | Obligación contractual      | Formación y consulta                                                             | ANEXO I 2026 03393 .pdf    | p.21                    | Leído             |
| NO CONSTA detalle tiempos SLA                  | Dato no localizado          | Tiempos concretos de respuesta y resolución remitidos a acuerdo posterior        | ANEXO I 2026 03393 .pdf    | p.16                    | Leído             |
| NO CONSTA herramienta ITSM/CMDB específica     | Dato no localizado          | No se menciona herramienta comercial concreta                                    | ANEXO I 2026 03393 .pdf    | N/A                     | Leído             |
| NO CONSTA detalle frecuencia reuniones         | Dato no localizado          | Periodicidad a establecer por RENFE                                              | ANEXO I 2026 03393 .pdf    | p.22                    | Leído             |
| NO CONSTA dimensionamiento equipo              | Dato no localizado          | No se especifica número de personas ni FTE                                       | ANEXO I 2026 03393 .pdf    | p.17-18                 | Leído             |

# Discrepancias y pendientes de aclaración

- NO CONSTA en la documentación revisada el detalle de los tiempos objetivo de respuesta y resolución para cada prioridad de incidencia, aunque se indica que se recogerán en el acuerdo de nivel de servicio aprobado para el contrato (ANEXO I, p.16).
- NO CONSTA mención expresa a herramientas ITSM o CMDB comerciales concretas.
- NO CONSTA detalle de la frecuencia de reuniones de seguimiento.
- NO CONSTA detalle de la cantidad de sesiones de formación continua más allá del mínimo inicial.
- NO CONSTA detalle de la volumetría de datos, número de incidencias esperadas, ni dimensionamiento de equipo.
- NO CONSTA mención a idiomas adicionales al castellano.
- NO CONSTA mención a soporte fuera del horario mínimo exigido (8h/día, 7d/semana).

No se han identificado discrepancias internas entre los documentos revisados.