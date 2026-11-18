1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS
- El pliego exige un modelo de migración cloud gestionada con operación estabilizada, SLAs exigentes, procesos ITIL formales y herramientas específicas. La empresa cumple la mayoría de capacidades técnicas, operativas y de procesos, pero presenta gaps en solvencia de equipo (solo un DevOps/cloud senior claro), seguro de RC insuficiente, y referencias de migración cloud en AP parcialmente alineadas. Hay riesgos en dimensionamiento, cobertura 24x7, automatización avanzada de CMDB y cumplimiento de penalizaciones por SLAs críticos.

2. Alcance y dimensionamiento del servicio:
- Servicios incluidos: Migración de 6 aplicaciones municipales a Azure AKS, contenerización, CI/CD, monitorización, backup, hardening, reversibilidad, operación estabilizada 9 meses.
- Sistemas afectados: 6 apps, 18 microservicios, 4 BBDD, 3 entornos/app.
- Usuarios: No especificados (gap relevante para dimensionar Service Desk y soporte).
- Sedes: No detalladas, pero alcance Aragon y modalidad remoto/guardias.
- Horarios: Soporte 12x5, guardia localizada en ventanas de migración (8 fines de semana).
- Presencialidad: Remoto, salvo ventanas críticas.
- Cobertura geográfica: Aragon, remoto para sedes distribuidas.
- Volumetrías: No especificadas (riesgo de infradimensionamiento).
- Impacto: Sin volumetrías ni usuarios, el dimensionamiento de Service Desk, soporte y guardias es incierto. El alcance técnico es alto y requiere perfiles senior dedicados.

3. Modelo de servicio exigido:
- Estructura: No se exige Service Desk N1 tradicional, sino equipo técnico senior (2 DevOps cloud, 1 backend, jefe de proyecto) para migración, operación estabilizada, automatización, monitorización y soporte especializado.
- Operación: Soporte 12x5, guardias en migraciones, gestión de cambios, incidentes críticos, administración cloud, pipelines, CI/CD, hardening, backup, reversibilidad.
- Mantenimiento: Correctivo y preventivo durante estabilización.
- Monitorización: Azure Monitor, Grafana, Prometheus.
- Servicios especializados: Seguridad cloud, escaneo contenedores, SAST/SCA, gestión de vulnerabilidades.

4. Procesos ITIL requeridos:
| Proceso                    | Explicito/Implicito | Evidencia textual                                               | Exigencia        | Capacidad actual         | Gap                         |
|---------------------------|---------------------|-----------------------------------------------------------------|------------------|--------------------------|-----------------------------|
| Change Management         | Explicito           | "Change Management formal con CAB semanal"                      | Formal           | Implantado (CAB ligero)  | Refuerzo CAB formal         |
| Release/Deployment        | Explicito           | "Release/Deployment Management, CI/CD"                         | Formal           | Implantado               | Sin gap relevante           |
| Event Management          | Explicito           | "Event Management, alertas, monitorización"                    | Formal           | Implantado (Azure/Grafana)| Gap en integración cliente  |
| Configuration Management  | Explicito           | "CMDB obligatoria, reconciliación mensual"                     | Formal           | Parcial                  | Gap en reconciliación auto  |
| Availability Management   | Explicito           | "Disponibilidad mínima 99,5%"                                  | Formal           | Parcial                  | Gap en HA y reporting       |
| Incident Management       | Implícito           | "SLA P1/P2, respuesta/resolución, penalizaciones"              | Formal           | Implantado               | Sin gap relevante           |
| Problem Management        | Implícito           | "RCA en 5 días, problemas recurrentes"                         | Formal           | Parcial                  | Gap en KEDB                |
| Knowledge Management      | Implícito           | "Runbooks, documentación, base de conocimiento"                | Formal           | Implantado               | Sin gap relevante           |
| Service Level Management  | Implícito           | "SLA, penalizaciones, reporting"                               | Formal           | Implantado               | Sin gap relevante           |
| Capacity Management       | Implícito           | "Informes de capacidad, reporting"                             | Formal           | Parcial                  | Gap en métricas iniciales   |
| Continuity Management     | Implícito           | "Plan de reversibilidad, backup, contingencia"                 | Formal           | Parcial                  | Gap en DR/BCP formal        |

