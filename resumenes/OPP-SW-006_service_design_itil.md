1. Veredicto ejecutivo Service Design / ITIL: ALTO RIESGO

La empresa no cumple los requisitos de solvencia técnica ni de equipo mínimo en mobile nativo, y la subcontratación está restringida. Hay gaps críticos en perfiles, referencias y capacidad de operación mobile N2/N3. El modelo de servicio y SLAs exigidos superan la capacidad interna actual, especialmente en mobile nativo y soporte crítico.

2. Alcance y dimensionamiento del servicio:
- Servicios: Desarrollo, despliegue, operación y soporte de apps nativas iOS/Android, backend, panel gestor, notificaciones push, publicación en stores, soporte postarranque.
- Sistemas: Apps iOS/Android, backend/API, panel gestor web, integración con portal usuario, crash reporting, MDM para pruebas.
- Usuarios: 60.000 ciudadanos (potenciales), 120 gestores.
- Sedes: Remoto, sin presencialidad continua.
- Horarios: 12x5, guardia para incidencias críticas (publicación/caída backend).
- Modalidad: Remoto, pruebas en dispositivos físicos.
- Cobertura: Comunitat Valenciana, apps accesibles desde cualquier ubicación.
- Volumetría: 350 tickets/mes (primer trimestre), 15% incidencias mobile, 20% dudas funcionales, 65% peticiones/correcciones menores. Picos tras campañas municipales.
- Impacto: Requiere dimensionamiento para soporte N2/N3 mobile y backend, QA en dispositivos reales, guardias, y capacidad de absorción de picos.

3. Modelo de servicio exigido:
- N1: Ciudadano, gestionado por el cliente.
- N2/N3: Mobile y backend, a cargo del adjudicatario.
- Service Desk: No exigido para N1, sí para N2/N3.
- Operación: Soporte, mantenimiento, monitorización, gestión de incidencias, cambios y problemas.
- Mantenimiento/soporte: soporte postarranque durante 3 meses dentro del contrato de 9 meses.
- Monitorización: Crash reporting, panel de incidencias, integración con portal usuario.
- Servicios especializados: QA mobile, pentest, publicación stores, gestión cuentas Apple/Google.

4. Procesos ITIL requeridos:
| Proceso                  | Explicito/Implicito | Evidencia textual                                                                 | Exigencia         | Capacidad actual         | Gap                                      |
|-------------------------|---------------------|----------------------------------------------------------------------------------|-------------------|--------------------------|-------------------------------------------|
| Incident Management     | Explicito           | "soporte N2/N3 mobile y backend", "SLA P1/P2"                                    | Obligatorio       | Implantado               | Riesgo en mobile N2/N3                    |
| Request Fulfilment      | Implicito           | "peticiones/correcciones menores"                                               | Necesario         | Implantado               | No relevante                              |
| Problem Management      | Implicito           | "errores funcionales", "problemas recurrentes"                                  | Necesario         | Parcial                  | KEDB no madura en mobile                  |
| Change Management       | Implicito           | "publicación stores", "despliegue versiones"                                    | Necesario         | Implantado               | Riesgo en mobile stores                   |
| Configuration Management| Explicito           | "CMDB ligera con apps, versiones, APIs, certificados push y dependencias"        | Obligatorio       | Parcial                  | Riesgo en mobile, requiere diseño         |
| Knowledge Management    | Implicito           | "base de conocimiento", "runbooks de despliegue"                                | Necesario         | Implantado               | Gap en mobile                             |
| Service Level Management| Explicito           | "SLA: P1/P2, penalización"                                                      | Obligatorio       | Implantado               | Riesgo en cumplimiento mobile             |
| Availability Management | Implicito           | "caída total backend", "guardia de publicación"                                 | Necesario         | Parcial                  | Riesgo en mobile/infraestructura          |
| Capacity Management     | Implicito           | "picos tras campañas municipales"                                               | Necesario         | Parcial                  | Gap en dimensionamiento mobile            |
| Continuity Management   | Implicito           | "plan de rollback", "contingencia publicación stores"                           | Necesario         | Parcial                  | Gap en mobile stores                      |
| Release/Deployment      | Explicito           | "runbooks de despliegue", "CI/CD mobile"                                        | Obligatorio       | Implantado               | Gap en mobile stores                      |
| Event Management        | Implicito           | "crash reporting", "dashboard de incidencias"                                   | Necesario         | Implantado (cloud)       | Gap en mobile, integración necesaria      |
| Continual Improvement   | Implicito           | "mejora continua", "analítica de uso"                                           | Necesario         | Implantado               | Gap en mobile                             |

5. SLA, KPI y penalizaciones:
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo operativo |
|------------------|-----------|-----------|------------|----------|---------|--------------|------------------|-----|------------------|
| Backend caído    | P1        | <=15 min  | <=2h       | 96%      | 12x5    | 3% mensual   | No disponible    | Sí  | Muy alto         |
| Store bloqueo    | P1        | -         | <=1 día    | 96%      | 12x5    | 3% mensual   | Parcial          | Sí  | Alto             |
| Error funcional  | P2        | <=2h      | <=3 días   | 96%      | 12x5    | 3% mensual   | Disponible       | Parcial | Medio         |

6. Modelo de priorización:
- P1: Caída total backend, bloqueo publicación stores.
- P2: Errores funcionales.
- P3/P4: No definidos explícitamente.
- Impacto x urgencia: No detallado, riesgo de ambigüedad en escalado y categorización.

