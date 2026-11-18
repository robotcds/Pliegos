## 1. Resumen factual Seguridad / DPO / ENS

El contrato para el Asistente Virtual de Participación Ciudadana del Ayuntamiento de Madrid establece requisitos de seguridad, protección de datos y cumplimiento del Esquema Nacional de Seguridad (ENS) en nivel básico, así como obligaciones específicas en materia de IA, cloud, confidencialidad, propiedad intelectual y medidas técnicas. No se exige tratamiento de datos personales por cuenta del Ayuntamiento ni acuerdo de encargo de tratamiento. Se detallan medidas de seguridad, gestión de riesgos, desarrollo seguro, logging, gestión de incidentes, auditorías, borrado seguro y confidencialidad, así como condiciones para subcontratación y despliegue en cloud pública. Se establecen consecuencias contractuales por incumplimiento y obligaciones de entrega de documentación y evidencias.

## 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
- Cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO para todos los servicios y sistemas desarrollados/desplegados/mantenidos en el contrato. | Básico | Servicios objeto del contrato y sistemas de información desarrollados/desplegados/mantenidos | Descripción de mecanismos de seguridad en la oferta técnica; validación por el órgano de contratación | Antes de la entrada en producción y durante la ejecución | ID_188_3.PDF, pág. 45-46
- Configuración de componentes tecnológicos conforme a guías CCN-STIC del CCN-CERT, adaptadas a las particularidades del Ayuntamiento y con aprobación del responsable del contrato. | Básico | Todos los componentes tecnológicos | Documentación de configuración segura | Durante ejecución | ID_188_3.PDF, pág. 46-47
- Designación de Punto o Persona de Contacto (POC) para la seguridad de la información tratada y el servicio prestado, o justificación de su no designación. | Básico | Seguridad de la información y servicio prestado | Designación/documentación | Inicio de ejecución | ID_188_3.PDF, pág. 46
- Análisis de riesgos conforme al ENS para servicios/sistemas desarrollados/desplegados/mantenidos, validado por el Ayuntamiento y con plan de tratamiento de riesgos. | Básico | Servicios/sistemas desarrollados/desplegados/mantenidos | Análisis de riesgos y plan de tratamiento | Inicio de ejecución y actualización periódica | ID_188_3.PDF, pág. 46

## 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
- No se precisa tratamiento de datos personales por cuenta del Ayuntamiento; no se requiere acuerdo de encargo de tratamiento. | Exención expresa | N/A | ID_188_3.PDF, pág. 50, 44
- Si se produjera tratamiento de datos personales, se aplicaría la normativa vigente (LOPDGDD, RGPD), pero el pliego indica expresamente que no es necesario en este contrato. | Exención expresa | N/A | ID_188_3.PDF, pág. 50
- Delegado de Protección de Datos (DPD) del Ayuntamiento: Coordinación General de Distritos, Transparencia y Participación Ciudadana, oficprotecciondatos@madrid.es | Información de contacto | N/A | ID_188_2.PDF, Anexo IX, pág. 95

## 4. Subencargados, cloud, localizacion y transferencias: requisito | condicion | fuente
- Despliegue de soluciones solo permitido en cloud pública de Microsoft Azure, Google Cloud Platform o Amazon AWS, en regiones del Espacio Económico Europeo (EEE). | Obligatorio | No se admiten otros clouders ni regiones fuera del EEE | ID_188_3.PDF, pág. 29-30, 33
- Subcontratación permitida dentro de los límites fijados en el contrato; el adjudicatario debe informar sobre la intervención de terceras empresas y cambios durante el contrato. | Obligatorio | Comunicación previa y justificación de aptitud | ID_188_3.PDF, pág. 29
- Prohibida la publicación directa de servicios PaaS en Internet sin autorización de IAM. | Obligatorio | Autorización previa | ID_188_3.PDF, pág. 33

## 5. Medidas tecnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente
- Configuración segura de todos los componentes tecnológicos según guías CCN-STIC. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 46-47
- Cifrado obligatorio de información no pública del Ayuntamiento cuando se transmita por redes ajenas; decisión de cifrado según valoración del responsable de la información. | Obligatoria | Durante transmisión por redes ajenas | ID_188_3.PDF, pág. 47
- Identificación y autenticación: personal municipal mediante plataforma de identidad corporativa; ciudadanía mediante sistema estatal CL@VE; otros métodos requieren autorización de IAM. | Obligatoria | Durante acceso a información no pública | ID_188_3.PDF, pág. 47
- Compatibilidad con doble factor de autenticación municipal para personal del contratista si es necesario. | Obligatoria | Durante acceso | ID_188_3.PDF, pág. 48
- Acceso remoto a red corporativa solo mediante servicio de acceso remoto para empresas del Ayuntamiento; cumplimiento de condiciones de uso. | Obligatoria | Durante gestión/mantenimiento | ID_188_3.PDF, pág. 48
- Principios de mínimo privilegio, necesidad de conocer y capacidad de autorizar para control de acceso. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48
- Restricción de roles de administración al mínimo imprescindible. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48
- Programas instalados en puestos corporativos: sin requerir permisos de administración para ejecución por usuarios no privilegiados. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Registro de actividad de usuarios, con retención de información necesaria para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas. | Obligatoria | Durante ejecución; entrega a requerimiento | ID_188_3.PDF, pág. 49
- Aplicación diligente y periódica de actualizaciones de seguridad; medidas compensatorias si no es posible aplicar una actualización. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Subsanación de vulnerabilidades comunicadas por el responsable del contrato. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Auditorías de seguridad por el Ayuntamiento; colaboración obligatoria del adjudicatario. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Eliminación segura de toda la información al finalizar el contrato, con certificado de destrucción. | Obligatoria | Al cierre del contrato | ID_188_3.PDF, pág. 9

