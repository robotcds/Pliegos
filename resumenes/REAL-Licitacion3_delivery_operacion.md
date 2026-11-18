1. Veredicto ejecutivo Delivery / Operacion: NO OPERABLE

2. Operational Readiness Score:
| Area                  | Score | Semaforo                  | Razon                                                                                 |
|-----------------------|-------|---------------------------|---------------------------------------------------------------------------------------|
| Personal              | 10    | Gap critico               | No se cubren perfiles ni certificaciones mínimas exigidas en ninguno de los lotes.      |
| Turnos                | 20    | Gap critico               | No hay FTE ni partners para cubrir 24x7 ni presencialidad nacional.                    |
| Herramientas          | 70    | Cubrible con acciones     | ITSM y monitorización cubribles, pero falta validación integración con cliente.         |
| Infraestructura       | 60    | Cubrible con acciones     | Hardware/logística cubrible con partner, pero dependiente de stock y acuerdos.         |
| Partners              | 10    | Gap critico               | No existe partner nacional que cubra solvencia técnica ni recursos humanos.            |
| Cobertura geografica  | 20    | Gap critico               | No hay red nacional ni cobertura 4h en todas provincias.                               |
| Transición            | 30    | Gap critico               | Sin recursos ni partners, transición y shadowing no son viables.                      |
| SLA                   | 10    | Gap critico               | No se puede garantizar SLA 24x7 ni ANS sin equipo ni partners.                        |
| Continuidad           | 20    | Gap critico               | Bus factor 1 en todos los roles críticos, sin backup ni refuerzo.                      |
| Dependencias cliente  | 50    | Info insuficiente         | Faltan detalles de accesos, inventario y colaboración del proveedor saliente.           |
Puntuación global: 25/100

3. Alcance operativo real:
| Elemento         | Valor/Detalle                                                                 | Fuente                  |
|------------------|------------------------------------------------------------------------------|-------------------------|
| Usuarios         | ~5.500 usuarios (Directorio Activo)                                           | Anexo III               |
| Sedes            | >100 sedes, 30 capitales de provincia, CPD Madrid, Castellana 67 y 112        | Anexo II                |
| Sistemas         | Windows, Linux, Oracle, SQL, VMware, O365, Azure, AWS, NetApp, Fortinet, etc. | Anexo III, IV           |
| Dispositivos     | >13.000 puestos, 7000 portátiles, 4000 monitores, 400 impresoras, etc.        | Anexo IV                |
| Horario          | 24x7 CAU, 8-20h presencial, guardias fuera horario, festivos incluidos        | PPT, PCAP               |
| Modalidad        | Presencial en Madrid, mixto en resto, remoto parcial                          | PPT                     |
| Tickets/mes      | CAU: ~730/mes, Soporte: ~615/mes, Lote 2: ~175/mes                            | Anexo VI                |
| Cambios          | No detallado, pero bolsa de horas para cambios y proyectos                    | PPT                     |
| Incidencias P1   | No detallado, pero SLA exige <15 min respuesta 24x7                           | PPT, ANS                |
| Cobertura geo    | Nacional, 30 capitales, Baleares, Canarias, Ceuta/Melilla (gap)               | Anexo II, PPT           |
| Duración         | 25 meses + 24 meses prórroga                                                  | PCAP                    |
| Go-live          | 1 mes transición, arranque pleno tras shadowing                               | PPT, PCAP               |

