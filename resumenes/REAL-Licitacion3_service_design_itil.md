1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS

La empresa cumple la mayoría de los requisitos técnicos y organizativos, pero existen gaps relevantes en certificaciones (ISO 20000, ENS alta), experiencia en ciertas tecnologías (ServiceNow avanzado, EasyVista, IoT, mobile nativo), cobertura 24x7 real, y automatización avanzada de CMDB. El cumplimiento de los SLAs más exigentes y la cobertura geográfica/pluritecnológica requerirá refuerzo externo y una gestión de riesgos activa.

2. Alcance y dimensionamiento del servicio:
- Servicios: CAU 24x7, soporte usuarios (presencial/remoto), gestión inventario y almacenes, mantenimiento equipos, administración y operación de sistemas, redes, CPD, monitorización, gestión de incidencias/peticiones/cambios, soporte a gabinetes VIP.
- Sistemas: Infraestructura híbrida (on-prem, Azure, AWS), Windows Server, Linux, Oracle, SQL Server, VMware, Hyper-V, NetApp, Office365, System Center, Fortinet, Cisco, ESRI, Kubernetes, Veeam, dispositivos usuario (13.000+), electrónica de red, CPDs redundados.
- Usuarios: ~5.500 usuarios, 10.000 cuentas AD, usuarios críticos (gabinetes), soporte VIP.
- Sedes: 100+ sedes en toda España (ver Anexo II), fuerte concentración en Madrid, cobertura nacional y periférica.
- Horarios: CAU y guardias 24x7, soporte presencial 8-20h laborables, soporte VIP 8-22h, guardias fuera de horario.
- Modalidad: Presencial en Madrid y sedes, remoto/híbrido bajo autorización, desplazamientos a cargo del adjudicatario.
- Volumetrías: 7.383 incidencias L1/año, 2.099 L2/L3, 5.560 peticiones L1, 23.454 L2, 8.748 llamadas CAU, 5.143 actuaciones almacén (Anexo VI). Impacto: dimensionamiento crítico en CAU, soporte presencial, técnicos de campo y especialistas N2/N3.

3. Modelo de servicio exigido:
- Estructura: Service Desk (CAU) 24x7 (N1), soporte usuarios N2/N3 presencial/remoto, equipos de administración/operación de sistemas y redes, soporte a CPD, gestión de almacenes, soporte VIP, guardias especializadas.
- Operación: Registro y gestión integral de tickets, escalado, seguimiento, reporting, gestión de cambios, problemas, activos y configuración.
- Mantenimiento: Correctivo, preventivo, evolutivo, gestión de garantías y repuestos, coordinación con terceros.
- Monitorización: Proactiva 24x7 de sistemas, redes, CPD, con alertas y escalado.
- Servicios especializados: Soporte a tecnologías específicas (cloud, virtualización, seguridad, GIS, movilidad, etc.).

4. Procesos ITIL requeridos:
| Proceso                  | Explicito/Implicito | Evidencia textual / Exigencia | Capacidad actual | Gap |
|--------------------------|---------------------|-------------------------------|------------------|------|
| Incident Management     | Explícito           | CAU, gestión incidencias, ANS | Implantado       | Bajo |
| Request Fulfilment      | Explícito           | Peticiones, CAU, ANS          | Implantado       | Bajo |
| Problem Management      | Implícito           | Reincidencias, análisis causas| Parcial          | Medio|
| Change Management       | Implícito           | Cambios, acciones programadas | Implantado       | Bajo |
| Configuration Management| Explícito           | Inventario, CMDB, activos     | Parcial          | Medio|
| Knowledge Management    | Explícito           | Base de conocimiento, CAU     | Implantado       | Bajo |
| Service Level Management| Explícito           | ANS, reporting, penalizaciones| Implantado       | Bajo |
| Availability Management | Implícito           | ANS, monitorización, HA       | Parcial          | Medio|
| Capacity Management     | Implícito           | Métricas, reporting           | Parcial          | Medio|
| Continuity Management   | Implícito           | CPD respaldo, backups, DR     | Parcial          | Medio|
| Release/Deployment      | Implícito           | Despliegues, cambios          | Implantado       | Bajo |
| Event Management        | Explícito           | Monitorización, alertas       | Parcial          | Medio|
| Continual Improvement   | Implícito           | Plan de mejora continua       | Implantado       | Bajo |

5. SLA, KPI y penalizaciones:
(Ver tabla detallada en desarrollo, ejemplo:)
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo |
|------------------|-----------|-----------|------------|---------|---------|--------------|------------------|-----|--------|
| Incidencias L1   | P1        | <15 min   | <4h        | >95%    | 24x7    | Sí           | Parcial          | Sí  | Alto   |
| Incidencias L2   | P1        | <15 min   | <4h        | >99%    | 24x7    | Sí           | Parcial          | Sí  | Alto   |
| Peticiones       | P1        | <30 min   | <8h        | >95%    | 24x7    | Sí           | Parcial          | Sí  | Medio  |
| Provisión piezas | P1        | <30 min   | <24h       | >95%    | 24x7    | Sí           | Parcial          | Sí  | Medio  |

