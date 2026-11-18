# 1. Resumen factual Seguridad / DPO / ENS

**Resumen:**
- El contrato exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para los sistemas y servicios objeto del contrato, con medidas de seguridad del Anexo II del ENS y guías CCN-STIC aplicables. No se exige certificación ENS ni ISO 27001.
- No se requiere tratamiento de datos personales por cuenta del Ayuntamiento ni acuerdo de encargado de tratamiento, según los pliegos y PPTP.
- El adjudicatario debe cumplir con la normativa de seguridad de la información vigente, la política de seguridad del Ayuntamiento de Madrid y las instrucciones de IAM y el Centro de Ciberseguridad municipal.
- Se establecen requisitos detallados para despliegue en cloud pública (Azure, AWS, GCP), localización de datos en el EEE, y prohibición de transferencias internacionales fuera del EEE.
- Se exige análisis de riesgos, plan de tratamiento, configuración segura, desarrollo seguro, cifrado de información no pública, identificación y autenticación, control de accesos, logging, gestión de vulnerabilidades, gestión de incidentes, auditorías, borrado seguro y confidencialidad.
- Se establecen penalizaciones económicas y consecuencias contractuales por incumplimiento de obligaciones de seguridad, confidencialidad, subcontratación y otras condiciones esenciales.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
| Requisito ENS | Categoria/Nivel | Alcance | Acreditación | Momento | Fuente |
|---|---|---|---|---|---|
| Cumplimiento ENS | BÁSICO | Servicios objeto del contrato y sistemas desarrollados/desplegados/mantenidos | Descripción de mecanismos de seguridad en la oferta técnica | Presentación de oferta y ejecución | ID_188_3.PDF, pág. 45-46, 11.1, 11.3, 11.4 |
| Aplicación medidas Anexo II ENS | BÁSICO | Servicios y sistemas objeto del contrato | Supervisión y comprobación por órgano de contratación | Ejecución | ID_188_3.PDF, pág. 46, 11.1 |
| Guías CCN-STIC | BÁSICO | Configuración de componentes tecnológicos | Configuración conforme a guías CCN-STIC | Ejecución | ID_188_3.PDF, pág. 46-47, 11.4 |
| Análisis de riesgos ENS | BÁSICO | Servicios y sistemas desarrollados/desplegados/mantenidos | Análisis de riesgos validado por el Ayuntamiento | Inicio de trabajos | ID_188_3.PDF, pág. 46, 11.3 |
| Designación POC seguridad | BÁSICO | Seguridad de la información tratada y servicio prestado | Designación de punto/persona de contacto | Ejecución | ID_188_3.PDF, pág. 46, 11.2 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|---|---|---|---|
| Tratamiento de datos personales por cuenta del Ayuntamiento | NO requerido | NO APLICA | ID_188_3.PDF, pág. 50, 11.18; ID_188_2.PDF, pág. 54, Anexo I, 1.8 |
| Acuerdo de encargado de tratamiento | NO requerido | NO APLICA | ID_188_2.PDF, pág. 54, Anexo I, 1.8 |
| DPO/DPD designado | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA |
| Información sobre protección de datos (contratación municipal) | Responsable: Dirección General de Contratación y Servicios | Conservación: mientras sean necesarios para la ejecución del contrato | ID_188_2.PDF, pág. 95, Anexo IX |

# 4. Subencargados, cloud, localización y transferencias
| Requisito | Condición | Fuente |
|---|---|---|
| Subcontratación permitida | Debe indicar parte subcontratada, importe y nombre/perfil del subcontratista; prohibida en tareas críticas (implantación y jefe de proyecto) | ID_188_2.PDF, pág. 75-76, Anexo I, 25-26; ID_188_3.PDF, pág. 29, 6.5 |
| Cloud pública admitida | Solo Azure, AWS, GCP; recursos en regiones del EEE | ID_188_3.PDF, pág. 29-30, 7 |
| Localización de datos | Recursos desplegados en regiones del EEE; prohibidas transferencias fuera del EEE | ID_188_3.PDF, pág. 30, 7; pág. 33, Organización de recursos |
| Transferencias internacionales | Prohibidas fuera del EEE | ID_188_3.PDF, pág. 30, 7; pág. 33 |

