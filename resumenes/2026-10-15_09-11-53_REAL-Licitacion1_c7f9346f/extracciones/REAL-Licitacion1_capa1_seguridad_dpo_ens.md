# 1. Resumen factual Seguridad / DPO / ENS

- El contrato exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para todos los servicios y sistemas desarrollados, desplegados o mantenidos en el marco del contrato. No se exige certificación ENS ni ISO 27001, pero sí la aplicación de las medidas del Anexo II del ENS nivel Básico y la justificación documental de su aplicación. 
- No se exige tratamiento de datos personales por cuenta del Ayuntamiento ni acuerdo de encargado de tratamiento, según se declara expresamente en el PPTP y Anexo I del PCAP. El adjudicatario no asume el rol de encargado de tratamiento de datos personales del Ayuntamiento.
- Se exige cumplimiento de la normativa de protección de datos (LOPDGDD, RGPD) para los datos tratados en la contratación municipal, pero no para el servicio objeto del contrato, ya que no implica tratamiento de datos personales por cuenta del Ayuntamiento.
- Se establecen requisitos detallados de seguridad de la información, gestión de identidades y accesos, control de privilegios, logging, gestión de vulnerabilidades, incidentes, desarrollo seguro, auditoría, borrado seguro y confidencialidad, todos ellos alineados con ENS nivel Básico y la política de seguridad del Ayuntamiento de Madrid.
- El despliegue cloud debe realizarse exclusivamente en las plataformas MultiCloud corporativas del Ayuntamiento (Azure, AWS, GCP), en regiones del Espacio Económico Europeo, bajo el modelo de gobierno y seguridad de IAM y CCMAD.
- Se exige la designación de un Punto o Persona de Contacto (POC) para seguridad de la información.
- Se exige análisis de riesgos conforme a ENS, plan de tratamiento, configuración segura, cifrado de información no pública en tránsito, autenticación y autorización conforme a la normativa municipal, y registro de actividad.
- Se exige borrado seguro de datos al finalizar el contrato, con certificado de destrucción.
- Se establecen penalizaciones específicas por destrucción, pérdida o alteración de datos, indisponibilidad del servicio, incumplimiento de medidas de seguridad y confidencialidad.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
| Requisito ENS | Nivel | Alcance | Acreditación | Momento | Fuente |
|----------------|-------|---------|--------------|---------|--------|
| Cumplimiento ENS | Básico | Todos los servicios y sistemas desarrollados/desplegados/mantenidos | Descripción de mecanismos de seguridad previstos en la oferta; documentación justificativa a requerimiento | Oferta y durante ejecución | ID_188_3.PDF, pág. 46-47, 11.1-11.3 |
| Análisis de riesgos ENS | Básico | Servicios digitales, desarrollo/mantenimiento SW, infraestructuras/plataformas | Análisis de riesgos validado por el Ayuntamiento | Inicio de los trabajos | ID_188_3.PDF, pág. 46, 11.3 |
| Medidas ENS Anexo II | Básico | Servicios y sistemas objeto del contrato | Supervisión y comprobación por el órgano de contratación | Durante ejecución | ID_188_3.PDF, pág. 46 |
| Configuración segura (CCN-STIC) | Básico | Todos los componentes tecnológicos | Adecuación a guías CCN-STIC, con aprobación del responsable del contrato | Durante ejecución | ID_188_3.PDF, pág. 46-47, 11.4 |
| Designación POC seguridad | Básico | Servicio prestado | Designación formal | Inicio ejecución | ID_188_3.PDF, pág. 46, 11.2 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|----------------------|-----------|----------------|--------|
| Tratamiento de datos personales por cuenta del Ayuntamiento | NO requerido; el contrato no implica tratamiento de datos personales por cuenta del responsable | NO APLICA | ID_188_3.PDF, pág. 48, 11.18; ID_188_2.PDF, pág. 54, Anexo I, 1.8 |
| Acuerdo de encargado de tratamiento | NO requerido | NO APLICA | ID_188_2.PDF, pág. 54, Anexo I, 1.8 |
| Cumplimiento LOPDGDD/RGPD para contratación municipal | Obligatorio para datos de contratación municipal (no para el servicio objeto del contrato) | Conservación mientras sean necesarios para la ejecución del contrato | ID_188_2.PDF, pág. 95, Anexo IX |
| DPO/DPD designado | DPD de Coordinación General de Distritos, Transparencia y Participación Ciudadana (solo para datos de contratación municipal) | NO APLICA AL SERVICIO | ID_188_2.PDF, pág. 95, Anexo IX |