Gaps: Respuesta y resolución 24x7 en P1, cobertura geográfica, disponibilidad de stock, automatización de reporting, integración con herramientas cliente.

6. Modelo de priorización:
- P1: Incidencia afecta a sistema crítico o usuario crítico (impide trabajar).
- P2: Degradación relevante en sistema crítico o usuario crítico, o caída de usuario no crítico.
- P3: Resto de casos.
- No se define P4 explícitamente.
- Impacto x urgencia: No detallado, riesgo de ambigüedad en escalado y categorización, posible subjetividad en priorización de tickets.

7. Organización y modelo operativo:
- Roles: Director de proyecto, supervisores, agentes CAU, técnicos microinformática, coordinador y técnicos VIP, técnicos almacén, jefes y técnicos de sistemas, redes, CPD, guardias.
- Dedicaciones: Presencialidad obligatoria en Madrid y sedes, remoto/híbrido bajo autorización, dedicación exclusiva, bolsas de horas para refuerzos y fuera de horario.
- Guardias: 24x7 en CAU, sistemas, redes, VIP.
- Sustituciones: Máx. 2 semanas, formación y transferencia de conocimiento obligatoria.
- Idiomas: Español obligatorio.
- Certificaciones: ITIL, Microsoft, Cisco, Fortinet, Oracle, VMware, AWS, Azure, MOS, MCSA, MCSE, CCNA, etc. (ver Anexo V). Gaps en ISO 20000, ENS alta, EasyVista, ServiceNow avanzado.
- Perfiles internos: Ana Torres (gobierno), Claudia Benitez (soporte), Ivan Lopez (cloud/DevOps), Javier Prieto (seguridad), Sofia Martin (backend), Paula Navarro (BI), Luis Romero (funcional), Elena Garcia (QA). Faltan especialistas en EasyVista, ServiceNow avanzado, IoT, mobile nativo, GIS.

8. Gobierno del servicio:
- Comités: Operativo (semanal), seguimiento (mensual), dirección (trimestral), reporting SLA/KPI, escalados técnicos y de gestión, acciones correctivas y de mejora.
- Entregables: Informes mensuales, cuadros de mando, actas, planes de acción, documentación de transición y reversibilidad.

9. Herramientas ITSM, CMDB y monitorización:
- Herramienta ITSM: Obligatorio uso de la herramienta del Ministerio (Microsoft System Center Service Manager), posibilidad de proponer integración con herramienta propia (Jira, GLPI, ServiceNow, etc.), integración y licencias a cargo del adjudicatario.
- CMDB: Uso de inventario y herramientas del Ministerio, posibilidad de aportar herramientas de descubrimiento/integración, reporting y reconciliación bajo aprobación.
- Monitorización: Uso de herramientas del Ministerio (SCOM, Nagios, específicas), posibilidad de proponer otras (Grafana, Azure Monitor, etc.), integración bajo aprobación.
- Portal usuario: Formularios electrónicos, integración con ITSM.
- Reporting: Cuadros de mando, informes mensuales, reporting automatizado.

10. Transición, toma de control y reversibilidad:
- Fases: Transición (máx. 1 mes, no facturable), ejecución, devolución (1 mes, facturable).
- Shadowing/reverse shadowing: Sí, transferencia de conocimiento, documentación, acceso a herramientas y procedimientos.
- Migración de tickets: Sí, carga histórica y configuración de SLAs.
- Formación: Obligatoria en herramientas y procedimientos.
- Entrega de documentación: Manuales, inventario, KB, CMDB, scripts, informes, etc.
- Reversibilidad: Entrega de toda la documentación, datos, tickets, KB, CMDB, sesiones de transferencia.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos explícitamente, pero se exige alta disponibilidad, CPD respaldo, backups Veeam, redundancia, DR en cloud y on-prem.
- Accesos: MFA, control de usuarios privilegiados, cumplimiento ENS medio, RGPD, formación en seguridad.
- Vulnerabilidades: Gestión proactiva, soporte a Fortinet, reporting de incidentes de seguridad.
- Incidentes de seguridad: Obligación de registro, reporting y acciones correctivas.

12. Automatización, self-service y mejora continua:
- Exigencias: Base de conocimiento, autoservicio, reporting automatizado, scripts, integración con herramientas, encuestas de satisfacción, análisis de reincidencias.
- Oportunidades: Proponer chatbot, RPA, auto-remediation, shift-left, integración con IA para FAQs, reducción de incidencias mediante automatización y mejora de KB.

