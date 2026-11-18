1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS

La empresa cumple la mayoria de requisitos tecnicos y de procesos ITIL para el servicio exigido, pero existen gaps en madurez de Problem/Configuration Management, cobertura 24x7, automatizacion avanzada y reporting ENS. El dimensionamiento es viable, pero el cumplimiento estricto de SLA y ENS MEDIA requiere atencion especial.

2. Alcance y dimensionamiento del servicio:
- Servicios: Desarrollo, despliegue y soporte postarranque (6 meses) del portal ciudadano, APIs, integraciones, gestor documental, registro y pagos.
- Sistemas: Portal web (React), backend (Java/Python), APIs REST, cloud Azure DEV/PRE/PRO, integraciones con sistemas municipales.
- Usuarios: 450 empleados públicos, hasta 25.000 ciudadanos potenciales.
- Sedes: Sede municipal (presencialidad puntual, 4 jornadas de arranque), resto remoto.
- Horarios: Soporte 8x5 remoto postarranque.
- Modalidad: Remoto, con presencialidad puntual.
- Cobertura: Comunidad de Madrid, acceso remoto.
- Volumetrias: 120 tickets/mes (2 meses), 60 tickets/mes estabilizado.
- Impacto: Dimensionamiento ajustado, equipo mínimo suficiente, riesgo si el volumen real supera lo estimado.

3. Modelo de servicio exigido:
- Estructura: Soporte N2/N3 aplicacional (no N1 ni Service Desk generalista), gestión de incidencias, peticiones, cambios menores y problemas.
- Operación: Sin monitorización 24x7, pero sí reporting y gestión de eventos críticos.
- Mantenimiento: Correctivo y evolutivo menor durante soporte.
- Servicios especializados: Ciberseguridad (ENS, OWASP, pentest), formación, gestión de cambios.

4. Procesos ITIL requeridos:
| Proceso                  | Explicito/Implicito | Evidencia textual                                               | Exigencia         | Capacidad actual         | Gap                  |
|--------------------------|---------------------|-----------------------------------------------------------------|-------------------|--------------------------|----------------------|
| Incident Management      | Explícito           | "gestión de incidencias"                                        | Obligatorio       | Implantado               | Ninguno              |
| Request Fulfilment       | Explícito           | "peticiones estándar"                                          | Obligatorio       | Implantado               | Ninguno              |
| Problem Management       | Implícito           | "problemas recurrentes"                                        | Recomendado       | Parcial                  | Madurez KEDB        |
| Change Management        | Explícito           | "gestión de cambios menores"                                   | Obligatorio       | Implantado               | Ninguno              |
| Configuration Management | Implícito           | "entrega de configuración, base de conocimiento"               | Recomendado       | Parcial                  | CMDB limitada        |
| Knowledge Management     | Implícito           | "base de conocimiento, runbooks"                               | Recomendado       | Implantado               | Ninguno              |
| Service Level Management | Explícito           | "SLA, penalización, reporting mensual"                         | Obligatorio       | Implantado               | Ninguno              |
| Availability Management  | Implícito           | "alta disponibilidad, backups, WAF, logs"                      | Recomendado       | Parcial                  | En legacy            |
| Capacity Management      | Implícito           | "dimensionamiento, volumetrías"                                | Recomendado       | Parcial                  | Métricas de entrada  |
| Continuity Management    | Implícito           | "backups, contingencia, reversibilidad"                        | Recomendado       | Parcial                  | DR/BCP bajo proyecto |
| Release/Deployment       | Implícito           | "plan de despliegue, CI/CD"                                    | Recomendado       | Implantado               | Ninguno              |
| Event Management         | Implícito           | "reporting de eventos críticos"                                | Recomendado       | Implantado (cloud)       | Parcial en cliente   |
| Continual Improvement    | Implícito           | "acciones de mejora, backlog"                                  | Recomendado       | Implantado               | Ninguno              |

5. SLA, KPI y penalizaciones:
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap                | Riesgo operativo           |
|------------------|-----------|-----------|------------|----------|---------|--------------|------------------|--------------------|----------------------------|
| Incidencias P1   | P1        | <=30 min  | <=4h       | 95%      | 8x5     | 1% mensual   | Disponible       | Ninguno            | Riesgo si volumen alto     |
| Incidencias P2   | P2        | <=2h      | <=2 días   | 95%      | 8x5     | 1% mensual   | Disponible       | Ninguno            | Bajo                      |
| Peticiones       | -         | -         | <=5 días   | 95%      | 8x5     | 1% mensual   | Disponible       | Ninguno            | Bajo                      |
| Seguridad        | P1        | <=2h      | <=48h      | 100%     | 8x5     | 1% mensual   | Disponible       | Ninguno            | Medio (ENS, brechas)      |

