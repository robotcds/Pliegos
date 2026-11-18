1. Veredicto ejecutivo Delivery / Operacion: OPERABLE CON GAPS

El servicio es operable en las condiciones del pliego, pero depende críticamente de la formalización de compromisos con partners para cloud (Cloud Partner Ficticio S.A.) y pentest (Pentest Lab Ficticio S.L.), así como de la validación de licencias SAST/SCA equivalentes. No existen gaps internos de perfiles, pero el bus factor en algunos roles es 1. La transición y el go-live requieren la colaboración activa del cliente para accesos, inventario y validación de integraciones. El readiness es medio-alto si se cierran las acciones previas a la oferta.

2. Operational Readiness Score:
| Área                  | Score | Semáforo                  | Razón                                                                 |
|-----------------------|-------|---------------------------|-----------------------------------------------------------------------|
| Personal              | 85    | Cubierto                  | Todos los perfiles mínimos están disponibles y cumplen requisitos.    |
| Turnos                | 80    | Cubrible con acciones     | 8x5 cubierto; 12x5 posible con refuerzo; no se exige 24x7.            |
| Herramientas          | 75    | Cubrible con acciones     | Jira, Power BI y SAST/SCA dependen de compras/partner.                |
| Infraestructura       | 80    | Cubrible con acciones     | Cloud Azure depende de partner y carta compromiso.                    |
| Partners              | 70    | Gap crítico si no cierran | Cloud y pentest dependen de partners; riesgo si no hay compromiso.    |
| Cobertura geográfica  | 90    | Cubierto                  | Remoto y presencial puntual en Madrid; no se exige cobertura nacional. |
| Transición            | 75    | Cubrible con acciones     | 4 semanas viables si cliente colabora y partners confirman.           |
| SLA                   | 80    | Cubierto                  | SLA 8x5 viable con equipo y herramientas propuestas.                   |
| Continuidad           | 70    | Cubrible con acciones     | Bus factor 1 en algunos roles; proponer backup y plan de contingencia. |
| Dependencias cliente  | 65    | Gap crítico si no cierran | Accesos, inventario y validación de integraciones son críticos.       |
| **Global**            | **77**| **Operable con acciones** | Viable si se cierran partners, compras y dependencias cliente.         |

3. Alcance operativo real:
| Elemento         | Valor/Detalle                                    | Fuente                  |
|------------------|--------------------------------------------------|-------------------------|
| Usuarios         | 450 empleados, 25.000 ciudadanos potenciales      | Pliego técnico          |
| Sedes            | Sede municipal (Madrid), remoto                   | Pliego técnico          |
| Sistemas         | Portal web, APIs, registro, gestor documental     | Pliego técnico          |
| Dispositivos     | No especificado; suponemos PCs y móviles usuario  | Supuesto operativo      |
| Horario          | 8x5 soporte postarranque (6 meses)                | Pliego técnico          |
| Modalidad        | Remoto, presencial puntual (4 jornadas arranque)  | Pliego técnico          |
| Tickets/mes      | 120 (2 meses), 60 estabilizado                    | Pliego técnico          |
| Cambios          | No especificado; suponemos 10-20/mes              | Supuesto operativo      |
| Incidencias P1   | No especificado; suponemos <5/mes                 | Supuesto operativo      |
| Cobertura geog.  | Madrid y remoto                                   | Pliego técnico          |
| Duración         | 12 meses                                          | Pliego administrativo   |
| Go-live          | 6 semanas tras formalización                      | Pliego técnico          |

4. Recursos humanos y dimensionamiento:
| Perfil                | Necesidad nominal | Necesidad real | Disponible | Gap | Turnos/guardias | Bus factor | Acción                       |
|-----------------------|-------------------|----------------|-----------|-----|------------------|-----------|-----------------------------|
| Jefe de proyecto      | 1 (35% FTE)       | 0.35 FTE       | 1         | No  | 8x5              | 1         | Proponer backup             |
| Backend senior        | 1 (80% FTE)       | 0.8 FTE        | 1         | No  | 8x5              | 1         | Proponer backup             |
| Frontend              | 1 (80% FTE)       | 0.8 FTE        | 1         | No  | 8x5              | 1         | Proponer backup             |
| QA                    | 1 (45% FTE)       | 0.45 FTE       | 1         | No  | 8x5              | 1         | Proponer backup             |
| Ciberseguridad        | 1 (20% FTE)       | 0.2 FTE        | 1         | No  | 8x5              | 1         | Proponer backup             |
| Soporte N2/N3         | 1-2 (postarranque)| 1-2            | 2         | No  | 8x5              | 2         | Cubierto                    |
| DevOps/cloud          | 1 (parcial)       | 0.2-0.3 FTE    | 1         | No  | 8x5              | 1         | Proponer backup             |