## 6. Identidad, accesos y privilegios
- Gestión de credenciales y accesos a recursos cloud es competencia del Ayuntamiento; usuarios externos usan credenciales proporcionadas por IAM. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 33
- Política de identificación y autenticación conforme a normativa municipal basada en ENS. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 47
- Restricción de privilegios y roles de administración. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48

## 7. Vulnerabilidades, parcheado y desarrollo seguro
- Aplicación periódica y continuada de actualizaciones de seguridad; medidas compensatorias si no es posible aplicar una actualización. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Subsanación de vulnerabilidades comunicadas por el responsable del contrato. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Desarrollo seguro y orientado a la privacidad, siguiendo metodologías y buenas prácticas verificables en todo el ciclo de vida del proyecto; documentación de prácticas empleadas. | Obligatoria | Durante desarrollo | ID_188_3.PDF, pág. 47

## 8. Incidentes, brechas y plazos de notificacion expresamente indicados
- Gestión de ciberincidentes en todo su ciclo de vida (detección, registro, contención, mitigación y recuperación) conforme a normativa específica del Ayuntamiento y guía CCN-STIC-817. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Notificación de cualquier ciberincidente que pueda afectar a información o servicios del Ayuntamiento al responsable del contrato tan pronto como se tenga conocimiento, manteniendo informado hasta el cierre del incidente. | Obligatoria | Inmediato tras conocimiento | ID_188_3.PDF, pág. 49
- Colaboración activa en la paliación y resolución total de incidentes detectados durante ejecución o garantía. | Obligatoria | Durante ejecución y garantía | ID_188_3.PDF, pág. 49

## 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retencion
- Registro de actividad de usuarios, con retención de información necesaria para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas; entrega a requerimiento. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Los sistemas deben facilitar información técnica (logs, trazas) para su ingesta por herramientas de observabilidad y monitorización de IAM si se solicita. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 31
- Copias de seguridad y restauración proporcionadas por IAM. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 31
- No se especifican expresamente RTO/RPO. | NO CONSTA EN LA DOCUMENTACION REVISADA | N/A | N/A

## 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Auditorías de seguridad por el Ayuntamiento; colaboración obligatoria del adjudicatario. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49
- Eliminación segura de toda la información al finalizar el contrato, con certificado de destrucción. | Obligatoria | Al cierre del contrato | ID_188_3.PDF, pág. 9
- Confidencialidad: obligación de guardar secreto sobre hechos, informaciones, documentos y otros elementos a los que se tenga acceso, subsistiendo tras la finalización del contrato. | Obligatoria | Durante ejecución y tras finalización | ID_188_3.PDF, pág. 53
- Plazo de confidencialidad: subsiste tras la finalización del contrato; no se especifica plazo concreto en el PPTP, pero en el PCAP se indica 5 años desde el conocimiento de la información. | Obligatoria | 5 años desde conocimiento (PCAP) | ID_188_2.PDF, Anexo I, pág. 79
- Seguridad del personal: obligación de proveer equipos de protección individual y cumplir normativa de prevención de riesgos laborales. | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 23, 51

## 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Incumplimiento de obligaciones de seguridad, confidencialidad, entrega de información, formación, adscripción de medios, condiciones especiales de ejecución, subcontratación o penalidades: penalidad económica del 5% o 10% del precio del contrato según gravedad, y posibilidad de resolución del contrato. | Obligación esencial/condición especial de ejecución | Durante ejecución | ID_188_2.PDF, Anexo I, pág. 75-78

