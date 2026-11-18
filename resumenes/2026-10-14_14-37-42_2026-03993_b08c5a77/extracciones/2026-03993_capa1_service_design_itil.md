# 1. Resumen factual del servicio requerido

El contrato exige la provisión de una solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para la operación ferroviaria de RENFE-Operadora. Incluye acceso web seguro, módulos de simulación de incendios e inundaciones, visualización geoespacial, integración de datos meteorológicos y geográficos, generación de alertas y boletines, soporte y mantenimiento, formación, asistencia técnica especializada, cumplimiento de requisitos de seguridad y continuidad, y mecanismos de integración con sistemas corporativos. El servicio debe estar disponible para al menos 15 usuarios nominativos, con posibilidad de ampliación, y cubrir toda la operación ferroviaria de RENFE-Operadora.

# 2. Alcance y volumetrías

| Dato/Concepto                                    | Valor/Unidad                        | Periodo         | Fuente/Referencia                |
|--------------------------------------------------|-------------------------------------|-----------------|----------------------------------|
| Usuarios nominativos mínimos                     | 15                                  | Vigencia contrato| ANEXO I, pág. 4                  |
| Ampliación de usuarios                           | Paquetes adicionales                | Vigencia contrato| ANEXO I, pág. 4                  |
| Acceso web seguro                               | Sí                                  | Vigencia contrato| ANEXO I, pág. 4                  |
| Ámbito de servicio                              | RENFE-Operadora y operación ferroviaria | Vigencia contrato| ANEXO I, pág. 3                  |
| Duración del servicio                           | 24 meses                            | 2 años          | PCP, pág. 22; ANEXO I, pág. 21    |
| Horario de soporte mínimo                       | 8h/día, 7 días/semana               | Vigencia contrato| ANEXO I, pág. 16                 |
| Bolsa de horas (soporte especializado)           | 350 UT/año (hora/UT)                | Anual           | ANEXO I, pág. 19                 |
| Capacidad máxima bolsa de horas                  | 350 UT/año, acumulable               | Anual           | ANEXO I, pág. 19                 |
| Plataformas y módulos incluidos                  | SaaS, simulación incendios, inundaciones | Vigencia contrato| ANEXO I, pág. 4                  |
| Perfiles de usuario                             | Administración, operación, análisis, consulta | Vigencia contrato| ANEXO I, pág. 4                  |
| Documentación y formación                       | Manuales, guías, videoteca, sesiones | Vigencia contrato| ANEXO I, págs. 20-21             |

# 3. Modelo de servicio exigido

- Solución SaaS accesible por web, sin despliegue de infraestructura física en RENFE.
- Incluye alojamiento, operación, actualización, mantenimiento y soporte.
- Soporte y mantenimiento: atención de incidencias técnicas y funcionales, consultas de uso, problemas de datos y solicitudes de configuración.
- Centro de soporte accesible por portal de solicitudes, correo electrónico y atención telefónica para incidencias urgentes.
- Asistencia técnica especializada para puesta en marcha, interpretación de información, evolución del servicio y transferencia de conocimiento.
- Bolsa de horas anual para soporte especializado, desarrollos adaptativos, nuevas integraciones, formación adicional y análisis complejos.
- Integración con sistemas corporativos de identidad, operación, analítica, comunicación y gestión de incidencias.

# 4. Procesos y actividades

