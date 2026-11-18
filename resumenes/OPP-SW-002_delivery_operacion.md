1. Veredicto ejecutivo Delivery / Operacion: OPERABLE CON GAPS

El servicio es operable si se cierran dependencias críticas de compras/partners (cloud IA UE, vector DB SaaS, anonimización, pentest/EIPD) y se valida la integración con herramientas del cliente (ServiceNow, dashboard, CMDB limitada). El equipo cumple solvencia, pero la operación real depende de la activación y compromiso de partners y de la disponibilidad de accesos, documentación y volumetría del cliente. Hay riesgos en logs 24 meses, SLA back-to-back cloud, y anonimización. No hay bloqueo crítico, pero sí acciones obligatorias antes de go-live.

2. Operational Readiness Score:
| Área                  | Score | Semáforo                  | Razón principal                                                                 |
|-----------------------|-------|---------------------------|---------------------------------------------------------------------------------|
| Personal              | 90    | Cubierto                  | Equipo cumple solvencia y experiencia, FTE suficiente para 12x5, backup parcial. |
| Turnos                | 80    | Cubrible con acciones     | 12x5 cubierto, 24x7 no requerido, solapes y vacaciones requieren planificación.   |
| Herramientas          | 75    | Cubrible con acciones     | ITSM y monitorización disponibles, integración ServiceNow requiere validación.   |
| Infraestructura       | 70    | Cubrible con acciones     | Cloud IA y vector DB dependen de partner, logs 24m y anonimización a validar.    |
| Partners              | 70    | Cubrible con acciones     | Cloud, pentest y anonimización dependen de compromisos y mercado.                |
| Cobertura geográfica  | 90    | Cubierto                  | Remoto y presencial planificado en Comunitat Valenciana, partners disponibles.   |
| Transición            | 70    | Cubrible con acciones     | 4-6 semanas viables si cliente colabora, depende de accesos y documentación.     |
| SLA                   | 75    | Cubrible con acciones     | 12x5 y P1 15min cubrible con runbooks y guardias, logs y cloud a validar.        |
| Continuidad           | 70    | Cubrible con acciones     | RTO/RPO y backup cubribles en cloud, prueba de restauración y runbooks a crear.  |
| Dependencias cliente  | 60    | Gap crítico               | Accesos, inventario, volumetría y documentación del cliente imprescindibles.     |

Puntuación global: 75/100

3. Alcance operativo real:
| Elemento         | Valor estimado                  | Fuente                  |
|------------------|---------------------------------|-------------------------|
| Usuarios         | 1.200 empleados públicos        | Pliego técnico          |
| Sedes            | Comunitat Valenciana, remoto    | Pliego técnico          |
| Sistemas         | Plataforma IA RAG/NLP, ServiceNow| Pliego técnico          |
| Dispositivos     | No hardware propio, cloud/SaaS  | Pliego técnico          |
| Horario          | 12x5                            | Pliego técnico          |
| Modalidad        | Remoto, presencial puntual      | Capacidades internas    |
| Tickets/mes      | No dato, suponer 100-200        | Supuesto operativo      |
| Cambios/mes      | No dato, suponer 10-20          | Supuesto operativo      |
| Incidencias P1   | No dato, suponer 1-2/mes        | Supuesto operativo      |
| Cobertura geog.  | Comunitat Valenciana, remoto    | Pliego técnico          |
| Duración         | 14 meses                        | Pliego administrativo   |
| Go-live          | 4-6 semanas tras adjudicación   | Capacidades internas    |

4. Recursos humanos y dimensionamiento:
| Perfil                | Necesidad nominal | Necesidad real | Disponible | Gap | Turnos/guardias | Bus factor | Acción                  |
|-----------------------|-------------------|----------------|------------|-----|------------------|------------|------------------------|
| Responsable proyecto  | 1                 | 1              | 1          | 0   | 12x5             | 2          | Cubierto               |
| Especialista IA/ML    | 1                 | 1              | 1          | 0   | 12x5             | 1          | Proponer backup        |
| Backend Python        | 1                 | 1              | 1          | 0   | 12x5             | 1          | Proponer backup        |
| Especialista datos    | 1                 | 1              | 1          | 0   | 12x5             | 2          | Cubierto               |
| DevOps/cloud          | 1                 | 1              | 1          | 0   | 12x5             | 1          | Proponer backup        |
| QA/soporte            | 0-1               | 0-1            | 1 parcial  | 0   | 12x5             | 1          | Refuerzo si necesario  |
| Ciberseguridad        | 0.2-0.5           | 0.2-0.5        | 1 parcial  | 0   | 12x5             | 1          | Refuerzo si necesario  |

