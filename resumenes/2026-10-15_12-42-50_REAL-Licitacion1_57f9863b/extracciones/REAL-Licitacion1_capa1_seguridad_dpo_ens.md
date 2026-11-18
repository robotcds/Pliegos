# 1. Resumen factual Seguridad / DPO / ENS

La licitación para el Asistente Virtual de Participación Ciudadana del Ayuntamiento de Madrid establece requisitos de seguridad, protección de datos y cumplimiento del Esquema Nacional de Seguridad (ENS) en nivel básico, así como obligaciones contractuales específicas en materia de confidencialidad, desarrollo seguro, gestión de incidentes, control de accesos, subcontratación, uso de cloud pública y gobernanza de IA. El pliego detalla medidas técnicas y organizativas, requisitos de arquitectura, gestión de riesgos, logging, auditorías, borrado seguro y entrega de documentación, pero no exige certificaciones ENS/ISO ni designación de DPO/DPD para el adjudicatario. Se declara expresamente que el contrato no requiere tratamiento de datos personales por cuenta del responsable, aunque se prevén medidas de anonimización y protección de la información. Se establecen consecuencias contractuales por incumplimiento de las obligaciones esenciales y condiciones especiales de ejecución.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente |
|---|---|---|---|---|---|
| Cumplimiento ENS | Básico | Servicios objeto del contrato y sistemas desarrollados/desplegados/mantenidos | Descripción de mecanismos de seguridad en la oferta técnica | Presentación de oferta y ejecución | ID_188_3.PDF, pág. 46-47, 11.1, 11.2 |
| Configuración según guías CCN-STIC | Básico | Componentes tecnológicos del servicio | Configuración conforme a guías CCN-STIC, adaptadas al Ayuntamiento | Ejecución | ID_188_3.PDF, pág. 47, 11.4 |
| Análisis de riesgos conforme ENS | Básico | Servicios y sistemas desarrollados/desplegados/mantenidos | Análisis de riesgos validado por el Ayuntamiento | Inicio de trabajos | ID_188_3.PDF, pág. 46, 11.3 |
| Plan de tratamiento del riesgo | Básico | Servicios y sistemas desarrollados/desplegados/mantenidos | Plan elaborado tras validación del análisis de riesgos | Tras validación análisis de riesgos | ID_188_3.PDF, pág. 46, 11.3 |
| Designación de POC de seguridad | Básico | Seguridad de la información tratada y servicio prestado | Designación de persona/contacto o justificación de no designación | Ejecución | ID_188_3.PDF, pág. 46, 11.2 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente |
|---|---|---|---|
| Tratamiento de datos personales por cuenta del responsable | No requerido para el adjudicatario | No aplica | ID_188_3.PDF, pág. 48, 11.18; ID_188_2.PDF, pág. 54, 1.8 |
| Anonimización de datos en consultas al asistente | Obligación de anonimizar datos personales incluidos voluntariamente | Durante la ejecución | ID_188_3.PDF, pág. 19, 5.3 |
| Información sobre protección de datos en contratación municipal | Responsable: Dirección General de Contratación y Servicios; DPD: Coordinación General de Distritos, Transparencia y Participación Ciudadana | Conservación mientras sean necesarios para la ejecución del contrato | ID_188_2.PDF, pág. 95, Anexo IX |
| Derechos de acceso, rectificación, supresión, limitación, oposición | Aplicable a los datos tratados por la Dirección General de Contratación y Servicios | Según normativa | ID_188_2.PDF, pág. 95, Anexo IX |

# 4. Subencargados, cloud, localizacion y transferencias: requisito | condicion | fuente

