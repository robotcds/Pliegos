1. Veredicto ejecutivo Delivery / Operacion: 
OPERABLE CON GAPS

2. Operational Readiness Score:
| Área                  | Score | Semáforo                        | Razón principal                                                                 |
|-----------------------|-------|----------------------------------|---------------------------------------------------------------------------------|
| Personal              | 65    | Cubrible con acciones            | Faltan evidencias de certificados vigentes y dedicaciones en algunos perfiles.   |
| Turnos                | 80    | Cubierto                         | 8x5 cubierto, 24x7 no exigido ni cubierto.                                      |
| Herramientas          | 70    | Cubrible con acciones            | ITSM y monitorización disponibles, falta validación de entorno cliente.          |
| Infraestructura       | 60    | Cubrible con acciones            | Azure disponible vía partner, falta compromiso firmado y especialización vigente.|
| Partners              | 60    | Cubrible con acciones            | Cloud Partner cubre Azure, falta compromiso y renovación de especialización.     |
| Cobertura geográfica  | 80    | Cubierto                         | Madrid y remoto cubiertos, presencialidad puntual.                              |
| Transición            | 70    | Cubrible con acciones            | 4 semanas factible, depende de accesos y documentación cliente.                  |
| SLA                   | 70    | Cubrible con acciones            | SLA N2 8x5 cubrible, falta detalle de métricas y reporting.                      |
| Continuidad           | 60    | Cubrible con acciones            | Bus factor bajo en algunos roles, falta backup en especialistas.                 |
| Dependencias cliente  | 60    | Cubrible con acciones            | Accesos, inventario y documentación no garantizados a tiempo.                    |

Puntuación global: 68/100

3. Alcance operativo real:
| Elemento         | Valor/condición         | Fuente                |
|------------------|------------------------|-----------------------|
| Usuarios internos| 150                    | PPT OPP-SW-011 T2     |
| Usuarios externos| 10.000                 | PPT OPP-SW-011 T2     |
| Sedes            | NO CONSTA              | PPT OPP-SW-011        |
| Sistemas         | Portal web, API, BBDD  | PPT OPP-SW-011 T1     |
| Dispositivos     | NO CONSTA              | PPT OPP-SW-011        |
| Horario          | 8x5                    | PPT OPP-SW-011 T2     |
| Modalidad        | Remoto, presencial puntual | Capacidades internas |
| Tickets/mes      | NO CONSTA              | PPT OPP-SW-011        |
| Cambios          | NO CONSTA              | PPT OPP-SW-011        |
| Incidencias crit.| NO CONSTA              | PPT OPP-SW-011        |
| Cobertura geog.  | Madrid, remoto España  | Capacidades internas  |
| Duración         | 12 meses               | PCAP OPP-SW-011 A1    |
| Go-live          | T0 tras 4 semanas      | PPT OPP-SW-011 T2     |

4. Recursos humanos y dimensionamiento:
| Perfil         | Necesidad nominal | Necesidad real | Disponible | Gap | Turnos/guardias | Bus factor | Acción |
|----------------|------------------|----------------|------------|-----|-----------------|------------|--------|
| Jefatura       | 1 (50%)          | 0.5 FTE        | 1          | 0   | 8x5             | 1          | Validar dedicación y backup |
| Backend        | 1 (100%)         | 1 FTE          | 1          | 0   | 8x5             | 1          | Validar certificación AWS   |
| Desarrollador  | 2                | 2 FTE          | 2          | 0   | 8x5             | 2          | Asignar perfiles y evidencias|
| QA             | 0.5              | 0.5 FTE        | 1          | 0   | 8x5             | 1          | Validar dedicación         |
| Soporte N2     | NO CONSTA        | 1-2 FTE (estimado) | 3      | 0   | 8x5             | 2          | Confirmar volumen y cobertura|

5. Cobertura de turnos y ubicaciones:
- 8x5 cubierto con equipo base.
- 12x5 posible con refuerzo.
- 16x5/24x7 no exigido ni cubierto.
- Presencialidad puntual posible en Madrid; resto remoto.
- Cobertura nacional presencial no exigida ni garantizada.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo      | Aporta         | Estado      | Necesario antes de | Impacto si falta | Acción                |
|------------------------|----------------|-------------|-------------------|------------------|-----------------------|
| ITSM (Jira/GLPI)       | Proveedor      | Disponible  | T-15              | Alto             | Configurar y validar  |
| Azure cloud            | Partner        | Parcial     | T-15              | Crítico          | Renovar especialización, firmar compromiso |
| Monitorización         | Proveedor      | Disponible  | T-7               | Medio            | Integrar con portal   |
| Backup                 | Proveedor      | Disponible  | T-7               | Alto             | Validar política      |
| MFA/TLS                | Proveedor      | Disponible  | T-7               | Alto             | Configurar            |
| Reporting              | Proveedor      | Disponible  | T-7               | Medio            | Adaptar KPIs          |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado | Impacto operativo | SLA tercero vs cliente | Riesgo | Acción |
|---------------------------|--------|-------------------|------------------------|--------|--------|
| Azure cloud (Cloud Partner)| Parcial| Crítico           | No acreditado          | Alto   | Renovar especialización, firmar compromiso |
| Licencias portal          | No consta| Medio            | No definido            | Medio  | Confirmar métricas y licencias             |

8. Modelo de soporte y escalados:
- L0: No definido.
- L1: No definido.
- L2: Interno, 8x5, soporte a usuarios y portal.
- L3: No definido, escalar a desarrolladores o partner si necesario.
- Escalado a partner cloud para incidencias Azure.

9. Plan de transición y go-live:
- Semana 1: Discovery, solicitud accesos, inventario.
- Semana 2: Configuración ITSM, formación, shadowing.
- Semana 3: Pruebas, carga de KB, validación backup.
- Semana 4: War room, go/no-go, arranque.