FTE total estimado: 4-5, aplicar factor 1,25 para vacaciones/picos.

5. Cobertura de turnos y ubicaciones:
- 12x5 cubierto con equipo base y planificación de solapes.
- 8x5 cubierto sobradamente.
- 16x5 posible con refuerzo puntual.
- 24x7 no requerido ni cubierto.
- Guardias para incidencias críticas planificables.
- Presencialidad puntual en Comunitat Valenciana, resto remoto.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo      | Aporta         | Estado      | Necesario antes de | Impacto si falta | Acción                |
|------------------------|----------------|-------------|--------------------|------------------|-----------------------|
| ITSM (ServiceNow API)  | Cliente        | Validar     | Go-live            | Alto             | Validar integración   |
| Jira Service Mgmt      | Proveedor      | Disponible  | Go-live            | Medio            | Configurar backup     |
| Monitorización Azure   | Proveedor      | Disponible  | Go-live            | Medio            | Configurar            |
| Vector DB SaaS         | Partner        | Pendiente   | Go-live            | Alto             | Validar equivalencia  |
| Cloud IA (Azure)       | Partner        | Pendiente   | Go-live            | Alto             | BOM, carta fabricante |
| SAST/SCA               | Proveedor      | Pendiente   | Go-live            | Medio            | RFQ, compra           |
| Anonimización          | Partner        | Pendiente   | Go-live            | Alto             | Buscar mercado        |
| Pentest/EIPD           | Partner        | Pendiente   | Go-live            | Alto             | Compromiso firmado    |
| CMDB limitada          | Proveedor      | Parcial     | Go-live            | Medio            | Cargar servicios      |
| Reporting Power BI     | Proveedor      | Disponible  | Go-live            | Bajo             | Adaptar KPIs          |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado         | Impacto operativo | SLA tercero vs SLA cliente | Riesgo | Acción                |
|---------------------------|----------------|-------------------|---------------------------|--------|-----------------------|
| Cloud IA UE (Azure)       | Pendiente carta| Crítico           | 12x5/24x7 extra           | Medio  | BOM, carta fabricante |
| Vector DB SaaS            | Validar        | Crítico           | SaaS, logs 24m            | Medio  | Validar equivalencia  |
| Anonimización             | Buscar mercado | Crítico           | SaaS/autónomo             | Medio  | Buscar mercado        |
| Pentest/EIPD              | Pendiente      | Alto              | Planificado               | Bajo   | Compromiso firmado    |
| SAST/SCA                  | Pendiente      | Medio             | Licencia                  | Bajo   | RFQ, compra           |

8. Modelo de soporte y escalados:
- L0/L1: Service Desk cliente (ServiceNow API), soporte funcional básico.
- L2: Especialistas IA, backend, datos, DevOps (interno), horario 12x5.
- L3: Escalado a partner cloud (Cloud Partner Ficticio), pentest (Pentest Lab), anonimización (partner/autónomo).
- Escalados: Incidentes críticos a cloud/partner, seguridad a Pentest Lab, anonimización a partner/autónomo.

9. Plan de transición y go-live:
- T-45: Plan de transición, solicitud accesos, Service Manager.
- T-30: Equipo núcleo, configuración ITSM, inventario, reporting.
- T-15: Refuerzos, partners, guardias, runbooks, formación.
- T-7: Pruebas de escalado, simulacro P1, validación SLA, go/no-go.
- T0: War room, operación inicial.
- T+30: Revisión, mejora continua, cierre de gaps.

10. Curva de incorporación:
| Hito      | Recursos/Acciones principales                                      |
|-----------|--------------------------------------------------------------------|
| T-60      | Preaviso, contacto partners, RFQ SaaS/licencias                    |
| T-45      | Plan transición, accesos, Service Manager                          |
| T-30      | Equipo núcleo, ITSM, inventario, reporting                         |
| T-15      | Partners, guardias, formación, runbooks                            |
| T-7       | Pruebas escalado, simulacro, validación SLA                        |
| T0        | War room, go-live                                                  |
| T+30      | Revisión, mejora continua, cierre gaps                              |