# 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente
| Medida | Obligatoria/Valorable/Condicionada | Parámetro/Plazo | Fuente |
|---|---|---|---|
| Análisis de riesgos ENS | Obligatoria | Al inicio de los trabajos | ID_188_3.PDF, pág. 46, 11.3 |
| Configuración segura (guías CCN-STIC) | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 46-47, 11.4 |
| Desarrollo seguro y orientado a la privacidad | Obligatoria | Durante ciclo de vida del proyecto | ID_188_3.PDF, pág. 47, 11.5 |
| Cifrado de información no pública | Obligatoria | Cuando se transmita por redes ajenas al Ayuntamiento | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación | Obligatoria | Según ENS y normativa municipal | ID_188_3.PDF, pág. 47, 11.7 |
| Compatibilidad doble factor autenticación | Obligatoria si aplica | Durante ejecución | ID_188_3.PDF, pág. 48, 11.8 |
| Control de acceso (mínimo privilegio, necesidad de conocer) | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48, 11.10 |
| Logging y registros de actividad | Obligatoria | Durante ejecución; entrega a requerimiento | ID_188_3.PDF, pág. 49, 11.12 |
| Actualizaciones de seguridad/parcheado | Obligatoria | Periódica y continuada | ID_188_3.PDF, pág. 49, 11.13 |
| Gestión de incidentes de seguridad | Obligatoria | Notificación inmediata al responsable del contrato | ID_188_3.PDF, pág. 49, 11.14 |
| Subsanación de vulnerabilidades | Obligatoria | A requerimiento del responsable del contrato | ID_188_3.PDF, pág. 49, 11.15 |
| Auditorías de seguridad | Obligatoria | A requerimiento del Ayuntamiento | ID_188_3.PDF, pág. 49, 11.16 |
| Borrado seguro y certificado de destrucción | Obligatoria | Al cierre del contrato | ID_188_3.PDF, pág. 9, Fase II Operación |
| Confidencialidad | Obligatoria | Durante y después del contrato | ID_188_3.PDF, pág. 53, 15 |

# 6. Identidad, accesos y privilegios
- Identificación y autenticación: Delegación en plataforma de identidad corporativa para personal municipal y en sistema estatal Cl@VE para ciudadanía. Otros métodos requieren autorización de IAM. (ID_188_3.PDF, pág. 47, 11.7)
- Control de acceso: Principios de mínimo privilegio y necesidad de conocer. Restricción de roles de administración. (ID_188_3.PDF, pág. 48, 11.10)
- Acceso remoto: Uso del servicio de acceso remoto para empresas del Ayuntamiento; cumplimiento de condiciones de uso. (ID_188_3.PDF, pág. 48-49, 11.9)

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- Subsanación de vulnerabilidades: Obligatoria a requerimiento del responsable del contrato. (ID_188_3.PDF, pág. 49, 11.15)
- Actualizaciones de seguridad/parcheado: Obligatoria, periódica y continuada. Medidas compensatorias si no es posible aplicar una actualización. (ID_188_3.PDF, pág. 49, 11.13)
- Desarrollo seguro: Metodologías y buenas prácticas verificables de desarrollo seguro durante todo el ciclo de vida. (ID_188_3.PDF, pág. 47, 11.5)

# 8. Incidentes, brechas y plazos de notificación expresamente indicados
- Gestión de incidentes de seguridad: Obligatoria, conforme a la guía CCN-STIC-817. Notificación inmediata al responsable del contrato y mantenimiento de información hasta cierre del incidente. (ID_188_3.PDF, pág. 49, 11.14)
- No se especifican plazos concretos en horas/días para la notificación, solo "tan pronto como tenga conocimiento".

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención
- Logging: Registro de actividades de usuarios, retención de información necesaria para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas. Entrega de registros a requerimiento. (ID_188_3.PDF, pág. 49, 11.12)
- Integración con herramientas de observabilidad y monitorización de IAM si se solicita. (ID_188_3.PDF, pág. 31)
- Copias de seguridad y restauración: Proporcionadas por IAM. (ID_188_3.PDF, pág. 31)
- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Continuidad: NO CONSTA EN LA DOCUMENTACION REVISADA ningún RTO/RPO ni plan de continuidad específico, salvo la obligación de resiliencia y disponibilidad 24x7 del servicio (ID_188_3.PDF, pág. 13, RAV_8).

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Auditorías de seguridad: El Ayuntamiento podrá realizar auditorías de seguridad de los sistemas implantados o utilizados. (ID_188_3.PDF, pág. 49, 11.16)
- Evidencias/certificados: Certificado de destrucción de datos al cierre del contrato. (ID_188_3.PDF, pág. 9, Fase II Operación)
- Certificaciones ISO/ENS: NO EXIGIDO EXPRESAMENTE. (ID_188_2.PDF, pág. 65, Anexo I, 5)
- Seguridad del personal: Obligación de proveer equipos de protección individual y cumplir normativa de prevención de riesgos laborales. (ID_188_3.PDF, pág. 23-24, 6)
- Borrado seguro: Obligatorio al cierre del contrato, con certificado. (ID_188_3.PDF, pág. 9, Fase II Operación)
- Confidencialidad: Obligación durante y después del contrato. (ID_188_3.PDF, pág. 53, 15)

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Penalizaciones económicas del 5% o 10% del precio del contrato por incumplimientos graves o muy graves, incluyendo destrucción, pérdida o alteración de datos, indisponibilidad del servicio, incumplimiento de órdenes, etc. (ID_188_2.PDF, pág. 76-77, Anexo I, 30)
- Resolución del contrato por reiteración de incumplimientos muy graves. (ID_188_2.PDF, pág. 78, Anexo I, 31)
- Incumplimiento de confidencialidad: Derecho del Ayuntamiento a ejercer acciones legales. (ID_188_3.PDF, pág. 53, 15)

