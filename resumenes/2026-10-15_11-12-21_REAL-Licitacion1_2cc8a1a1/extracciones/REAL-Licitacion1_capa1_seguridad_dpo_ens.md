# 1. Resumen factual Seguridad / DPO / ENS

**Seguridad y ENS:**
- El contrato exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para todos los servicios y sistemas desarrollados/desplegados/mantenidos, conforme a la guía CCN-STIC-803 y el RD 311/2022. Se requiere análisis de riesgos, plan de tratamiento, configuración segura según guías CCN-STIC, desarrollo seguro, cifrado de información no pública en tránsito, identificación y autenticación conforme a normativa municipal (delegación en plataformas corporativas), control de acceso por mínimo privilegio y necesidad de conocer, logging de actividad, gestión de vulnerabilidades y actualizaciones, gestión de incidentes según CCN-STIC-817, auditorías de seguridad por el Ayuntamiento, y designación de un Punto de Contacto (POC) para seguridad.

**Protección de datos/DPO:**
- El pliego indica expresamente que el contrato NO requiere tratamiento de datos personales por cuenta del responsable (Ayuntamiento), por lo que no se exige acuerdo de encargo de tratamiento ni cláusulas de protección de datos en los términos de la LOPDGDD/RGPD. El responsable del tratamiento de los datos de contratación es la Dirección General de Contratación y Servicios. Se identifica el DPD del Ayuntamiento, pero no se exige DPO/DPD al adjudicatario.

**Subencargados, cloud, localización y transferencias:**
- El despliegue debe realizarse exclusivamente en cloud pública (Azure, AWS, GCP) del Ayuntamiento, en regiones del Espacio Económico Europeo (EEE), prohibiéndose otros proveedores y localizaciones fuera del EEE. El adjudicatario debe informar sobre subcontratistas y cambios, y cumplir las políticas de privacidad y seguridad del Ayuntamiento. No se admiten transferencias internacionales fuera del EEE.

**Medidas técnicas:**
- Se exige configuración segura, cifrado de información no pública en tránsito, autenticación delegada en sistemas corporativos, control de acceso por mínimo privilegio, logging, actualización y parcheo, gestión de vulnerabilidades, desarrollo seguro, integración con monitorización corporativa, y entrega de logs a requerimiento. No se exige expresamente MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, SIEM, DLP, ni se especifican RTO/RPO.

**Identidad, accesos y privilegios:**
- Gestión de credenciales y accesos por el Ayuntamiento. Acceso de usuarios externos mediante credenciales IAM. Acceso a información no pública requiere autenticación conforme a normativa municipal. Principios de mínimo privilegio y necesidad de conocer. Prohibido acceso administrativo innecesario.

**Vulnerabilidades, parcheado y desarrollo seguro:**
- Obligación de subsanar vulnerabilidades notificadas por el Ayuntamiento. Aplicación diligente de actualizaciones de seguridad. Desarrollo seguro y orientado a la privacidad, con documentación de prácticas empleadas.

**Incidentes y brechas:**
- Gestión de ciberincidentes conforme a CCN-STIC-817. Notificación inmediata al responsable del contrato de cualquier incidente que afecte a información o servicios del Ayuntamiento, manteniendo informado hasta el cierre. Colaboración activa en la resolución.

**Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención:**
- Registro de actividad de usuarios, entrega de logs a requerimiento. Integración con herramientas de observabilidad y monitorización de IAM si se solicita. Copias de seguridad y restauración proporcionadas por IAM. No se especifican SOC/SIEM, RTO/RPO ni retención concreta.

**Auditorías, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad:**
- El Ayuntamiento puede auditar la seguridad de los sistemas. Borrado seguro de datos al finalizar el contrato, con certificado de destrucción. Confidencialidad obligatoria durante y después del contrato. No se exige certificación ISO/ENS ni formación/certificación específica del personal en seguridad.

**Consecuencias contractuales:**
- Incumplimientos graves y muy graves en materia de seguridad, confidencialidad, destrucción de datos, etc., conllevan penalidades del 5% o 10% del precio del contrato, y pueden ser causa de resolución.