| Proceso/Actividad                                      | Expreso en pliego | Exigencia descrita                                                                 | Fuente/Referencia         |
|--------------------------------------------------------|-------------------|-----------------------------------------------------------------------------------|---------------------------|
| Gestión de incidencias y soporte                       | ITIL NO CITADO    | Atención de incidencias técnicas y funcionales, consultas, problemas de datos      | ANEXO I, pág. 16          |
| Gestión de alertas y avisos                            | ITIL NO CITADO    | Generación, configuración y envío de alertas y boletines automáticos               | ANEXO I, págs. 10-12      |
| Gestión de usuarios y perfiles                         | ITIL NO CITADO    | Perfiles diferenciados, autenticación segura, integración con sistema de identidad | ANEXO I, pág. 4, 14-15    |
| Integración de datos y sistemas                        | ITIL NO CITADO    | APIs documentadas, servicios geoespaciales, integración con sistemas corporativos  | ANEXO I, pág. 14-15       |
| Gestión de cambios y evolución                         | ITIL NO CITADO    | Gestión formal de cambios de alcance y evolución de requisitos                     | ANEXO I, pág. 22-23       |
| Gestión de la continuidad y recuperación               | ITIL NO CITADO    | Planes de contingencia, continuidad, recuperación, salida programada y sobrevenida | ANEXO I, pág. 38-39       |
| Gestión de la seguridad de la información              | ITIL NO CITADO    | Cumplimiento ENS, análisis de riesgos, gestión de vulnerabilidades, cifrado, etc.  | ANEXO I, págs. 24-39      |
| Transferencia de conocimiento y formación              | ITIL NO CITADO    | Formación inicial, continua, materiales, videoteca, sesiones periódicas            | ANEXO I, págs. 20-21      |
| Monitorización de la infraestructura                   | ITIL NO CITADO    | Monitorización 24x7 de la infraestructura para detectar incidencias e incidentes    | ANEXO I, pág. 36-37       |
| Reporting e informes de servicio                       | ITIL NO CITADO    | Informes mensuales de disponibilidad, incidencias, cambios, bolsa de horas         | ANEXO I, pág. 19-20       |

# 5. SLA/KPI/penalizaciones

| Servicio/Actividad         | Prioridad | Respuesta/Resolución | Horario           | Objetivo/Umbral | Penalización | Fuente/Referencia         |
|---------------------------|-----------|----------------------|-------------------|-----------------|-------------|---------------------------|
| Soporte e incidencias     | Crítica   | Atención prioritaria, seguimiento continuo hasta restauración | 8h/día, 7d/sem | A definir en acuerdo de nivel de servicio | 2% importe contrato por superación de tiempo de respuesta/restauración | PCP, pág. 29; ANEXO I, pág. 16 |
| Soporte e incidencias     | Alta      | Atención preferente, plan de recuperación comunicado         | 8h/día, 7d/sem | A definir en acuerdo de nivel de servicio | 1,5% importe contrato por superación de tiempo de respuesta/restauración | PCP, pág. 29; ANEXO I, pág. 16 |
| Soporte e incidencias     | Media     | Resolución planificada dentro del ciclo de soporte           | 8h/día, 7d/sem | A definir en acuerdo de nivel de servicio | 1% (o 0,5%) importe contrato por superación de tiempo de respuesta/restauración | PCP, pág. 29; ANEXO I, pág. 16 |
| Soporte e incidencias     | Baja      | Gestión ordinaria, incorporación a planificación             | 8h/día, 7d/sem | A definir en acuerdo de nivel de servicio | NO CONSTA EN LA DOCUMENTACION REVISADA         |
| Calidad de servicios      | N/A       | N/A                  | N/A               | N/A             | Hasta 10% importe total contrato por falta de calidad manifiesta | PCP, pág. 30                |
| Equipo no conforme        | N/A       | N/A                  | N/A               | N/A             | 5.000 € por incumplimiento de conocimientos, rotación no comunicada | PCP, pág. 30                |
| Incomparecencia a reuniones | N/A     | N/A                  | N/A               | N/A             | Hasta 1% importe total contrato | PCP, pág. 30                |
| Incumplimiento oferta técnica | N/A   | N/A                  | N/A               | N/A             | Hasta 2.000 € por incumplimiento | PCP, pág. 30                |
| Incumplimiento confidencialidad, datos, PI | N/A | N/A | N/A | N/A | Hasta 20% importe total contrato | PCP, pág. 30                |
| Incumplimiento obligaciones seguridad | N/A | N/A | N/A | N/A | Hasta 10% importe total contrato, penalizaciones específicas por plazos | PCP, pág. 31                |