| Requisito | Condición | Fuente |
|---|---|---|
| Uso de cloud pública | Solo permitido en Microsoft Azure, Google Cloud Platform o Amazon AWS, en regiones del EEE | ID_188_3.PDF, pág. 29-30, 7 |
| Subcontratación | Permitida salvo tareas críticas de implantación y jefe de proyecto; debe informarse y cumplir límites contractuales | ID_188_3.PDF, pág. 29, 6.5; ID_188_2.PDF, pág. 74, 26 |
| Localización de datos | Recursos desplegados deben estar en regiones del EEE | ID_188_3.PDF, pág. 33, Organización de recursos |
| Transferencias internacionales | No permitidas fuera del EEE; cumplimiento art. 45 RGPD | ID_188_3.PDF, pág. 30, 33 |

# 5. Medidas tecnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente

| Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente |
|---|---|---|---|
| Configuración segura según guías CCN-STIC | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 47, 11.4 |
| Cifrado de información no pública en tránsito por redes ajenas | Obligatoria si la información no es pública | Durante ejecución | ID_188_3.PDF, pág. 47, 11.6 |
| Identificación y autenticación conforme ENS | Obligatoria | Acceso a información no pública; delegación en identidad corporativa o CL@VE | ID_188_3.PDF, pág. 47, 11.7 |
| Compatibilidad con doble factor de autenticación municipal | Obligatoria si aplica | Durante ejecución | ID_188_3.PDF, pág. 48, 11.8 |
| Control de acceso: mínimo privilegio, necesidad de conocer, capacidad de autorizar | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 48, 11.10 |
| Logging de actividad de usuarios | Obligatoria | Retención suficiente para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas | ID_188_3.PDF, pág. 49, 11.12 |
| Actualizaciones de seguridad y parches | Obligatoria | Periódica y continuada; medidas compensatorias si no es posible aplicar actualización | ID_188_3.PDF, pág. 49, 11.13 |
| Gestión de ciberincidentes (detección, registro, contención, mitigación, recuperación) | Obligatoria | Conforme guía CCN-STIC-817; notificación inmediata al responsable del contrato | ID_188_3.PDF, pág. 49, 11.14 |
| Subsanación de vulnerabilidades notificadas por el responsable | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49, 11.15 |
| Auditorías de seguridad por el Ayuntamiento | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 49, 11.16 |
| Desarrollo seguro y orientado a la privacidad | Obligatoria si hay desarrollo/mantenimiento SW | Metodologías y buenas prácticas verificables; documentadas | ID_188_3.PDF, pág. 47, 11.5 |
| Infraestructura como código (IaC) y DevSecOps | Obligatoria | Despliegue inicial y redespliegues; código en repositorio IAM | ID_188_3.PDF, pág. 30, 33 |
| Anonimización de datos personales en consultas | Obligatoria | Durante ejecución | ID_188_3.PDF, pág. 19, 5.3 |
| Borrado seguro y certificado de destrucción al cierre | Obligatoria | Al cierre del contrato; certificado de destrucción | ID_188_3.PDF, pág. 9, 3.2 |

# 6. Identidad, accesos y privilegios
- Gestión de credenciales y accesos a recursos cloud es competencia del Ayuntamiento; usuarios externos usan credenciales proporcionadas por IAM (ID_188_3.PDF, pág. 33).
- Acceso a panel de control mediante navegador estándar; perfiles de acceso diferenciados (ID_188_3.PDF, pág. 14).
- Principios de mínimo privilegio y necesidad de conocer para todos los accesos (ID_188_3.PDF, pág. 48).
- Acceso remoto a red corporativa solo mediante servicio de acceso remoto para empresas, cumpliendo condiciones de uso (ID_188_3.PDF, pág. 48).

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- Subsanación obligatoria de vulnerabilidades notificadas por el responsable del contrato (ID_188_3.PDF, pág. 49).
- Aplicación diligente y periódica de actualizaciones de seguridad y parches; medidas compensatorias si no es posible aplicar actualización (ID_188_3.PDF, pág. 49).
- Desarrollo seguro y orientado a la privacidad, con metodologías y buenas prácticas verificables y documentadas (ID_188_3.PDF, pág. 47).

