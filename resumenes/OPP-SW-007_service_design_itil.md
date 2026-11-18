1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS
- La empresa cumple la mayoría de requisitos técnicos, de solvencia y certificación, pero presenta un gap relevante en el número de pentesters senior internos y en la cobertura de roles de auditoría simultánea. El modelo de servicio y procesos ITIL son parcialmente adecuados, pero hay riesgos en la capacidad de respuesta ante picos de trabajo y en la segregación de funciones.

2. Alcance y dimensionamiento del servicio:
- Servicios: Auditoría ENS (categoría media), pentesting web, revisión de configuraciones, acompañamiento técnico, retest, transferencia de conocimiento, custodia de evidencias.
- Sistemas: 20 aplicaciones web, 6 APIs, configuraciones críticas.
- Usuarios: Equipo técnico y responsables de seguridad del cliente.
- Sedes: No especificadas; cobertura Castilla y León, modalidad remota con posible presencialidad puntual.
- Horarios: No 24x7, pero exige respuesta rápida ante hallazgos críticos (<=1-2h).
- Volumetrías: No detalladas; impacto: dimensionamiento ajustado, riesgo de sobrecarga si surgen múltiples hallazgos críticos simultáneos.

3. Modelo de servicio exigido:
- No hay Service Desk general. Se exige canal de gestión de hallazgos, roles de responsable de seguridad, coordinador de auditoría, pentesters senior y consultor de evidencias.
- Operación tipo proyecto, no servicio gestionado continuo. No se exige soporte N1/N2/N3 clásico, pero sí gestión de incidencias de seguridad y cambios de remediación.
- Monitorización limitada a seguimiento de hallazgos y remediaciones.

4. Procesos ITIL requeridos:
| Proceso                  | Explicito/Implicito | Evidencia textual                                      | Exigencia         | Capacidad actual         | Gap                  |
|-------------------------|---------------------|--------------------------------------------------------|-------------------|--------------------------|----------------------|
| Incident Management     | Implícito           | "gestión de incidencias de seguridad"                  | Alta              | Implantado               | Bajo                 |
| Change Management       | Implícito           | "cambios de remediación"                              | Media             | Implantado               | Bajo                 |
| Knowledge Management    | Implícito           | "lecciones aprendidas, transferencia"                 | Media             | Implantado               | Bajo                 |
| Service Level Management| Explícito           | "SLA vulnerabilidad crítica..."                       | Alta              | Implantado               | Bajo                 |
| Configuration Management| Implícito           | "revisión de configuraciones críticas"                | Media             | Parcial                  | Medio                |
| Security Management     | Explícito           | "ENS, ISO 27001, custodia de evidencias, MFA"         | Alta              | Alta                     | Bajo                 |
| Reporting               | Explícito           | "matriz de riesgos, estado de remediación"            | Alta              | Alta                     | Bajo                 |

5. SLA, KPI y penalizaciones:
| Servicio                | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo operativo |
|-------------------------|-----------|-----------|------------|----------|---------|--------------|------------------|-----|------------------|
| Vulnerabilidad crítica  | P1        | <=1-2h    | <=8h prop. contención | Alta     | Laboral | 2%/retraso, 10% confidencialidad | Parcial | Medio | Alto (pico trabajo) |
| Vulnerabilidad alta     | P2        | <=2d      | Retest <=5d | Media    | Laboral | 2%/retraso | Alta | Bajo | Bajo |
| Evidencias críticas     | P1        | <=2h      | Entrega inmediata | Alta | Laboral | 2%/retraso | Parcial | Medio | Medio |

6. Modelo de priorización:
- P1: Vulnerabilidad crítica explotable, requiere comunicación inmediata (<=1h) y contención (<=8h).
- P2: Vulnerabilidad alta, informe en <=2 días, retest en <=5 días.
- No se detallan P3/P4 ni matriz impacto x urgencia. Riesgo: ambigüedad en priorización de hallazgos no críticos.

7. Organización y modelo operativo:
- Roles exigidos: Responsable de seguridad, coordinador de auditoría, dos pentesters senior, consultor de evidencias, auditor ISO 27001 Lead Auditor.
- Dedicaciones: No detalladas, pero alto peso en pentesters (70%+50%).
- Guardias: No exigidas, pero sí disponibilidad rápida ante hallazgos críticos.
- Presencialidad: Remoto, presencialidad puntual posible.
- Sustituciones: No detalladas; riesgo si baja un pentester.
- Idiomas: Español.
- Certificaciones: ISO 27001, ENS media, Lead Auditor, CEH (valorable).
- Perfiles internos: Javier Prieto cubre ENS, ISO y pentesting, pero falta segundo pentester senior.

8. Gobierno del servicio:
- Comité operativo quincenal, comité de riesgos mensual, canal urgente para hallazgos críticos.
- Entregables: Matriz de riesgos, estado de remediación, excepciones, tendencias.
- Escalados: No detallados, pero canal urgente para P1.

