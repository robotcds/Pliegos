1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS

2. Alcance y dimensionamiento del servicio:
- Servicios incluidos: Desarrollo de modelo de datos, ETL, dashboards Power BI, calidad de datos, formacion y soporte/operacion 6 meses post-produccion.
- Servicios excluidos: No se menciona soporte 24x7, ni mantenimiento evolutivo mayor, ni soporte a usuarios finales masivos.
- Sistemas afectados: Bases de datos existentes, Power BI Service, conectores a SQL Server, CSV, API REST y sistema legacy.
- Usuarios: 35 usuarios gestores.
- Sedes: No especificado; se asume remoto con posible presencialidad puntual.
- Horarios: Soporte 8x5.
- Modalidad: Remoto.
- Cobertura geografica: Andalucia (cliente), pero servicio remoto.
- Volumetrias: 8 fuentes de datos, 12 dashboards, cargas ETL diarias, 35 usuarios. No se especifican volumetrias de tickets/incidencias/cambios.
- Impacto: Dimensionamiento bajo-medio; equipo reducido pero con alta especializacion. Riesgo si aumentan volumetrias o se amplian conectores/usuarios.

3. Modelo de servicio exigido:
- Estructura: Soporte N2 remoto (no N1 ni N3), gestion de incidencias, peticiones de informes, cambios menores, gestion de conocimiento.
- Operacion: Mantenimiento correctivo y soporte funcional sobre BI/ETL.
- Monitorizacion: Alertas automáticas de fallos ETL (valoradas, no obligatorias).
- Servicios especializados: Calidad de datos, formacion, reporting mensual.

4. Procesos ITIL requeridos:
| Proceso                | Explicito/Implicito | Evidencia textual | Exigencia | Capacidad actual | Gap |
|------------------------|---------------------|-------------------|-----------|------------------|-----|
| Incident Management    | Explicito           | "gestion de incidencias" | Obligatorio | Implantado | Ninguno |
| Request Fulfilment     | Explicito           | "peticiones de informes" | Obligatorio | Implantado | Ninguno |
| Change Management      | Explicito           | "cambios menores" | Obligatorio | Implantado | Ninguno |
| Knowledge Management   | Explicito           | "gestion de conocimiento", "manuales" | Obligatorio | Implantado | Ninguno |
| Service Level Mgmt     | Implícito           | "SLA", "objetivo de satisfaccion" | Obligatorio | Implantado | Ninguno |
| Problem Management     | Implícito           | No citado | Recomendado | Parcial | Bajo |
| Configuration Mgmt     | Implícito           | No citado | No exigido | Parcial | Bajo |
| Availability Mgmt      | Implícito           | "errores de calidad", "cargas ETL diarias" | Recomendado | Parcial | Bajo |
| Capacity Mgmt          | Implícito           | No citado | No exigido | Parcial | Bajo |
| Event Management       | Implícito           | "alertas automáticas de fallos ETL" | Valorada | Implantado | Ninguno |
| Continual Improvement  | Implícito           | "satisfacción usuarios", "mejora continua" | Valorada | Implantado | Ninguno |

5. SLA, KPI y penalizaciones:
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo operativo |
|------------------|-----------|-----------|------------|----------|---------|--------------|------------------|-----|------------------|
| Incidencias BI   | Crítica   | <=2h      | <=1 día     | 100%     | 8x5     | 2% hito      | Disponible       | Bajo| Bajo             |
| Errores datos    | Media     | -         | <=3 días    | 100%     | 8x5     | No definida  | Disponible       | Bajo| Bajo             |
| Petición informe | Baja      | -         | <=10 días   | 100%     | 8x5     | No definida  | Disponible       | Bajo| Bajo             |

6. Modelo de priorización:
- No se define modelo P1/P2/P3/P4 formal. Se distingue entre incidencias críticas (impiden visualizar indicadores), errores de datos no críticos y peticiones de nuevos indicadores.
- Ambigüedad: No hay reglas de impacto x urgencia ni definición formal de prioridades intermedias. Riesgo de interpretación en escalado y reporting.

7. Organización y modelo operativo:
- Roles exigidos: Especialista BI/datos (100%), analista funcional (50%), backend integraciones (30%), QA (20%).
- Guardias: No exigidas.
- Presencialidad: Remoto.
- Sustituciones: No especificadas.
- Idiomas: Español.
- Certificaciones: No exigidas, pero se valora experiencia en sector público y Power BI.
- Perfiles internos: Paula (BI), Luis (analista), Sofia (backend), Elena (QA) cumplen requisitos.
- Faltantes: Ninguno relevante.

