# 1. Resumen factual del servicio requerido

El contrato exige la provisión de una solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para la operación ferroviaria de RENFE-Operadora. Incluye acceso web seguro, módulos de simulación de incendios e inundaciones, visualización geoespacial, integración de datos meteorológicos y geográficos, generación de alertas y boletines, soporte y mantenimiento, asistencia técnica especializada, formación, documentación, cumplimiento de requisitos de seguridad y continuidad, y mecanismos de integración con sistemas corporativos. El servicio debe estar disponible para al menos 15 usuarios nominativos, con posibilidad de ampliación, y cubrirá la operación ferroviaria de RENFE-Operadora durante 24 meses.

# 2. Alcance y volumetrías

| Dato | Valor/Unidad | Periodo | Fuente |
|------|--------------|---------|--------|
| Usuarios nominativos mínimos | 15 | Vigencia contrato | ANEXO I, p.4 |
| Ampliación usuarios | Paquetes adicionales | Vigencia contrato | ANEXO I, p.4 |
| Perfiles de usuario | Administración, operación, análisis, consulta | Vigencia contrato | ANEXO I, p.4 |
| Acceso | Web seguro, navegadores corporativos soportados | Vigencia contrato | ANEXO I, p.4 |
| Módulos incluidos | Inteligencia meteorológica, visualización geoespacial, simulación incendios, simulación inundaciones | Vigencia contrato | ANEXO I, p.4 |
| Duración del servicio | 24 meses | Desde formalización | PCP, p.22; ANEXO I, p.21 |
| Horario soporte | 8 horas/día, 7 días/semana | Vigencia contrato | ANEXO I, p.16 |
| Bolsa de horas | 350 UT/año (máx.) | Anual | ANEXO I, p.19 |
| Formación inicial | 2 jornadas mínimas, remotas o equivalente | Inicio | ANEXO I, p.20 |
| Informes mensuales | Disponibilidad, incidencias, cambios, bolsa de horas | Mensual | ANEXO I, p.19-20 |

# 3. Modelo de servicio exigido

- Solución SaaS accesible por web, sin despliegue de infraestructura física en RENFE.
- Incluye alojamiento, operación, actualización, mantenimiento y soporte.
- Acceso a módulos funcionales y fuentes de datos meteorológicos y geoespaciales.
- Perfiles diferenciados de usuario (administrador, operador, analista, consulta).
- Soporte y mantenimiento con centro de soporte accesible por portal, email y teléfono.
- Asistencia técnica especializada multidisciplinar.
- Integración con sistemas corporativos de RENFE (identidad, datos, incidencias, etc.).
- Bolsa de horas para evolutivos y soporte especializado.

# 4. Procesos y actividades

| Proceso/actividad | Expreso en pliego | Exigencia descrita | Fuente |
|-------------------|------------------|-------------------|--------|
| Gestión de incidencias | ITIL NO CITADO EXPRESAMENTE | Centro de soporte, registro, trazabilidad, clasificación por prioridad | ANEXO I, p.16 |
| Gestión de cambios | ITIL NO CITADO EXPRESAMENTE | Gestión formal de cambios de alcance y evolución de requisitos | ANEXO I, p.22-23 |
| Gestión de alertas y avisos | ITIL NO CITADO EXPRESAMENTE | Configuración, emisión, registro, exportación y consulta histórica | ANEXO I, p.10-11 |
| Gestión de usuarios y accesos | ITIL NO CITADO EXPRESAMENTE | Perfiles, autenticación, integración con sistema de identidad | ANEXO I, p.14-15, 31-32 |
| Gestión de integraciones | ITIL NO CITADO EXPRESAMENTE | APIs, servicios geoespaciales, formatos interoperables | ANEXO I, p.14-15 |
| Gestión de la continuidad | ITIL NO CITADO EXPRESAMENTE | Planes de contingencia, continuidad, salida programada y sobrevenida | ANEXO I, p.38-39 |
| Gestión de la seguridad | ITIL NO CITADO EXPRESAMENTE | Análisis de riesgos, cumplimiento ENS, gestión de vulnerabilidades | ANEXO I, p.24-39 |
| Monitorización de la infraestructura | ITIL NO CITADO EXPRESAMENTE | Monitorización 24x7 de incidencias e incidentes | ANEXO I, p.36-37 |
| Reporting e informes | ITIL NO CITADO EXPRESAMENTE | Informes mensuales, análisis de causa raíz, consumo de bolsa de horas | ANEXO I, p.19-20 |
| Formación y transferencia de conocimiento | ITIL NO CITADO EXPRESAMENTE | Programa de formación, materiales, sesiones periódicas | ANEXO I, p.20-21 |

