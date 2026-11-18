1. Veredicto ejecutivo Delivery / Operacion: NO OPERABLE

El servicio NO es operable en las condiciones exigidas por el pliego desde el día 1 ni durante toda la duración contractual con los recursos, herramientas y red de partners actuales. El gap de desarrolladores Java senior es crítico y bloqueante, y no existe cobertura interna ni externa identificada para cubrirlo. El resto de capacidades (soporte L2, jefe de servicio, QA, DBA puntual, herramientas) son cubribles, pero el gap de personal técnico principal impide arrancar y operar el servicio conforme a pliego.

2. Operational Readiness Score:
| Área                | Score | Semáforo                  | Razón                                                                                 |
|---------------------|-------|---------------------------|---------------------------------------------------------------------------------------|
| Personal            | 30    | Gap crítico               | Faltan 2 desarrolladores Java senior, jefe de servicio sin ITIL Foundation             |
| Turnos              | 80    | Cubrible con acciones     | 8x5 cubierto, vacaciones requieren refuerzo mínimo                                     |
| Herramientas        | 85    | Cubierto                  | ITSM, monitorización y QA disponibles, salvo detalles de integración                   |
| Infraestructura     | 90    | Cubierto                  | Operación remota y entornos de pruebas cubribles                                       |
| Partners            | 40    | Gap crítico               | No hay partner ni autónomo Java senior disponible                                      |
| Cobertura geográfica| 90    | Cubierto                  | Remoto y sedes principales cubiertos                                                   |
| Transición          | 60    | Cubrible con acciones     | Plan estándar viable si se cierra gap de personal                                      |
| SLA                 | 60    | Cubrible con acciones     | Riesgo de incumplimiento por falta de personal                                         |
| Continuidad         | 40    | Gap crítico               | Bus factor 1 en soporte Java, sin backup                                               |
| Dependencias cliente| 70    | Cubrible con acciones     | Accesos, documentación y KT dependen del saliente                                      |
| **Score global**    | **56**| **ALTO RIESGO OPERATIVO** | Gap de personal crítico, resto cubrible con acciones                                   |

3. Alcance operativo real:
| Elemento           | Valor / Detalle                                      | Fuente                  |
|--------------------|------------------------------------------------------|-------------------------|
| Usuarios           | 900 internos                                         | Pliego técnico          |
| Sedes              | 3                                                    | Pliego técnico          |
| Aplicaciones       | 12 Java legacy                                       | Pliego técnico          |
| Dispositivos       | No especificado (supuesto: solo acceso remoto)       | Supuesto operativo      |
| Horario            | 8x5, guardias puntuales para despliegues             | Pliego técnico          |
| Modalidad          | Remoto, presencial puntual                           | Pliego técnico          |
| Tickets/mes        | 180 (20% incidencias, 60% peticiones, 20% cambios)   | Pliego técnico          |
| Cambios/mes        | 8 menores                                            | Pliego técnico          |
| Incidencias críticas| ~36/mes (20% de 180)                                | Pliego técnico          |
| Cobertura geográfica| País Vasco, remoto                                  | Pliego técnico          |
| Duración           | 24 meses                                             | Pliego administrativo   |
| Go-live            | 30 días desde adjudicación                           | Pliego técnico          |

4. Recursos humanos y dimensionamiento:
| Perfil                  | Necesidad nominal | Necesidad real | Disponible | Gap | Turnos/guardias | Bus factor | Acción                  |
|-------------------------|-------------------|----------------|------------|-----|------------------|-----------|------------------------|
| Jefe de servicio        | 1                 | 1              | 1*         | Parcial | 8x5           | 1         | ITIL Foundation/backup |
| Desarrollador Java      | 3                 | 3              | 1          | 2   | 8x5             | 1         | Contratar 2 externos   |
| Soporte L2              | 1                 | 1              | 1          | 0   | 8x5             | 1         | Backup necesario       |
| QA                      | 0,2               | 0,2            | 1          | 0   | 8x5             | 1         | Cubierto               |
| DBA Oracle puntual      | 0,1               | 0,1            | 0          | 0   | Bajo demanda     | 1         | Preacuerdo autónomo    |
*Ana Torres: experiencia en dirección de proyectos, no explícita en mantenimiento ni ITIL Foundation.

