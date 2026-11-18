1. Veredicto ejecutivo Service Design / ITIL: ALTO RIESGO

El pliego exige un servicio gestionado IoT 24x7 con ENS ALTA, SOC, SIEM, CMDB avanzada, SLA críticos y equipo experto en IoT, Node.js tiempo real y GIS. La empresa no cumple los perfiles clave internos ni las referencias de solvencia técnica, y tiene limitaciones en 24x7, ENS ALTA, CMDB automática y experiencia IoT/GIS. El gap es estructural y no subsanable solo con refuerzo puntual.

2. Alcance y dimensionamiento del servicio:
- Servicios: Operación gestionada IoT 24x7, monitorización, Service Desk, N1/N2/N3, mantenimiento, administración, seguridad, integración, pruebas de campo, soporte a sensores y gateways, gestión de alertas, API, dashboard GIS, backup, continuidad, reversibilidad.
- Sistemas: Plataforma IoT cloud, 1.500 sensores, 12 gateways, dashboard GIS, API, SIEM/SOC, CMDB, backup, almacenamiento cloud UE.
- Usuarios: Operadores municipales, técnicos de campo, responsables de seguridad, usuarios de API y dashboard.
- Sedes: 8 distritos urbanos, 25 ubicaciones para pruebas, cobertura Andalucía.
- Horarios: 24x7 para operación, monitorización y soporte crítico.
- Modalidad: Remoto + presencial para pruebas/instalación.
- Volumetrías: 5.000 mensajes/minuto, históricos 36 meses, alertas <30s, 40 visitas presenciales mínimas.
- Impacto: Requiere dimensionamiento realista de turnos, guardias, soporte 24x7, capacidad cloud, almacenamiento, backup, desplazamientos y gestión de incidencias críticas.

3. Modelo de servicio exigido:
- Service Desk 24x7 integrado con herramienta municipal.
- N1: Operación y monitorización IoT.
- N2: Soporte IoT/GIS especializado.
- N3: Soporte plataforma, desarrollo, DevOps, seguridad.
- Guardias y turnos para 24x7 real.
- Servicios gestionados: monitorización, administración, mantenimiento, seguridad, continuidad, reversibilidad.

4. Procesos ITIL requeridos:
| Proceso                  | Explicito/Implicito | Evidencia textual/pliego         | Exigencia | Capacidad actual | Gap |
|--------------------------|---------------------|----------------------------------|-----------|------------------|-----|
| Incident Management      | Explicito           | "ITIL formal requerido..."       | Obligatorio 24x7 | Parcial (no 24x7 real) | Sí |
| Event Management         | Explicito           | "monitorización 24x7..."         | Obligatorio | Parcial | Sí |
| Change Management        | Explicito           | "ITIL formal requerido..."       | Obligatorio | Sí | No |
| Configuration Management | Explicito           | "CMDB obligatoria..."            | Obligatorio, auto-discovery | Parcial | Sí |
| Availability Management  | Explicito           | "Disponibilidad 99,9%..."        | Obligatorio | Parcial | Sí |
| Continuity Management    | Explicito           | "RTO 2h, RPO 15min..."           | Obligatorio | Parcial | Sí |
| Service Level Management | Implícito           | "SLA, penalizaciones..."         | Obligatorio | Sí | No |
| Knowledge Management     | Implícito           | "Base de conocimiento..."        | Recomendado | Sí | No |
| Problem Management       | Implícito           | "RCA, problemas recurrentes..."  | Recomendado | Parcial | Sí |

5. SLA, KPI y penalizaciones:
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo operativo |
|------------------|-----------|-----------|------------|----------|---------|--------------|------------------|-----|------------------|
| Ingesta masiva   | P1        | ≤15 min   | ≤2h        | 99,9%    | 24x7    | 4%-15%/mes   | No 24x7 real     | Sí  | Muy alto         |
| Pérdida distrito | P2        | ≤30 min   | ≤4h        | 99,9%    | 24x7    | No explícita | Parcial          | Sí  | Alto             |
| Alertas          | P1        | <30s      | N/A        | 98%      | 24x7    | No explícita | Parcial          | Sí  | Alto             |
| Monitorización   | P1        | ≤15 min   | ≤2h        | 99,9%    | 24x7    | 10%/mes      | Parcial          | Sí  | Muy alto         |

6. Modelo de priorización:
- P1: Pérdida masiva de ingesta, monitorización, ciberseguridad.
- P2: Pérdida parcial (distrito).
- P3/P4: No definidos, riesgo de ambigüedad en escalado y gestión de backlog.
- Impacto x urgencia: No detallado, riesgo de interpretación y priorización subjetiva.

