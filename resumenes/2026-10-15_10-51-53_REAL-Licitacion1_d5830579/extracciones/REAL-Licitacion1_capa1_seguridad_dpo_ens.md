# 1. Resumen factual Seguridad / DPO / ENS

- El contrato exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para todos los servicios y sistemas objeto del contrato, con medidas de seguridad del Anexo II del ENS y guías CCN-STIC aplicables. No se exige certificación ENS ni ISO 27001, solo cumplimiento y supervisión por el órgano de contratación.
- No se exige tratamiento de datos personales por cuenta del responsable ni cesión de datos personales del Ayuntamiento al adjudicatario. El adjudicatario no asume el rol de encargado de tratamiento ni se requiere acuerdo de encargo de tratamiento.
- Se exige despliegue en cloud pública (Azure, AWS, GCP) en regiones del Espacio Económico Europeo (EEE), bajo el modelo de gobierno cloud del Ayuntamiento de Madrid, con control de acceso, seguridad, monitorización, logs, y cumplimiento de políticas de IAM y Centro de Ciberseguridad municipal.
- Se establecen medidas técnicas obligatorias: análisis de riesgos ENS, configuración segura CCN-STIC, cifrado de información no pública en tránsito, identificación y autenticación conforme a ENS, control de acceso de mínimo privilegio y necesidad de conocer, logging de actividad, actualización de seguridad, gestión de incidentes y vulnerabilidades, desarrollo seguro, supervisión humana de IA, y borrado seguro con certificado al cierre.
- Se exige punto de contacto de seguridad, colaboración en auditorías, entrega de documentación técnica y logs, y cumplimiento de la política de seguridad municipal.
- No se exige DPO/DPD propio del adjudicatario ni se requiere EIPD.
- Consecuencias contractuales: penalidades económicas por incumplimientos graves y muy graves, resolución por reiteración, obligación de subsanar vulnerabilidades e incidentes, y entrega de logs y documentación a requerimiento.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
| Requisito ENS | Categoria/Nivel | Alcance | Acreditación | Momento | Fuente |
|----------------|----------------|---------|--------------|---------|--------|
| Cumplimiento ENS | Básico | Todos los servicios y sistemas objeto del contrato | Descripción de mecanismos de seguridad en la oferta; supervisión por órgano de contratación | Antes de la entrada en producción y durante la ejecución | ID_188_3.PDF, pág. 45-46, 11.1, 11.3, 11.4 |
| Análisis de riesgos ENS | Básico | Servicios digitales, desarrollo/mantenimiento SW, infraestructuras/plataformas | Análisis de riesgos validado por el Ayuntamiento | Inicio de los trabajos | ID_188_3.PDF, pág. 46, 11.3 |
| Configuración segura CCN-STIC | Básico | Todos los componentes tecnológicos | Configuración conforme a guías CCN-STIC, con aprobación del responsable del contrato | Antes de la entrada en producción y durante la ejecución | ID_188_3.PDF, pág. 46, 11.4 |
| Medidas de seguridad ENS Anexo II | Básico | Servicios y sistemas desarrollados/desplegados/mantenidos | Supervisión y comprobación por órgano de contratación | Durante la ejecución | ID_188_3.PDF, pág. 46, 11.1 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|----------------------|-----------|----------------|--------|
| Tratamiento de datos personales por cuenta del responsable | NO requerido: "en ningún momento se precisa por parte del adjudicatario la realización de ningún tratamiento de datos personales por cuenta de la Dirección General de Participación Ciudadana" | NO CONSTA | ID_188_3.PDF, pág. 50, 11.18 |
| Acuerdo de encargo de tratamiento | NO requerido | NO CONSTA | ID_188_3.PDF, pág. 50, 11.18 |
| DPO/DPD propio del adjudicatario | NO EXIGIDO EXPRESAMENTE | NO CONSTA | ID_188_3.PDF, pág. 50, 11.18 |
| EIPD | NO EXIGIDO EXPRESAMENTE | NO CONSTA | ID_188_3.PDF, pág. 50, 11.18 |

