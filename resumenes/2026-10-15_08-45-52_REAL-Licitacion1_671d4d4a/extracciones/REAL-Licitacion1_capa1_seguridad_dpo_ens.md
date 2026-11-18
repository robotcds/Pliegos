# 1. Resumen factual Seguridad / DPO / ENS

- El contrato exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para todos los servicios y sistemas desarrollados, desplegados o mantenidos en el marco del contrato. No se exige certificación ENS ni ISO 27001, pero sí la aplicación de las medidas del Anexo II del ENS nivel Básico y la justificación documental de su aplicación. 
- No se exige tratamiento de datos personales por cuenta del Ayuntamiento ni acuerdo de encargo de tratamiento, según se indica expresamente en los pliegos y PPTP. El adjudicatario no asume el rol de encargado de tratamiento ni subencargado. 
- Se exige cumplimiento de la normativa de seguridad de la información vigente, incluyendo ENS, normativa municipal y guías CCN-STIC, así como la designación de un punto de contacto (POC) para seguridad de la información.
- Se establecen medidas técnicas obligatorias: análisis de riesgos, configuración segura, desarrollo seguro, cifrado de información no pública en tránsito, identificación y autenticación, compatibilidad con doble factor, control de acceso, logging, gestión de vulnerabilidades, gestión de incidentes, auditorías, y borrado seguro al finalizar el contrato.
- La solución debe desplegarse en cloud pública (Azure, AWS, GCP) bajo el modelo de gobierno y seguridad del Ayuntamiento de Madrid, con localización de recursos en el Espacio Económico Europeo (EEE) y prohibición de transferencias internacionales fuera del EEE.
- Se exige la entrega de logs, documentación técnica, evidencias de borrado y cumplimiento de obligaciones de confidencialidad durante y tras el contrato.
- No se exige DPO/DPD al adjudicatario ni se requiere EIPD, ya que no hay tratamiento de datos personales por cuenta del Ayuntamiento.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
| Requisito ENS | Categoria/Nivel | Alcance | Acreditación | Momento | Fuente |
|----------------|----------------|--------|--------------|---------|--------|
| Cumplimiento ENS | Básico | Todos los servicios y sistemas desarrollados/desplegados/mantenidos | Descripción de mecanismos de seguridad en la oferta; documentación justificativa durante ejecución | Oferta y ejecución | ID_188_3.PDF, pág. 46-47, 11.1, 11.3, 11.4 |
| Aplicación medidas Anexo II ENS | Básico | Servicios objeto del contrato | Supervisión y comprobación por órgano de contratación | Ejecución | ID_188_3.PDF, pág. 46 |
| Guías CCN-STIC | Básico | Configuración de componentes tecnológicos | Configuración conforme a guías CCN-STIC, validación por responsable del contrato | Ejecución | ID_188_3.PDF, pág. 46-47, 11.4 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|----------------------|-----------|------------------|--------|
| Tratamiento de datos personales por cuenta del responsable | NO requerido; expresamente excluido | NO APLICA | ID_188_3.PDF, pág. 43, 11.18; ID_188_2.PDF, pág. 54, 1.8 |
| Acuerdo de encargo de tratamiento | NO requerido | NO APLICA | ID_188_3.PDF, pág. 43, 11.18; ID_188_2.PDF, pág. 54, 1.8 |
| DPO/DPD designación | NO requerido | NO APLICA | ID_188_3.PDF, pág. 43, 11.18 |
| EIPD | NO requerido | NO APLICA | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Conservación de datos personales | NO APLICA | NO APLICA | ID_188_3.PDF, pág. 43, 11.18 |

# 4. Subencargados, cloud, localización y transferencias
| Requisito | Condición | Fuente |
|-----------|-----------|--------|
| Subencargados | No aplica, no hay encargo de tratamiento | ID_188_3.PDF, pág. 43, 11.18 |
| Cloud pública | Solo Azure, AWS, GCP; recursos en EEE | ID_188_3.PDF, pág. 29-34, 7 |
| Localización de datos | Recursos desplegados en regiones del EEE | ID_188_3.PDF, pág. 33 |
| Transferencias internacionales | Prohibidas fuera del EEE | ID_188_3.PDF, pág. 33 |