8. Gobierno del servicio:
- Comités: No definidos, pero se exige reporting mensual. Se recomienda comité operativo mensual y seguimiento trimestral.
- Entregables: Informe mensual de ejecución ETL, errores, tickets, cambios, satisfacción.
- Escalados: No definidos; se recomienda definirlos en la oferta.

9. Herramientas ITSM, CMDB y monitorización:
- ITSM: No se exige herramienta concreta. Jira Service Management o GLPI son válidas.
- CMDB: No exigida.
- Monitorización: Alertas automáticas de fallos ETL valoradas. Azure Monitor, Grafana o scripts propios son válidos.
- Reporting: Power BI, informes mensuales.

10. Transición, toma de control y reversibilidad:
- Fases: 3 semanas de transición (formación, runbooks, traspaso de documentación), 1 semana de reversibilidad (exportación PBIX, scripts ETL, documentación).
- Shadowing: No exigido, pero recomendable.
- Migración de tickets: No aplica.
- Configuración SLA: Sí, en arranque.
- Entrega de documentación: Obligatoria.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos.
- Alta disponibilidad: No exigida.
- Backups: Diario, restauración mensual de prueba.
- Contingencia: No detallada.
- Accesos: MFA para admins, RBAC, logs 12 meses.
- ENS/RGPD: ENS básica si hosting cliente, media si cloud adjudicatario. RGPD: encargado del tratamiento, registro de accesos.
- Incidentes de seguridad: No detallados.

12. Automatización, self-service y mejora continua:
- Exigencias: Se valoran alertas automáticas de fallos ETL y autoservicio de consultas frecuentes.
- Oportunidades: Automatización de reporting, scripts de control de calidad, base de conocimiento, FAQs.

13. Reporting y gestión del conocimiento:
- Informes: Mensuales (ETL, errores, tickets, cambios, satisfacción).
- Cuadros de mando: Power BI.
- Base de conocimiento: Manuales, runbooks ETL, FAQs.
- Propiedad documental: Cliente.

14. Matriz de evaluación Service Design:
| Requisito | Exigencia | Impacto | Capacidad actual | Gap | Riesgo | Acción recomendada | Diferenciación posible |
|-----------|-----------|---------|------------------|-----|--------|--------------------|-----------------------|
| Soporte N2 remoto | Obligatorio | Medio | Disponible | Ninguno | Bajo | Ofertar con equipo senior | Experiencia BI sector público |
| SLA 2h/1d | Obligatorio | Medio | Disponible | Ninguno | Bajo | Garantizar cobertura 8x5 | Reporting proactivo |
| Calidad de datos | Obligatorio | Medio | Disponible | Ninguno | Bajo | Proponer plan detallado | Herramientas propias |
| Alertas ETL | Valorada | Bajo | Disponible | Ninguno | Bajo | Automatizar alertas | Scripts propios |
| ENS básica/media | Obligatorio | Medio | Disponible | Ninguno | Bajo | Aportar declaración | Experiencia ENS |
| Reporting mensual | Obligatorio | Bajo | Disponible | Ninguno | Bajo | Estandarizar informes | Power BI avanzado |

15. Riesgos operativos principales:
- Ambigüedad en volumetría de tickets/incidencias.
- Posible escalada de alcance en conectores o dashboards.
- Falta de definición formal de prioridades y escalados.
- Riesgo de penalización si validación funcional no se supera en dos iteraciones.
- Dependencia de infraestructura Power BI del cliente.

16. Modelo operativo recomendado para ofertar:
- Estructura: Equipo senior BI, analista funcional, backend y QA, todos con experiencia sector público.
- Procesos: Incident, Request, Change, Knowledge, Service Level Management documentados.
- Herramientas: Jira Service Management para tickets, Power BI para reporting, scripts de monitorización ETL.
- Gobierno: Comité operativo mensual, informes mensuales, escalado definido.
- Transición: 3 semanas con formación, documentación y runbooks; reversibilidad 1 semana.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Volumetría estimada de tickets/incidencias/cambios mensuales?
- ¿Modelo de escalado y priorización formal (P1/P2/P3)?
- ¿Herramienta ITSM preferida o integración con sistemas del cliente?
- ¿RTO/RPO objetivo para restauración de backups?
- ¿Penalizaciones adicionales por incumplimiento de SLA no funcionales?
- ¿Infraestructura de gateway Power BI: cliente o adjudicatario?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-005 BI expedientes
2. Pliego técnico OPP-SW-005 BI expedientes
3. Anexo solvencia OPP-SW-005 BI expedientes