# 4. Subencargados, cloud, localización y transferencias
| Requisito | Condición | Fuente |
|-----------|-----------|--------|
| Subcontratación permitida | Sí, con comunicación previa y dentro de los límites fijados en el contrato | ID_188_2.PDF, pág. 54, Anexo I, 26; ID_188_3.PDF, pág. 29, 6.5 |
| Cloud público permitido | Solo en MultiCloud corporativa (Azure, AWS, GCP) en regiones EEE | ID_188_3.PDF, pág. 29-34, 7 |
| Localización de datos | Recursos desplegados en regiones del Espacio Económico Europeo (EEE) | ID_188_3.PDF, pág. 33 |
| Transferencias internacionales | No permitidas fuera del EEE; cumplimiento art. 45 RGPD | ID_188_3.PDF, pág. 33 |

# 5. Medidas técnicas
| Medida | Obligatoria/valorable/condicionada | Parámetro/plazo | Fuente |
|--------|-------------------------------|------------------|--------|
| Cifrado de información no pública en tránsito | Obligatoria | Cuando se transmita por redes ajenas al Ayuntamiento; según valoración del responsable | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación | Obligatoria | Delegación en plataforma de identidad corporativa (personal municipal) o CL@VE (ciudadanía); otros métodos requieren autorización | ID_188_3.PDF, pág. 47, 11.7 |
| Doble factor de autenticación | Obligatoria si lo requiere el servicio | Provisión de medios por el adjudicatario | ID_188_3.PDF, pág. 48, 11.8 |
| Control de acceso y privilegios | Obligatoria | Principios de mínimo privilegio y necesidad de conocer; restricción de roles de administración | ID_188_3.PDF, pág. 48, 11.10 |
| Logging y registros de actividad | Obligatoria | Registro de actividades de usuarios, entrega a requerimiento | ID_188_3.PDF, pág. 49, 11.12 |
| Actualizaciones de seguridad | Obligatoria | Aplicación periódica y continuada; medidas compensatorias si no es posible | ID_188_3.PDF, pág. 49, 11.13 |
| Gestión de vulnerabilidades | Obligatoria | Subsanación de vulnerabilidades comunicadas por el responsable del contrato | ID_188_3.PDF, pág. 49, 11.15 |
| Gestión de incidentes | Obligatoria | Notificación inmediata al responsable del contrato; colaboración hasta cierre | ID_188_3.PDF, pág. 49, 11.14 |
| Desarrollo seguro | Obligatoria | Metodologías y buenas prácticas verificables de desarrollo seguro; documentación | ID_188_3.PDF, pág. 47, 11.5 |
| Borrado seguro de datos | Obligatoria | Al finalizar el contrato; certificado de destrucción | ID_188_3.PDF, pág. 9, 3.2; pág. 39, Art. 9.3 |
| Auditoría de seguridad | Obligatoria | El Ayuntamiento podrá auditar los sistemas implantados o utilizados | ID_188_3.PDF, pág. 49, 11.16 |
| Designación POC seguridad | Obligatoria | Inicio ejecución | ID_188_3.PDF, pág. 46, 11.2 |

# 6. Identidad, accesos y privilegios
- Gestión de credenciales y accesos a recursos cloud es competencia del Ayuntamiento; usuarios externos usan credenciales proporcionadas por IAM (ID_188_3.PDF, pág. 33).
- Acceso a información no pública: autenticación delegada en plataforma de identidad corporativa o CL@VE; otros métodos requieren autorización de IAM (ID_188_3.PDF, pág. 47).
- Principios de mínimo privilegio y necesidad de conocer; restricción de roles de administración (ID_188_3.PDF, pág. 48).

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- Subsanación de vulnerabilidades comunicadas por el responsable del contrato (ID_188_3.PDF, pág. 49).
- Aplicación periódica y continuada de actualizaciones de seguridad; medidas compensatorias si no es posible (ID_188_3.PDF, pág. 49).
- Desarrollo seguro: uso de metodologías y buenas prácticas verificables, documentadas (ID_188_3.PDF, pág. 47).