9. Herramientas ITSM, CMDB y monitorización:
- Herramientas obligatorias: Repositorio cifrado de evidencias, gestor de vulnerabilidades, tablero de seguimiento.
- Integraciones/API: No detalladas.
- Portal: No exigido.
- CMDB: No exigida, pero revisión de configuraciones críticas.
- Reporting: Matriz de riesgos, informes técnicos y ejecutivos.

10. Transición, toma de control y reversibilidad:
- Fases: Plan de pruebas, ejecución, informes, retest, transferencia.
- Duración: 6 meses.
- Shadowing: No detallado.
- Migración de tickets: No aplica.
- Configuración SLA: Sí, para hallazgos críticos.
- Formación: Transferencia de conocimiento (hasta 12h).
- Entrega de documentación: Evidencias, informes, matriz de riesgos, recomendaciones.
- Reversibilidad: Entrega de todo lo anterior y custodia de evidencias 24 meses.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos.
- Alta disponibilidad: No exigida.
- Backups: Custodia de evidencias cifradas 24 meses.
- Contingencia: No detallada.
- Accesos: MFA, segregación de funciones, control de accesos.
- Vulnerabilidades: Gestión priorizada, retest.
- ENS/RGPD: ENS media obligatoria, comunicación inmediata de brechas.

12. Automatización, self-service y mejora continua:
- No se exige automatización, pero uso de gestor de vulnerabilidades y tablero de seguimiento permite cierta eficiencia.
- Oportunidad: Automatizar reporting, gestión de evidencias y retest.

13. Reporting y gestión del conocimiento:
- Informes técnicos y ejecutivos, matriz de riesgos, estado de remediación, tendencias.
- Frecuencia: Según entregables y comités.
- Base de conocimiento: Lecciones aprendidas, transferencia.
- Propiedad documental: Cliente.

14. Matriz de evaluación Service Design:
| Requisito                        | Exigencia | Impacto | Capacidad actual | Gap | Riesgo | Acción recomendada | Diferenciación posible |
|-----------------------------------|-----------|---------|------------------|-----|--------|--------------------|-----------------------|
| 2 pentesters senior internos      | Obligatoria| Alta    | 1 disponible     | Sí  | Alto   | Contratar/reforzar | Experiencia ENS/ISO   |
| Auditor ISO 27001 Lead Auditor   | Obligatoria| Alta    | 1 disponible     | No  | Bajo   | Asignar Javier     | Certificación         |
| ENS media e ISO 27001 empresa    | Obligatoria| Alta    | Sí               | No  | Bajo   | Aportar certificados|                      |
| No subcontratar pentesting       | Obligatoria| Alta    | Parcial          | Sí  | Alto   | Contratar directo  |                      |
| SLA críticos <=2h                | Obligatoria| Alta    | Parcial          | Sí  | Medio  | Refuerzo equipo    |                      |
| Custodia evidencias cifrada      | Obligatoria| Media   | Sí               | No  | Bajo   | Procedimiento      |                      |
| Transferencia conocimiento 12h   | Mejora     | Media   | Sí               | No  | Bajo   | Ofertar máximo     |                      |

15. Riesgos operativos principales:
- Falta de segundo pentester senior interno.
- Riesgo de sobrecarga ante múltiples hallazgos críticos simultáneos.
- Ambigüedad en priorización de hallazgos no críticos.
- Penalizaciones severas por filtración/confidencialidad.
- Dependencia de perfiles clave (baja, vacaciones).

16. Modelo operativo recomendado para ofertar:
- Estructura: Responsable de seguridad (Javier), coordinador de auditoría (Ana), pentesters senior (Javier + nuevo fichaje), consultor de evidencias (apoyo QA), auditor ISO 27001 (Javier).
- Procesos: Gestión de hallazgos, reporting, transferencia, retest, custodia de evidencias.
- Herramientas: Gestor de vulnerabilidades, repositorio cifrado, tablero de seguimiento (Jira/Confluence).
- Gobierno: Comité operativo quincenal, comité de riesgos mensual, canal urgente.
- Transición: Kick-off, plan de pruebas, asignación de roles, formación inicial, checklist de evidencias.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Se puede detallar la volumetría esperada de hallazgos críticos y altas?
- ¿Se permite presencialidad puntual para sesiones clave?
- ¿Qué herramientas de gestor de vulnerabilidades y repositorio cifrado son aceptadas?
- ¿Se exige integración con sistemas del cliente?
- ¿Hay requisitos de reporting automatizado o formatos específicos?
- ¿Se puede clarificar la priorización de hallazgos P3/P4?
- ¿Qué ocurre si un pentester causa baja temporal?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-007 ciberseguridad
2. Pliego técnico OPP-SW-007 ciberseguridad
3. Anexo solvencia OPP-SW-007 ciberseguridad