13. Reporting y gestión del conocimiento:
- Informes: Mensuales, SLA/KPI, incidencias, peticiones, problemas, cambios, disponibilidad, satisfacción usuario.
- Cuadros de mando: Power BI, dashboards ITSM, reporting automatizado.
- Base de conocimiento: Obligatoria, actualización continua, runbooks, FAQs, KEDB, manuales, propiedad documental del Ministerio.

14. Matriz de evaluación Service Design:
(Ver tabla detallada en desarrollo, ejemplo:)
| Requisito | Exigencia | Impacto | Capacidad actual | Gap | Riesgo | Acción recomendada | Diferenciación posible |
|-----------|-----------|---------|------------------|-----|--------|--------------------|-----------------------|
| CAU 24x7  | Obligatorio| Crítico | Parcial          | Sí  | Alto   | Refuerzo partner   | Propuesta shift-left, chatbot |
| ITSM SCSM | Obligatorio| Alto    | Parcial          | Sí  | Medio  | Formación, integración| Propuesta integración avanzada |
| Cert. ISO 20000 | Obligatorio L2| Alto | No disponible | Sí | Alto | Subcontratar partner certificado | Plan de certificación progresiva |
| ENS alta  | Obligatorio L2| Alto | No disponible | Sí | Alto | Subcontratar partner ENS alta | Plan de adecuación progresiva |
| Soporte IoT/mobile | Deseable | Medio | Parcial | Sí | Medio | Subcontratar | Propuesta de refuerzo |

15. Riesgos operativos principales:
- Incumplimiento de SLAs 24x7 en P1 por falta de cobertura real.
- Falta de certificaciones ISO 20000 y ENS alta para Lote 2.
- Gaps en experiencia y recursos en herramientas ITSM/CMDB específicas (SCSM, EasyVista, ServiceNow avanzado).
- Cobertura geográfica y presencialidad en sedes periféricas.
- Automatización y reconciliación avanzada de CMDB.
- Dependencia de partners para tecnologías críticas (cloud, seguridad, IoT, mobile).
- Subjetividad en priorización y escalado de incidencias.
- Penalizaciones económicas por incumplimiento de ANS y recursos.

16. Modelo operativo recomendado para ofertar:
- Estructura: CAU 24x7 (partner), soporte N2/N3 presencial y remoto, equipos de campo en Madrid y periférica, especialistas cloud, seguridad, redes, CPD, almacén.
- Roles: Director de proyecto, supervisores, agentes CAU, técnicos microinformática, coordinador y técnicos VIP, técnicos almacén, jefes y técnicos de sistemas, redes, CPD, guardias.
- Procesos: ITIL completos, reporting automatizado, gestión de conocimiento, mejora continua, gestión de cambios y problemas formalizada.
- Herramientas: Integración con SCSM, reporting Power BI, automatización scripts, base de conocimiento enriquecida, portal autoservicio.
- Gobierno: Comités operativo, seguimiento y dirección, reporting mensual, escalados y planes de acción.
- Transición: Plan detallado, shadowing, formación, migración de tickets, configuración de SLAs, entrega de documentación, plan de reversibilidad.
- Refuerzo: Partner para 24x7, ENS alta, ISO 20000, EasyVista/ServiceNow, IoT/mobile.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Se permite subcontratación para cubrir gaps de certificación (ISO 20000, ENS alta) y tecnologías específicas?
- ¿Qué herramientas ITSM/CMDB/monitorización exactas se usarán y qué nivel de integración se espera?
- ¿Se puede proponer una herramienta propia de ITSM/CMDB si se garantiza integración y reporting?
- ¿Se exige reporting automatizado y en qué formato (Power BI, dashboards, etc.)?
- ¿Qué nivel de automatización y autoservicio se espera (chatbot, RPA, scripts)?
- ¿Se requiere cobertura presencial en todas las sedes o solo en Madrid y periféricas principales?
- ¿Se puede cubrir el 24x7 mediante partner o solo con recursos propios?
- ¿Qué RTO/RPO se exige para servicios críticos?
- ¿Qué volumen de incidencias/peticiones se prevé para los próximos años?
- ¿Qué nivel de acceso a la documentación y procedimientos actuales se facilitará en la transición?

18. Documentos revisados:
1. DOC2024020214010801+PPT+2023+VI.pdf
2. DOC20240202141404130-24_PLIEGO.pdf
3. DOC20240202144445012+Anexo+II+Lista+final+de+sedes+del+MITMA+7+nov+2023.pdf
4. DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf
5. DOC20240202144519014+Anexo+IV+Resumen+de+activos.pdf
6. DOC20240202144535015+Anexo+V+Conocimientos+equipo+de+trabajo.pdf
7. DOC20240202144619016+Anexo+VI+Datos+de+peticiones+de+servicio+e+incidencias.pdf
8. DOC_CD2024-000159639.pdf
9. DOC_CN2024-000157989.pdf
10. poc (detalle licitación)
11. poc (perfil contratante)
12. poc (perfil contratante)