# 5. SLA/KPI/penalizaciones

| Servicio | Prioridad | Respuesta | Resolución | Horario | Objetivo | Penalización | Fuente |
|---------|----------|----------|-----------|--------|---------|-------------|--------|
| Soporte e incidencias | Crítica | Atención prioritaria, seguimiento continuo | Hasta restauración | 8x7 | A definir en acuerdo de nivel de servicio | 2% importe contrato por superación de tiempo de respuesta/restauración | ANEXO I, p.16; PCP, p.29 |
| Soporte e incidencias | Alta | Atención preferente, plan de recuperación comunicado | A definir | 8x7 | A definir en acuerdo de nivel de servicio | 1,5% importe contrato por superación de tiempo de respuesta/restauración | ANEXO I, p.16; PCP, p.29 |
| Soporte e incidencias | Media | Resolución planificada dentro del ciclo de soporte | A definir | 8x7 | A definir en acuerdo de nivel de servicio | 1% importe contrato por superación de tiempo de respuesta/restauración | ANEXO I, p.16; PCP, p.29 |
| Soporte e incidencias | Baja | Gestión ordinaria | A definir | 8x7 | A definir en acuerdo de nivel de servicio | 0,5% importe contrato por superación de tiempo de respuesta/restauración | ANEXO I, p.16; PCP, p.29 |
| Calidad del servicio | N/A | N/A | N/A | N/A | N/A | Hasta 10% importe total contrato por falta de calidad manifiesta | PCP, p.30 |
| Equipo de trabajo | N/A | N/A | N/A | N/A | N/A | 5.000 € por incumplimiento de nivel de conocimientos, rotación no comunicada | PCP, p.30 |
| Reuniones de seguimiento | N/A | N/A | N/A | N/A | N/A | Hasta 1% importe total contrato por incomparecencia | PCP, p.30 |
| Incumplimiento oferta técnica | N/A | N/A | N/A | N/A | N/A | Hasta 2.000 € por incumplimiento | PCP, p.30 |
| Seguridad/confidencialidad | N/A | N/A | N/A | N/A | N/A | Hasta 20% importe total contrato | PCP, p.30 |
| Seguridad/ciberseguridad (documentación, ENS, POC) | N/A | N/A | N/A | N/A | N/A | Hasta 10% importe total contrato o penalizaciones específicas (1.000-3.000 €) | PCP, p.31 |

Nota: Los tiempos concretos de respuesta y resolución se definirán en el acuerdo de nivel de servicio aprobado para el contrato (ANEXO I, p.16).

# 6. Organización y roles exigidos

- Project Manager (Responsable del servicio): titulación universitaria oficial (preferentemente Ingeniería, Informática, Telecomunicaciones, Física, Matemáticas, Geografía, Ciencias Ambientales o equivalente), mínimo 3 años de experiencia en proyectos análogos. (ANEXO I, p.17)
- Especialista en meteorología y predicción: titulación universitaria en Física, Meteorología, Ciencias Atmosféricas, Matemáticas, Ciencias Ambientales o equivalente, formación en meteorología y predicción numérica. (ANEXO I, p.18)
- Especialista en algoritmos de predicción a corto plazo: titulación universitaria en Física, Meteorología, Ciencias Atmosféricas, Matemáticas, Ingeniería o equivalente, formación en meteorología y predicción numérica. (ANEXO I, p.18)
- Especialista en software, datos e integraciones: titulación universitaria en Informática, Telecomunicaciones, Ingeniería, Matemáticas, Ciencia de Datos o equivalente. (ANEXO I, p.18)
- Especialista en riesgos naturales: titulación universitaria en Ingeniería de Montes, Forestal, Caminos, Civil, Hidrología, Geología, Geografía, Ciencias Ambientales o equivalente, formación en incendios o inundaciones. (ANEXO I, p.18)
- Equipo estable, suficiente y multidisciplinar, disponible desde la puesta en marcha. (ANEXO I, p.18)
- Sustituciones solo por causa de fuerza mayor, previa comunicación. (ANEXO I, p.18)
- Formación y concienciación en seguridad para el personal involucrado. (ANEXO I, p.27)