## 12. Datos no localizados o ambiguos, sin recomendaciones
- No se exige certificación ISO 27001 ni declaración/certificación ENS formal, solo cumplimiento de medidas ENS nivel básico. | NO EXIGIDO EXPRESAMENTE | ID_188_3.PDF, pág. 45-46
- No se exige DPO propio del adjudicatario, solo contacto del DPD del Ayuntamiento. | NO EXIGIDO EXPRESAMENTE | ID_188_2.PDF, Anexo IX, pág. 95
- No se exige acuerdo de encargo de tratamiento ni subencargados de tratamiento. | NO EXIGIDO EXPRESAMENTE | ID_188_3.PDF, pág. 50
- No se especifican expresamente medidas como MFA, RBAC, PAM, VPN, bastionado, segmentación, EDR/XDR, WAF, SIEM, DLP, backups (más allá de los proporcionados por IAM), ni parámetros de retención, RTO/RPO, ni frecuencia de auditorías. | NO CONSTA EN LA DOCUMENTACION REVISADA | N/A

## 13. Documentos revisados: enumera todos los documentos del indice, uno por uno.
- ID_188_1.PDF (Documento licitacion real)
- ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares y Anexos)
- ID_188_3.PDF (Pliego de Prescripciones Técnicas Particulares)
- poc (enlace detalle licitación)
- poc (enlace perfil contratante)
- poc (enlace perfil contratante)
- 147409-2026 (anuncio DOUE)
- perfilContratante (enlace perfil contratante)

## Tabla de trazabilidad

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|----------------|-----------|-----------------|------------------|
| Cumplimiento ENS nivel básico | Obligación contractual | Aplicable a todos los servicios y sistemas desarrollados/desplegados/mantenidos | ID_188_3.PDF | 45-46 | TEXTO EXTRAIDO |
| Configuración segura CCN-STIC | Obligación contractual | Todos los componentes tecnológicos | ID_188_3.PDF | 46-47 | TEXTO EXTRAIDO |
| Designación POC seguridad | Obligación contractual | Designación/documentación o justificación | ID_188_3.PDF | 46 | TEXTO EXTRAIDO |
| Análisis de riesgos ENS | Obligación contractual | Análisis y plan de tratamiento validados | ID_188_3.PDF | 46 | TEXTO EXTRAIDO |
| No tratamiento de datos personales por cuenta del Ayuntamiento | Exención expresa | No se requiere acuerdo de encargo | ID_188_3.PDF | 50 | TEXTO EXTRAIDO |
| Cloud pública EEE | Obligación contractual | Solo Azure, GCP, AWS en EEE | ID_188_3.PDF | 29-30, 33 | TEXTO EXTRAIDO |
| Subcontratación permitida con límites | Obligación contractual | Comunicación previa y justificación | ID_188_3.PDF | 29 | TEXTO EXTRAIDO |
| Cifrado de información no pública | Obligación contractual | Según valoración del responsable | ID_188_3.PDF | 47 | TEXTO EXTRAIDO |
| Identificación/autenticación | Obligación contractual | Plataforma corporativa/CL@VE/otros con autorización | ID_188_3.PDF | 47 | TEXTO EXTRAIDO |
| Registro de actividad/logs | Obligación contractual | Monitorización, análisis, entrega a requerimiento | ID_188_3.PDF | 49 | TEXTO EXTRAIDO |
| Actualizaciones de seguridad | Obligación contractual | Aplicación periódica y continuada | ID_188_3.PDF | 49 | TEXTO EXTRAIDO |
| Gestión de ciberincidentes | Obligación contractual | Notificación inmediata, colaboración activa | ID_188_3.PDF | 49 | TEXTO EXTRAIDO |
| Auditorías de seguridad | Obligación contractual | Realización por el Ayuntamiento | ID_188_3.PDF | 49 | TEXTO EXTRAIDO |
| Eliminación segura y certificado | Obligación contractual | Al cierre del contrato | ID_188_3.PDF | 9 | TEXTO EXTRAIDO |
| Confidencialidad | Obligación contractual | Durante ejecución y tras finalización | ID_188_3.PDF | 53 | TEXTO EXTRAIDO |
| Plazo confidencialidad | Obligación contractual | 5 años desde conocimiento (PCAP) | ID_188_2.PDF | Anexo I, 79 | TEXTO EXTRAIDO |
| Penalidades por incumplimiento | Obligación esencial/condición especial | 5% o 10% del precio del contrato | ID_188_2.PDF | Anexo I, 75-78 | TEXTO EXTRAIDO |
| No se exige ISO 27001 | Exención expresa | No exigido | ID_188_3.PDF | 45-46 | TEXTO EXTRAIDO |
| No se exige DPO propio | Exención expresa | No exigido | ID_188_2.PDF | Anexo IX, 95 | TEXTO EXTRAIDO |
| No se exige acuerdo de encargo | Exención expresa | No exigido | ID_188_3.PDF | 50 | TEXTO EXTRAIDO |
| No se especifican MFA, RBAC, PAM, VPN, etc. | NO CONSTA | N/A | N/A | N/A | N/A |

## Discrepancias y pendientes de aclaración
No se han identificado discrepancias en la documentación revisada.