**Datos no localizados o ambiguos:**
- No consta exigencia de ISO 27001, MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, SIEM, DLP, RTO/RPO, ni requisitos de SBOM, SAST, DAST, SCA, ni plazos de retención/logs. No se exige DPO/DPD al adjudicatario ni acuerdo de encargado/subencargado. No se detallan medidas específicas de backup ni continuidad más allá de lo indicado.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
| Requisito ENS | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente |
|----------------|----------------|---------|--------------|---------|--------|
| Cumplimiento ENS | Básico | Todos los servicios y sistemas desarrollados/desplegados/mantenidos | Descripción de mecanismos de seguridad en la oferta; análisis de riesgos; plan de tratamiento; configuración segura; documentación de prácticas | Oferta y durante ejecución | ID_188_3.PDF, pág. 45-46, 11.1-11.5 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|----------------------|-----------|------------------|--------|
| No se requiere tratamiento de datos personales por cuenta del responsable | Contrato no implica encargo de tratamiento | No aplica | ID_188_3.PDF, pág. 50, 11.18 |
| Responsable del tratamiento de datos de contratación: Dirección General de Contratación y Servicios | Solo para datos de contratación | Conservación mientras sean necesarios para la ejecución del contrato | ID_188_2.PDF, Anexo IX |
| DPD del Ayuntamiento identificado | No se exige DPO/DPD al adjudicatario | No aplica | ID_188_2.PDF, Anexo IX |

# 4. Subencargados, cloud, localización y transferencias
| Requisito | Condición | Fuente |
|-----------|-----------|--------|
| Despliegue en cloud pública del Ayuntamiento (Azure, AWS, GCP) | Solo en regiones EEE; prohibido fuera del EEE | ID_188_3.PDF, pág. 29-34, 7 |
| Subcontratistas: informar sobre su participación y cambios | Obligación de informar y cumplir límites de subcontratación | ID_188_3.PDF, pág. 29, 6.5 |
| Transferencias internacionales fuera del EEE | Prohibidas | ID_188_3.PDF, pág. 30, 7 |

# 5. Medidas técnicas
| Medida | Obligatoria/valorable/condicionada | Parámetro/plazo | Fuente |
|--------|-----------------------------------|------------------|--------|
| Configuración segura según guías CCN-STIC | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 46, 11.4 |
| Cifrado de información no pública en tránsito | Obligatoria si la información no es pública | Durante ejecución | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación conforme a normativa municipal | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 47, 11.7 |
| Control de acceso por mínimo privilegio y necesidad de conocer | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48, 11.10 |
| Logging de actividad de usuarios | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49, 11.12 |
| Actualización y parcheo de seguridad | Obligatoria | Periódica y continuada | ID_188_3.PDF, pág. 49, 11.13 |
| Gestión de vulnerabilidades | Obligatoria | Subsanar vulnerabilidades notificadas | ID_188_3.PDF, pág. 49, 11.15 |
| Desarrollo seguro y orientado a la privacidad | Obligatoria si hay desarrollo | Durante ejecución | ID_188_3.PDF, pág. 47, 11.5 |
| Integración con monitorización corporativa | Obligatoria si lo solicita IAM | Durante ejecución | ID_188_3.PDF, pág. 31, 7 |
| Entrega de logs a requerimiento | Obligatoria | A requerimiento | ID_188_3.PDF, pág. 49, 11.12 |

# 6. Identidad, accesos y privilegios
- Gestión de credenciales y accesos por el Ayuntamiento. Acceso de usuarios externos mediante credenciales IAM. Acceso a información no pública requiere autenticación conforme a normativa municipal. Principios de mínimo privilegio y necesidad de conocer. Prohibido acceso administrativo innecesario. (ID_188_3.PDF, pág. 33-34, 7)

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- Obligación de subsanar vulnerabilidades notificadas por el Ayuntamiento. Aplicación diligente de actualizaciones de seguridad. Desarrollo seguro y orientado a la privacidad, con documentación de prácticas empleadas. (ID_188_3.PDF, pág. 47, 11.5; pág. 49, 11.13, 11.15)

# 8. Incidentes, brechas y plazos de notificación expresamente indicados
- Gestión de ciberincidentes conforme a CCN-STIC-817. Notificación inmediata al responsable del contrato de cualquier incidente que afecte a información o servicios del Ayuntamiento, manteniendo informado hasta el cierre. Colaboración activa en la resolución. (ID_188_3.PDF, pág. 49, 11.14)

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención
- Registro de actividad de usuarios, entrega de logs a requerimiento. Integración con herramientas de observabilidad y monitorización de IAM si se solicita. Copias de seguridad y restauración proporcionadas por IAM. No se especifican SOC/SIEM, RTO/RPO ni retención concreta. (ID_188_3.PDF, pág. 31, 7; pág. 49, 11.12)

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- El Ayuntamiento puede auditar la seguridad de los sistemas. Borrado seguro de datos al finalizar el contrato, con certificado de destrucción. Confidencialidad obligatoria durante y después del contrato. No se exige certificación ISO/ENS ni formación/certificación específica del personal en seguridad. (ID_188_3.PDF, pág. 49, 11.16; pág. 9, 3.2; pág. 53, 15)

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Incumplimientos graves y muy graves en materia de seguridad, confidencialidad, destrucción de datos, etc., conllevan penalidades del 5% o 10% del precio del contrato, y pueden ser causa de resolución. (ID_188_2.PDF, pág. 75-77, 30)