# 8. Incidentes, brechas y plazos de notificación
- Notificación de ciberincidentes al responsable del contrato tan pronto como se tenga conocimiento; mantener informado hasta cierre (ID_188_3.PDF, pág. 49).
- Gestión de incidentes conforme a guía CCN-STIC-817 y normativa específica del Ayuntamiento (ID_188_3.PDF, pág. 49).
- Colaboración activa en la paliación y resolución total del incidente (ID_188_3.PDF, pág. 49).
- No se especifican plazos concretos en horas o días para la notificación.

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención
- Registro de actividades de usuarios, retención de logs para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas; entrega a requerimiento (ID_188_3.PDF, pág. 49).
- Integración con herramientas de observabilidad y monitorización de IAM si se solicita (ID_188_3.PDF, pág. 30).
- Copias de seguridad y restauración proporcionadas por IAM (ID_188_3.PDF, pág. 31).
- No se especifican requisitos de SOC/SIEM, RTO/RPO ni pruebas de continuidad.

# 10. Auditorías, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Auditoría de seguridad: el Ayuntamiento podrá auditar los sistemas implantados o utilizados (ID_188_3.PDF, pág. 49).
- Borrado seguro de datos al finalizar el contrato, con certificado de destrucción (ID_188_3.PDF, pág. 9, 3.2; pág. 39, Art. 9.3).
- Confidencialidad: obligación de confidencialidad y secreto sobre la información a la que se acceda, subsiste tras la finalización del contrato (ID_188_3.PDF, pág. 53; ID_188_2.PDF, pág. 35, 36).
- Seguridad del personal: obligación de proveer equipos de protección individual y cumplir normativa de prevención de riesgos laborales (ID_188_3.PDF, pág. 23, 51).
- No se exige certificación ENS ni ISO 27001.

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Penalidad del 5% del precio del contrato por destrucción, pérdida o alteración de datos que generen daños al Ayuntamiento, indisponibilidad del asistente virtual superior a 48 horas, incumplimiento de órdenes del responsable del contrato, no presentación de informes, etc. (ID_188_2.PDF, pág. 76, 30; ID_188_3.PDF, pág. 76).
- Penalidad del 10% del precio del contrato por incumplimientos muy graves (reiteración, indisponibilidad superior a 5 días, etc.) (ID_188_2.PDF, pág. 77).
- Resolución del contrato por reiteración de incumplimientos muy graves, destrucción de datos con dolo o reincidencia, etc. (ID_188_2.PDF, pág. 77).

# 12. Datos no localizados o ambiguos
- No se exige certificación ENS ni ISO 27001.
- No se exige acuerdo de encargado de tratamiento ni subencargados para el servicio objeto del contrato.
- No se especifican requisitos de SOC/SIEM, RTO/RPO, pruebas de continuidad, ni medidas técnicas concretas como MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, DLP, backups (más allá de la referencia a copias de seguridad de IAM), ni requisitos de SBOM, SAST, DAST, SCA, CI/CD, OWASP, salvo la exigencia genérica de desarrollo seguro y buenas prácticas.
- No se exige designación de DPO/DPD para el adjudicatario.
- No se exige EIPD ni medidas específicas de protección de datos para el servicio objeto del contrato.