10. Curva de incorporación:
| Hito    | Recursos           | Herramientas | Partners         | Bloqueos |
|---------|--------------------|--------------|------------------|----------|
| T-45    | Jefatura           | ITSM         | -                | -        |
| T-30    | Backend, QA        | Azure        | Cloud Partner    | Compromiso partner |
| T-15    | Desarrolladores    | Monitorización| -               | Accesos  |
| T-7     | Soporte N2         | Reporting    | -                | Inventario|
| T0      | Todos              | Todas        | -                | -        |

11. Dependencias de transición:
| Dependencia         | Necesaria antes de | Responsable | Estado   | Riesgo | Mitigación           |
|---------------------|-------------------|-------------|----------|--------|----------------------|
| Accesos VPN         | T-15              | Cliente     | Pendiente| Alto   | Solicitar pronto     |
| Inventario sistemas | T-15              | Cliente     | Pendiente| Alto   | Solicitar pronto     |
| Compromiso partner  | T-30              | Proveedor   | Pendiente| Alto   | Formalizar           |

12. Continuidad, capacidad y picos:
- Capacidad suficiente para volumen medio, riesgo en picos si baja dedicación o ausencia de backup.
- Bus factor bajo en jefatura y backend.
- Contingencia: refuerzo con partner o bolsa de horas.

13. Procedimientos operativos requeridos:
- Incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad.

14. Automatización y shift-left:
- Oportunidad de auto-remediation en cloud, scripts de backup, chatbot para FAQs, reporting automatizado.

15. Gap analysis operacional:
| Capacidad         | Necesidad | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción | Fecha límite |
|-------------------|-----------|------------|-----|--------------|---------|--------|--------|-------------|
| Azure especialización| Sí      | No         | Sí  | Alta         | Crítico | Alto   | Renovar| T-30        |
| CBE 2º proyecto   | Sí        | No         | Sí  | Alta         | Crítico | Alto   | Obtener| T-30        |
| Certificados ISO/ENS| Sí      | Parcial    | Sí  | Alta         | Crítico | Alto   | Renovar| T-30        |
| QA evidencia      | Sí        | Parcial    | Sí  | Media        | Medio   | Medio  | Aportar| T-30        |

16. Riesgos operativos principales:
1. No renovación especialización Azure VMware Solution: impide operar cloud.
2. Falta CBE segundo proyecto: exclusión administrativa.
3. Certificados ISO/ENS no cubren producción: riesgo de exclusión y penalización.
4. Bus factor bajo en jefatura/backend: riesgo de ausencia crítica.
5. Accesos e inventario cliente no entregados a tiempo: retraso en transición.

17. Supuestos operativos:
- Se asume que el cliente facilitará accesos, inventario y documentación en la primera semana de transición.
- Se asume que el partner renovará la especialización Azure VMware Solution antes de go-live.
- Se asume que se obtendrá el segundo CBE válido antes de la presentación.
- Validar todos antes de oferta.

18. Preguntas al cliente:
- ¿Puede confirmar la volumetría mensual de tickets y cambios esperados?
- ¿Qué herramienta ITSM y monitorización prefiere o aporta el cliente?
- ¿Se requiere presencialidad regular en alguna sede?
- ¿Qué documentación/inventario se entregará en transición?
- ¿Quién es el proveedor saliente y qué colaboración se prevé?
- ¿Qué métricas de licencias y entornos cloud se exigen?

19. Decisión operativa:
Operar con acciones: solo ofertar si se renueva la especialización Azure VMware Solution, se obtiene el segundo CBE, se actualizan certificados ISO/ENS para cubrir producción y se formaliza compromiso partner cloud. Condición mínima para go-live: accesos, inventario y documentación cliente entregados; herramientas ITSM y backup configurados; personal y partners adscritos y acreditados.

20. Documentos revisados:
1. A2 · Administrativo-legal
2. A3 · Requisitos de solvencia de la empresa
3. A4 · Criterios de adjudicación
4. A6 · Requisitos del servicio
5. A8 · Perfiles y equipo
6. A9 · Seguridad y protección de datos
7. A10 · Compras, proveedores y colaboradores

---

Extracción de viabilidad:
| Parámetro                  | Estado     | Dato decisivo                                    | Fuente                  | Acción                       |
|----------------------------|------------|--------------------------------------------------|-------------------------|------------------------------|
| Especialización Azure VMware| NO ACREDITADO| Caducada, sin renovación aportada                | Dossier interno E5      | Renovar y formalizar partner |
| CBE segundo proyecto       | NO ACREDITADO| No aportado, solo ficha comercial                | Dossier interno E3      | Obtener CBE firmado          |
| ISO 20000-1                | NO ACREDITADO| No disponible                                    | Dossier interno E4      | No ofertar sin alternativa   |
| ISO 27001/ENS producción   | NO ACREDITADO| Alcance no cubre producción                      | Dossier interno E4      | Ampliar alcance o partner    |
| Certificados personales    | PENDIENTE VALIDACION| Falta evidencia de vigencia AWS y PMP     | Dossier interno E6      | Aportar certificados         |
| ROLECE                     | CUMPLE     | Certificado vigente a 15/09/2026                 | Dossier interno E7      | Aportar declaración variaciones|
| Seguro RC                  | CUMPLE     | Vigente hasta 31/12/2026                         | Dossier interno E2      | Compromiso renovación        |
| Patrimonio neto            | CUMPLE     | 410.000 EUR a 31/12/2025                         | Dossier interno E1      | -                            |
| Volumen ventas IT          | CUMPLE     | 1.180.000 EUR en 2025                            | Dossier interno E1      | -                            |