# 7. Gobierno y reporting exigidos

- Designación de responsable del servicio por el adjudicatario. (ANEXO I, p.22)
- Reuniones de seguimiento con periodicidad establecida por RENFE. (ANEXO I, p.22)
- Cuadro de acciones, responsables, fechas objetivo, riesgos y decisiones. (ANEXO I, p.22)
- Gestión formal de cambios y evolución de requisitos. (ANEXO I, p.22)
- Escalado de incidencias, riesgos de continuidad y desviaciones relevantes. (ANEXO I, p.22)
- Revisión periódica de indicadores, calidad del dato, uso de la solución y oportunidades de mejora. (ANEXO I, p.23)
- Informes mensuales de servicio: disponibilidad, incidencias, consultas, tiempos de atención, problemas recurrentes, cambios, bolsa de horas, análisis de causa raíz, riesgos y propuestas de mejora. (ANEXO I, p.19-20)

# 8. Herramientas ITSM, CMDB, monitorización e integraciones exigidas

- Centro de soporte accesible por portal de solicitudes, correo electrónico y teléfono. (ANEXO I, p.16)
- APIs documentadas para consulta de predicciones, observaciones, alertas, informes y simulaciones. (ANEXO I, p.14-15)
- Servicios geoespaciales normalizados para publicación y consumo de mapas, entidades y teselas. (ANEXO I, p.15)
- Integración con sistema corporativo de identidad (autenticación, SSO). (ANEXO I, p.14-15, 31-32)
- Inventario de activos de información, software, hardware, configuraciones, usuarios, derechos de acceso. (ANEXO I, p.26)
- Monitorización de la infraestructura para incidencias e incidentes 24x7. (ANEXO I, p.36-37)
- Entrega de logs al SIEM de RENFE o API para captura de logs. (ANEXO I, p.36)
- Herramientas de gestión de vulnerabilidades, backup, restauración, cifrado, DLP, antimalware, defensa perimetral, IDS/IPS, WAF, CASB, CWPP, proxys, protección de correo, 2FA según naturaleza del servicio. (ANEXO I, p.34-36)
- Documentación de usuario y técnica accesible durante toda la vigencia del servicio. (ANEXO I, p.4, 21)

# 9. Transición, continuidad y reversibilidad exigidas

- Servicio estándar disponible desde el inicio; configuración completa en máximo 3 meses desde que RENFE facilite información y accesos. (ANEXO I, p.21)
- Planificación de puesta en marcha: reunión inicial, inventario, configuración, carga de capas, definición de alertas, pruebas, formación, aceptación. (ANEXO I, p.21)
- Garantía técnica durante toda la vigencia: disponibilidad, corrección de defectos, funcionamiento de integraciones, actualización de datos, conservación de configuraciones. (ANEXO I, p.21-22)
- Plan de devolución, exportación de datos, entrega documental y certificado de supresión al finalizar. (ANEXO I, p.22)
- Planes de contingencia, crisis, continuidad de negocio, salida programada y sobrevenida, devolución y destrucción segura de información, certificación de destrucción. (ANEXO I, p.38-39)
- Mecanismos de respaldo de información, redundancia, balanceo, localizaciones alternativas. (ANEXO I, p.38)

# 10. Automatización, self-service y gestión del conocimiento

- Automatización: generación y envío automático de boletines y alertas, exportación de informes en formatos interoperables. (ANEXO I, p.11-12, 14)
- Portal de solicitudes para soporte (self-service). (ANEXO I, p.16)
- Documentación de usuario, manuales, guías rápidas, videoteca, materiales grabados, sesiones periódicas, actualización tras cambios funcionales. (ANEXO I, p.21)