5. Cobertura de turnos y ubicaciones:
- 8x5 cubierto con equipo base si se cierra gap Java.
- Guardias puntuales cubribles con refuerzo.
- Vacaciones/ausencias: riesgo alto por bus factor 1 en Java y jefe de servicio.
- Cobertura geográfica: País Vasco remoto, presencialidad puntual planificable.
- 24x7 no requerido ni cubierto.

6. Herramientas, activos e infraestructuras:
| Herramienta/Activo         | Aporta         | Estado     | Necesario antes de | Impacto si falta | Acción                |
|---------------------------|----------------|------------|--------------------|------------------|-----------------------|
| ITSM Jira/cliente         | Cliente        | Validar    | Go-live            | Alto             | Confirmar integración |
| Monitorización aplicacional| Proveedor      | Contratar  | Go-live            | Medio            | RFQ urgente           |
| SAST/SCA                  | Proveedor      | Contratar  | Go-live            | Medio            | RFQ urgente           |
| Entorno de pruebas        | Proveedor      | Cubrible   | Go-live            | Medio            | Provisionar           |
| Repositorio documental    | Cliente        | Validar    | Go-live            | Bajo             | Confirmar acceso      |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado A10 | Impacto operativo | SLA tercero vs cliente | Riesgo | Acción                |
|---------------------------|------------|-------------------|-----------------------|--------|-----------------------|
| Desarrollador Java senior | Gap crítico| No arranca        | N/A                   | Máximo | Contratar externo     |
| DBA Oracle puntual        | Parcial    | Riesgo puntual    | SLA bajo demanda      | Medio  | Preacuerdo urgente    |
| SAST/monitorización       | Pendiente  | Arranque retrasado| SLA propio            | Bajo   | RFQ urgente           |

8. Modelo de soporte y escalados:
- L0/L1: Cliente (Service Desk)
- L2: Adjudicatario (Claudia Benitez, soporte Java)
- L3: Adjudicatario (Sofia Martin, faltan 2 Java)
- Escalado DBA: Autónomo (Héctor Campos)
- Horario: 8x5, guardias puntuales
- Gap: sin backup Java ni jefe de servicio ITIL

9. Plan de transición y go-live:
- Semana 1: Accesos, inventario, KT con saliente, configuración ITSM
- Semana 2-3: Discovery intensivo, carga KB, runbooks, pruebas
- Semana 4: War room, validación SLA, go/no-go
- Condición: No arrancar sin equipo Java completo

10. Curva de incorporación:
| Hito      | Recursos clave           | Herramientas | Partners | Bloqueos principales           |
|-----------|-------------------------|--------------|----------|-------------------------------|
| T-45      | Jefe de servicio        | Plan trans.  | -        | Gap Java                      |
| T-30      | 3 Java, soporte L2      | ITSM         | -        | Gap Java                      |
| T-15      | QA, DBA, SAST           | Monitorización| Autónomo | Preacuerdo DBA, SAST          |
| T-7       | Equipo completo         | Todo         | -        | Validar accesos, KT saliente  |
| T0        | Operación               | Todo         | -        | -                             |

11. Dependencias de transición:
| Dependencia           | Necesaria antes de | Responsable | Estado     | Riesgo | Mitigación           |
|----------------------|--------------------|-------------|------------|--------|----------------------|
| Accesos VPN/cuentas  | Go-live            | Cliente     | Pendiente  | Alto   | Solicitar T-30       |
| KT saliente          | Go-live            | Cliente     | Pendiente  | Alto   | Discovery intensivo  |
| Inventario apps      | Go-live            | Cliente     | Pendiente  | Medio  | Discovery intensivo  |
| Equipo Java completo | Go-live            | Adjudicatario| Gap crítico| Máximo | Contratar externo    |

