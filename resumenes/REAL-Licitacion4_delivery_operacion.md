1. Veredicto ejecutivo Delivery / Operacion: NO OPERABLE

2. Operational Readiness Score:
| Area                | Score | Semaforo                  | Razon                                                                                 |
|---------------------|-------|---------------------------|---------------------------------------------------------------------------------------|
| Personal            | 20    | Gap critico               | No se cubre el número ni la experiencia/certificaciones mínimas exigidas.              |
| Turnos              | 30    | Gap critico               | No hay FTE ni cobertura real para vacaciones, bajas, picos ni suplencias.              |
| Herramientas        | 80    | Cubrible con acciones     | ITSM, GLPI, O365, hardware y móviles comprables, pero dependen de compras.             |
| Infraestructura     | 80    | Cubrible con acciones     | Centro alternativo y material cubrible, pero depende de compras y stock.               |
| Partners            | 20    | Gap critico               | No hay partners ni autónomos que cubran los gaps de personal ni certificaciones.        |
| Cobertura geografica| 20    | Gap critico               | No hay personal ni partners para cubrir todas las sedes periféricas.                   |
| Transicion          | 40    | Gap critico               | Sin personal ni partners, no es posible asumir la transición ni el shadowing.           |
| SLA                 | 30    | Gap critico               | No se puede garantizar respuesta/resolución crítica ni ANS sin equipo completo.         |
| Continuidad         | 30    | Gap critico               | Bus factor 1 en todos los roles, sin backups ni suplentes.                             |
| Dependencias cliente| 60    | Cubrible con acciones     | Accesos, inventario y documentación dependen del cliente, pero no bloquean por sí solas.|
Puntuación global: 30/100 (ALTO RIESGO OPERATIVO)

3. Alcance operativo real:
| Elemento           | Valor/Detalle                                                                 | Fuente         |
|--------------------|------------------------------------------------------------------------------|---------------|
| Usuarios           | ~900 usuarios AGE                                                             | PPT, PCAP     |
| Sedes              | Madrid (central) + 9 zonas periféricas (ver detalle PPT)                      | PPT           |
| Sistemas           | Windows Server, SQL Server, Linux, Citrix, VMware, GLPI, Zabbix, eREGES, O365 | PPT           |
| Dispositivos       | PCs, portátiles, móviles, impresoras, multifunción, switches, firewalls        | PPT           |
| Horario            | L-J 9-18h, V 8-15h, bolsa de horas para fuera de horario                      | PPT           |
| Modalidad          | Presencial en sedes, remoto para parte del soporte                            | PPT           |
| Tickets/mes        | ~1.000 (estimado, 12.000/año)                                                 | PPT           |
| Cambios            | No especificado, pero incluye cambios en sistemas y usuarios                  | PPT           |
| Incidencias crit.  | No volumetría, pero ANS exige respuesta 10min/resolución 2h                  | PPT           |
| Cobertura geog.    | Nacional, 10 zonas (Madrid + 9 periféricas)                                  | PPT           |
| Duración           | 24 meses (+24 meses prórroga)                                                | PCAP, PPT     |
| Go-live            | 1 junio 2025 o tras formalización                                             | PPT           |

4. Recursos humanos y dimensionamiento:
| Perfil                        | Necesidad nominal | Necesidad operativa real | Disponible | Gap | Turnos/guardias | Bus factor | Acción                |
|------------------------------|-------------------|-------------------------|------------|-----|------------------|-----------|----------------------|
| Técnico sistemas admin       | 2                 | 2+ backups              | 1          | 1+  | 8x5              | 1         | Contratar/partner    |
| Técnico sistemas DBA         | 1                 | 1+ backup               | 0          | 1+  | 8x5              | 0         | Contratar/partner    |
| Coordinador técnico Madrid   | 1                 | 1+ backup               | 1          | 0    | 8x5              | 1         | Contratar/partner    |
| Técnicos soporte Madrid      | 4                 | 4+ backups              | 2          | 2+  | 8x5              | 1         | Contratar/partner    |
| Técnicos soporte periferia   | 9                 | 9+ backups              | 0          | 9+  | 8x5              | 0         | Contratar/partner    |
| Certificaciones valorables   | N/A               | N/A                     | Parcial    | Sí   | N/A              | N/A       | Buscar mercado       |

5. Cobertura de turnos y ubicaciones:
- 8x5: No cubierto (faltan FTE en todas las zonas y backups).
- 12x5/16x5: No cubierto.
- 24x7: No exigido, pero tampoco cubierto.
- Guardias: Solo para incidencias puntuales, no para operación regular.
- Sedes: No hay personal ni partners para cubrir todas las sedes periféricas.
- Remoto/presencial: No hay personal suficiente para cubrir presencialidad exigida.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo | Aporta | Estado | Necesario antes de | Impacto si falta | Acción |
|--------------------|--------|--------|-------------------|------------------|--------|
| Portátiles         | Proveedor | No comprados | Go-live | No pueden operar | Comprar |
| Móviles/SIM        | Proveedor | No comprados | Go-live | No pueden operar | Comprar |
| O365/Visio/Planner | Proveedor | No comprados | Go-live | No pueden operar | Comprar |
| GLPI               | Cliente/Proveedor | Validar | Go-live | No pueden operar | Validar |
| Material oficina   | Proveedor | No comprado | Go-live | No pueden operar | Comprar |
| Centro alternativo | Proveedor | No asegurado | Go-live | Sin contingencia | Asegurar |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado A10 | Impacto operativo | SLA tercero vs SLA cliente | Riesgo | Acción |
|---------------------------|------------|-------------------|---------------------------|--------|--------|
| Personal técnico          | Gap        | No arranca ni opera| N/A                       | Crítico| Buscar mercado |
| Certificaciones valorables| Gap        | No puntúa ni opera | N/A                       | Alto   | Buscar mercado |
| Hardware/licencias        | Pendiente  | No arranca         | N/A                       | Bajo   | Planificar compras |