# 11. Datos no localizados o ambiguos en la documentación

- No consta en la documentación revisada la definición concreta de los tiempos de respuesta y resolución para cada prioridad de incidencia; se remite a un acuerdo de nivel de servicio a definir tras la adjudicación (ANEXO I, p.16).
- No consta en la documentación revisada la volumetría exacta de datos, número de incidencias estimadas, ni dimensionamiento de equipo más allá de los perfiles mínimos.
- No consta en la documentación revisada la existencia de un Service Desk con niveles N1/N2/N3 expresamente definidos según ITIL.
- No consta en la documentación revisada la exigencia de una CMDB específica, aunque se requiere inventario de activos y configuraciones.
- No consta en la documentación revisada la exigencia de herramientas ITSM concretas por marca o producto.
- No consta en la documentación revisada la exigencia de reporting automatizado más allá de los informes mensuales y exportaciones descritas.

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

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---------------|------|----------------|-----------|-----------------|-------------------|
| Usuarios nominativos mínimos | Obligación contractual | 15 | ANEXO I | p.4 | Leído |
| Acceso web seguro | Obligación contractual | Navegadores corporativos soportados | ANEXO I | p.4 | Leído |
| Módulos incluidos | Obligación contractual | Inteligencia meteorológica, visualización geoespacial, simulación incendios, simulación inundaciones | ANEXO I | p.4 | Leído |
| Duración del servicio | Obligación contractual | 24 meses | PCP, ANEXO I | p.22, p.21 | Leído |
| Horario soporte | Obligación contractual | 8 horas/día, 7 días/semana | ANEXO I | p.16 | Leído |
| Bolsa de horas | Obligación contractual | 350 UT/año (máx.) | ANEXO I | p.19 | Leído |
| Project Manager | Obligación contractual | Titulación universitaria, 3 años experiencia | ANEXO I | p.17 | Leído |
| Especialistas (meteorología, predicción, software, riesgos) | Obligación contractual | Titulación y experiencia según perfil | ANEXO I | p.18 | Leído |
| Centro de soporte | Obligación contractual | Portal, email, teléfono | ANEXO I | p.16 | Leído |
| Integración con sistemas corporativos | Obligación contractual | Identidad, APIs, servicios geoespaciales | ANEXO I | p.14-15 | Leído |
| Informes mensuales | Obligación contractual | Disponibilidad, incidencias, cambios, bolsa de horas | ANEXO I | p.19-20 | Leído |
| Plan de devolución y destrucción de datos | Obligación contractual | Exportación, certificado de supresión | ANEXO I | p.22, 39 | Leído |
| Planes de contingencia, continuidad, salida | Obligación contractual | Descritos | ANEXO I | p.38-39 | Leído |
| Penalizaciones por SLA | Penalización | 0,5%-2% importe contrato según prioridad | PCP | p.29 | Leído |
| Penalizaciones por calidad, equipo, seguridad | Penalización | Hasta 20% importe contrato, 5.000 €, 1.000-3.000 € | PCP | p.30-31 | Leído |
| Automatización de boletines y alertas | Obligación contractual | Generación y envío automático | ANEXO I | p.11-12 | Leído |
| Documentación y materiales formativos | Obligación contractual | Manuales, guías, videoteca, sesiones | ANEXO I | p.21 | Leído |
| SLA tiempos de respuesta/resolución | NO LOCALIZADO | A definir en acuerdo posterior | ANEXO I | p.16 | Leído |
| Niveles N1/N2/N3 ITIL | NO CONSTA | No expresados | ANEXO I | p.16 | Leído |
| CMDB específica | NO CONSTA | No exigida expresamente | ANEXO I | p.26 | Leído |
| Herramienta ITSM concreta | NO CONSTA | No exigida expresamente | ANEXO I | p.16 | Leído |
| Reporting automatizado | NO CONSTA | No exigido más allá de informes mensuales | ANEXO I | p.19-20 | Leído |

# Discrepancias y pendientes de aclaración

- No se han identificado discrepancias en la documentación revisada.