6. Modelo de priorización:
- P1: Incidencias críticas (servicio caído, datos personales expuestos, pagos bloqueados).
- P2: Incidencias importantes (funcionalidad degradada, impacto parcial).
- P3/P4: No definidos explícitamente, riesgo de ambigüedad en priorización de peticiones menores.
- Impacto x urgencia: No detallado, se recomienda clarificar con el cliente.
- Riesgo: Ambigüedad en escalado de P1/P2 si no se documenta bien en la base de conocimiento.

7. Organización y modelo operativo:
- Roles exigidos: Jefe de proyecto (PMP), backend senior, frontend, QA, ciberseguridad ENS/OWASP.
- Dedicaciones: 35% jefe proyecto, 80% backend, 80% frontend, 45% QA, 20% ciberseguridad.
- Guardias: Solo para despliegue, no para soporte 24x7.
- Presencialidad: 4 jornadas de arranque, resto remoto.
- Sustituciones: No detalladas, riesgo en bajas imprevistas.
- Idiomas: Español (suficiente), catalán no requerido.
- Certificaciones: PMP/Scrum Master, WCAG, ITIL (no exigida formalmente).
- Perfiles internos: Todos cubiertos salvo posible refuerzo en QA/ciberseguridad si hay picos.

8. Gobierno del servicio:
- Comité operativo: Semanal (2 meses), luego mensual.
- Informes: SLA, backlog, incidencias, cambios, acciones de mejora.
- Escalados: No detallados, se recomienda definir rutas de escalado y responsables.

9. Herramientas ITSM, CMDB y monitorización:
- ITSM: Jira Service Management (obligatorio, 5 agentes), aceptado por el cliente.
- Integraciones: No exigidas, pero posible API con sistemas municipales.
- Portal: Incluido en Jira SM.
- Inventario/CMDB: No exigido, pero recomendable para control de CIs críticos.
- Monitorización: Azure Monitor/Grafana para cloud, no exigida para el portal.
- Reporting: Power BI Pro (3 usuarios), informes mensuales.

10. Transición, toma de control y reversibilidad:
- Fases: 4 semanas transición (formación, runbooks, alta usuarios, configuración SLA, KB inicial), 2 semanas reversibilidad (entrega documentación, tickets, repositorios, configuración, KB).
- Shadowing/reverse shadowing: No exigido, pero recomendable para asegurar transferencia de conocimiento.
- Migración de tickets: No aplicable (servicio nuevo).

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos, riesgo si el cliente exige valores estrictos.
- Alta disponibilidad: Exigida en cloud Azure, WAF, backups diarios, logs 12 meses.
- Contingencia: Backups cifrados, MFA, RBAC, cuentas nominativas.
- Vulnerabilidades: SAST/SCA, pentest previo a producción, corrección vulnerabilidades críticas <=48h.
- ENS/RGPD: ENS MEDIA obligatorio, DPO, anexo encargado tratamiento, comunicación de incidentes <=2h.

12. Automatización, self-service y mejora continua:
- Exigencias: No obligatorias, pero Jira SM permite portal self-service, base de conocimiento y automatización básica.
- Oportunidades: Chatbot FAQ, scripts de auto-remediación, RPA ligero, reporting automatizado.

13. Reporting y gestión del conocimiento:
- Informes: Mensuales, SLA, backlog, incidencias, cambios, acciones de mejora.
- Cuadros de mando: Power BI, Jira dashboards.
- Base de conocimiento: Requerida, runbooks, manuales, FAQs.
- Propiedad documental: Entrega al cliente en reversibilidad.

14. Matriz de evaluación Service Design:
(Se adjunta tabla en respuesta extendida por límite de espacio)

15. Riesgos operativos principales:
- Volumen real de tickets superior al estimado.
- Ambigüedad en priorización P1/P2.
- Incumplimiento de SLA por picos de demanda o bajas no cubiertas.
- Gaps en madurez Problem/Configuration Management.
- Requisitos ENS MEDIA no cubiertos en toda la cadena (partners, cloud, soporte).
- Penalizaciones económicas por incumplimiento de SLA.

16. Modelo operativo recomendado para ofertar:
- Estructura: Equipo mínimo exigido, refuerzo puntual QA/ciberseguridad si hay picos.
- Procesos: ITIL implantados, madurar KEDB y CMDB básica para CIs críticos.
- Herramientas: Jira SM, Power BI, Azure Monitor.
- Gobierno: Comité operativo/mensual, reporting detallado, rutas de escalado claras.
- Transición: Plan detallado, shadowing, formación, KB inicial robusta.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Se confirmarán volumetrías reales de tickets/incidencias tras arranque?
- ¿Se aceptan equivalentes a Jira SM y Power BI?
- ¿Se exige CMDB formal o solo inventario básico?
- ¿Qué RTO/RPO se espera para el portal y backups?
- ¿Cómo se priorizan peticiones menores (P3/P4)?
- ¿Se permite automatización avanzada (chatbot, RPA) en el portal de soporte?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-001 portal ciudadano
2. Pliego técnico OPP-SW-001 portal ciudadano
3. Anexo solvencia OPP-SW-001 portal ciudadano