4. Recursos humanos y dimensionamiento:
| Perfil                                 | Necesidad nominal | Necesidad real | Disponible | Gap | Turnos/guardias | Bus factor | Acción |
|----------------------------------------|-------------------|----------------|------------|-----|-----------------|-----------|--------|
| Director de proyecto                   | 1                 | 1              | 1          | 0   | 8x5             | 2         | Cubierto solo para L1, no L2 |
| Supervisor CAU                         | 1                 | 1              | 0          | 1   | 24x7            | 1         | Buscar externo |
| Agentes CAU                            | 6+                | 8-10           | 0          | 8-10| 24x7            | 1         | Buscar externo |
| Técnicos microinformática              | 6                 | 8-10           | 0          | 8-10| 8x5/guardias    | 1         | Buscar externo |
| Coordinador soporte gabinetes          | 1                 | 1              | 0          | 1   | 8-22h           | 1         | Buscar externo |
| Técnicos senior microinf. gabinetes    | 3                 | 3-4            | 0          | 3-4 | 8-22h           | 1         | Buscar externo |
| Técnicos gestión almacenes             | 2                 | 2              | 0          | 2   | 8x5             | 1         | Buscar externo |
| Jefe equipo administración sistemas    | 1                 | 1              | 0          | 1   | 8-20h           | 1         | Buscar externo |
| Técnico senior sistemas                | 6                 | 6-8            | 0          | 6-8 | 8-20h/guardias  | 1         | Buscar externo |
| Técnico junior sistemas                | 2                 | 2              | 0          | 2   | 8-20h           | 1         | Buscar externo |
| Jefe equipo redes                      | 1                 | 1              | 0          | 1   | 8-20h/guardias  | 1         | Buscar externo |
| Técnico senior redes                   | 2                 | 2              | 0          | 2   | 8-20h/guardias  | 1         | Buscar externo |
| Técnico soporte infra/cableado/CPD     | 1                 | 1              | 0          | 1   | 8-20h           | 1         | Buscar externo |
| Bolsa especialistas (horas extra)      | 2.640-7.040h      | 2.640-7.040h   | 0          | 100%| Variable        | 0         | Buscar externo |

5. Cobertura de turnos y ubicaciones:
- 24x7 CAU: No cubierto, ni con guardias ni con equipo base.
- 8x5/12x5/16x5: No cubierto, falta personal para solapes, vacaciones y picos.
- Guardias: No cubierto, no hay personal ni partner.
- Fines de semana/festivos: No cubierto.
- Sedes: No hay red nacional ni partner con solvencia técnica.
- Remoto/presencial: Solo Madrid cubierto parcialmente, resto gap total.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo         | Aporta         | Estado     | Necesario antes de | Impacto si falta         | Acción                |
|----------------------------|----------------|------------|--------------------|--------------------------|----------------------|
| ITSM (cliente)             | Cliente        | OK         | Go-live            | Bajo                     | Validar integración  |
| ITSM (propio)              | Proveedor      | OK         | Go-live            | Bajo                     | No necesario         |
| Monitorización             | Cliente        | OK         | Go-live            | Bajo                     | Validar integración  |
| CMDB                       | Cliente        | OK         | Go-live            | Bajo                     | Validar integración  |
| Stock hardware             | Partner        | Pendiente  | Go-live            | Crítico                  | RFQ urgente          |
| Logística/RAEE             | Partner        | OK         | Go-live            | Medio                    | Confirmar compromiso |
| Licencias software         | Cliente        | OK         | Go-live            | Bajo                     | Validar              |
| Accesos VPN                | Cliente        | Pendiente  | Go-live            | Crítico                  | Solicitar            |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado | Impacto operativo | SLA tercero vs SLA cliente | Riesgo | Acción |
|---------------------------|--------|-------------------|---------------------------|--------|--------|
| Personal técnico nacional  | Gap    | No arranca        | N/A                       | Máximo | Buscar partner nacional |
| Certificaciones empresa    | Gap    | No arranca        | N/A                       | Máximo | Buscar partner nacional |
| Stock hardware             | OK     | Cubrible          | NBD                       | Bajo   | RFQ/confirmar stock    |
| Logística/RAEE             | OK     | Cubrible          | 48/72h                    | Medio  | Confirmar compromiso   |

8. Modelo de soporte y escalados:
- L0: No aplica.
- L1: CAU 24x7, no cubierto.
- L2: Soporte microinformática, sistemas, redes, no cubierto.
- L3: Escalado a fabricante/partner, no cubierto.
- Escalados: No hay partner/fabricante con SLA back-to-back.

9. Plan de transición y go-live:
- Fase 1: Discovery y solicitud de accesos (T-30)
- Fase 2: Incorporación de personal y shadowing (T-15)
- Fase 3: Configuración herramientas y pruebas (T-7)
- Fase 4: War room y go/no-go (T0)
- Fase 5: Operación estable (T+30)
No viable sin personal ni partner.

10. Curva de incorporación:
| Hito   | Recursos | Herramientas | Partners | Bloqueos |
|--------|----------|--------------|----------|----------|
| T-60   | 0        | 0            | 0        | Total    |
| T-45   | 0        | 0            | 0        | Total    |
| T-30   | 0        | 0            | 0        | Total    |
| T-15   | 0        | 0            | 0        | Total    |
| T-7    | 0        | 0            | 0        | Total    |
| T0     | 0        | 0            | 0        | Total    |
| T+30   | 0        | 0            | 0        | Total    |