# 4. Subencargados, cloud, localización y transferencias: requisito | condición | fuente
| Requisito | Condición | Fuente |
|-----------|-----------|--------|
| Subcontratación/subencargados | Permitida, pero no para tareas críticas (fase de implantación y jefe/a de proyecto); debe informarse al órgano de contratación y cumplir límites del contrato | ID_188_3.PDF, pág. 29, 6.5; ID_188_2.PDF, pág. 74, 26 |
| Cloud pública | Solo Azure, AWS, GCP; recursos en regiones EEE; cumplimiento modelo de gobierno cloud municipal | ID_188_3.PDF, pág. 29-34, 7 |
| Localización de datos | Recursos desplegados en regiones del Espacio Económico Europeo (EEE) | ID_188_3.PDF, pág. 33, Organización de recursos |
| Transferencias internacionales | No permitidas fuera del EEE; cumplimiento art. 45 RGPD | ID_188_3.PDF, pág. 33, Organización de recursos |

# 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente
| Medida | Tipo | Parámetro/Plazo | Fuente |
|--------|------|----------------|--------|
| Análisis de riesgos ENS | Obligatoria | Al inicio de los trabajos | ID_188_3.PDF, pág. 46, 11.3 |
| Configuración segura CCN-STIC | Obligatoria | Antes de producción y durante ejecución | ID_188_3.PDF, pág. 46, 11.4 |
| Cifrado de información no pública en tránsito | Obligatoria | Según valoración del responsable de la información | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación conforme ENS | Obligatoria | Según normativa municipal | ID_188_3.PDF, pág. 47, 11.7 |
| Control de acceso mínimo privilegio/"necesidad de conocer" | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48, 11.10 |
| Logging de actividad | Obligatoria | Durante ejecución; entrega a requerimiento | ID_188_3.PDF, pág. 49, 11.12 |
| Actualizaciones de seguridad/parcheado | Obligatoria | Periódica y continuada | ID_188_3.PDF, pág. 49, 11.13 |
| Gestión de incidentes de seguridad | Obligatoria | Notificación inmediata al responsable del contrato | ID_188_3.PDF, pág. 49, 11.14 |
| Subsanación de vulnerabilidades | Obligatoria | A requerimiento | ID_188_3.PDF, pág. 49, 11.15 |
| Desarrollo seguro | Obligatoria | Metodologías y buenas prácticas verificables; documentar | ID_188_3.PDF, pág. 47, 11.5 |
| Supervisión humana de IA | Obligatoria | Durante uso del sistema | ID_188_3.PDF, pág. 39, Art. 6 |
| Borrado seguro y certificado | Obligatoria | Al cierre del contrato | ID_188_3.PDF, pág. 9, Fase II Operación |
| Punto de contacto de seguridad | Obligatoria | Designación al inicio | ID_188_3.PDF, pág. 46, 11.2 |
| Colaboración en auditorías | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49, 11.16 |

# 6. Identidad, accesos y privilegios
- Gestión de credenciales y accesos a recursos cloud es competencia del Ayuntamiento de Madrid; usuarios externos usan credenciales proporcionadas por IAM (ID_188_3.PDF, pág. 33).
- Identificación y autenticación: personal municipal mediante plataforma de identidad corporativa; ciudadanía mediante sistema estatal CL@VE; otros métodos requieren autorización de IAM (ID_188_3.PDF, pág. 47, 11.7).
- Control de acceso: mínimo privilegio y necesidad de conocer; solo personal competente puede autorizar accesos; restringir roles de administración (ID_188_3.PDF, pág. 48, 11.10).
- Compatibilidad con doble factor de autenticación municipal si es requerido (ID_188_3.PDF, pág. 48, 11.8).

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- El adjudicatario debe subsanar vulnerabilidades comunicadas por el responsable del contrato (ID_188_3.PDF, pág. 49, 11.15).
- Actualizaciones de seguridad: aplicación periódica y continuada de parches; medidas compensatorias si no es posible aplicar una actualización (ID_188_3.PDF, pág. 49, 11.13).
- Desarrollo seguro: uso de metodologías y buenas prácticas verificables en todo el ciclo de vida; documentar prácticas empleadas (ID_188_3.PDF, pág. 47, 11.5).