5. SLA, KPI y penalizaciones:
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo      | Horario | Penalización                  | Capacidad actual         | Gap                        | Riesgo operativo           |
|------------------|-----------|-----------|------------|--------------|---------|------------------------------|--------------------------|----------------------------|----------------------------|
| Migración/Op.    | P1        | <=30 min  | <=4h       | 99,5% disp.  | 12x5    | 2%/mes <99,5%; 1% cambio KO  | Parcial (12x5, no 24x7)  | Riesgo en guardias y P1    | Alto si volumetría alta    |
| Migración/Op.    | P2        | <=2h      | <=1 día    |              | 12x5    |                              | Disponible               | Sin gap relevante          | Medio si backlog alto      |
| Seguridad        | CVE crit. | <=24h     |            |              |         |                              | Disponible               | Sin gap relevante          | Bajo                      |
| Seguridad        | CVE alta  | <=7 días  |            |              |         |                              | Disponible               | Sin gap relevante          | Bajo                      |

6. Modelo de priorización:
- P1: Incidente crítico, afecta servicio productivo, requiere respuesta <=30 min y resolución <=4h.
- P2: Incidente relevante, afecta parcialmente, respuesta <=2h, resolución <=1 día.
- P3/P4: No definidos en pliego (gap). No hay reglas explícitas de impacto x urgencia. Riesgo de ambigüedad en escalado y reporting.

7. Organización y modelo operativo:
- Roles exigidos: 2 DevOps/cloud senior (100% 8 meses), backend senior, jefe de proyecto (35% 10 meses).
- Guardias: Localizadas en ventanas de migración (8 fines de semana).
- Presencialidad: Remoto, salvo migraciones críticas.
- Sustituciones: No detalladas (gap).
- Idiomas: Español (catalán no exigido).
- Certificaciones: CKA, Azure Administrator, ISO 27001.
- Perfiles internos: Ivan Lopez (DevOps), Sofia Martin (backend), Ana Torres (jefe proyecto). Falta un segundo DevOps/cloud senior.

8. Gobierno del servicio:
- Comités: No definidos en pliego, pero habitual: operativo semanal, seguimiento mensual, dirección trimestral.
- Entregables: Informes SLA, KPIs, incidentes, cambios, disponibilidad, riesgos, mejora continua.
- Escalados: No definidos, pero necesarios para incidentes críticos y cambios urgentes.

9. Herramientas ITSM, CMDB y monitorización:
- ITSM: Jira Service Management aceptado, ServiceNow solo si cliente aporta licencias.
- CMDB: Obligatoria, apps, servicios, contenedores, pipelines, BBDD, dependencias, propietarios. Reconciliación mensual.
- Monitorización: Azure Monitor, Grafana, Prometheus.
- Inventario: Discovery inicial, actualización mensual.
- Reporting: Dashboards, informes mensuales.
- Automatización: Repositorio IaC, pipelines CI/CD, escaneo contenedores, SAST/SCA.

10. Transición, toma de control y reversibilidad:
- Fases: 8 semanas transición (inventario, discovery, CMDB, runbooks, backup, simulacro rollback, reverse shadowing), 4 semanas reversibilidad (exportación config, pipelines, IaC, CMDB, tickets, informes capacidad).
- Shadowing/reverse shadowing: Exigido.
- Migración de tickets: Incluida.
- Configuración SLA: Incluida.
- Formación: No detallada (gap).
- Entrega documentación: Incluida.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos (gap relevante).
- Alta disponibilidad: Exigida para 99,5% disponibilidad.
- Backups: Incluidos, pruebas y simulacros.
- Contingencia: Plan de reversibilidad, rollback.
- Accesos: MFA, PAM, bastionado, gestión de secretos, cifrado, network policies, WAF, logs 18 meses.
- ENS: Categoría MEDIA, ISO 27001 exigida.
- Incidentes seguridad: Comunicación <=1h, RCA 5 días, evidencias forenses.

12. Automatización, self-service y mejora continua:
- Exigencias: Automatización CI/CD, escaneo contenedores, SAST/SCA, reporting dashboards.
- Oportunidades: Auto-remediation cloud, scripts, runbooks, base de conocimiento, shift-left, chatbot FAQ (no exigido pero diferenciador).