8. Modelo de soporte y escalados:
- L0: No exigido, pero valorable (no cubierto).
- L1: Técnicos soporte (faltan en todas las zonas).
- L2: Técnicos sistemas (faltan backups y DBA).
- L3: No definido, pero no hay especialistas para escalado avanzado.
- Escalados: No hay partners/fabricantes para Citrix, VMware, DBA, etc.

9. Plan de transicion y go-live:
- Fase 1 (T-30): No posible sin personal ni partners.
- Fase 2 (T-15): No posible sin personal ni partners.
- Fase 3 (T-7): No posible sin personal ni partners.
- Go-live: No posible sin equipo completo y herramientas compradas.

10. Curva de incorporacion:
| Hito      | Recursos | Herramientas | Partners | Bloqueos |
|-----------|----------|--------------|----------|----------|
| T-60      | Buscar mercado | N/A | N/A | Gap personal |
| T-45      | Buscar mercado | N/A | N/A | Gap personal |
| T-30      | Buscar mercado | N/A | N/A | Gap personal |
| T-15      | Buscar mercado | N/A | N/A | Gap personal |
| T-7       | Buscar mercado | N/A | N/A | Gap personal |
| T0        | No operativo | N/A | N/A | Gap personal |
| T+30      | No operativo | N/A | N/A | Gap personal |

11. Dependencias de transicion:
| Dependencia         | Necesaria antes de | Responsable | Estado | Riesgo | Mitigacion |
|---------------------|-------------------|-------------|--------|--------|------------|
| Personal completo   | Go-live           | Proveedor   | Gap    | Crítico| Buscar mercado |
| Herramientas        | Go-live           | Proveedor   | Pendiente| Medio | Planificar compras |
| Accesos/documentos  | Go-live           | Cliente     | Pendiente| Bajo  | Solicitar pronto |

12. Continuidad, capacidad y picos:
- No hay capacidad para cubrir bajas, vacaciones, picos ni rotación.
- Bus factor 1 en todos los roles.
- Sin backups ni suplentes.
- Sin contingencia de sede ni de herramienta.

13. Procedimientos operativos requeridos:
- Incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad (todos a crear/adaptar).

14. Automatizacion y shift-left:
- Oportunidad de automatizar reporting, base de conocimiento, scripts de despliegue, pero no resuelve el gap de personal.

15. Gap analysis operacional:
| Capacidad           | Necesidad | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción | Fecha limite |
|---------------------|-----------|------------|-----|--------------|---------|--------|--------|-------------|
| Personal técnico    | 17        | 2-3        | 14+ | 100%         | Crítico | Crítico| Buscar mercado | T-60 |
| Certificaciones     | Sí        | Parcial     | Sí  | 100%         | Alto    | Alto   | Buscar mercado | T-60 |
| Cobertura geográfica| 10 zonas  | 2-3        | 7+  | 100%         | Crítico | Crítico| Buscar mercado | T-60 |
| Herramientas        | Sí        | No         | Sí  | 100%         | Medio   | Medio  | Comprar        | T-30 |

16. Riesgos operativos principales:
1. No disponer de personal ni partners para arrancar ni operar el servicio (crítico).
2. No cubrir la distribución geográfica ni los turnos mínimos (crítico).
3. No poder cumplir los ANS ni los SLA de respuesta/resolución (crítico).
4. No poder cubrir bajas, vacaciones ni rotación (crítico).
5. No poder acreditar experiencia ni certificaciones (alto).

17. Supuestos operativos:
- Se asume que el cliente no aporta personal ni herramientas más allá de GLPI.
- Se asume que la subcontratación total es aceptable si se justifica.
- Se asume que la transición requiere al menos 4 semanas de shadowing.
- Todos estos supuestos deben validarse antes de oferta.

18. Preguntas al cliente:
- ¿Se permite subcontratación total de los perfiles técnicos requeridos?
- ¿Se aceptan autónomos/freelance para cubrir los gaps?
- ¿El cliente aporta alguna herramienta de ticketing o todo debe ser aportado?
- ¿Se puede cubrir la periferia con empresas locales?
- ¿Se puede acreditar experiencia/certificaciones mediante partners externos?
- ¿Se puede ampliar el plazo de transición si no se consigue el equipo completo?

19. Decision operativa:
NO OFERTAR SIN REDISEÑO. No es posible arrancar ni operar el servicio en las condiciones exigidas por el pliego con los recursos, partners y herramientas disponibles. Condiciones mínimas para pasar a oferta: cerrar acuerdos firmes con partners/subcontratistas que aporten todos los perfiles, experiencia y certificaciones requeridas, y asegurar la cobertura geográfica y de turnos. Condiciones mínimas para go-live: disponer de todo el personal, herramientas y material antes de la fecha de inicio.

20. Documentos revisados:
1. Anuncio.pdf
2. PCAP.pdf
3. PPT.pdf
4. poc (detalle licitación)
5. poc (perfil del contratante)
6. poc (perfil del contratante)