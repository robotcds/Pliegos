# 1. Resumen factual Seguridad / DPO / ENS

**ENS:**
- Se exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para los servicios y sistemas objeto del contrato, según valoración de la guía CCN-STIC-803. El adjudicatario debe aplicar las medidas del Anexo II del ENS nivel Básico. Se requiere designación de un Punto o Persona de Contacto (POC) para la seguridad de la información. Se exige análisis de riesgos conforme al ENS al inicio de los trabajos, validado por el Ayuntamiento, y elaboración de un plan de tratamiento del riesgo. Todos los componentes tecnológicos deben configurarse según guías CCN-STIC. El desarrollo debe seguir buenas prácticas de desarrollo seguro. Se exige cifrado de información no pública en tránsito por redes ajenas al Ayuntamiento, según valoración del responsable. Se requiere registro de actividad de usuarios y entrega de logs a requerimiento. El adjudicatario debe aplicar actualizaciones de seguridad periódicamente y subsanar vulnerabilidades comunicadas por el responsable del contrato. El Ayuntamiento podrá auditar la seguridad de los sistemas. El adjudicatario debe notificar incidentes de seguridad al responsable del contrato tan pronto como tenga conocimiento y colaborar en la resolución. (ID_188_3.PDF, págs. 45-50)

**RGPD/DPO:**
- El contrato indica expresamente que no se precisa tratamiento de datos personales por cuenta del responsable (Dirección General de Participación Ciudadana) por parte del adjudicatario, por lo que no se exige acuerdo de encargo de tratamiento ni se define rol de encargado. No obstante, se prevé anonimización de datos personales que los usuarios puedan incluir voluntariamente en sus consultas al asistente virtual. (ID_188_3.PDF, pág. 46, 50)
- El Anexo IX del pliego administrativo describe el tratamiento de datos personales para la gestión contractual, siendo responsable la Dirección General de Contratación y Servicios. Se identifican categorías de datos: identificación, claves, direcciones, información comercial y económica. Conservación: mientras sean necesarios para la ejecución del contrato. Derechos: acceso, rectificación, supresión, limitación, oposición. (ID_188_2.PDF, Anexo IX, pág. 95)
- Se identifica Delegado de Protección de Datos (DPD) del Ayuntamiento de Madrid, pero no se exige DPO/DPD al adjudicatario. (ID_188_2.PDF, Anexo IX, pág. 95)

**Subencargados, cloud, localización y transferencias:**
- Solo se permite despliegue en cloud pública de Microsoft Azure, Google Cloud Platform o Amazon AWS, en regiones del Espacio Económico Europeo (EEE). No se admiten otros proveedores. El adjudicatario debe garantizar que los recursos estén localizados en el EEE y cumplir el art. 45 RGPD sobre transferencias basadas en decisión de adecuación. (ID_188_3.PDF, pág. 29-34)
- El adjudicatario debe informar sobre subcontratación y cambios durante el contrato. La subcontratación está permitida salvo para tareas críticas. (ID_188_3.PDF, pág. 29)

**Medidas técnicas:**
- Se exige configuración segura conforme a guías CCN-STIC. Se requiere cifrado de información no pública en tránsito por redes ajenas. Identificación y autenticación: personal municipal mediante plataforma de identidad corporativa, ciudadanía mediante sistema estatal Cl@ve, otros métodos requieren autorización. Acceso remoto solo mediante servicio de acceso remoto para empresas del Ayuntamiento. Principios de mínimo privilegio y necesidad de conocer. Restricción de roles de administración. Registro de actividad de usuarios. Aplicación de actualizaciones de seguridad periódicas. Subsanación de vulnerabilidades comunicadas. (ID_188_3.PDF, págs. 45-49)
- El adjudicatario debe colaborar en integración con monitorización corporativa, EDR/XDR, antivirus y backup proporcionados por IAM. (ID_188_3.PDF, pág. 31)
- Desarrollo seguro: se exige seguir metodologías y buenas prácticas verificables de desarrollo seguro en todo el ciclo de vida. (ID_188_3.PDF, pág. 47)

