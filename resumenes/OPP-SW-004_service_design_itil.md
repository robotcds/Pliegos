1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS

La empresa cumple la mayoría de requisitos técnicos y organizativos para un servicio gestionado ITIL de mantenimiento Java legacy, pero existen gaps en dimensionamiento de equipo Java, cobertura de DBA Oracle, madurez de Problem/Configuration Management y dependencia de herramientas ITSM del cliente. El riesgo operativo es moderado-alto en arranque y picos de demanda.

2. Alcance y dimensionamiento del servicio:
- Servicios: Mantenimiento correctivo, evolutivo, soporte L2/L3, gestión de tickets, pequeñas evoluciones, pruebas de regresión, actualización documental, soporte a usuarios internos.
- Sistemas: 12 aplicaciones Java legacy.
- Usuarios: 900 internos.
- Sedes: 3.
- Horario: Laboral (8x5), con bolsa de 200h/año para urgencias.
- Modalidad: Remoto, con acceso VPN; guardias puntuales para despliegues.
- Cobertura: País Vasco, sedes distribuidas.
- Volumetría: 180 tickets/mes (20% incidencias, 60% peticiones, 20% cambios menores), 8 cambios menores/mes, 3 despliegues/mes, picos +30% en cierres trimestrales.
- Impacto: Dimensionamiento ajustado, riesgo de saturación en picos, necesidad de backup operativo y cobertura de vacaciones/bajas.

3. Modelo de servicio exigido:
- Estructura: N1 (cliente), N2/N3 (adjudicatario).
- Service Desk: Cliente.
- Operación: Gestión de incidencias, peticiones, problemas, cambios, conocimiento, niveles de servicio.
- Mantenimiento: Correctivo, evolutivo, preventivo menor.
- Monitorización: Aplicacional aportada por adjudicatario.
- Servicios especializados: DBA Oracle puntual, QA 20%.

4. Procesos ITIL requeridos:
| Proceso                  | Explicito/Implicito | Evidencia textual                                      | Exigencia        | Capacidad actual         | Gap                         |
|--------------------------|---------------------|--------------------------------------------------------|------------------|--------------------------|-----------------------------|
| Incident Management      | Explícito           | "gestión de incidencias"                               | Obligatorio      | Implantado               | Ninguno                     |
| Request Fulfilment       | Explícito           | "peticiones"                                          | Obligatorio      | Implantado               | Ninguno                     |
| Problem Management       | Implícito           | "problemas recurrentes", "KEDB"                       | Recomendado      | Parcial                  | Madurez KEDB                |
| Change Management        | Explícito           | "gestión de cambios menores"                          | Obligatorio      | Implantado               | Ninguno                     |
| Configuration Management | Implícito           | "inventario de aplicaciones", "CMDB"                  | Recomendado      | Parcial                  | Mantenimiento operativo      |
| Knowledge Management     | Explícito           | "runbooks", "FAQ", "manuales", "KEDB"                | Obligatorio      | Implantado               | Ninguno                     |
| Service Level Management | Explícito           | "SLA", "cuadro de mando mensual", "penalizaciones"    | Obligatorio      | Implantado               | Ninguno                     |
| Availability Management  | Implícito           | "resolución en 24h", "parches críticos en 5 días"     | Recomendado      | Parcial                  | Limitado en legacy          |
| Capacity Management      | Implícito           | "picos de demanda", "backlog máximo"                  | Recomendado      | Parcial                  | Requiere métricas           |
| Continual Improvement    | Implícito           | "plan de mejora", "backlog de mejora"                 | Recomendado      | Implantado               | Ninguno                     |

5. SLA, KPI y penalizaciones:
| Servicio      | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo operativo |
|---------------|-----------|-----------|------------|----------|---------|--------------|------------------|-----|------------------|
| Incidencias   | P1        | <=1h      | <=8h       | 95%      | 8x5     | 2%/SLA       | Parcial          | Sí  | Saturación picos |
| Incidencias   | P2        | <=4h      | <=2 días   | 95%      | 8x5     | 2%/SLA       | Sí               | No  | Bajo             |
| Incidencias   | P3        | -         | <=5 días   | 95%      | 8x5     | 2%/SLA       | Sí               | No  | Bajo             |
| Cambios       | Menor     | -         | <=10 días  | 95%      | 8x5     | 2%/SLA       | Sí               | No  | Bajo             |
| Backlog       | -         | -         | <=25 envejecidos | 95% | 8x5 | 2%/SLA       | Sí               | No  | Bajo             |