# 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente
| Medida | Tipo | Parámetro/Plazo | Fuente |
|--------|------|----------------|--------|
| Análisis de riesgos ENS | Obligatoria | Al inicio de los trabajos, validación por Ayuntamiento | ID_188_3.PDF, pág. 46, 11.3 |
| Configuración segura (CCN-STIC) | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 46-47, 11.4 |
| Desarrollo seguro | Obligatoria | Todo el ciclo de vida, prácticas reflejadas en documentación | ID_188_3.PDF, pág. 47, 11.5 |
| Cifrado de información no pública | Obligatoria | En tránsito por redes ajenas al Ayuntamiento | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación | Obligatoria | Personal municipal: identidad corporativa; ciudadanía: CL@VE; otros métodos requieren autorización | ID_188_3.PDF, pág. 47-48, 11.7 |
| Doble factor de autenticación | Obligatoria si aplica | Adjudicatario proporciona medios a su personal | ID_188_3.PDF, pág. 48, 11.8 |
| Acceso remoto | Obligatoria | Uso del servicio de acceso remoto del Ayuntamiento | ID_188_3.PDF, pág. 48, 11.9 |
| Control de acceso (mínimo privilegio, necesidad de conocer) | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48, 11.10 |
| Logging y registros de actividad | Obligatoria | Entrega a requerimiento, retención durante contrato | ID_188_3.PDF, pág. 49, 11.12 |
| Gestión de vulnerabilidades | Obligatoria | Subsanación a requerimiento del responsable | ID_188_3.PDF, pág. 49, 11.15 |
| Gestión de incidentes | Obligatoria | Notificación inmediata al responsable del contrato | ID_188_3.PDF, pág. 49, 11.14 |
| Auditorías de seguridad | Obligatoria | El Ayuntamiento puede auditar en cualquier momento | ID_188_3.PDF, pág. 49, 11.16 |
| Borrado seguro al finalizar contrato | Obligatoria | Certificado de destrucción, afecta a todos los sistemas con información del Ayuntamiento | ID_188_3.PDF, pág. 9, 3.2 |

# 6. Identidad, accesos y privilegios
- Identificación y autenticación: Personal municipal mediante plataforma de identidad corporativa; ciudadanía mediante sistema estatal CL@VE; otros métodos requieren autorización de IAM. (ID_188_3.PDF, pág. 47-48, 11.7)
- Doble factor: El adjudicatario debe proporcionar los medios necesarios a su personal si se requiere el doble factor municipal. (ID_188_3.PDF, pág. 48, 11.8)
- Control de acceso: Principios de mínimo privilegio y necesidad de conocer. (ID_188_3.PDF, pág. 48, 11.10)
- Acceso remoto: Solo mediante el servicio de acceso remoto del Ayuntamiento. (ID_188_3.PDF, pág. 48, 11.9)

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- Subsanación de vulnerabilidades: El adjudicatario debe subsanar las vulnerabilidades comunicadas por el responsable del contrato. (ID_188_3.PDF, pág. 49, 11.15)
- Parcheado: El adjudicatario debe mantener actualizados los elementos de la infraestructura, instalando actualizaciones y parches. (ID_188_3.PDF, pág. 30, 11.13)
- Desarrollo seguro: Metodologías y buenas prácticas verificables durante todo el ciclo de vida, reflejadas en la documentación del proyecto. (ID_188_3.PDF, pág. 47, 11.5)

# 8. Incidentes, brechas y plazos de notificación expresamente indicados
- Gestión de incidentes: El adjudicatario debe notificar cualquier ciberincidente que pueda afectar a información o servicios del Ayuntamiento al responsable del contrato tan pronto como tenga conocimiento, y mantenerle informado hasta el cierre del incidente. (ID_188_3.PDF, pág. 49, 11.14)
- No se especifican plazos concretos en horas o días, solo "tan pronto como tenga conocimiento".

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención
- Logging: El sistema debe registrar actividades de usuarios, permitiendo monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas, identificando a la persona que actúa. Entrega de registros a requerimiento. (ID_188_3.PDF, pág. 49, 11.12)
- Integración con herramientas de observabilidad y monitorización de IAM si se solicita. (ID_188_3.PDF, pág. 30)
- Backups: IAM proporciona servicios de copias de seguridad y restauración. (ID_188_3.PDF, pág. 31)
- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Continuidad: NO CONSTA EN LA DOCUMENTACION REVISADA ninguna exigencia de plan de continuidad o DR específico.

# 10. Auditorías, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Auditorías: El Ayuntamiento puede realizar auditorías de seguridad en cualquier momento. (ID_188_3.PDF, pág. 49, 11.16)
- Evidencias: Entrega de logs, documentación técnica, certificado de destrucción de datos al finalizar el contrato. (ID_188_3.PDF, pág. 9, 3.2)
- Certificaciones: No se exige certificación ENS ni ISO 27001. (ID_188_3.PDF, pág. 46-47)
- Seguridad del personal: El adjudicatario debe informar a sus empleados de la obligación de confidencialidad y cumplir con la normativa de seguridad. (ID_188_3.PDF, pág. 53, 15)
- Borrado: Eliminación segura de toda la información del servicio a su finalización, con certificado de destrucción. (ID_188_3.PDF, pág. 9, 3.2)
- Confidencialidad: Obligación de confidencialidad durante y tras el contrato, incluyendo a empleados y subcontratistas. (ID_188_3.PDF, pág. 53, 15)

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Incumplimiento de obligaciones de seguridad, confidencialidad, entrega de información, etc., puede dar lugar a penalidades del 5% o 10% del precio del contrato según la gravedad, y a la resolución del contrato en caso de reiteración. (ID_188_2.PDF, pág. 76-77, 30)
- Incumplimiento de la obligación de borrado seguro o entrega de información al finalizar el contrato puede impedir la recepción y liquidación final. (ID_188_3.PDF, pág. 9, 3.2)