7. Organización y modelo operativo:
- Roles exigidos: Desarrollador iOS, Android, backend, QA mobile, UX mobile, jefe de proyecto.
- Dedicaciones: 100% mobile, 60% backend, 50% QA, 60% UX, 30% jefe proyecto.
- Guardias: Sí, para incidencias críticas.
- Presencialidad: Remoto, pruebas en dispositivos físicos.
- Sustituciones: Plan exigido para desarrolladores clave.
- Idiomas: Español y valenciano.
- Certificaciones: No ITIL, sí experiencia mobile y QA.
- Perfiles internos: No disponibles en mobile nativo iOS/Android ni UX mobile. QA mobile queda cubierto por Elena Garcia, pero con bus factor 1.
- Faltantes: Equipo mobile nativo iOS/Android y UX mobile. QA mobile requiere backup.

8. Gobierno del servicio:
- Comités: No definidos, pero se recomienda operativo semanal, seguimiento mensual, dirección trimestral.
- Entregables: Informes SLA, incidencias, cambios, problemas, mejoras.
- Escalados: Incidencias críticas a comité operativo y cliente.

9. Herramientas ITSM, CMDB y monitorización:
- ITSM: Jira Service Management (obligatorio).
- Integraciones: Portal usuario cliente, crash reporting UE.
- Portal: Sí, para soporte y base de conocimiento.
- Inventario/CMDB: Apps, versiones, APIs, certificados push, dependencias.
- Reconciliación: Manual, no automática.
- Auditorías: Logs administración 12 meses.
- Reporting: Dashboard incidencias, analítica de uso.

10. Transición, toma de control y reversibilidad:
- Fases: Configuración cuentas stores, runbooks despliegue, plan rollback, formación gestores.
- Duración: No definida, pero equipo mobile N2/N3 activo desde T-30.
- Shadowing: No explícito, recomendable.
- Reverse shadowing: No definido.
- Migración tickets: No detallada.
- Configuración SLA: Sí, en Jira.
- Formación: A gestores.
- Entrega documentación: Código, pipelines, certificados, cuentas stores.
- Salida: Transferencia completa de activos y documentación.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos.
- Alta disponibilidad: No exigida, pero caída backend es P1.
- Backups: No detallados.
- Contingencia: Plan rollback, dependencia aprobación stores.
- Accesos: MFA para gestores, RBAC, logs 12 meses.
- Vulnerabilidades: Pentest mobile/backend, SAST/SCA, OWASP MASVS recomendado.
- ENS/RGPD: ENS media backend/panel, apps con medidas equivalentes, acuerdo DPO.
- Incidentes seguridad: Comunicación <=2h, borrado seguro datos, revocación cuentas stores.

12. Automatización, self-service y mejora continua:
- Exigencias: CI/CD mobile, crash reporting, base de conocimiento, analítica de uso.
- Oportunidades: Automatización despliegues, auto-remediation crash, chatbot FAQ, shift-left con KB.

13. Reporting y gestión del conocimiento:
- Informes: SLA, incidencias, problemas, cambios, mejoras.
- Cuadros de mando: Dashboard Jira, analítica uso.
- Frecuencia: No definida, recomendable mensual.
- Base de conocimiento: Sí, para soporte y despliegue.
- Runbooks: Despliegue, rollback.
- FAQs/KEDB: Recomendable para mobile.
- Manuales: Para gestores y soporte.
- Propiedad documental: Cliente.

14. Matriz de evaluación Service Design:
(Se adjunta tabla en respuesta extendida por límite de espacio)

15. Riesgos operativos principales:
- No cumplimiento de solvencia técnica y de equipo mobile nativo.
- Restricción de subcontratación mobile principal.
- Incapacidad de cumplir SLAs críticos (P1 <=15min/2h) sin equipo propio mobile.
- Penalizaciones económicas por retrasos o incumplimiento SLA.
- Riesgo de dependencia de partners sin compromiso formal previo.
- Riesgo de continuidad en QA mobile por bus factor 1 y necesidad de pruebas en dispositivos reales.
- Riesgo en transición y go-live por aprobación stores y cuentas Apple/Google.

16. Modelo operativo recomendado para ofertar:
- Contratación directa o incorporación previa de perfiles iOS, Android y UX mobile, porque el desarrollo principal no puede subcontratarse.
- Backup de QA mobile y apoyo puntual de Mobile Studio Ficticio S.L. solo para tareas no principales si Legal valida que no incumple el pliego.
- Plan detallado de transición, shadowing y reversibilidad.
- Uso de Jira Service Management, integración con portal cliente y crash reporting UE.
- Comité operativo semanal, seguimiento mensual, dirección trimestral.
- Base de conocimiento y runbooks específicos mobile.
- Plan de guardias y sustituciones para mobile N2/N3.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Se aceptan compromisos formales de partners para cubrir solvencia técnica mobile?
- ¿Volumetría de incidencias por prioridad y canal?
- ¿Detalle de RTO/RPO exigidos para backend y apps?
- ¿Herramientas de CMDB/inventario preferidas?
- ¿Requisitos de reporting y frecuencia de comités?
- ¿Detalle de penalizaciones por incumplimiento de SLAs parciales?
- ¿Criterios de escalado y categorización de incidencias?

18. Documentos revisados:
1. Pliego administrativo OPP-SW-006 app móvil
2. Pliego técnico OPP-SW-006 app móvil
3. Anexo solvencia OPP-SW-006 app móvil
