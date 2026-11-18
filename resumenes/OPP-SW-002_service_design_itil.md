1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS

La empresa cumple la mayoria de requisitos tecnicos y organizativos, pero existen gaps relevantes en SLA criticos, CMDB avanzada, cobertura 24x7, y experiencia ServiceNow avanzada. El riesgo operativo es gestionable si se refuerzan recursos y se planifica la transicion.

2. Alcance y dimensionamiento del servicio:
- Servicios: Operacion y soporte de plataforma IA documental (RAG/NLP), monitorizacion, gestion de incidencias, cambios, reindexacion, mejora continua, formacion y seguridad.
- Sistemas: Plataforma IA, pipelines, embeddings, vector DB, APIs, monitorizacion, almacenamiento documental, logs.
- Usuarios: 1.200 empleados publicos.
- Sedes: No se especifican; cobertura Comunitat Valenciana, modalidad remota con posible presencialidad puntual.
- Horarios: 12x5 para SLA criticos, soporte y operacion.
- Volumetrias: 80.000 documentos iniciales, +5.000/mes; consumo IA 3M tokens/mes; no se detallan tickets/incidencias.
- Impacto: Dimensionamiento N2/N3 especializado, refuerzo en DevOps y seguridad, soporte a crecimiento documental y picos de uso.

3. Modelo de servicio exigido:
- Service Desk: Uso de herramienta del cliente (ServiceNow), soporte N2/N3 especializado propio.
- Operacion: Monitorizacion pipelines, gestion de cambios, reindexacion, mejora continua.
- Mantenimiento: Correctivo y evolutivo sobre IA, pipelines y conectores.
- Monitorizacion: Proactiva, con paneles y alertas.
- Servicios especializados: IA, NLP, seguridad, gobierno del dato.

4. Procesos ITIL requeridos:
| Proceso                | Explicito/Implicito | Evidencia textual                                               | Exigencia         | Capacidad actual         | Gap                  |
|------------------------|---------------------|-----------------------------------------------------------------|-------------------|--------------------------|----------------------|
| Incident Management    | Explicito           | "gestion de incidencias funcionales y tecnicas"                | Obligatoria       | Implantado               | Bajo                 |
| Request Fulfilment     | Implicito           | "gestion de cambios de prompts, reindexacion"                  | Recomendado       | Implantado               | Bajo                 |
| Problem Management     | Implicito           | "mejora continua del modelo"                                   | Recomendado       | Parcial                  | Medio                |
| Change Management      | Explicito           | "gestion de cambios de prompts"                                | Obligatoria       | Implantado               | Bajo                 |
| Configuration Mgmt     | Explicito           | "CMDB limitada a servicios, pipelines, indices, modelos"       | Obligatoria       | Parcial                  | Medio                |
| Knowledge Management   | Explicito           | "registro de trazabilidad, panel de evaluacion"                | Obligatoria       | Implantado               | Bajo                 |
| Service Level Mgmt     | Explicito           | "SLA: indisponibilidad..."                                     | Obligatoria       | Implantado               | Bajo                 |
| Availability Mgmt      | Explicito           | "objetivo 97%..."                                              | Obligatoria       | Parcial                  | Medio                |
| Capacity Mgmt          | Implicito           | "crecimiento documental, consumo tokens"                       | Recomendado       | Parcial                  | Medio                |
| Continuity Mgmt        | Explicito           | "RTO 4h, RPO 24h, prueba restauracion"                         | Obligatoria       | Parcial                  | Medio                |
| Release/Deployment     | Implicito           | "despliegues cloud, pipelines"                                 | Recomendado       | Implantado               | Bajo                 |
| Event Management       | Explicito           | "monitorizacion de pipelines, alertas"                         | Obligatoria       | Implantado               | Bajo                 |
| Continual Improvement  | Explicito           | "backlog de mejora continua"                                   | Obligatoria       | Implantado               | Bajo                 |

5. SLA, KPI y penalizaciones:
| Servicio         | Prioridad | Respuesta | Resolucion | Objetivo | Horario | Penalizacion | Capacidad actual | Gap | Riesgo operativo |
|------------------|-----------|-----------|------------|----------|---------|--------------|------------------|-----|------------------|
| Buscador IA      | P1        | <=15 min  | <=2h       | 97%      | 12x5    | Hasta 5% mes | Parcial          | Medio| Alto (SLA critico)|
| Respuesta IA err | P2        | <=1h      | <=1 dia    | 97%      | 12x5    | Hasta 5% mes | Disponible       | Bajo | Medio            |
| Reindexacion     | P1        | -         | <=8h       | 97%      | 12x5    | Hasta 5% mes | Disponible       | Bajo | Bajo             |
| Brecha seg.      | P1        | <=1h      | Remediar 48h| 100%    | 24x7    | No detalla   | Parcial          | Medio| Alto             |