*Nota: Todos los roles críticos tienen bus factor 1; se recomienda identificar backups internos o de partner para continuidad.*

5. Cobertura de turnos y ubicaciones:
- 8x5: Cubierto con equipo base.
- 12x5: Posible con refuerzo puntual.
- 16x5/24x7: No requerido ni cubierto.
- Guardias: Solo para ventanas de despliegue, no para operación continua.
- Presencialidad: Solo 4 jornadas de arranque; resto remoto.
- Geográfica: Madrid y remoto; no se exige cobertura nacional.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo         | Aporta         | Estado     | Necesario antes de | Impacto si falta | Acción                  |
|---------------------------|----------------|------------|-------------------|------------------|-------------------------|
| Jira Service Management   | Partner        | Pendiente  | Go-live           | No tickets       | Validar compra/licencia |
| Power BI Pro              | Partner        | Pendiente  | Go-live           | No reporting     | Validar compra/licencia |
| SAST/SCA                  | Partner        | Pendiente  | Desarrollo        | Riesgo seguridad | Validar compra/licencia |
| Cloud Azure DEV/PRE/PRO   | Partner        | Pendiente  | Desarrollo        | No entornos      | Carta compromiso        |
| Pentest web               | Partner        | Pendiente  | Pre-producción    | No paso a prod   | Compromiso firmado      |
| VPN/accesos               | Cliente        | Pendiente  | T-30              | No acceso        | Solicitar pronto        |
| Documentación técnica     | Cliente        | Pendiente  | T-30              | Riesgo migración | Solicitar pronto        |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado A10 | Impacto operativo         | SLA tercero vs SLA cliente | Riesgo | Acción                  |
|---------------------------|------------|--------------------------|----------------------------|--------|-------------------------|
| Cloud Azure/Cloud Partner | Pendiente  | No entornos, no go-live  | 99,5% Azure vs 8x5 cliente | Medio  | Carta compromiso        |
| Jira/Power BI/Partner     | Pendiente  | No tickets/reporting     | 12x5 soporte vs 8x5 cliente| Bajo   | Validar licencias       |
| SAST/SCA                  | Pendiente  | Riesgo seguridad         | N/A                        | Medio  | Validar equivalencia    |
| Pentest/Pentest Lab       | Pendiente  | No paso a producción     | Bajo planificación         | Medio  | Compromiso firmado      |

8. Modelo de soporte y escalados:
- L0: No aplica (usuarios finales autogestión).
- L1: No aplica (soporte N2/N3 directo).
- L2: Soporte aplicacional (Claudia Benitez, Sofia Martin, Karim El Haddad).
- L3: Desarrollo y ciberseguridad (Sofia Martin, Javier Prieto).
- Escalado a partner: Cloud (Cloud Partner Ficticio S.A.), Pentest (Pentest Lab Ficticio S.L.).
- Horario: 8x5.

9. Plan de transición y go-live:
- Semana 1: Kick-off, solicitud accesos, discovery, inventario, plan de trabajo.
- Semana 2: Configuración herramientas, carga KB, formación inicial, pruebas integraciones.
- Semana 3: Runbooks, pruebas de escalado, validación de reporting, simulacro P1.
- Semana 4: War room, validación de SLA, go/no-go, paso a producción.

10. Curva de incorporación:
| Hito      | Recursos/Acciones                                 |
|-----------|---------------------------------------------------|
| T-45      | Service Manager, plan transición, accesos         |
| T-30      | N2/N3, configuración ITSM, inventario, reporting  |
| T-15      | Refuerzos, partners, guardias, runbooks, formación|
| T-7       | Pruebas escalado, simulacro P1, validación SLA    |
| T0        | Operación con war room inicial                    |
| T+30      | Revisión backlog, mejora continua, reporting      |