Nota: Los tiempos concretos de respuesta y resolución se recogerán en el acuerdo de nivel de servicio aprobado para el contrato (ANEXO I, pág. 16).

# 6. Organización y roles exigidos

- Project Manager: Titulación universitaria oficial (preferentemente Ingeniería, Informática, Telecomunicaciones, Física, Matemáticas, Geografía, Ciencias Ambientales o equivalente), mínimo 3 años de experiencia en gestión de proyectos/servicios análogos. (ANEXO I, pág. 17)
- Especialista en meteorología y predicción: Titulación universitaria en Física, Meteorología, Ciencias Atmosféricas, Matemáticas, Ciencias Ambientales o equivalente, formación acreditable en meteorología y predicción numérica. (ANEXO I, pág. 18)
- Especialista en algoritmos de predicción a corto plazo: Titulación universitaria en Física, Meteorología, Ciencias Atmosféricas, Matemáticas, Ingeniería o equivalente, formación acreditable en meteorología y predicción numérica. (ANEXO I, pág. 18)
- Especialista en software, datos e integraciones: Titulación universitaria en Informática, Telecomunicaciones, Ingeniería, Matemáticas, Ciencia de Datos o equivalente. (ANEXO I, pág. 18)
- Especialista en riesgos naturales: Titulación universitaria en Ingeniería de Montes, Forestal, Caminos, Civil, Hidrología, Geología, Geografía, Ciencias Ambientales o equivalente, formación relacionada con incendios o inundaciones. (ANEXO I, pág. 18)
- El equipo debe ser estable, suficiente y multidisciplinar, con experiencia conjunta mínima de 4 años en proyectos análogos. (ANEXO I, pág. 17)
- Perfiles diferenciados de administración, operación, análisis y consulta para usuarios. (ANEXO I, pág. 4)
- Idioma: Castellano. (PCP, pág. 7)
- Sustituciones solo por causa de fuerza mayor, previa comunicación. (ANEXO I, pág. 18)

# 7. Gobierno y reporting exigidos

- Designación de responsable del servicio por parte del adjudicatario. (ANEXO I, pág. 22)
- Reuniones de seguimiento con periodicidad establecida por RENFE-Operadora. (ANEXO I, pág. 22)
- Cuadro de acciones, responsables, fechas objetivo, riesgos y decisiones. (ANEXO I, pág. 22)
- Gestión formal de cambios de alcance y evolución de requisitos. (ANEXO I, pág. 22)
- Escalado de incidencias, riesgos de continuidad y desviaciones relevantes. (ANEXO I, pág. 22)
- Revisión periódica de indicadores, calidad del dato, uso de la solución y oportunidades de mejora. (ANEXO I, pág. 23)
- Informes mensuales de servicio: disponibilidad, incidencias, consultas, tiempos de atención, problemas recurrentes, cambios, bolsa de horas, análisis de causa raíz, riesgos, dependencias, propuestas de mejora. (ANEXO I, pág. 19-20)

# 8. Herramientas ITSM, CMDB, monitorización e integraciones exigidas

- Centro de soporte accesible por portal de solicitudes, correo electrónico y atención telefónica. (ANEXO I, pág. 16)
- APIs documentadas para consulta de predicciones, observaciones, alertas, informes y resultados de simulación. (ANEXO I, pág. 14-15)
- Servicios geoespaciales normalizados para publicación y consumo de mapas, entidades y teselas. (ANEXO I, pág. 15)
- Integración con sistema corporativo de identidad para autenticación y, cuando se determine, inicio de sesión único. (ANEXO I, pág. 14)
- Mecanismos de autenticación de sistemas, control de cuota, registro de llamadas y tratamiento de errores. (ANEXO I, pág. 15)
- Monitorización 24x7 de la infraestructura para detectar incidencias e incidentes. (ANEXO I, pág. 36-37)
- Inventario de activos de información, software, hardware, configuraciones, usuarios, derechos de acceso. (ANEXO I, pág. 26)
- Entrega de logs al SIEM del Grupo Renfe o API para captura de logs. (ANEXO I, pág. 36)
- Herramientas de gestión de identidades y control de accesos, integración con directorio corporativo. (ANEXO I, pág. 31-32)
- Solución comercial de DLP para descubrimiento de datos personales y tarjetas de pago. (ANEXO I, pág. 29)

