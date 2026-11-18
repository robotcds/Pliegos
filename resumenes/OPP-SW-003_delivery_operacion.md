1. Veredicto ejecutivo Delivery / Operacion: NO OPERABLE

El servicio NO es operable en las condiciones exigidas por el pliego desde el día 1 ni durante toda la duración contractual, debido a un gap crítico de personal (falta un segundo perfil DevOps/cloud senior con experiencia específica y demostrable). El resto de capacidades (herramientas, cloud, partners, licencias, guardias) son cubribles, pero dependen de cerrar la contratación/alianza para el segundo DevOps senior antes de ofertar. No es posible arrancar ni operar el servicio conforme a pliego sin resolver este gap.

2. Operational Readiness Score:
| Área                  | Score | Semáforo textual           | Razón principal                                                                 |
|-----------------------|-------|----------------------------|---------------------------------------------------------------------------------|
| Personal              | 40    | Gap crítico                | Falta 1 DevOps/cloud senior, bus factor 1 en DevOps, riesgo de incumplimiento    |
| Turnos                | 70    | Cubrible con acciones      | 12x5 y guardias cubribles con partner, pero depende de cerrar DevOps externo     |
| Herramientas          | 85    | Cubierto                   | ITSM, monitorización, SAST/SCA, cloud, reporting cubribles con compras/partner   |
| Infraestructura       | 90    | Cubierto                   | Todo cloud/software, sin dependencias físicas                                    |
| Partners              | 80    | Cubrible con acciones      | Cloud Partner Ficticio S.A. disponible, pero depende de compromiso formal        |
| Cobertura geográfica  | 90    | Cubierto                   | Remoto y partners cubren Aragón y España peninsular                              |
| Transición            | 60    | Cubrible con acciones      | 8 semanas posibles si se cierra DevOps, depende de accesos/documentación cliente |
| SLA                   | 70    | Cubrible con acciones      | SLA 12x5 y guardias cubribles, pero depende de cerrar DevOps y partner           |
| Continuidad           | 60    | Gap crítico                | Bus factor 1 en DevOps, riesgo de ausencia clave                                 |
| Dependencias cliente  | 70    | Cubrible con acciones      | Accesos, inventario, documentación, colaboración saliente                        |
| **Score global**      | **65**| **ALTO RIESGO OPERATIVO**  | Gap personal bloqueante, resto cubrible si se actúa antes de oferta              |

3. Alcance operativo real:
| Usuarios      | Sedes      | Sistemas/aplicaciones | Dispositivos/activos | Horario | Modalidad | Tickets/mes | Cambios | Incidencias críticas | Cobertura geográfica | Duración | Go-live      | Fuente         |
|--------------|------------|----------------------|---------------------|---------|----------|-------------|---------|---------------------|----------------------|----------|-------------|----------------|
| 6 apps, 18 microservicios, 4 BBDD, 3 entornos | Aragón, remoto | Azure, AKS, Docker, CI/CD, Grafana, Jira | Cloud, pipelines, contenedores | 12x5 + guardias | Remoto + puntual presencial | No definido (supuesto: 60-100/mes) | 10-20/mes | 1-2/mes | Aragón, remoto España | 10 meses | T0+8 semanas | Pliego técnico |

4. Recursos humanos y dimensionamiento:
| Perfil                | Necesidad nominal | Necesidad operativa real | Disponible | Gap | Turnos/guardias | Bus factor | Acción                       |
|-----------------------|-------------------|-------------------------|------------|-----|------------------|------------|-----------------------------|
| DevOps/cloud senior   | 2                 | 2                       | 1          | 1   | 12x5+guardias    | 1          | Contratar/partner urgente   |
| Backend senior        | 1                 | 1                       | 1          | 0   | 12x5             | 1          | Cubierto                   |
| Jefe de proyecto      | 1                 | 1                       | 1          | 0   | 8x5              | 1          | Cubierto                   |
| Soporte/QA/otros      | 0-1               | 0-1                     | 1+         | 0   | 8x5              | 2          | Cubierto                   |

5. Cobertura de turnos y ubicaciones:
- 12x5 cubrible con equipo y partner si se cierra DevOps externo.
- Guardias para fines de semana migración: cubrible con partner.
- 24x7 no requerido ni cubierto.
- Presencialidad puntual en Aragón: cubrible con partner.
- Remoto: cubierto.
- Cobertura geográfica: Aragón y remoto España cubiertos.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo         | Aporta           | Estado     | Necesario antes de | Impacto si falta | Acción                       |
|---------------------------|------------------|------------|-------------------|------------------|------------------------------|
| Azure cloud temporal       | Partner/compra   | Cubrible   | T-2 semanas       | No arranque      | RFQ, deal registration       |
| SAST/SCA                  | Compra/partner   | Gap medio  | T-2 semanas       | Riesgo seguridad | RFQ urgente                  |
| Grafana/Prometheus        | Compra/partner   | Cubrible   | T-2 semanas       | Sin monitorización| BOM, integración             |
| Jira Service Management    | Compra           | Cubrible   | T-2 semanas       | Sin ITSM         | Compra directa/licencias     |
| Guardias DevOps           | Partner          | Cubrible   | T-2 semanas       | Sin soporte      | Compromiso firmado           |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado A10   | Impacto operativo | SLA tercero vs SLA cliente | Riesgo   | Acción                    |
|---------------------------|-------------|-------------------|---------------------------|----------|--------------------------|
| DevOps/cloud senior (2º)   | Gap crítico | No arranque       | N/A                       | Máximo   | Contratar/partner urgente|
| Cloud Partner Ficticio S.A.| Cubrible    | Arranque posible  | SLA 12x5/guardias         | Medio    | Carta compromiso         |
| SAST/SCA fabricante        | Gap medio   | Riesgo seguridad  | N/A                       | Medio    | RFQ urgente              |

