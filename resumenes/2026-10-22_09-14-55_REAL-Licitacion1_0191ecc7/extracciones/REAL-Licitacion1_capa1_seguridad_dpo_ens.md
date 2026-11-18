# 1. Resumen factual Seguridad / DPO / ENS

- El contrato exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para todos los servicios y sistemas desarrollados, desplegados o mantenidos en el marco del contrato. Se requiere la designación de un Punto o Persona de Contacto (POC) para seguridad de la información, análisis de riesgos conforme al ENS, aplicación de medidas de seguridad del Anexo II ENS nivel Básico, configuración segura según guías CCN-STIC, desarrollo seguro, cifrado de información no pública en tránsito por redes ajenas, identificación y autenticación conforme a normativa municipal, control de acceso basado en mínimo privilegio y necesidad de conocer, logging de actividad, aplicación de actualizaciones de seguridad, gestión de ciberincidentes y vulnerabilidades, auditorías de seguridad, y colaboración con el Centro de Ciberseguridad municipal.
- No se exige certificación ENS ni ISO 27001, solo cumplimiento material y documentación de medidas.
- El contrato especifica que no requiere tratamiento de datos personales por cuenta del responsable, por lo que no se exige acuerdo de encargo de tratamiento ni obligaciones de subencargado, ni designación de DPO/DPD para el adjudicatario. El responsable de tratamiento de los datos de contratación es la Dirección General de Contratación y Servicios del Ayuntamiento de Madrid.
- Los sistemas deben desplegarse exclusivamente en nubes públicas autorizadas (Azure, AWS, GCP) en regiones del Espacio Económico Europeo (EEE), prohibiéndose el despliegue en otros proveedores o fuera del EEE.
- Se exige cumplimiento de la política de seguridad de la información municipal, normativa ENS, guías CCN-STIC, y normativa europea y nacional de ciberseguridad.
- Se establecen obligaciones de confidencialidad durante la ejecución y subsistencia tras la finalización del contrato, con plazo de 5 años desde el conocimiento de la información.
- Se exige borrado seguro de datos al finalizar el contrato, con entrega de certificado de destrucción.
- Se detallan medidas técnicas y organizativas obligatorias en materia de seguridad, acceso, logging, gestión de incidentes, vulnerabilidades, desarrollo seguro, y colaboración con el cliente en auditorías y respuesta a incidentes.
- No se exige SOC/SIEM propio, pero sí integración de logs y trazas con herramientas de observabilidad y monitorización de IAM si se solicita.
- No se establecen requisitos de RTO/RPO ni de continuidad de negocio específicos, más allá de la obligación de resiliencia y disponibilidad del servicio.
- No se exige designación de DPO/DPD para el adjudicatario ni se prevé tratamiento de datos personales por cuenta del responsable.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente |
|---|---|---|---|---|---|
| Cumplimiento ENS | Básico | Todos los servicios y sistemas desarrollados/desplegados/mantenidos en el contrato | Descripción de mecanismos de seguridad en la oferta, documentación de medidas, análisis de riesgos, plan de tratamiento, configuración según guías CCN-STIC | Oferta y durante ejecución | ID_188_3.PDF, pág. 45-46, 11.1-11.5 |
| Designación POC seguridad | N/A | Servicio prestado y solución proveída | Designación de persona/contacto o justificación de no designación | Inicio ejecución | ID_188_3.PDF, pág. 46, 11.2 |
| Análisis de riesgos ENS | N/A | Servicios digitales, desarrollo/mantenimiento SW, infraestructuras/plataformas | Análisis de riesgos validado por el Ayuntamiento, plan de tratamiento | Inicio ejecución | ID_188_3.PDF, pág. 46, 11.3 |
| Configuración segura CCN-STIC | N/A | Todos los componentes tecnológicos | Configuración conforme a guías CCN-STIC, adecuación a particularidades municipales | Durante ejecución | ID_188_3.PDF, pág. 46, 11.4 |
| Desarrollo seguro | N/A | Actividades de desarrollo/mantenimiento SW | Metodologías y buenas prácticas verificables, documentación | Durante ejecución | ID_188_3.PDF, pág. 47, 11.5 |
| Cifrado información no pública | N/A | Información propiedad del Ayuntamiento no pública | Cifrado en tránsito por redes ajenas, según valoración del responsable | Durante ejecución | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación | N/A | Acceso a información no pública | Delegación en plataforma de identidad municipal o CL@VE, otros métodos previa autorización | Durante ejecución | ID_188_3.PDF, pág. 47, 11.7 |
| Control de acceso | N/A | Servicio/sistema objeto del contrato | Principios de mínimo privilegio, necesidad de conocer, capacidad de autorizar | Durante ejecución | ID_188_3.PDF, pág. 48, 11.10 |
| Logging de actividad | N/A | Servicio/sistema objeto del contrato | Registro de actividades de usuarios, entrega de logs a requerimiento | Durante ejecución | ID_188_3.PDF, pág. 49, 11.12 |
| Actualizaciones de seguridad | N/A | Servicio/sistema objeto del contrato | Aplicación periódica y continuada de actualizaciones, medidas compensatorias si no es posible | Durante ejecución | ID_188_3.PDF, pág. 49, 11.13 |
| Gestión de ciberincidentes | N/A | Servicio/sistema objeto del contrato | Gestión ciclo completo, notificación inmediata al responsable del contrato, colaboración hasta cierre | Durante ejecución | ID_188_3.PDF, pág. 49, 11.14 |
| Subsanación de vulnerabilidades | N/A | Sistemas del adjudicatario | Subsanación de vulnerabilidades comunicadas por el responsable | Durante ejecución | ID_188_3.PDF, pág. 49, 11.15 |
| Auditorías de seguridad | N/A | Sistemas implantados/utilizados | Colaboración en auditorías realizadas por el Ayuntamiento | Durante ejecución | ID_188_3.PDF, pág. 49, 11.16 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente |
|---|---|---|---|
| No se precisa tratamiento de datos personales por cuenta del responsable | Exención expresa para el adjudicatario | No aplica | ID_188_3.PDF, pág. 50, 11.18 |
| Responsable de tratamiento de datos de contratación: Dirección General de Contratación y Servicios | Solo para datos de contratación municipal | Conservación mientras sean necesarios para la ejecución del contrato | ID_188_2.PDF, pág. 95, Anexo IX |
| Delegado de Protección de Datos: Coordinación General de Distritos, Transparencia y Participación Ciudadana | Solo para datos de contratación municipal | NO CONSTA PLAZO | ID_188_2.PDF, pág. 95, Anexo IX |