**Identidad, accesos y privilegios:**
- Gestión de credenciales y accesos a recursos cloud es competencia del Ayuntamiento. Usuarios externos usan credenciales proporcionadas por IAM. No se permite asignación de IP pública a máquinas virtuales. Acceso a la red corporativa solo mediante mecanismos autorizados. (ID_188_3.PDF, pág. 33-34, 47-48)

**Vulnerabilidades, parcheado y desarrollo seguro:**
- El adjudicatario debe aplicar actualizaciones de seguridad periódicamente y subsanar vulnerabilidades comunicadas. Desarrollo seguro obligatorio en todo el ciclo de vida. (ID_188_3.PDF, pág. 47, 49)

**Incidentes, brechas y plazos de notificación:**
- El adjudicatario debe notificar cualquier ciberincidente que pueda afectar a información o servicios del Ayuntamiento al responsable del contrato tan pronto como tenga conocimiento y mantenerle informado hasta el cierre del incidente. Debe colaborar activamente en la resolución. (ID_188_3.PDF, pág. 49)

**Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención:**
- Se exige registro de actividad de usuarios, retención de logs para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas. Entrega de logs a requerimiento. Integración con herramientas de observabilidad y monitorización de IAM si se solicita. Backup y restauración proporcionados por IAM. No se especifican RTO/RPO. (ID_188_3.PDF, pág. 31, 49)

**Auditorías, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad:**
- El Ayuntamiento podrá auditar la seguridad de los sistemas. El adjudicatario debe eliminar de forma segura toda la información del servicio a la finalización del contrato y aportar certificado de destrucción. Confidencialidad: obligación de guardar secreto sobre información y datos a los que tenga acceso, subsistiendo tras la finalización del contrato. (ID_188_3.PDF, pág. 9, 15, 53)
- Se exige designación de POC de seguridad, pero no DPO/DPD al adjudicatario. (ID_188_3.PDF, pág. 46)

**Consecuencias contractuales expresamente asociadas al incumplimiento:**
- Incumplimiento de obligaciones de seguridad, confidencialidad, plazos de implantación, indisponibilidad del servicio, etc., conlleva penalidades económicas (5% o 10% del precio del contrato según gravedad) y puede ser causa de resolución. (ID_188_2.PDF, pág. 75-77)

**Datos no localizados o ambiguos:**
- No se exige certificación ENS ni ISO 27001, solo cumplimiento material del ENS nivel básico. No se especifican medidas técnicas concretas como MFA, PAM, VPN, segmentación, DLP, WAF, SIEM, SAST, DAST, SCA, SBOM, ni parámetros de RTO/RPO. No se exige DPO/DPD al adjudicatario. No se define rol de encargado de tratamiento para el adjudicatario. No se exige acuerdo de encargo de tratamiento. No se detallan plazos de retención de logs ni de conservación de backups. No se exige plan de continuidad ni DR específico. No se exige auditoría ENS ni ISO periódica.