# 8. Incidentes, brechas y plazos de notificacion expresamente indicados
- Gestión de ciberincidentes en todo su ciclo de vida conforme a guía CCN-STIC-817 (detección, registro, contención, mitigación, recuperación) (ID_188_3.PDF, pág. 49).
- Notificación inmediata de cualquier ciberincidente que pueda afectar a información o servicios al responsable del contrato, manteniéndole informado hasta el cierre (ID_188_3.PDF, pág. 49).
- Colaboración activa en la paliación y resolución total de incidentes detectados durante la ejecución o garantía (ID_188_3.PDF, pág. 49).

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retencion
- Logging de actividad de usuarios, con retención suficiente para monitorizar, analizar, investigar y documentar actividades indebidas o no autorizadas; entrega a requerimiento (ID_188_3.PDF, pág. 49).
- Integración con herramientas de observabilidad y monitorización de IAM si se solicita (ID_188_3.PDF, pág. 30).
- Copias de seguridad y restauración proporcionadas por IAM (ID_188_3.PDF, pág. 31).
- No se especifican expresamente RTO/RPO ni pruebas de continuidad en la documentación revisada.

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Auditorías de seguridad por el Ayuntamiento sobre sistemas implantados o utilizados (ID_188_3.PDF, pág. 49).
- Borrado seguro de toda la información al cierre del contrato, con certificado de destrucción (ID_188_3.PDF, pág. 9).
- Confidencialidad: obligación de guardar secreto sobre información y datos a los que se acceda, subsistiendo tras la finalización del contrato (ID_188_3.PDF, pág. 53).
- Seguridad del personal: obligación de proveer equipos de protección individual y cumplir normativa de prevención de riesgos laborales (ID_188_3.PDF, pág. 23, 51).
- No se exige certificación ENS ni ISO 27001 para el adjudicatario; solo cumplimiento de medidas ENS nivel básico (ID_188_3.PDF, pág. 46).

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Incumplimiento de obligaciones esenciales (incluidas las de seguridad, confidencialidad, adscripción de medios, formación, interlocutor único) puede dar lugar a penalidades económicas del 5% o 10% del precio del contrato, según gravedad, o resolución del contrato (ID_188_2.PDF, pág. 76-77).
- Incumplimiento de condiciones de subcontratación: penalidad del 5% del precio del contrato (ID_188_2.PDF, pág. 78).
- Incumplimiento de borrado seguro y entrega de información al cierre: obligación contractual esencial (ID_188_3.PDF, pág. 9).

# 12. Datos no localizados o ambiguos, sin recomendaciones
- No se exige certificación ENS ni ISO 27001 para el adjudicatario, solo cumplimiento de medidas ENS nivel básico.
- No se exige designación de DPO/DPD para el adjudicatario.
- No se especifican plazos de retención de logs ni de conservación de copias de seguridad.
- No se detallan requisitos de RTO/RPO ni pruebas de continuidad.
- No se exige explícitamente SIEM/SOC propio, solo integración con herramientas de IAM si se solicita.
- No se exige SBOM, SAST, DAST, SCA, ni requisitos OWASP específicos.
- No se exige plan de continuidad ni DR detallado.