6. Modelo de priorizacion:
- P1: Indisponibilidad buscador IA, brechas de seguridad.
- P2: Errores de respuesta IA con impacto alto.
- P3/P4: No definidos, ambigüedad en catalogo de incidencias menores.
- Impacto x urgencia: No detallado, riesgo de interpretacion en priorizacion y escalado.

7. Organizacion y modelo operativo:
- Roles exigidos: Responsable proyecto, especialista IA, backend, datos, DevOps, ciberseguridad.
- Dedicaciones: IA 100%, backend 70%, datos 80%, DevOps 40%, ciberseguridad 20%.
- Guardias: No exigidas, pero SLA critico requiere refuerzo horario.
- Presencialidad: Remoto, posible presencialidad puntual.
- Sustituciones: No detalladas.
- Idiomas: Español, posible valenciano.
- Certificaciones: ISO 27001, ENS medio.
- Perfiles internos: Todos cubiertos salvo posible refuerzo en ServiceNow y guardias.

8. Gobierno del servicio:
- Comite operativo semanal, comite calidad IA mensual, comite direccion trimestral.
- Entregables: Backlog mejora, informes SLA/KPI, riesgos, evaluacion IA, auditorias.
- Escalados: No detallados, pero implicitos en comites y SLA.

9. Herramientas ITSM, CMDB y monitorizacion:
- ITSM: ServiceNow cliente via API, experiencia media interna.
- CMDB: Limitada a servicios, pipelines, indices, modelos, conectores.
- Monitorizacion: Proactiva, paneles y alertas; Azure Monitor, Grafana compatibles.
- Reporting: Dashboard evaluacion IA, informes SLA/KPI.

10. Transicion, toma de control y reversibilidad:
- Fases: Shadowing, configuracion, migracion, formacion, entrega documentacion.
- Duracion: 4-6 semanas (estandar), 8-12 si CMDB avanzada.
- Reversibilidad: Entrega de documentacion, datos, tickets, KB, CMDB, codigo.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO 4h, RPO 24h, prueba restauracion semestral.
- Backups, HA cloud, MFA, RBAC, logs 24 meses, pentest, SAST/SCA, SBOM.
- ENS medio, RGPD, EIPD, control subencargados, prohibido transferencias fuera UE.

12. Automatizacion, self-service y mejora continua:
- Oportunidades: Chatbot, scripts, auto-remediation cloud, base de conocimiento, paneles self-service.
- Exigencias: No explicitas, pero recomendables para eficiencia y SLA.

13. Reporting y gestion del conocimiento:
- Informes SLA/KPI, evaluacion IA, riesgos, auditorias, cuadros de mando.
- Base de conocimiento, runbooks, manuales, propiedad compartida.

14. Matriz de evaluacion Service Design:
(Se adjunta tabla en respuesta extendida por limite de espacio)

15. Riesgos operativos principales:
- Incumplimiento SLA critico (P1 <=15min/2h) por dimensionamiento o falta de guardias.
- Gap en CMDB avanzada y ServiceNow si se exige administracion profunda.
- Riesgo de penalizaciones por precision IA, trazabilidad o disponibilidad.
- Riesgo por incremento de costes cloud/IA no cubiertos por revision de precios.
- Ambigüedad en priorizacion P3/P4 y catalogo de incidencias.

16. Modelo operativo recomendado para ofertar:
- Estructura: N2/N3 especializado, refuerzo horario en picos, soporte remoto, ServiceNow via API.
- Roles: Responsable proyecto, IA, backend, datos, DevOps, ciberseguridad, soporte ServiceNow externo si necesario.
- Procesos: ITIL implantados, refuerzo en Problem, Configuration y Availability.
- Herramientas: Jira Service Management para internos, ServiceNow cliente, Azure Monitor/Grafana.
- Gobierno: Comites y reporting segun pliego, backlog mejora continua.
- Transicion: Shadowing, formacion, entrega documentacion, plan reversibilidad.

17. Preguntas o aclaraciones al organo de contratacion:
- ¿Detalle de volumetrias de tickets/incidencias por tipo y prioridad?
- ¿Catalogo de servicios/incidencias P3/P4 y reglas de priorizacion?
- ¿Nivel de administracion requerido en ServiceNow (usuario, agente, admin)?
- ¿Detalle de CIs y alcance de CMDB?
- ¿Herramientas de monitorizacion preferidas o integraciones obligatorias?
- ¿Requiere presencialidad en alguna fase o sede concreta?
- ¿Detalle de penalizaciones por brechas de seguridad?
- ¿Requiere soporte 24x7 en algun escenario?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-002 IA documental
2. Pliego tecnico OPP-SW-002 IA documental
3. Anexo solvencia OPP-SW-002 IA documental