# 12. Datos no localizados o ambiguos, sin recomendaciones
- No se exige certificación ENS ni ISO 27001.
- No se exige DPO/DPD ni EIPD.
- No se exige acuerdo de encargo de tratamiento ni subencargados.
- No se exige plan de continuidad, DR, RTO/RPO, ni integración con SOC/SIEM específico.
- No se especifican plazos concretos para notificación de incidentes más allá de "tan pronto como tenga conocimiento".
- No se exige SBOM, SAST, DAST, SCA, ni requisitos DevSecOps específicos más allá de "buenas prácticas verificables".

# 13. Documentos revisados
1. ID_188_1.PDF (Documento licitacion real)
2. ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares y Anexos)
3. ID_188_3.PDF (Pliego de Prescripciones Técnicas Particulares)
4. poc (enlazado desde ID_188_1.PDF, texto extraído)
5. poc (enlazado desde ID_188_1.PDF, texto extraído)
6. poc (enlazado desde ID_188_1.PDF, texto extraído)
7. 147409-2026 (enlazado desde ID_188_1.PDF, sin texto extraíble; pendiente de lectura/OCR)
8. perfilContratante (enlazado desde ID_188_2.PDF, texto extraído)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|----------------|-----------|-----------------|------------------|
| ENS cumplimiento | Obligación contractual | Nivel Básico, medidas Anexo II ENS | ID_188_3.PDF | 46-47, 11.1 | Leído |
| Certificación ENS/ISO | NO EXIGIDO EXPRESAMENTE | No se exige certificación | ID_188_3.PDF | 46-47 | Leído |
| DPO/DPD | NO EXIGIDO EXPRESAMENTE | No se exige designación | ID_188_3.PDF | 43, 11.18 | Leído |
| Acuerdo de encargo | NO EXIGIDO EXPRESAMENTE | No se exige acuerdo | ID_188_3.PDF | 43, 11.18 | Leído |
| Subencargados | NO EXIGIDO EXPRESAMENTE | No aplica | ID_188_3.PDF | 43, 11.18 | Leído |
| Cloud pública | Obligación contractual | Solo Azure, AWS, GCP; EEE | ID_188_3.PDF | 29-34, 7 | Leído |
| Localización de datos | Obligación contractual | Regiones EEE | ID_188_3.PDF | 33 | Leído |
| Transferencias internacionales | Prohibición | No fuera del EEE | ID_188_3.PDF | 33 | Leído |
| Análisis de riesgos | Obligación contractual | Al inicio, validación por Ayuntamiento | ID_188_3.PDF | 46, 11.3 | Leído |
| Configuración segura | Obligación contractual | Guías CCN-STIC | ID_188_3.PDF | 46-47, 11.4 | Leído |
| Desarrollo seguro | Obligación contractual | Buenas prácticas verificables | ID_188_3.PDF | 47, 11.5 | Leído |
| Cifrado | Obligación contractual | Información no pública en tránsito | ID_188_3.PDF | 47, 11.6 | Leído |
| Identidad/acceso | Obligación contractual | Identidad corporativa/CL@VE | ID_188_3.PDF | 47-48, 11.7 | Leído |
| Doble factor | Obligación contractual | Si aplica, medios a cargo adjudicatario | ID_188_3.PDF | 48, 11.8 | Leído |
| Acceso remoto | Obligación contractual | Servicio acceso remoto Ayuntamiento | ID_188_3.PDF | 48, 11.9 | Leído |
| Control de acceso | Obligación contractual | Mínimo privilegio, necesidad de conocer | ID_188_3.PDF | 48, 11.10 | Leído |
| Logging | Obligación contractual | Registro de actividad, entrega a requerimiento | ID_188_3.PDF | 49, 11.12 | Leído |
| Vulnerabilidades | Obligación contractual | Subsanación a requerimiento | ID_188_3.PDF | 49, 11.15 | Leído |
| Parcheado | Obligación contractual | Actualizaciones periódicas | ID_188_3.PDF | 30, 11.13 | Leído |
| Incidentes | Obligación contractual | Notificación inmediata al responsable | ID_188_3.PDF | 49, 11.14 | Leído |
| Auditorías | Obligación contractual | El Ayuntamiento puede auditar | ID_188_3.PDF | 49, 11.16 | Leído |
| Borrado seguro | Obligación contractual | Certificado de destrucción al cierre | ID_188_3.PDF | 9, 3.2 | Leído |
| Confidencialidad | Obligación contractual | Durante y tras el contrato | ID_188_3.PDF | 53, 15 | Leído |
| RTO/RPO | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |
| SOC/SIEM | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |
| EIPD | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |
| SBOM, SAST, DAST, SCA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |

# Discrepancias y pendientes de aclaración
- No se han identificado discrepancias en la documentación revisada.
- Documento 147409-2026 pendiente de lectura/OCR; no se ha podido verificar si contiene requisitos adicionales.