# 4. Subencargados, cloud, localizacion y transferencias

| Requisito | Condicion | Fuente |
|---|---|---|
| Despliegue solo en nubes públicas autorizadas (Azure, AWS, GCP) | Prohibido el despliegue en otros proveedores o fuera del EEE | ID_188_3.PDF, pág. 29-30, 7 |
| Recursos desplegados deben estar localizados en regiones del EEE | Cumplimiento art. 45 RGPD, transferencias basadas en decisión de adecuación | ID_188_3.PDF, pág. 33, Organización de recursos |
| Subcontratación permitida dentro de límites del contrato | Obligación de informar sobre subcontratistas y cambios, conservación de garantías jurídicas | ID_188_3.PDF, pág. 29, 6.5 |
| Prohibida publicación directa de servicios PaaS en Internet | Solo previa autorización de IAM | ID_188_3.PDF, pág. 33, Topología de red |

# 5. Medidas tecnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente

| Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente |
|---|---|---|---|
| Configuración segura según guías CCN-STIC | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 46, 11.4 |
| Cifrado de información no pública en tránsito | Obligatoria | Según valoración del responsable | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación conforme a normativa municipal | Obligatoria | Delegación en plataforma de identidad municipal o CL@VE | ID_188_3.PDF, pág. 47, 11.7 |
| Control de acceso mínimo privilegio/need to know | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48, 11.10 |
| Logging de actividad | Obligatoria | Entrega de logs a requerimiento | ID_188_3.PDF, pág. 49, 11.12 |
| Aplicación de actualizaciones de seguridad | Obligatoria | Periódica y continuada | ID_188_3.PDF, pág. 49, 11.13 |
| Gestión de ciberincidentes | Obligatoria | Notificación inmediata, colaboración hasta cierre | ID_188_3.PDF, pág. 49, 11.14 |
| Subsanación de vulnerabilidades | Obligatoria | A requerimiento del responsable | ID_188_3.PDF, pág. 49, 11.15 |
| Desarrollo seguro y orientado a la privacidad | Obligatoria | Metodologías y buenas prácticas verificables | ID_188_3.PDF, pág. 47, 11.5 |
| Integración de logs/trazas con herramientas de IAM | Condicionada a requerimiento | Durante ejecución | ID_188_3.PDF, pág. 30, 7 |
| No se permite IP pública en máquinas virtuales | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 34, Seguridad y privacidad |
| No se permite publicación directa de servicios PaaS en Internet | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 33, Topología de red |

# 6. Identidad, accesos y privilegios