**Documentos revisados:**
- ID_188_1.PDF (Documento licitación real)
- ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares y Anexos)
- ID_188_3.PDF (Pliego de Prescripciones Técnicas)

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
| Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente |
|---|---|---|---|---|---|
| Cumplimiento ENS | Básico | Servicios y sistemas objeto del contrato | Descripción de mecanismos de seguridad en la oferta | Presentación de oferta | ID_188_3.PDF, pág. 46 |
| Análisis de riesgos ENS | Básico | Servicios prestados/sistemas desarrollados | Análisis de riesgos validado por el Ayuntamiento | Inicio de los trabajos | ID_188_3.PDF, pág. 46 |
| Designación POC seguridad | Básico | Seguridad de la información tratada y servicio prestado | Designación de POC o justificación de no designación | Inicio de ejecución | ID_188_3.PDF, pág. 46 |
| Configuración segura CCN-STIC | Básico | Todos los componentes tecnológicos | Configuración conforme a guías CCN-STIC | Ejecución | ID_188_3.PDF, pág. 47 |
| Desarrollo seguro | Básico | Software desarrollado/mantenido | Metodologías y buenas prácticas verificables | Ejecución | ID_188_3.PDF, pág. 47 |
| Registro de actividad | Básico | Sistemas objeto del contrato | Entrega de logs a requerimiento | Ejecución | ID_188_3.PDF, pág. 49 |
| Actualizaciones de seguridad | Básico | Sistemas objeto del contrato | Aplicación periódica y continuada | Ejecución | ID_188_3.PDF, pág. 49 |
| Subsanación de vulnerabilidades | Básico | Sistemas objeto del contrato | Subsanación a requerimiento | Ejecución | ID_188_3.PDF, pág. 49 |
| Auditoría de seguridad | Básico | Sistemas implantados/utilizados | Auditoría por el Ayuntamiento | Ejecución | ID_188_3.PDF, pág. 49 |
| Notificación de incidentes | Básico | Servicios/sistemas objeto del contrato | Notificación inmediata al responsable del contrato | Ejecución | ID_188_3.PDF, pág. 49 |
| Borrado seguro y certificado | Básico | Todos los sistemas de la solución | Certificado de destrucción | Cierre del contrato | ID_188_3.PDF, pág. 9 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
| Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente |
|---|---|---|---|
| No se precisa tratamiento de datos personales por cuenta del responsable | Contrato no requiere encargo de tratamiento | NO APLICA | ID_188_3.PDF, pág. 50 |
| Anonimización de datos personales incluidos voluntariamente por usuarios | Obligación de anonimizar | NO ESPECIFICADO | ID_188_3.PDF, pág. 46 |
| Tratamiento de datos personales para gestión contractual (Dirección General de Contratación y Servicios) | Responsable: Ayuntamiento de Madrid | Mientras sean necesarios para la ejecución del contrato | ID_188_2.PDF, Anexo IX, pág. 95 |
| Delegado de Protección de Datos del Ayuntamiento de Madrid | DPD identificado para el Ayuntamiento | NO ESPECIFICADO | ID_188_2.PDF, Anexo IX, pág. 95 |

# 4. Subencargados, cloud, localización y transferencias: requisito | condicion | fuente
| Requisito | Condición | Fuente |
|---|---|---|
| Despliegue solo en cloud pública Microsoft Azure, Google Cloud Platform o Amazon AWS | Solo en regiones del EEE | ID_188_3.PDF, pág. 29-34 |
| Subcontratación permitida salvo tareas críticas | Debe informar sobre subcontratistas y cambios | ID_188_3.PDF, pág. 29 |
| Transferencias internacionales | Solo permitidas si la región está en el EEE (art. 45 RGPD) | ID_188_3.PDF, pág. 30, 34 |

# 5. Medidas tecnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente
| Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente |
|---|---|---|---|
| Configuración segura CCN-STIC | Obligatoria | Ejecución | ID_188_3.PDF, pág. 47 |
| Cifrado de información no pública en tránsito | Obligatoria si la información no es pública | Según valoración del responsable | ID_188_3.PDF, pág. 47 |
| Identificación y autenticación | Obligatoria | Personal municipal: identidad corporativa; ciudadanía: Cl@ve; otros: autorización | ID_188_3.PDF, pág. 47 |
| Acceso remoto | Obligatoria | Solo mediante servicio de acceso remoto para empresas | ID_188_3.PDF, pág. 48 |
| Principio de mínimo privilegio y necesidad de conocer | Obligatoria | Ejecución | ID_188_3.PDF, pág. 48 |
| Restricción de roles de administración | Obligatoria | Ejecución | ID_188_3.PDF, pág. 48 |
| Registro de actividad de usuarios | Obligatoria | Entrega de logs a requerimiento | ID_188_3.PDF, pág. 49 |
| Aplicación de actualizaciones de seguridad | Obligatoria | Periódica y continuada | ID_188_3.PDF, pág. 49 |
| Subsanación de vulnerabilidades | Obligatoria | A requerimiento | ID_188_3.PDF, pág. 49 |
| Integración con monitorización, EDR/XDR, antivirus, backup de IAM | Obligatoria si lo solicita IAM | Ejecución | ID_188_3.PDF, pág. 31 |
| Desarrollo seguro | Obligatoria | Todo el ciclo de vida | ID_188_3.PDF, pág. 47 |