13. Reporting y gestión del conocimiento:
- Informes: SLA, KPIs, incidentes, cambios, disponibilidad, problemas, mejora continua.
- Cuadros de mando: Grafana, Power BI, Jira dashboards.
- Base de conocimiento: Runbooks, FAQs, manuales, KEDB (recomendado).
- Propiedad documental: Entrega en reversibilidad.

14. Matriz de evaluación Service Design:
| Requisito                        | Exigencia         | Impacto         | Capacidad actual         | Gap                        | Riesgo         | Acción recomendada         | Diferenciación posible     |
|----------------------------------|-------------------|-----------------|--------------------------|----------------------------|----------------|----------------------------|---------------------------|
| 2 DevOps/cloud senior            | Obligatorio       | Crítico         | 1 disponible            | Falta 1 DevOps             | Alto           | Subcontratar/partner       | Certificaciones extra      |
| Backend senior                   | Obligatorio       | Alto            | Disponible              | Ninguno                    | Bajo           |                          |                           |
| Jefe de proyecto senior          | Obligatorio       | Alto            | Disponible              | Ninguno                    | Bajo           |                          |                           |
| Solvencia migraciones cloud      | Obligatorio       | Crítico         | 2 referencias válidas    | Falta 3ª referencia        | Alto           | Buscar partner/referencia  |                           |
| Seguro RC 1,5M EUR               | Obligatorio       | Crítico         | 1M EUR                  | Gap 0,5M EUR               | Alto           | Ampliar póliza             |                           |
| CMDB avanzada                    | Obligatorio       | Alto            | Parcial                  | Gap en reconciliación auto | Medio          | Proyecto específico        | Descubrimiento auto       |
| SLA P1 30min/4h                  | Obligatorio       | Alto            | Parcial                  | Riesgo en guardias         | Alto           | Refuerzo guardias          | Runbooks auto-remediation |
| Disponibilidad 99,5%             | Obligatorio       | Alto            | Parcial                  | Gap en HA                  | Medio          | Arquitectura HA            | Reporting avanzado        |
| ENS media, ISO 27001             | Obligatorio       | Medio           | Cumplido                 | Ninguno                    | Bajo           |                          |                           |

15. Riesgos operativos principales:
1. Falta de segundo DevOps/cloud senior (incumplimiento equipo mínimo, riesgo de exclusión).
2. Seguro de RC insuficiente (1M vs 1,5M EUR exigido).
3. Referencias de migración cloud en AP insuficientes (solo 2 válidas, exige 3).
4. Volumetrías y usuarios no definidos (riesgo de infradimensionamiento y SLA).
5. Gap en automatización avanzada de CMDB y reconciliación.
6. Riesgo de penalizaciones por SLAs críticos (P1, disponibilidad).
7. Ambigüedad en priorización P3/P4 y escalados.
8. RTO/RPO no definidos (riesgo en continuidad y reversibilidad).

16. Modelo operativo recomendado para ofertar:
- Estructura: Equipo mínimo exigido, reforzar con partner para segundo DevOps/cloud senior y seguro RC.
- Roles: Jefe de proyecto (Ana Torres), DevOps (Ivan Lopez + partner), backend (Sofia Martin).
- Procesos: Formalizar CAB semanal, reporting mensual, runbooks, KEDB, simulacros reversibilidad.
- Herramientas: Jira Service Management, Azure Monitor, Grafana, CMDB propia o GLPI, automatización pipelines.
- Gobierno: Comité operativo semanal, seguimiento mensual, dirección trimestral, informes SLA/KPI.
- Transición: 8 semanas con shadowing, discovery, carga CMDB, formación, simulacro rollback.
- Reversibilidad: 4 semanas, entrega documentación, exportación IaC, borrado seguro.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Volumetría de tickets, incidencias, cambios y usuarios afectados por aplicación?
- ¿Detalle de sedes, usuarios y cobertura geográfica real?
- ¿Definición formal de P3/P4 y reglas de priorización impacto x urgencia?
- ¿Herramienta CMDB preferida y alcance de automatización?
- ¿RTO/RPO exigidos en reversibilidad y continuidad?
- ¿Detalle de penalizaciones por incumplimiento de SLAs parciales?
- ¿Requisitos de formación y transferencia de conocimiento?
- ¿Requisitos de reporting y frecuencia de comités?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-003 migración cloud
2. Pliego técnico OPP-SW-003 migración cloud
3. Anexo solvencia OPP-SW-003 migración cloud