8. Modelo de soporte y escalados:
- L1: No aplica (soporte técnico directo).
- L2: Backend senior, DevOps/cloud senior.
- L3: Escalado a partner/fabricante (Cloud Partner Ficticio S.A., Microsoft).
- Horario: 12x5 + guardias migración.
- Gaps: Bus factor 1 en DevOps, escalado solo posible si partner formalizado.

9. Plan de transición y go-live:
- T-60: Plan de transición, solicitud accesos, carta partner.
- T-45: Incorporación jefe proyecto, discovery, inventario.
- T-30: Incorporación backend y DevOps, configuración ITSM, licencias.
- T-15: Incorporación DevOps externo, formación, runbooks, pruebas.
- T-7: Simulacro, validación SLA, war room.
- T0: Go-live, operación estabilizada.

10. Curva de incorporación:
| Hito      | Recursos clave                | Herramientas/partners         | Bloqueos principales           |
|-----------|------------------------------|------------------------------|-------------------------------|
| T-60      | Jefe proyecto                | Carta partner                 | Gap DevOps                    |
| T-45      | Backend, DevOps (1)          | ITSM, cloud                   | Gap DevOps                    |
| T-30      | DevOps (2º), QA              | SAST/SCA, monitorización      | Gap DevOps, licencias SAST    |
| T-15      | Todos                        | Guardias, reporting           | Gap DevOps, formación         |
| T-7       | Todos                        | Simulacro, war room           | Gap DevOps                    |
| T0        | Todos                        | Operación                     | Gap DevOps                    |

11. Dependencias de transición:
| Dependencia           | Necesaria antes de | Responsable | Estado   | Riesgo | Mitigación                |
|----------------------|-------------------|-------------|----------|--------|---------------------------|
| Accesos VPN          | T-30              | Cliente     | Pendiente| Medio  | Solicitar pronto          |
| Inventario apps      | T-45              | Cliente     | Pendiente| Medio  | Solicitar pronto          |
| Carta partner cloud  | T-45              | Partner     | Pendiente| Alto   | Solicitar urgente         |
| DevOps (2º)          | T-30              | Compras     | Gap      | Máximo | Contratar/partner urgente |

12. Continuidad, capacidad y picos:
- Riesgo de bus factor 1 en DevOps/cloud senior.
- Picos de trabajo en ventanas de migración: solo cubribles si se cierra DevOps externo y guardias partner.
- Caída de herramienta: mitigable con cloud y SaaS.
- Ausencia de personas clave: riesgo máximo en DevOps.

13. Procedimientos operativos requeridos:
- Incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad. Adaptar runbooks y KB a migración cloud.

14. Automatización y shift-left:
- Oportunidad de automatizar pipelines CI/CD, escaneo de contenedores, alertas automáticas, reporting dashboards, auto-remediation cloud, KB para FCR.

15. Gap analysis operacional:
| Capacidad             | Necesidad         | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción                    | Fecha límite |
|----------------------|-------------------|------------|-----|--------------|---------|--------|--------------------------|--------------|
| DevOps/cloud senior  | 2                 | 1          | 1   | Alta         | Máximo  | Máximo | Contratar/partner urgente| T-30         |
| SAST/SCA             | 1                 | 0          | 1   | Media        | Medio   | Medio  | RFQ urgente              | T-30         |
| Carta partner cloud  | 1                 | 0          | 1   | Media        | Alto    | Alto   | Solicitar urgente        | T-45         |

16. Riesgos operativos principales:
1. Gap DevOps/cloud senior: No arranque ni operación posible. Propietario: RRHH/Compras. Mitigación: Contratar/partner urgente.
2. Bus factor 1 en DevOps: Riesgo de indisponibilidad. Propietario: Operaciones. Mitigación: Backup/partner.
3. Licencias SAST/SCA: Riesgo de incumplimiento seguridad. Propietario: Compras. Mitigación: RFQ urgente.
4. Accesos/inventario cliente: Riesgo de retraso. Propietario: Cliente. Mitigación: Solicitar pronto.

17. Supuestos operativos:
- Volumetría de tickets y cambios no definida: se asume 60-100 tickets/mes, 10-20 cambios/mes.
- Accesos, inventario y documentación cliente disponibles antes de T-30.
- Cloud Partner Ficticio S.A. puede aportar DevOps senior y cubrir guardias.
- SAST/SCA compatible con pipelines y licencias disponibles antes de go-live.
- Validar todos los supuestos antes de oferta.

18. Preguntas al cliente:
- ¿Se acepta solvencia por medios externos para el segundo DevOps/cloud senior?
- ¿Qué fabricantes de SAST/SCA son aceptados como equivalentes?
- ¿Se permite subcontratar el segundo DevOps/cloud senior si se declara en oferta?
- ¿El cloud temporal puede ser facturado por partner o debe ser directo?
- ¿Volumetría de tickets, cambios y picos esperados?
- ¿Accesos, inventario y documentación estarán disponibles antes de transición?

19. Decisión operativa:
NO OFERTAR SIN REDISEÑO. No es posible operar ni arrancar el servicio conforme a pliego sin cerrar la contratación/alianza para el segundo DevOps/cloud senior. Condición mínima para pasar a oferta: disponer de compromiso formal de DevOps/cloud senior externo (contrato/partner/carta). Condición mínima para go-live: DevOps senior incorporado, licencias y herramientas listas, accesos y documentación cliente disponibles.

20. Documentos revisados:
1. Pliego administrativo OPP-SW-003 migración cloud
2. Pliego técnico OPP-SW-003 migración cloud
3. Anexo solvencia OPP-SW-003 migración cloud