- Gestión de credenciales y accesos a recursos de nube es competencia del Ayuntamiento de Madrid. Usuarios externos deben usar credenciales proporcionadas por IAM. No se proporciona a proveedores permisos de gestión de accesos a recursos. (ID_188_3.PDF, pág. 33)
- Acceso a información no pública: personal municipal mediante plataforma de identidad corporativa, ciudadanía mediante CL@VE, otros métodos previa autorización de IAM. (ID_188_3.PDF, pág. 47)
- Principios de mínimo privilegio y necesidad de conocer para control de acceso. (ID_188_3.PDF, pág. 48)
- Restricción de roles de administración al mínimo imprescindible. (ID_188_3.PDF, pág. 48)

# 7. Vulnerabilidades, parcheado y desarrollo seguro

- El adjudicatario debe subsanar vulnerabilidades comunicadas por el responsable del contrato. (ID_188_3.PDF, pág. 49)
- Aplicación periódica y continuada de actualizaciones de seguridad; si no es posible, aplicar medidas compensatorias. (ID_188_3.PDF, pág. 49)
- Desarrollo seguro: uso de metodologías y buenas prácticas verificables, reflejadas en la documentación del proyecto. (ID_188_3.PDF, pág. 47)

# 8. Incidentes, brechas y plazos de notificacion expresamente indicados

- El adjudicatario es responsable de la gestión de ciberincidentes en todo su ciclo de vida (detección, registro, contención, mitigación y recuperación) conforme a la normativa específica del Ayuntamiento y guía CCN-STIC-817. (ID_188_3.PDF, pág. 49)
- Notificación de cualquier ciberincidente que pueda afectar a información o servicios del Ayuntamiento al responsable del contrato tan pronto como tenga conocimiento, manteniendo informado hasta el cierre. (ID_188_3.PDF, pág. 49)
- Colaboración activa en la paliación y resolución total de incidentes detectados durante ejecución o garantía. (ID_188_3.PDF, pág. 49)
- No se establecen plazos numéricos expresos para la notificación, solo "tan pronto como tenga conocimiento".

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retencion

- Logging: registro de actividades de usuarios, retención de información necesaria para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas, permitiendo identificar a la persona que actúa. Entrega de logs a requerimiento del responsable del contrato. (ID_188_3.PDF, pág. 49)
- Integración de logs y trazas con herramientas de observabilidad y monitorización de IAM si se solicita. (ID_188_3.PDF, pág. 30)
- No se exige SOC/SIEM propio, pero sí integración si se requiere.
- Copias de seguridad y restauración proporcionadas por IAM. (ID_188_3.PDF, pág. 31)
- No se establecen requisitos de RTO/RPO ni de continuidad de negocio específicos, más allá de la obligación de resiliencia y disponibilidad del servicio. (ID_188_3.PDF, pág. 19)
- Retención de logs: durante la vigencia del contrato, entrega al finalizar. (ID_188_3.PDF, pág. 38)

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad

- El Ayuntamiento podrá realizar auditorías de seguridad de los sistemas implantados o utilizados en el contrato. (ID_188_3.PDF, pág. 49)
- El adjudicatario debe colaborar en auditorías y facilitar la documentación requerida. (ID_188_3.PDF, pág. 49)
- No se exige certificación ENS ni ISO 27001, solo cumplimiento material y documentación de medidas. (ID_188_3.PDF, pág. 45-46)
- Seguridad del personal: obligación de proveer equipos de protección individual en caso de situaciones excepcionales, cumplimiento de normativa de prevención de riesgos laborales. (ID_188_3.PDF, pág. 23, 51)
- Borrado seguro de datos al finalizar el contrato, con entrega de certificado de destrucción. (ID_188_3.PDF, pág. 9)
- Confidencialidad: obligación durante la ejecución y subsistencia tras la finalización del contrato, con plazo de 5 años desde el conocimiento de la información. (ID_188_2.PDF, pág. 79, Anexo I, 33)

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento

- Incumplimiento de obligaciones de seguridad, confidencialidad, entrega de información, etc., puede dar lugar a penalidades económicas (5% o 10% del precio del contrato según gravedad), resolución del contrato, incautación de garantía, e indemnización de daños y perjuicios. (ID_188_2.PDF, pág. 76-77, Anexo I, 30)
- Incumplimiento de condiciones especiales de ejecución en materia de seguridad y adscripción de medios personales/materiales es causa de penalidad y puede ser causa de resolución. (ID_188_2.PDF, pág. 77, Anexo I, 31)

# 12. Datos no localizados o ambiguos, sin recomendaciones