# 8. Incidentes, brechas y plazos de notificación expresamente indicados
- El adjudicatario es responsable de la gestión de ciberincidentes en todo su ciclo de vida (detección, registro, contención, mitigación, recuperación) conforme a la guía CCN-STIC-817 y normativa municipal (ID_188_3.PDF, pág. 49, 11.14).
- Notificación de incidentes: "tan pronto como tenga conocimiento del mismo" al responsable del contrato; mantener informado hasta el cierre del incidente (ID_188_3.PDF, pág. 49, 11.14).
- Colaboración activa en la resolución de incidentes durante ejecución y garantía (ID_188_3.PDF, pág. 49, 11.14).

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención
- Logging: registro de actividades de usuarios, retención durante la ejecución, entrega a requerimiento del responsable del contrato (ID_188_3.PDF, pág. 49, 11.12).
- Integración con herramientas de observabilidad y monitorización de IAM si se solicita (ID_188_3.PDF, pág. 31).
- Copias de seguridad y restauración: proporcionadas por IAM (ID_188_3.PDF, pág. 31).
- Continuidad, RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA.

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Auditorías de seguridad: el Ayuntamiento podrá realizarlas sobre los sistemas implantados o utilizados (ID_188_3.PDF, pág. 49, 11.16).
- Evidencias/certificados: entrega de logs, documentación técnica, y certificado de borrado seguro al cierre (ID_188_3.PDF, pág. 9, Fase II Operación).
- Certificaciones ENS/ISO: NO EXIGIDO EXPRESAMENTE; solo cumplimiento ENS nivel básico (ID_188_3.PDF, pág. 45-46).
- Seguridad del personal: obligación de proveer equipos de protección individual en situaciones excepcionales (ID_188_3.PDF, pág. 23, 6).
- Confidencialidad: obligación de confidencialidad y secreto sobre información y datos a los que se acceda, subsiste tras la finalización del contrato (ID_188_3.PDF, pág. 53, 15).

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Penalidades económicas por incumplimientos graves (5% del precio del contrato) y muy graves (10%), resolución por reiteración, obligación de subsanar vulnerabilidades e incidentes, y entrega de logs y documentación a requerimiento (ID_188_2.PDF, pág. 76-77, 30).

# 12. Datos no localizados o ambiguos, sin recomendaciones
- No se exige certificación ENS ni ISO 27001, solo cumplimiento.
- No se exige DPO/DPD propio del adjudicatario.
- No se exige EIPD.
- No se especifican RTO/RPO ni pruebas de continuidad.
- No se exige acuerdo de encargo de tratamiento ni subencargados de tratamiento.
- No se exige SOC/SIEM dedicado, solo integración con monitorización de IAM si se solicita.
- No se exige SBOM, SAST, DAST, SCA, ni requisitos DevSecOps específicos más allá de "buenas prácticas verificables".