# 6. Identidad, accesos y privilegios
- Gestión de credenciales y accesos a recursos cloud es competencia del Ayuntamiento. Usuarios externos usan credenciales proporcionadas por IAM. No se permite asignación de IP pública a máquinas virtuales. Acceso a la red corporativa solo mediante mecanismos autorizados. (ID_188_3.PDF, pág. 33-34, 47-48)

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- El adjudicatario debe aplicar actualizaciones de seguridad periódicamente y subsanar vulnerabilidades comunicadas. Desarrollo seguro obligatorio en todo el ciclo de vida. (ID_188_3.PDF, pág. 47, 49)

# 8. Incidentes, brechas y plazos de notificación expresamente indicados
- El adjudicatario debe notificar cualquier ciberincidente que pueda afectar a información o servicios del Ayuntamiento al responsable del contrato tan pronto como tenga conocimiento y mantenerle informado hasta el cierre del incidente. Debe colaborar activamente en la resolución. (ID_188_3.PDF, pág. 49)

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retencion
- Se exige registro de actividad de usuarios, retención de logs para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas. Entrega de logs a requerimiento. Integración con herramientas de observabilidad y monitorización de IAM si se solicita. Backup y restauración proporcionados por IAM. No se especifican RTO/RPO. (ID_188_3.PDF, pág. 31, 49)

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- El Ayuntamiento podrá auditar la seguridad de los sistemas. El adjudicatario debe eliminar de forma segura toda la información del servicio a la finalización del contrato y aportar certificado de destrucción. Confidencialidad: obligación de guardar secreto sobre información y datos a los que tenga acceso, subsistiendo tras la finalización del contrato. (ID_188_3.PDF, pág. 9, 15, 53)
- Se exige designación de POC de seguridad, pero no DPO/DPD al adjudicatario. (ID_188_3.PDF, pág. 46)

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Incumplimiento de obligaciones de seguridad, confidencialidad, plazos de implantación, indisponibilidad del servicio, etc., conlleva penalidades económicas (5% o 10% del precio del contrato según gravedad) y puede ser causa de resolución. (ID_188_2.PDF, pág. 75-77)

# 12. Datos no localizados o ambiguos, sin recomendaciones
- No se exige certificación ENS ni ISO 27001, solo cumplimiento material del ENS nivel básico. No se especifican medidas técnicas concretas como MFA, PAM, VPN, segmentación, DLP, WAF, SIEM, SAST, DAST, SCA, SBOM, ni parámetros de RTO/RPO. No se exige DPO/DPD al adjudicatario. No se define rol de encargado de tratamiento para el adjudicatario. No se exige acuerdo de encargo de tratamiento. No se detallan plazos de retención de logs ni de conservación de backups. No se exige plan de continuidad ni DR específico. No se exige auditoría ENS ni ISO periódica.

# 13. Documentos revisados
- ID_188_1.PDF (Documento licitación real)
- ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares y Anexos)
- ID_188_3.PDF (Pliego de Prescripciones Técnicas)