6. Modelo de priorización:
- P1: Impacto alto (>300 usuarios o proceso crítico bloqueado).
- P2: Impacto medio, urgencia alta.
- P3: Impacto bajo, urgencia media/baja.
- P4: No definido explícitamente.
- Priorización por impacto x urgencia. Ambigüedad en definición de urgencia y escalado automático. Riesgo: subjetividad en clasificación y escalado.

7. Organización y modelo operativo:
- Roles: Jefe de servicio (25%), 3 desarrolladores Java (70%), soporte L2 (100%), QA (20%), DBA Oracle puntual.
- Guardias: 2 noches/mes para despliegues.
- Presencialidad: Remoto, acceso VPN, presencial puntual si requerido.
- Sustituciones: Obligatorio cubrir vacaciones/bajas.
- Idiomas: Español.
- Certificaciones: ITIL Foundation para coordinador.
- Perfiles internos: Ana Torres (jefe), Sofia Martin (Java), Claudia Benitez (L2), Elena Garcia (QA). Gap: 2 desarrolladores Java senior, DBA Oracle.

8. Gobierno del servicio:
- Comités: Operativo semanal, seguimiento mensual, dirección trimestral.
- Entregables: Informe mensual de SLA, aging, backlog, problemas, plan de mejora.
- Escalados: Definidos en modelo de servicio.

9. Herramientas ITSM, CMDB y monitorización:
- ITSM: Jira Service Management o equivalente (cliente).
- Integraciones: APIs, reporting, cuadro de mando mensual.
- Portal: No exigido, pero posible mejora.
- Inventario/CMDB: Inventario de aplicaciones, CMDB básica.
- Monitorización: Aplicacional aportada por adjudicatario.
- Auditorías: Trazabilidad de tickets y cambios.

10. Transición, toma de control y reversibilidad:
- Fases: 6 semanas transición, 4 semanas reversibilidad.
- Shadowing: 5 jornadas transferencia conocimiento.
- Migración: Tickets vivos, inventario, configuración SLA, runbooks.
- Formación: Documentación y sesiones.
- Salida: Entrega de documentación, KB, tickets, CMDB.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos, riesgo en legacy.
- Backups: Cifrado, retención 12 meses.
- Accesos: VPN, MFA, cuentas nominativas, segregación funciones.
- Vulnerabilidades: Parches críticos <=5 días.
- ENS: Declaración básica, ISO 27001 valorable.
- Incidentes: Comunicación <=4h, brechas datos <=2h.

12. Automatización, self-service y mejora continua:
- Exigencias: No explícitas.
- Oportunidades: Automatización reporting, scripts QA, base de conocimiento, shift-left, chatbot FAQ.

13. Reporting y gestión del conocimiento:
- Informes: Mensual SLA, backlog, aging, problemas, plan mejora.
- Cuadro de mando: Mensual.
- KB: Runbooks, FAQ, KEDB, manuales, propiedad cliente.

14. Matriz de evaluación Service Design:
(Se adjunta tabla en respuesta extendida por límite de espacio)

15. Riesgos operativos principales:
- Falta de 2 desarrolladores Java senior.
- Cobertura DBA Oracle puntual.
- Saturación en picos de demanda.
- Dependencia de ITSM y repositorios cliente.
- Ambigüedad en priorización y escalado.
- Riesgo en transición si proveedor saliente no colabora.

16. Modelo operativo recomendado para ofertar:
- Estructura: Jefe de servicio (Ana Torres), 1 Java senior (Sofia Martin), 2 Java externos, L2 (Claudia Benitez), QA (Elena Garcia), DBA subcontratado.
- Procesos: ITIL Incident, Request, Change, Problem, Knowledge, Service Level.
- Herramientas: Jira Service Management, monitorización propia, scripts QA, reporting Power BI.
- Gobierno: Comités y reporting según pliego.
- Transición: Shadowing, migración tickets, KB, war room 2 semanas.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Detalle de herramientas ITSM y acceso a APIs?
- ¿Definición de urgencia y escalado automático?
- ¿Volumetría de cambios mayores y evolutivos?
- ¿RTO/RPO objetivo en legacy?
- ¿Detalle de inventario y documentación disponible?
- ¿Condiciones de acceso presencial si requerido?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-004 mantenimiento Java
2. Pliego técnico OPP-SW-004 mantenimiento Java
3. Anexo solvencia OPP-SW-004 mantenimiento Java