# 12. Datos no localizados o ambiguos
- No consta exigencia de ISO 27001, MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, SIEM, DLP, RTO/RPO, ni requisitos de SBOM, SAST, DAST, SCA, ni plazos de retención/logs. No se exige DPO/DPD al adjudicatario ni acuerdo de encargado/subencargado. No se detallan medidas específicas de backup ni continuidad más allá de lo indicado.

# 13. Documentos revisados
1. ID_188_1.PDF
2. ID_188_2.PDF
3. ID_188_3.PDF
4. poc (enlazado desde ID_188_1.PDF)
5. poc (enlazado desde ID_188_1.PDF)
6. poc (enlazado desde ID_188_1.PDF)
7. 147409-2026 (Sin texto extraíble; pendiente de lectura/OCR)
8. perfilContratante (enlazado desde ID_188_2.PDF)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|----------------|-----------|-----------------|------------------|
| ENS | Obligatorio | Nivel Básico, servicios y sistemas desarrollados/desplegados/mantenidos | ID_188_3.PDF | 45-46, 11.1-11.5 | Leído |
| Análisis de riesgos ENS | Obligatorio | Al inicio de los trabajos, validado por el Ayuntamiento | ID_188_3.PDF | 46, 11.3 | Leído |
| Configuración segura CCN-STIC | Obligatorio | Durante ejecución | ID_188_3.PDF | 46, 11.4 | Leído |
| Desarrollo seguro | Obligatorio | Si hay desarrollo, durante ejecución | ID_188_3.PDF | 47, 11.5 | Leído |
| Cifrado información no pública | Obligatorio | En tránsito, si la información no es pública | ID_188_3.PDF | 47, 11.6 | Leído |
| Identificación/autenticación | Obligatorio | Conforme a normativa municipal | ID_188_3.PDF | 47, 11.7 | Leído |
| Control de acceso mínimo privilegio | Obligatorio | Durante ejecución | ID_188_3.PDF | 48, 11.10 | Leído |
| Logging de actividad | Obligatorio | Durante ejecución | ID_188_3.PDF | 49, 11.12 | Leído |
| Actualizaciones/parcheo | Obligatorio | Periódica y continuada | ID_188_3.PDF | 49, 11.13 | Leído |
| Gestión de vulnerabilidades | Obligatorio | Subsanar vulnerabilidades notificadas | ID_188_3.PDF | 49, 11.15 | Leído |
| Gestión de incidentes | Obligatorio | Notificación inmediata, colaboración activa | ID_188_3.PDF | 49, 11.14 | Leído |
| Auditoría de seguridad | Derecho del cliente | El Ayuntamiento puede auditar | ID_188_3.PDF | 49, 11.16 | Leído |
| Borrado seguro y certificado | Obligatorio | Al finalizar el contrato | ID_188_3.PDF | 9, 3.2 | Leído |
| Confidencialidad | Obligatorio | Durante y después del contrato | ID_188_3.PDF | 53, 15 | Leído |
| Cloud pública EEE | Obligatorio | Solo Azure, AWS, GCP, en EEE | ID_188_3.PDF | 29-34, 7 | Leído |
| Subcontratistas | Obligatorio | Informar sobre participación y cambios | ID_188_3.PDF | 29, 6.5 | Leído |
| Penalidades por incumplimiento | Consecuencia | 5% o 10% del precio del contrato | ID_188_2.PDF | 75-77, 30 | Leído |
| RGPD/LOPDGDD | No exigido | No se requiere encargo de tratamiento | ID_188_3.PDF | 50, 11.18 | Leído |
| DPO/DPD adjudicatario | No exigido | No se exige | ID_188_2.PDF | Anexo IX | Leído |
| ISO 27001 | No exigido | No se exige | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - |
| MFA, RBAC, PAM, VPN, bastionado, EDR/XDR, WAF, SIEM, DLP, RTO/RPO, SBOM, SAST, DAST, SCA | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |

# Discrepancias y pendientes de aclaración
- Documento 147409-2026: Sin texto extraíble; pendiente de lectura/OCR. No se ha podido verificar si contiene requisitos adicionales o contradictorios.
- No se han identificado discrepancias internas en los documentos revisados.