# Registro documental de preventa
| Materia | Requisito completo | Fuente |
|---|---|---|
| Seguridad e IA | El adjudicatario debe cumplir el ENS nivel básico para todos los servicios y sistemas objeto del contrato, aplicando las medidas del Anexo II del ENS nivel Básico. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | El adjudicatario debe designar un Punto o Persona de Contacto (POC) para la seguridad de la información tratada y el servicio prestado, o justificar su no designación. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | El adjudicatario debe realizar un análisis de riesgos conforme al ENS al inicio de los trabajos, validado por el Ayuntamiento, y elaborar un plan de tratamiento del riesgo. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | Todos los componentes tecnológicos deben configurarse conforme a las guías CCN-STIC del CCN-CERT, adaptadas a las particularidades del Ayuntamiento. | ID_188_3.PDF, pág. 47 |
| Seguridad e IA | El adjudicatario debe seguir metodologías y buenas prácticas verificables de desarrollo seguro de software en todo el ciclo de vida del proyecto. | ID_188_3.PDF, pág. 47 |
| Seguridad e IA | La información propiedad del Ayuntamiento que no sea pública debe ser cifrada cuando se transmita a través de redes ajenas al Ayuntamiento, según valoración del responsable. | ID_188_3.PDF, pág. 47 |
| Seguridad e IA | Identificación y autenticación: personal municipal mediante plataforma de identidad corporativa, ciudadanía mediante sistema estatal Cl@ve, otros métodos requieren autorización. | ID_188_3.PDF, pág. 47 |
| Seguridad e IA | Acceso remoto solo mediante servicio de acceso remoto para empresas del Ayuntamiento. | ID_188_3.PDF, pág. 48 |
| Seguridad e IA | Principios de mínimo privilegio y necesidad de conocer para el acceso a los sistemas. | ID_188_3.PDF, pág. 48 |
| Seguridad e IA | Restricción al mínimo imprescindible de roles con privilegios especiales de administración. | ID_188_3.PDF, pág. 48 |
| Seguridad e IA | El sistema debe registrar las actividades de los usuarios, reteniendo la información necesaria para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas, permitiendo identificar en cada momento a la persona que actúa. | ID_188_3.PDF, pág. 49 |
| Seguridad e IA | El adjudicatario debe aplicar actualizaciones de seguridad periódicamente y subsanar vulnerabilidades comunicadas por el responsable del contrato. | ID_188_3.PDF, pág. 49 |
| Seguridad e IA | El Ayuntamiento podrá auditar la seguridad de los sistemas de información y comunicaciones implantados o utilizados en el ámbito del contrato. | ID_188_3.PDF, pág. 49 |
| Seguridad e IA | El adjudicatario debe notificar cualquier ciberincidente que pueda afectar a información o servicios del Ayuntamiento al responsable del contrato tan pronto como tenga conocimiento y mantenerle informado hasta el cierre del incidente. | ID_188_3.PDF, pág. 49 |
| Seguridad e IA | El adjudicatario debe eliminar de forma segura toda la información del servicio a la finalización del contrato y aportar certificado de destrucción. | ID_188_3.PDF, pág. 9 |
| Seguridad e IA | El adjudicatario debe colaborar en la integración con monitorización corporativa, EDR/XDR, antivirus y backup proporcionados por IAM si así se solicita. | ID_188_3.PDF, pág. 31 |
| Seguridad e IA | Gestión de credenciales y accesos a recursos cloud es competencia del Ayuntamiento. Usuarios externos usan credenciales proporcionadas por IAM. No se permite asignación de IP pública a máquinas virtuales. | ID_188_3.PDF, pág. 33-34 |
| Seguridad e IA | Solo se permite despliegue en cloud pública de Microsoft Azure, Google Cloud Platform o Amazon AWS, en regiones del Espacio Económico Europeo (EEE). | ID_188_3.PDF, pág. 29-34 |
| Seguridad e IA | El adjudicatario debe informar sobre subcontratación y cambios durante el contrato. La subcontratación está permitida salvo para tareas críticas. | ID_188_3.PDF, pág. 29 |
| Seguridad e IA | Transferencias internacionales solo permitidas si la región está en el EEE (art. 45 RGPD). | ID_188_3.PDF, pág. 30, 34 |
| Seguridad e IA | El adjudicatario debe anonimizar datos personales que los usuarios puedan incluir voluntariamente en sus consultas al asistente virtual. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | El Ayuntamiento podrá auditar la seguridad de los sistemas. | ID_188_3.PDF, pág. 49 |
| Seguridad e IA | Confidencialidad: obligación de guardar secreto sobre información y datos a los que tenga acceso, subsistiendo tras la finalización del contrato. | ID_188_3.PDF, pág. 53 |
| Seguridad e IA | Incumplimiento de obligaciones de seguridad, confidencialidad, plazos de implantación, indisponibilidad del servicio, etc., conlleva penalidades económicas (5% o 10% del precio del contrato según gravedad) y puede ser causa de resolución. | ID_188_2.PDF, pág. 75-77 |
| Seguridad e IA | No se exige certificación ENS ni ISO 27001, solo cumplimiento material del ENS nivel básico. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | No se exige DPO/DPD al adjudicatario. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | No se define rol de encargado de tratamiento para el adjudicatario. | ID_188_3.PDF, pág. 50 |
| Seguridad e IA | No se exige acuerdo de encargo de tratamiento. | ID_188_3.PDF, pág. 50 |
| Seguridad e IA | No se detallan plazos de retención de logs ni de conservación de backups. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se exige plan de continuidad ni DR específico. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se exige auditoría ENS ni ISO periódica. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se especifican medidas técnicas concretas como MFA, PAM, VPN, segmentación, DLP, WAF, SIEM, SAST, DAST, SCA, SBOM, ni parámetros de RTO/RPO. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | El Anexo IX del pliego administrativo describe el tratamiento de datos personales para la gestión contractual, siendo responsable la Dirección General de Contratación y Servicios. | ID_188_2.PDF, Anexo IX, pág. 95 |
| Seguridad e IA | Se identifica Delegado de Protección de Datos (DPD) del Ayuntamiento de Madrid, pero no se exige DPO/DPD al adjudicatario. | ID_188_2.PDF, Anexo IX, pág. 95 |
| Seguridad e IA | Conservación de datos personales: mientras sean necesarios para la ejecución del contrato. | ID_188_2.PDF, Anexo IX, pág. 95 |
| Seguridad e IA | Derechos de los interesados: acceso, rectificación, supresión, limitación, oposición. | ID_188_2.PDF, Anexo IX, pág. 95 |
| Seguridad e IA | Categorías de datos tratados para gestión contractual: identificación, claves, direcciones, información comercial y económica. | ID_188_2.PDF, Anexo IX, pág. 95 |
| Seguridad e IA | No se exige acuerdo de encargo de tratamiento ni se define rol de encargado para el adjudicatario. | ID_188_3.PDF, pág. 50 |
| Seguridad e IA | No se exige DPO/DPD al adjudicatario. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | No se exige certificación ENS ni ISO 27001. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | No se especifican medidas técnicas concretas como MFA, PAM, VPN, segmentación, DLP, WAF, SIEM, SAST, DAST, SCA, SBOM, ni parámetros de RTO/RPO. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se exige plan de continuidad ni DR específico. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se exige auditoría ENS ni ISO periódica. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se detallan plazos de retención de logs ni de conservación de backups. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se define rol de encargado de tratamiento para el adjudicatario. | ID_188_3.PDF, pág. 50 |
| Seguridad e IA | No se exige acuerdo de encargo de tratamiento. | ID_188_3.PDF, pág. 50 |
| Seguridad e IA | No se exige DPO/DPD al adjudicatario. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | No se exige certificación ENS ni ISO 27001. | ID_188_3.PDF, pág. 46 |
| Seguridad e IA | No se especifican medidas técnicas concretas como MFA, PAM, VPN, segmentación, DLP, WAF, SIEM, SAST, DAST, SCA, SBOM, ni parámetros de RTO/RPO. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se exige plan de continuidad ni DR específico. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se exige auditoría ENS ni ISO periódica. | NO CONSTA EN LA DOCUMENTACION REVISADA |
| Seguridad e IA | No se detallan plazos de retención de logs ni de conservación de backups. | NO CONSTA EN LA DOCUMENTACION REVISADA |

# Discrepancias y pendientes de aclaración
No se han identificado discrepancias en la documentación revisada.