7. Organización y modelo operativo:
- Roles exigidos: Arquitecto IoT, DevOps, Node.js tiempo real, GIS, técnico de campo, responsable de seguridad.
- Dedicaciones: 25%-70% según rol, guardias 24x7.
- Presencialidad: Pruebas y despliegues en campo, resto remoto.
- Sustituciones: No detalladas.
- Idiomas: Español.
- Certificaciones: ENS ALTA, ITIL formal, experiencia smart city.
- Perfiles internos: Solo DevOps (Ivan) encaja parcialmente. Faltan IoT, Node.js tiempo real, GIS y experiencia smart city reciente.

8. Gobierno del servicio:
- Comités: Operativo semanal, seguimiento mensual, dirección trimestral.
- Entregables: Informes SLA, KPI, incidencias, problemas, cambios, disponibilidad, mejora continua.
- Escalados: No detallados, pero necesarios para 24x7 y penalizaciones.

9. Herramientas ITSM, CMDB y monitorización:
- ITSM: Integración obligatoria con herramienta municipal (no especificada).
- CMDB: Obligatoria, auto-discovery, reconciliación semanal, CIs sensores, gateways, cloud, GIS, APIs.
- Monitorización: 24x7, SIEM, SOC, EDR, logs inmutables, alertas automáticas.
- Reporting: SLA, KPI, disponibilidad, incidentes, problemas.

10. Transición, toma de control y reversibilidad:
- Fases: Shadowing, inventario, carga KB, configuración SLA, formación, pruebas, migración histórica, entrega de documentación.
- Duración: No detallada, pero reversibilidad 8 semanas.
- Reversibilidad: Exportación histórica, CMDB, reglas, dashboards, borrado seguro, certificado de destrucción.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO: 2h, RPO: 15min, backup diario, prueba trimestral.
- Alta disponibilidad: 99,9% cloud, redundancia, segmentación.
- Accesos: MFA, PAM, logs, RBAC, hardening, rotación de claves.
- ENS ALTA: Obligatorio, SOC 24x7, SIEM, EDR, SBOM, cadena de suministro.
- Incidentes: P1 ciberseguridad ≤30min, contención ≤2h, RCA ≤5d, brecha datos ≤1h.

12. Automatización, self-service y mejora continua:
- Exigencias: Auto-discovery CMDB, alertas automáticas, reporting, backup, borrado seguro.
- Oportunidades: Chatbot, scripts, RPA, auto-remediation, shift-left, base de conocimiento, reducción de incidencias.

13. Reporting y gestión del conocimiento:
- Informes: SLA, KPI, tickets, problemas, cambios, disponibilidad, mejora continua.
- Cuadros de mando: Power BI, Grafana, dashboards.
- Base de conocimiento: Obligatoria para operación y reversibilidad.
- Manuales y runbooks: Requeridos.

14. Matriz de evaluación Service Design:
(Ver siguiente respuesta por límite de espacio)

15. Riesgos operativos principales:
- Incapacidad de cumplir 24x7 real y SLA críticos sin refuerzo externo.
- Falta de perfiles clave (IoT, Node.js tiempo real, GIS) y referencias smart city.
- ENS ALTA y SOC 24x7 fuera de alcance interno.
- CMDB auto-discovery y reconciliación avanzada no disponible.
- Penalizaciones severas por indisponibilidad y SLA incumplidos.
- Riesgo de subcontratación excesiva y dependencia de partners.
- Coste y margen erosionados por hardware, cloud, seguridad y guardias.

16. Modelo operativo recomendado para ofertar:
- UTE o subcontratación con partners expertos en IoT, GIS, ENS ALTA y SOC.
- Refuerzo de Service Desk y N1/N2 24x7 con partner.
- Herramienta ITSM compatible con integración municipal.
- CMDB y monitorización con partner especializado.
- Plan de transición y reversibilidad detallado.
- Gobierno con comités y reporting formal.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Qué herramienta ITSM y CMDB usa el cliente? ¿Integración vía API?
- ¿Volumetría real de tickets, incidencias, cambios y llamadas?
- ¿Detalle de turnos, guardias y presencialidad exigida?
- ¿Requisitos de formación, sustituciones y backup de roles?
- ¿Detalle de penalizaciones por cada SLA y prioridad?
- ¿Requisitos de reporting y frecuencia de comités?
- ¿Alcance exacto de ENS ALTA y SIEM/SOC?
- ¿Requisitos de reversibilidad y exportación de datos?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-009 IoT smart city
2. Pliego técnico OPP-SW-009 IoT smart city
3. Anexo solvencia OPP-SW-009 IoT smart city