# 13. Documentos revisados
1. ID_188_1.PDF (Documento licitación real)
2. ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares y Anexos)
3. ID_188_3.PDF (Pliego de Prescripciones Técnicas Particulares)
4. poc (Documento enlazado, detalle licitación, sin información relevante de seguridad)
5. poc (Documento enlazado, perfil contratante, sin información relevante de seguridad)
6. poc (Documento enlazado, perfil contratante, sin información relevante de seguridad)
7. 147409-2026 (Documento enlazado, sin texto extraíble; pendiente de lectura/OCR)
8. perfilContratante (Documento enlazado, sin información relevante de seguridad)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|----------------|-----------|-----------------|-------------------|
| Cumplimiento ENS | Obligación contractual | Nivel Básico, medidas Anexo II ENS | ID_188_3.PDF | 46-47, 11.1-11.3 | Leído |
| Certificación ENS/ISO 27001 | NO EXIGIDO EXPRESAMENTE | No se exige | ID_188_3.PDF | 46 | Leído |
| Análisis de riesgos ENS | Obligación contractual | Al inicio, validado por Ayuntamiento | ID_188_3.PDF | 46, 11.3 | Leído |
| Configuración segura (CCN-STIC) | Obligación contractual | Guías CCN-STIC, aprobación responsable | ID_188_3.PDF | 46-47, 11.4 | Leído |
| Designación POC seguridad | Obligación contractual | Inicio ejecución | ID_188_3.PDF | 46, 11.2 | Leído |
| Tratamiento de datos personales | NO EXIGIDO EXPRESAMENTE | No aplica al servicio | ID_188_3.PDF | 48, 11.18 | Leído |
| Acuerdo de encargado/subencargado | NO EXIGIDO EXPRESAMENTE | No aplica al servicio | ID_188_2.PDF | 54, Anexo I, 1.8 | Leído |
| Subcontratación | Permitida | Comunicación previa, límites del contrato | ID_188_2.PDF | 54, Anexo I, 26 | Leído |
| Cloud público | Permitido | Solo MultiCloud corporativa, EEE | ID_188_3.PDF | 29-34, 7 | Leído |
| Localización de datos | Obligación contractual | Regiones EEE | ID_188_3.PDF | 33 | Leído |
| Transferencias internacionales | Prohibidas fuera EEE | Cumplimiento art. 45 RGPD | ID_188_3.PDF | 33 | Leído |
| Cifrado información no pública | Obligación contractual | En tránsito por redes ajenas | ID_188_3.PDF | 47, 11.6 | Leído |
| Identificación/autenticación | Obligación contractual | Delegación en identidad corporativa/CL@VE | ID_188_3.PDF | 47, 11.7 | Leído |
| Doble factor autenticación | Obligación contractual | Si lo requiere el servicio | ID_188_3.PDF | 48, 11.8 | Leído |
| Control de acceso/privilegios | Obligación contractual | Mínimo privilegio, necesidad de conocer | ID_188_3.PDF | 48, 11.10 | Leído |
| Logging/registros actividad | Obligación contractual | Registro, entrega a requerimiento | ID_188_3.PDF | 49, 11.12 | Leído |
| Actualizaciones de seguridad | Obligación contractual | Periódica y continuada | ID_188_3.PDF | 49, 11.13 | Leído |
| Gestión de vulnerabilidades | Obligación contractual | Subsanación a requerimiento | ID_188_3.PDF | 49, 11.15 | Leído |
| Gestión de incidentes | Obligación contractual | Notificación inmediata, colaboración | ID_188_3.PDF | 49, 11.14 | Leído |
| Desarrollo seguro | Obligación contractual | Buenas prácticas verificables | ID_188_3.PDF | 47, 11.5 | Leído |
| Borrado seguro de datos | Obligación contractual | Al finalizar, certificado destrucción | ID_188_3.PDF | 9, 3.2; 39, Art. 9.3 | Leído |
| Auditoría de seguridad | Derecho del cliente | El Ayuntamiento podrá auditar | ID_188_3.PDF | 49, 11.16 | Leído |
| Penalidades por destrucción/pérdida de datos | Consecuencia contractual | 5% o 10% del precio del contrato | ID_188_2.PDF | 76-77, 30 | Leído |
| Resolución por incumplimientos muy graves | Consecuencia contractual | Reiteración, dolo, indisponibilidad | ID_188_2.PDF | 77, 31 | Leído |
| DPO/DPD designado | Información descriptiva | Solo para datos de contratación municipal | ID_188_2.PDF | 95, Anexo IX | Leído |
| SOC/SIEM, RTO/RPO, pruebas continuidad | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |
| MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, DLP, SBOM, SAST, DAST, SCA, CI/CD, OWASP | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |

# Discrepancias y pendientes de aclaración
- No se han identificado discrepancias en la documentación revisada.
- Documento 147409-2026 pendiente de lectura/OCR; no se ha podido verificar si contiene requisitos adicionales de seguridad, ENS o protección de datos.