11. Dependencias de transición:
| Dependencia         | Necesaria antes de | Responsable | Estado    | Riesgo | Mitigación           |
|---------------------|-------------------|-------------|-----------|--------|----------------------|
| Accesos VPN/cuentas | T-30              | Cliente     | Pendiente | Alto   | Solicitar pronto     |
| Documentación       | T-30              | Cliente     | Pendiente | Alto   | Solicitar pronto     |
| Inventario activos  | T-30              | Cliente     | Pendiente | Alto   | Solicitar pronto     |
| Volumetría tickets  | T-30              | Cliente     | Pendiente | Medio  | Solicitar pronto     |
| Partners cloud      | T-15              | Proveedor   | Pendiente | Medio  | BOM, carta fabricante|
| SaaS/anonimización  | T-15              | Proveedor   | Pendiente | Medio  | Buscar mercado       |

12. Continuidad, capacidad y picos:
- Crecimiento: 5.000 documentos/mes, usuarios estables.
- Picos: dimensionar 120-130% volumen medio.
- Rotación: bajo riesgo, equipo estable, backup parcial.
- Caída herramienta/VPN: plan de contingencia, soporte remoto.
- Ausencia clave: bus factor 1 en IA, backend, DevOps; proponer backup.
- Contingencias: war room inicial, simulacro P1, backup cloud.

13. Procedimientos operativos requeridos:
- Gestión de incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad.

14. Automatización y shift-left:
- Automatización pipelines IA, auto-remediation cloud, scripts de monitorización, chatbot FAQ, reporting automático, runbooks para P1/P2, base de conocimiento para FCR.

15. Gap analysis operacional:
| Capacidad           | Necesidad         | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción                | Fecha límite |
|---------------------|-------------------|------------|-----|--------------|---------|--------|-----------------------|--------------|
| Cloud IA UE         | Crítica           | No         | Sí  | Media        | Alto    | Medio  | BOM, carta fabricante | T-7          |
| Vector DB SaaS      | Crítica           | No         | Sí  | Media        | Alto    | Medio  | Validar equivalencia  | T-10         |
| Anonimización       | Crítica           | No         | Sí  | Media        | Alto    | Medio  | Buscar mercado        | T-10         |
| Accesos/documentos  | Crítica           | No         | Sí  | Alta         | Alto    | Alto   | Solicitar pronto      | T-30         |
| Logs 24 meses       | Crítica           | Parcial    | Sí  | Media        | Medio   | Medio  | Validar SaaS          | T-10         |
| Backup IA/DevOps    | Importante        | Parcial    | Sí  | Media        | Medio   | Medio  | Proponer backup       | T-15         |

16. Riesgos operativos principales:
1. Falta de acceso/documentación cliente: bloquea transición y go-live. Mitigación: solicitar pronto, plan de contingencia.
2. No cierre de compromisos cloud/partners: bloquea operación. Mitigación: activar compras, cartas, acuerdos.
3. Logs 24 meses no cubiertos en SaaS: riesgo de incumplimiento. Mitigación: validar SaaS, presupuesto extra.
4. Bus factor 1 en IA, backend, DevOps: riesgo de ausencia. Mitigación: proponer backup, formación cruzada.
5. Anonimización sin partner: riesgo de incumplimiento. Mitigación: buscar mercado, validar alternativas.

17. Supuestos operativos:
- Volumetría tickets/cambios/incidencias no facilitada: se asume carga media (100-200 tickets/mes).
- Accesos, inventario y documentación estarán disponibles T-30.
- ServiceNow API del cliente es accesible y documentada.
- SaaS de vector DB y anonimización admitidos por cliente.
- Logs 24 meses pueden almacenarse en cloud propio si SaaS no lo soporta.

18. Preguntas al cliente:
- ¿Qué volumetría de tickets, cambios e incidencias se prevé mensualmente?
- ¿Cuándo estarán disponibles accesos, inventario y documentación técnica?
- ¿La integración con ServiceNow es vía API estándar o requiere desarrollo específico?
- ¿Qué SaaS de vector DB y anonimización se consideran válidos?
- ¿Se admite almacenamiento de logs 24 meses en cloud propio?
- ¿Se exige declaración de subcontratistas en oferta?

19. Decisión operativa:
Operar con acciones: El servicio es operable si se cierran dependencias de cloud IA, vector DB SaaS, anonimización y pentest/EIPD antes de go-live, y si el cliente facilita accesos, inventario y documentación en plazo. Condiciones mínimas para pasar a oferta: compromisos cloud y partners activados, plan de transición realista, supuestos validados. Condiciones mínimas para go-live: accesos, documentación, SaaS validados, backups y runbooks operativos.

20. Documentos revisados:
- Pliego administrativo OPP-SW-002 IA documental
- Pliego técnico OPP-SW-002 IA documental
- Anexo solvencia OPP-SW-002 IA documental