# 13. Documentos revisados
1. ID_188_1.PDF (Documento licitación real)
2. ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares)
3. ID_188_3.PDF (Pliego de Prescripciones Técnicas)
4. poc (Documento enlazado, detalle licitación, texto extraído)
5. poc (Documento enlazado, perfil contratante, texto extraído)
6. poc (Documento enlazado, perfil contratante, texto extraído)
7. 147409-2026 (Documento enlazado, sin texto extraíble; pendiente de lectura/OCR)
8. perfilContratante (Documento enlazado, texto extraído)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|----------------|-----------|-----------------|------------------|
| Cumplimiento ENS | Obligación contractual | Nivel básico, Anexo II ENS, guías CCN-STIC | ID_188_3.PDF | 45-46, 11.1 | Leído |
| Certificación ENS/ISO | NO EXIGIDO EXPRESAMENTE | Solo cumplimiento ENS, no certificación | ID_188_3.PDF | 45-46 | Leído |
| Análisis de riesgos ENS | Obligación contractual | Al inicio, validado por Ayuntamiento | ID_188_3.PDF | 46, 11.3 | Leído |
| Configuración segura CCN-STIC | Obligación contractual | Antes de producción y durante ejecución | ID_188_3.PDF | 46, 11.4 | Leído |
| Cifrado información no pública | Obligación contractual | Según valoración responsable información | ID_188_3.PDF | 47, 11.6 | Leído |
| Identificación/autenticación ENS | Obligación contractual | Según normativa municipal | ID_188_3.PDF | 47, 11.7 | Leído |
| Control de acceso mínimo privilegio | Obligación contractual | Durante ejecución | ID_188_3.PDF | 48, 11.10 | Leído |
| Logging de actividad | Obligación contractual | Durante ejecución, entrega a requerimiento | ID_188_3.PDF | 49, 11.12 | Leído |
| Actualizaciones de seguridad | Obligación contractual | Periódica y continuada | ID_188_3.PDF | 49, 11.13 | Leído |
| Gestión de incidentes | Obligación contractual | Notificación inmediata, colaboración | ID_188_3.PDF | 49, 11.14 | Leído |
| Subsanación de vulnerabilidades | Obligación contractual | A requerimiento | ID_188_3.PDF | 49, 11.15 | Leído |
| Desarrollo seguro | Obligación contractual | Buenas prácticas verificables, documentar | ID_188_3.PDF | 47, 11.5 | Leído |
| Supervisión humana IA | Obligación contractual | Durante uso | ID_188_3.PDF | 39, Art. 6 | Leído |
| Borrado seguro/certificado | Obligación contractual | Al cierre del contrato | ID_188_3.PDF | 9, Fase II Operación | Leído |
| Punto de contacto de seguridad | Obligación contractual | Designación al inicio | ID_188_3.PDF | 46, 11.2 | Leído |
| Auditorías de seguridad | Derecho del Ayuntamiento | Durante ejecución | ID_188_3.PDF | 49, 11.16 | Leído |
| Subcontratación/subencargados | Permitida con límites | No para tareas críticas, informar | ID_188_3.PDF | 29, 6.5 | Leído |
| Cloud pública | Obligatoria | Azure, AWS, GCP, regiones EEE | ID_188_3.PDF | 29-34, 7 | Leído |
| Localización de datos | Obligatoria | Regiones EEE | ID_188_3.PDF | 33 | Leído |
| Transferencias internacionales | Prohibidas fuera EEE | Cumplimiento art. 45 RGPD | ID_188_3.PDF | 33 | Leído |
| DPO/DPD propio | NO EXIGIDO EXPRESAMENTE | No requerido | ID_188_3.PDF | 50, 11.18 | Leído |
| EIPD | NO EXIGIDO EXPRESAMENTE | No requerido | ID_188_3.PDF | 50, 11.18 | Leído |
| Acuerdo de encargo de tratamiento | NO EXIGIDO EXPRESAMENTE | No requerido | ID_188_3.PDF | 50, 11.18 | Leído |
| RTO/RPO, continuidad | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |
| SOC/SIEM dedicado | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |
| SBOM, SAST, DAST, SCA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |

# Discrepancias y pendientes de aclaración
- Documento 147409-2026: Sin texto extraíble; documento pendiente de lectura/OCR. No se ha podido verificar si contiene requisitos adicionales o contradictorios.
- No se han identificado discrepancias internas en la documentación revisada.