- No se exige certificación ENS ni ISO 27001, solo cumplimiento material.
- No se exige designación de DPO/DPD para el adjudicatario.
- No se exige acuerdo de encargo de tratamiento ni subencargados, salvo para datos de contratación municipal.
- No se establecen requisitos de RTO/RPO numéricos ni de continuidad de negocio específicos.
- No se exige SOC/SIEM propio, solo integración si se requiere.
- No se exige plan de continuidad ni DRP específico.
- No se exige SBOM, SAST, DAST, SCA, ni requisitos DevSecOps específicos más allá de buenas prácticas de desarrollo seguro.
- No se exige MFA, RBAC, PAM, VPN, bastionado, segmentación, EDR/XDR, WAF, DLP, salvo lo que derive de la política de IAM y la configuración segura.

# 13. Documentos revisados

1. ID_188_1.PDF (Documento licitacion real)
2. ID_188_2.PDF (Documento licitacion real)
3. ID_188_3.PDF (Pliego de Prescripciones Técnicas)
4. poc (Documento enlazado, detalle licitación)
5. poc (Documento enlazado, perfil contratante)
6. poc (Documento enlazado, perfil contratante)
7. 147409-2026 (Documento enlazado, anuncio DOUE)
8. perfilContratante (Documento enlazado)

# Tabla de trazabilidad

| Requisito/dato | Tipo | Valor/condicion | Documento | Pagina/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Cumplimiento ENS | Obligación contractual | Nivel Básico, Anexo II ENS, servicios y sistemas del contrato | ID_188_3.PDF | 45-46, 11.1-11.5 | TEXTO EXTRAIDO |
| Designación POC seguridad | Obligación contractual | Designación de persona/contacto o justificación | ID_188_3.PDF | 46, 11.2 | TEXTO EXTRAIDO |
| Análisis de riesgos ENS | Obligación contractual | Análisis de riesgos validado, plan de tratamiento | ID_188_3.PDF | 46, 11.3 | TEXTO EXTRAIDO |
| Configuración segura CCN-STIC | Obligación contractual | Guías CCN-STIC, adecuación municipal | ID_188_3.PDF | 46, 11.4 | TEXTO EXTRAIDO |
| Desarrollo seguro | Obligación contractual | Buenas prácticas verificables, documentación | ID_188_3.PDF | 47, 11.5 | TEXTO EXTRAIDO |
| Cifrado información no pública | Obligación contractual | Cifrado en tránsito por redes ajenas | ID_188_3.PDF | 47, 11.6 | TEXTO EXTRAIDO |
| Identificación y autenticación | Obligación contractual | Plataforma identidad municipal/CL@VE | ID_188_3.PDF | 47, 11.7 | TEXTO EXTRAIDO |
| Control de acceso | Obligación contractual | Mínimo privilegio, necesidad de conocer | ID_188_3.PDF | 48, 11.10 | TEXTO EXTRAIDO |
| Logging de actividad | Obligación contractual | Registro de actividades, entrega de logs | ID_188_3.PDF | 49, 11.12 | TEXTO EXTRAIDO |
| Actualizaciones de seguridad | Obligación contractual | Aplicación periódica y continuada | ID_188_3.PDF | 49, 11.13 | TEXTO EXTRAIDO |
| Gestión de ciberincidentes | Obligación contractual | Notificación inmediata, colaboración | ID_188_3.PDF | 49, 11.14 | TEXTO EXTRAIDO |
| Subsanación de vulnerabilidades | Obligación contractual | Subsanación a requerimiento | ID_188_3.PDF | 49, 11.15 | TEXTO EXTRAIDO |
| Auditorías de seguridad | Obligación contractual | Colaboración en auditorías | ID_188_3.PDF | 49, 11.16 | TEXTO EXTRAIDO |
| Borrado seguro de datos | Obligación contractual | Borrado seguro y certificado al cierre | ID_188_3.PDF | 9 | TEXTO EXTRAIDO |
| Confidencialidad | Obligación contractual | 5 años desde conocimiento | ID_188_2.PDF | 79, Anexo I, 33 | TEXTO EXTRAIDO |
| No tratamiento de datos personales por cuenta del responsable | Exención expresa | No aplica | ID_188_3.PDF | 50, 11.18 | TEXTO EXTRAIDO |
| Despliegue solo en nubes públicas autorizadas | Obligación contractual | Azure, AWS, GCP, regiones EEE | ID_188_3.PDF | 29-30, 33 | TEXTO EXTRAIDO |
| Subcontratación permitida con límites | Obligación contractual | Información y conservación de garantías | ID_188_3.PDF | 29, 6.5 | TEXTO EXTRAIDO |
| Penalidades por incumplimiento | Consecuencia contractual | 5% o 10% del precio, resolución, incautación garantía | ID_188_2.PDF | 76-77, Anexo I, 30 | TEXTO EXTRAIDO |

# Discrepancias y pendientes de aclaración

No se han identificado discrepancias en la documentación revisada.