11. Dependencias de transición:
| Dependencia         | Necesaria antes de | Responsable | Estado   | Riesgo   | Mitigación         |
|---------------------|--------------------|-------------|----------|----------|--------------------|
| Accesos VPN         | Go-live            | Cliente     | Pendiente| Crítico  | Solicitar urgente  |
| Inventario activos  | Go-live            | Cliente     | Pendiente| Crítico  | Solicitar urgente  |
| Documentación KT    | Go-live            | Cliente     | Pendiente| Crítico  | Solicitar urgente  |
| Personal técnico    | Go-live            | Proveedor   | Gap      | Máximo   | Buscar partner     |

12. Continuidad, capacidad y picos:
- No hay capacidad de crecimiento, picos ni contingencia.
- Bus factor 1 en todos los roles críticos.
- Sin personal, cualquier ausencia implica caída del servicio.
- No hay plan de contingencia ni backup.

13. Procedimientos operativos requeridos:
- Incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad. Todos deben ser adaptados y validados con el cliente.

14. Automatización y shift-left:
- No aplicable sin equipo. Oportunidades futuras: chatbot CAU, auto-remediation, scripts, reporting automatizado.

15. Gap analysis operacional:
| Capacidad                  | Necesidad | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción | Fecha límite |
|----------------------------|-----------|------------|-----|--------------|---------|--------|--------|-------------|
| Personal técnico           | 100%      | 0%         | 100%| 100%         | Máximo  | Máximo | Buscar partner | T-30 |
| Certificaciones empresa    | 100%      | 30%        | 70% | 100%         | Máximo  | Máximo | Buscar partner | T-30 |
| Cobertura nacional         | 100%      | 0%         | 100%| 100%         | Máximo  | Máximo | Buscar partner | T-30 |
| SLA 24x7                   | 100%      | 0%         | 100%| 100%         | Máximo  | Máximo | Buscar partner | T-30 |
| Stock hardware             | 100%      | 80%        | 20% | 50%          | Medio   | Medio  | RFQ           | T-15 |

16. Riesgos operativos principales:
1. Falta total de personal técnico: Exclusión inmediata.
2. Falta de certificaciones: Exclusión inmediata.
3. No cobertura nacional: Penalización y exclusión.
4. No cumplimiento SLA: Penalización y exclusión.
5. No acceso a herramientas/inventario: Arranque fallido.

17. Supuestos operativos:
- Se asume que el cliente aporta herramientas ITSM, monitorización y licencias base.
- Se asume que la subcontratación nacional es permitida y viable.
- Se asume que el cliente facilitará accesos, inventario y documentación antes de go-live.
- Todos estos supuestos deben validarse antes de oferta.

18. Preguntas al cliente:
- ¿Se permite subcontratación total de servicios técnicos?
- ¿Se aceptan UTEs para aportar solvencia técnica y certificaciones?
- ¿Qué documentación exacta se exige para acreditar experiencia/certificaciones?
- ¿El cliente aporta todas las licencias de software base?
- ¿Se puede ampliar el plazo de transición si no hay solapamiento con proveedor saliente?
- ¿Se puede presentar oferta condicionada a cierre de partner nacional?

19. Decision operativa:
NO OFERTAR SIN REDISEÑO RADICAL DEL MODELO. No es operable ni arrancable con los recursos, partners y certificaciones actuales. Condiciones mínimas para pasar a oferta: cierre de acuerdo con partner nacional que aporte todos los perfiles, certificaciones y cobertura. Condiciones mínimas para go-live: personal adscrito, certificaciones acreditadas, stock y accesos validados, transición de al menos 4 semanas.

20. Documentos revisados:
1. DOC2024020214010801+PPT+2023+VI.pdf
2. DOC20240202141404130-24_PLIEGO.pdf
3. DOC20240202144445012+Anexo+II+Lista+final+de+sedes+del+MITMA+7+nov+2023.pdf
4. DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf
5. DOC20240202144519014+Anexo+IV+Resumen+de+activos.pdf
6. DOC20240202144535015+Anexo+V+Conocimientos+equipo+de+trabajo.pdf
7. DOC20240202144619016+Anexo+VI+Datos+de+peticiones+de+servicio+e+incidencias.pdf
8. DOC_CD2024-000159639.pdf
9. DOC_CN2024-000157989.pdf
10. poc (DOC_CD2024-000159639.pdf)
11. poc (DOC_CD2024-000159639.pdf)
12. poc (DOC_CD2024-000159639.pdf)