# 12. Datos no localizados o ambiguos, sin recomendaciones
- No consta exigencia de certificación ENS ni ISO 27001.
- No consta exigencia de DPO/DPD para el adjudicatario.
- No consta exigencia de RTO/RPO ni plan de continuidad específico.
- No consta exigencia de SIEM/SOC dedicado.
- No consta exigencia de MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, DLP, backups gestionados por el adjudicatario, ni SBOM.
- No consta exigencia de SAST, DAST, SCA, OWASP, CI/CD, ni SDLC formalizado.
- No consta exigencia de EIPD (Evaluación de Impacto de Protección de Datos).
- No consta exigencia de acuerdos de subencargado de tratamiento.

# 13. Documentos revisados: enumera todos los documentos del índice, uno por uno
1. ID_188_1.PDF (Documento licitación real)
2. ID_188_2.PDF (Documento licitación real)
3. ID_188_3.PDF (Pliego de Prescripciones Técnicas)
4. poc (Documento enlazado, detalle licitación)
5. poc (Documento enlazado, perfil contratante)
6. poc (Documento enlazado, perfil contratante)
7. 147409-2026 (Documento enlazado, sin texto extraíble; pendiente de lectura/OCR)
8. perfilContratante (Documento enlazado)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Cumplimiento ENS | Obligación contractual | Nivel BÁSICO, medidas Anexo II ENS | ID_188_3.PDF | 45-46, 11.1 | Leído |
| Certificación ENS/ISO 27001 | NO EXIGIDO EXPRESAMENTE | No se exige | ID_188_2.PDF | 65, Anexo I, 5 | Leído |
| Análisis de riesgos ENS | Obligación contractual | Al inicio de los trabajos | ID_188_3.PDF | 46, 11.3 | Leído |
| Configuración segura (CCN-STIC) | Obligación contractual | Durante ejecución | ID_188_3.PDF | 46-47, 11.4 | Leído |
| Desarrollo seguro | Obligación contractual | Buenas prácticas verificables | ID_188_3.PDF | 47, 11.5 | Leído |
| Cifrado información no pública | Obligación contractual | Cuando se transmita por redes ajenas | ID_188_3.PDF | 47, 11.6 | Leído |
| Identificación y autenticación | Obligación contractual | Delegación en sistemas corporativos | ID_188_3.PDF | 47, 11.7 | Leído |
| Control de acceso | Obligación contractual | Mínimo privilegio, necesidad de conocer | ID_188_3.PDF | 48, 11.10 | Leído |
| Logging y registros de actividad | Obligación contractual | Registro y entrega a requerimiento | ID_188_3.PDF | 49, 11.12 | Leído |
| Actualizaciones de seguridad | Obligación contractual | Periódica y continuada | ID_188_3.PDF | 49, 11.13 | Leído |
| Gestión de incidentes | Obligación contractual | Notificación inmediata | ID_188_3.PDF | 49, 11.14 | Leído |
| Subsanación de vulnerabilidades | Obligación contractual | A requerimiento | ID_188_3.PDF | 49, 11.15 | Leído |
| Auditorías de seguridad | Obligación contractual | A requerimiento | ID_188_3.PDF | 49, 11.16 | Leído |
| Borrado seguro y certificado | Obligación contractual | Al cierre del contrato | ID_188_3.PDF | 9, Fase II Operación | Leído |
| Confidencialidad | Obligación contractual | Durante y después del contrato | ID_188_3.PDF | 53, 15 | Leído |
| Subcontratación | Permitida con condiciones | Prohibida en tareas críticas | ID_188_2.PDF | 75-76, Anexo I, 25-26 | Leído |
| Cloud pública | Permitida con condiciones | Solo Azure, AWS, GCP; EEE | ID_188_3.PDF | 29-30, 7 | Leído |
| Localización de datos | Obligación contractual | Regiones del EEE | ID_188_3.PDF | 30, 7; 33 | Leído |
| Transferencias internacionales | Prohibidas fuera del EEE | Obligación contractual | ID_188_3.PDF | 30, 7; 33 | Leído |
| Penalizaciones por incumplimiento | Consecuencia contractual | 5% o 10% del precio del contrato | ID_188_2.PDF | 76-77, Anexo I, 30 | Leído |
| Resolución por incumplimiento | Consecuencia contractual | Reiteración de muy graves | ID_188_2.PDF | 78, Anexo I, 31 | Leído |
| DPO/DPD | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |
| RTO/RPO | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |
| SIEM/SOC | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |
| MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, DLP, SBOM | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |
| SAST, DAST, SCA, OWASP, CI/CD, SDLC formalizado | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |
| EIPD | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |

# Discrepancias y pendientes de aclaración
- Documento 7 (147409-2026) pendiente de lectura/OCR. No se ha podido verificar si contiene requisitos adicionales o contradictorios.
- No se han identificado discrepancias internas en los documentos revisados.
- No se han localizado requisitos de seguridad, ENS, DPO, RGPD, medidas técnicas o consecuencias contractuales fuera de los recogidos en este informe.