# 9. Transición, continuidad y reversibilidad exigidas

- La versión estándar del servicio debe estar disponible desde el inicio de la prestación. (ANEXO I, pág. 21)
- Configuración, personalización, carga de datos corporativos, integración de la red ferroviaria y puesta en marcha completa en un plazo máximo de 3 meses desde que RENFE facilite la información y accesos necesarios. (ANEXO I, pág. 21)
- Planificación de puesta en marcha: reunión inicial, inventario de datos e integraciones, configuración de usuarios, carga de capas, definición de alertas prioritarias, pruebas, formación y aceptación del servicio. (ANEXO I, pág. 21)
- Criterios de aceptación: cumplimiento de requisitos funcionales y técnicos, acceso correcto de usuarios, carga y visualización de capas, actualización de fuentes, funcionamiento de alertas, informes, exportaciones y simulaciones, ejecución de pruebas de seguridad, continuidad e integración, entrega y validación de documentación y formación. (ANEXO I, pág. 21)
- Garantía técnica durante toda la vigencia de la prestación: disponibilidad, corrección de defectos, funcionamiento de integraciones, actualización de datos y conservación de configuraciones, sin consumo de bolsa de horas cuando derive de defecto del servicio. (ANEXO I, pág. 22)
- Plan de devolución, exportación de datos, entrega documental y certificado de supresión cuando proceda al finalizar el contrato. (ANEXO I, pág. 22)
- Planes de contingencia, continuidad, crisis, salida programada y sobrevenida, devolución y destrucción segura de información, certificaciones de destrucción. (ANEXO I, pág. 38-39)
- Mecanismos de respaldo de la información, pruebas de restauración, redundancia y balanceo de arquitecturas. (ANEXO I, pág. 38)

# 10. Automatización, self-service y gestión del conocimiento

- Automatización: Generación y envío automático de alertas y boletines por correo electrónico, configuración de reglas y ventanas temporales, mecanismos para evitar duplicidades. (ANEXO I, pág. 10-12)
- Self-service: NO CONSTA EN LA DOCUMENTACION REVISADA
- Gestión del conocimiento: Manuales, guías rápidas, documentación específica, videoteca, materiales grabados, sesiones periódicas, actualización tras cambios funcionales. (ANEXO I, pág. 20-21)

# 11. Datos no localizados o ambiguos en la documentación

- No se localizan tiempos concretos de respuesta y resolución para cada prioridad; se indica que se definirán en el acuerdo de nivel de servicio aprobado para el contrato. (ANEXO I, pág. 16)
- No se localiza detalle de la herramienta ITSM concreta a utilizar, ni de CMDB específica, más allá de los requisitos funcionales y de integración.
- No se localiza información sobre self-service para usuarios finales.
- No se localiza detalle de la volumetría de datos, número de incidencias estimadas, ni dimensionamiento de equipo más allá de los mínimos exigidos.
- No se localiza información sobre idiomas adicionales al castellano.
- No se localiza información sobre ventanas de mantenimiento, soporte fuera de horario mínimo, ni cobertura de emergencias fuera del horario de soporte.

# 12. Documentos revisados

1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393 .pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Plataforma de Contratación del Sector Público, información general)
7. poc (Perfil de contratante RENFE-Operadora, información general)
8. poc (Perfil de contratante RENFE-Operadora, información general)

# 13. Trazabilidad de requisitos y datos