# 13. Documentos revisados
- ID_188_1.PDF (Documento licitación real)
- ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares y Anexos)
- ID_188_3.PDF (Pliego de Prescripciones Técnicas)
- poc (enlazado desde ID_188_1.PDF, detalle licitación)
- poc (enlazado desde ID_188_1.PDF, perfil contratante)
- poc (enlazado desde ID_188_1.PDF, perfil contratante)
- 147409-2026 (enlazado desde ID_188_1.PDF, anuncio DOUE)
- perfilContratante (enlazado desde ID_188_2.PDF, perfil contratante)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Cumplimiento ENS | Obligación contractual | Nivel básico, medidas del Anexo II ENS | ID_188_3.PDF | 46-47, 11.1 | TEXTO EXTRAIDO |
| Configuración CCN-STIC | Obligación contractual | Guías CCN-STIC adaptadas al Ayuntamiento | ID_188_3.PDF | 47, 11.4 | TEXTO EXTRAIDO |
| Análisis de riesgos ENS | Obligación contractual | Análisis y plan de tratamiento validados | ID_188_3.PDF | 46, 11.3 | TEXTO EXTRAIDO |
| POC de seguridad | Obligación contractual | Designación o justificación | ID_188_3.PDF | 46, 11.2 | TEXTO EXTRAIDO |
| Cifrado información | Obligación contractual | Información no pública en tránsito por redes ajenas | ID_188_3.PDF | 47, 11.6 | TEXTO EXTRAIDO |
| Identidad y autenticación | Obligación contractual | Delegación en identidad corporativa/CL@VE | ID_188_3.PDF | 47, 11.7 | TEXTO EXTRAIDO |
| Control de acceso | Obligación contractual | Mínimo privilegio, necesidad de conocer | ID_188_3.PDF | 48, 11.10 | TEXTO EXTRAIDO |
| Logging actividad | Obligación contractual | Retención suficiente, entrega a requerimiento | ID_188_3.PDF | 49, 11.12 | TEXTO EXTRAIDO |
| Actualizaciones/parches | Obligación contractual | Periódica y continuada, medidas compensatorias | ID_188_3.PDF | 49, 11.13 | TEXTO EXTRAIDO |
| Gestión de incidentes | Obligación contractual | Notificación inmediata, ciclo completo | ID_188_3.PDF | 49, 11.14 | TEXTO EXTRAIDO |
| Subsanación vulnerabilidades | Obligación contractual | Subsanación obligatoria | ID_188_3.PDF | 49, 11.15 | TEXTO EXTRAIDO |
| Auditorías de seguridad | Obligación contractual | Por el Ayuntamiento | ID_188_3.PDF | 49, 11.16 | TEXTO EXTRAIDO |
| Desarrollo seguro | Obligación contractual | Metodologías y buenas prácticas verificables | ID_188_3.PDF | 47, 11.5 | TEXTO EXTRAIDO |
| Borrado seguro | Obligación contractual | Al cierre, certificado de destrucción | ID_188_3.PDF | 9, 3.2 | TEXTO EXTRAIDO |
| Confidencialidad | Obligación contractual | Secreto subsiste tras finalización | ID_188_3.PDF | 53, 15 | TEXTO EXTRAIDO |
| Subcontratación | Condición de ejecución | Permitida salvo tareas críticas, informar y cumplir límites | ID_188_3.PDF | 29, 6.5 | TEXTO EXTRAIDO |
| Cloud pública | Condición de ejecución | Solo Azure, GCP, AWS en EEE | ID_188_3.PDF | 29-30, 33 | TEXTO EXTRAIDO |
| Localización de datos | Condición de ejecución | Regiones EEE | ID_188_3.PDF | 33 | TEXTO EXTRAIDO |
| Transferencias internacionales | Condición de ejecución | No permitidas fuera del EEE | ID_188_3.PDF | 30, 33 | TEXTO EXTRAIDO |
| Penalidades por incumplimiento | Consecuencia contractual | 5% o 10% del precio del contrato según gravedad | ID_188_2.PDF | 76-77 | TEXTO EXTRAIDO |
| Certificación ENS/ISO 27001 | NO EXIGIDO EXPRESAMENTE | Solo cumplimiento ENS básico | ID_188_3.PDF | 46 | TEXTO EXTRAIDO |
| DPO/DPD adjudicatario | NO EXIGIDO EXPRESAMENTE | No requerido | ID_188_3.PDF | 48, 11.18 | TEXTO EXTRAIDO |
| RTO/RPO, SIEM/SOC, SBOM, SAST, DAST, SCA, OWASP | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - | - |

# Discrepancias y pendientes de aclaración
No se han identificado discrepancias en la documentación revisada.