12. Continuidad, capacidad y picos:
- Picos de +30% tickets en cierres trimestrales.
- Riesgo de caída de servicio por bus factor 1 en Java y jefe de servicio.
- Contingencia: teletrabajo, backup QA y soporte L2, pero no Java.

13. Procedimientos operativos requeridos:
- Incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad.

14. Automatización y shift-left:
- Oportunidad: Automatización de pruebas de regresión, scripts de monitorización, runbooks para incidencias comunes, chatbot FAQ para usuarios.

15. Gap analysis operacional:
| Capacidad             | Necesidad | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción              | Fecha límite |
|-----------------------|-----------|------------|-----|-------------|---------|--------|---------------------|-------------|
| Desarrollador Java    | 3         | 1          | 2   | Máxima      | Máximo  | Crítico| Contratar externo   | T-30        |
| Jefe de servicio ITIL | 1         | 1*         | Parcial| Alta      | Alto    | Alto   | Certificar/refuerzo | T-30        |
| DBA Oracle puntual    | 1         | 0          | 0   | Media       | Medio   | Medio  | Preacuerdo autónomo | T-15        |
| SAST/monitorización   | 1         | 0          | 0   | Media       | Bajo    | Bajo   | RFQ urgente         | T-15        |

16. Riesgos operativos principales:
1. Gap desarrolladores Java: No arranca el servicio. Propietario: Operaciones. Mitigación: Contratar externo urgente.
2. Bus factor 1 en Java y jefe de servicio: Caída de servicio por baja/rotación. Propietario: RRHH. Mitigación: Backup y refuerzo.
3. Falta de KT/documentación saliente: Arranque lento, errores. Propietario: Cliente. Mitigación: Discovery intensivo.
4. Accesos y herramientas cliente: Retraso go-live. Propietario: Cliente. Mitigación: Solicitar T-30.

17. Supuestos operativos:
- El cliente aporta ITSM y repositorio documental.
- El entorno de pruebas puede ser cloud.
- El soporte L2/L3 no puede subcontratarse fuera de la UE.
- La bolsa de horas adicional es opcional.
- Validar antes de oferta.

18. Preguntas al cliente:
- ¿Se aceptan desarrolladores Java subcontratados o solo personal propio?
- ¿El entorno de pruebas puede ser cloud?
- ¿Qué herramienta ITSM exacta usará el cliente?
- ¿Cuántos usuarios ITSM debe aportar el adjudicatario?
- ¿Se exige backup formal para cada perfil crítico?
- ¿Qué grado de colaboración se espera del proveedor saliente?

19. Decisión operativa:
NO OFERTAR SIN REDISEÑO. El servicio no es operable sin incorporar al menos dos desarrolladores Java senior con experiencia acreditada en Spring, SQL y mantenimiento de aplicaciones corporativas antes de la presentación de la oferta. Además, se recomienda reforzar el perfil de jefe de servicio con certificación ITIL Foundation y experiencia específica en mantenimiento. El resto de gaps son gestionables con acciones previas a go-live.

Condiciones mínimas para pasar a oferta:
- Incorporar dos desarrolladores Java senior acreditados.
- Certificar jefe de servicio en ITIL Foundation.
- Preacuerdo con DBA Oracle.

Condiciones mínimas para go-live:
- Equipo completo y operativo.
- Accesos, documentación y KT transferidos.
- Herramientas y entornos listos.

20. Documentos revisados:
1. Pliego administrativo OPP-SW-004 mantenimiento Java
2. Pliego técnico OPP-SW-004 mantenimiento Java
3. Anexo solvencia OPP-SW-004 mantenimiento Java