11. Dependencias de transición:
| Dependencia           | Necesaria antes de | Responsable | Estado     | Riesgo | Mitigación           |
|----------------------|--------------------|-------------|------------|--------|----------------------|
| Accesos VPN/cuentas  | T-30               | Cliente     | Pendiente  | Alto   | Solicitar pronto     |
| Documentación técnica| T-30               | Cliente     | Pendiente  | Medio  | Solicitar pronto     |
| Inventario apps      | T-30               | Cliente     | Pendiente  | Medio  | Solicitar pronto     |
| Carta partner cloud  | T-15               | Partner     | Pendiente  | Medio  | Solicitar pronto     |
| Compromiso pentest   | T-15               | Partner     | Pendiente  | Medio  | Solicitar pronto     |

12. Continuidad, capacidad y picos:
- Volumen tickets bajo-medio; picos asumibles con equipo base.
- Bus factor 1 en roles críticos; proponer backups.
- Contingencia: teletrabajo, backup en Barcelona/Valencia.
- Simulacros recomendados antes de go-live.

13. Procedimientos operativos requeridos:
- Gestión de incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad.

14. Automatización y shift-left:
- Automatización de pruebas (Playwright), reporting (Power BI), scripts de despliegue (CI/CD), base de conocimiento y chatbot FAQ para usuarios internos.

15. Gap analysis operacional:
| Capacidad         | Necesidad         | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción                | Fecha límite |
|-------------------|------------------|------------|-----|--------------|---------|--------|-----------------------|--------------|
| Cloud Azure       | Cloud DEV/PRE/PRO| No         | Sí  | Media        | Alto    | Medio  | Carta compromiso      | T-15         |
| Jira/Power BI     | Licencias        | No         | Sí  | Baja         | Medio   | Bajo   | Validar compra        | T-15         |
| SAST/SCA          | Licencia         | No         | Sí  | Media        | Medio   | Medio  | Validar equivalencia  | T-15         |
| Pentest web       | Servicio         | No         | Sí  | Baja         | Alto    | Medio  | Compromiso firmado    | T-15         |
| Accesos cliente   | Accesos VPN      | No         | Sí  | Media        | Alto    | Alto   | Solicitar pronto      | T-30         |
| Documentación     | Técnica/inventario| No        | Sí  | Media        | Medio   | Medio  | Solicitar pronto      | T-30         |
| Backups/continuidad| Planes/backup   | Parcial    | Sí  | Baja         | Medio   | Bajo   | Revisar y adaptar     | T-7          |

16. Riesgos operativos principales:
1. Falta de compromiso formal de partners (cloud, pentest): bloquea go-live. Mitigación: cerrar acuerdos antes de oferta.
2. Accesos e inventario del cliente no entregados a tiempo: retrasa transición y go-live. Mitigación: solicitar formalmente y condicionar planning.
3. Bus factor 1 en roles críticos: riesgo de ausencia. Mitigación: identificar backups internos o de partner.
4. Licencias SAST/SCA no validadas: riesgo de incumplimiento de seguridad. Mitigación: validar equivalencia antes de oferta.

17. Supuestos operativos:
- El cliente entregará accesos, inventario y documentación técnica en la semana 1 de transición.
- El cloud Azure puede estar en tenant del partner si cumple ENS MEDIA y residencia UE.
- Se permite subcontratar pentest a partner homologado.
- No se requiere presencia física continua, solo 4 jornadas de arranque.
- Volumen de cambios y P1 es bajo; si es superior, se revisará dimensionamiento.
*Validar estos supuestos antes de oferta o go-live.*

18. Preguntas al cliente:
- ¿Se admite SonarQube Community/Enterprise o hay preferencia de fabricante para SAST/SCA?
- ¿El cloud Azure puede estar en tenant del partner o debe ser en tenant del cliente?
- ¿Se exige carta de fabricante Microsoft o basta con carta de partner cloud?
- ¿Se permite subcontratar el pentest web a partner homologado?
- ¿Se puede disponer de inventario de aplicaciones y documentación técnica antes de la transición?
- ¿Hay histórico de tickets/incidencias para ajustar dimensionamiento?

19. Decisión operativa:
- Operar con acciones: El servicio es operable si se cierran compromisos formales con partners (cloud, pentest), se validan licencias y equivalentes SAST/SCA, y el cliente colabora en accesos e inventario. Condiciones mínimas para pasar a oferta: cartas/compromisos de partners, validación de licencias, supuestos validados. Condiciones mínimas para go-live: accesos, inventario, herramientas y partners operativos.

20. Documentos revisados:
1. Pliego administrativo OPP-SW-001 portal ciudadano
2. Pliego técnico OPP-SW-001 portal ciudadano
3. Anexo solvencia OPP-SW-001 portal ciudadano