| Requisito/Dato                                 | Tipo                        | Valor/Condición/Umbral/Regla                                                                 | Documento         | Página/Apartado         | Estado de lectura |
|------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------------------|-------------------|-------------------------|-------------------|
| Usuarios nominativos mínimos                   | Obligación contractual      | 15                                                                                          | ANEXO I           | pág. 4                  | Leído             |
| Horario de soporte mínimo                      | Obligación contractual      | 8h/día, 7 días/semana                                                                       | ANEXO I           | pág. 16                 | Leído             |
| Bolsa de horas anual                           | Obligación contractual      | 350 UT/año, acumulable                                                                      | ANEXO I           | pág. 19                 | Leído             |
| Project Manager titulación y experiencia       | Obligación contractual      | Titulación universitaria, 3 años experiencia mínima                                          | ANEXO I           | pág. 17                 | Leído             |
| Especialistas multidisciplinares               | Obligación contractual      | Meteorología, predicción, software, datos, riesgos naturales, experiencia mínima 4 años      | ANEXO I           | pág. 17-18              | Leído             |
| SLA soporte e incidencias                      | Obligación contractual      | A definir en acuerdo de nivel de servicio                                                    | ANEXO I           | pág. 16                 | Leído             |
| Penalizaciones por incumplimiento SLA          | Penalización                | 2%/1,5%/1%/0,5% importe contrato según prioridad y superación de tiempos                    | PCP               | pág. 29                 | Leído             |
| Penalización por falta de calidad              | Penalización                | Hasta 10% importe total contrato                                                            | PCP               | pág. 30                 | Leído             |
| Penalización por equipo no conforme            | Penalización                | 5.000 € por incumplimiento                                                                  | PCP               | pág. 30                 | Leído             |
| Penalización por incomparecencia reuniones     | Penalización                | Hasta 1% importe total contrato                                                             | PCP               | pág. 30                 | Leído             |
| Penalización por incumplimiento oferta técnica | Penalización                | Hasta 2.000 € por incumplimiento                                                            | PCP               | pág. 30                 | Leído             |
| Penalización por confidencialidad/datos/PI     | Penalización                | Hasta 20% importe total contrato                                                            | PCP               | pág. 30                 | Leído             |
| Penalización por seguridad                     | Penalización                | Hasta 10% importe total contrato, penalizaciones específicas por plazos                      | PCP               | pág. 31                 | Leído             |
| Plan de devolución y reversibilidad            | Obligación contractual      | Exportación de datos, entrega documental, certificado de supresión                          | ANEXO I           | pág. 22                 | Leído             |
| Planes de contingencia, continuidad, salida    | Obligación contractual      | Planes de contingencia, continuidad, crisis, salida programada y sobrevenida                | ANEXO I           | pág. 38-39              | Leído             |
| Monitorización 24x7 infraestructura           | Obligación contractual      | Monitorización 24x7 para detectar incidencias e incidentes                                  | ANEXO I           | pág. 36-37              | Leído             |
| Entrega de logs al SIEM                        | Obligación contractual      | Entrega de logs al SIEM del Grupo Renfe o API para captura de logs                          | ANEXO I           | pág. 36                 | Leído             |
| Automatización de alertas y boletines          | Obligación contractual      | Generación y envío automático de alertas y boletines                                        | ANEXO I           | pág. 10-12              | Leído             |
| Gestión del conocimiento                       | Obligación contractual      | Manuales, guías, videoteca, materiales, sesiones periódicas                                 | ANEXO I           | pág. 20-21              | Leído             |

# 14. Discrepancias y pendientes de aclaración

- No se han identificado discrepancias en la documentación revisada.
- Tiempos concretos de respuesta y resolución para cada prioridad quedan pendientes de definir en el acuerdo de nivel de servicio posterior a la adjudicación.
- No consta detalle de herramienta ITSM ni CMDB específica, solo requisitos funcionales.
- No consta información sobre self-service para usuarios finales.
- No consta información sobre idiomas adicionales al castellano.
- No consta información sobre ventanas de mantenimiento ni soporte fuera del horario mínimo.
- No consta información sobre volumetría de datos, incidencias estimadas ni dimensionamiento de equipo más allá de mínimos exigidos.

---

**Fin del análisis objetivo conforme a la documentación revisada.**