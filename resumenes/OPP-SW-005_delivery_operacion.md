1. Veredicto ejecutivo Delivery / Operacion: OPERABLE

2. Operational Readiness Score:
| Area                  | Score | Semaforo                        | Razon                                                                                 |
|-----------------------|-------|----------------------------------|---------------------------------------------------------------------------------------|
| Personal              | 95    | Cubierto                         | Todos los perfiles requeridos disponibles, experiencia relevante, sin gaps críticos.   |
| Turnos                | 90    | Cubierto                         | 8x5 cubierto con equipo base, sin necesidad de 24x7 ni fines de semana.               |
| Herramientas          | 85    | Cubrible con acciones            | Licencias Power BI Pro y gateway deben comprarse antes de inicio.                     |
| Infraestructura       | 85    | Cubrible con acciones            | Workspace cloud y gateway requieren validación con cliente y compra si aplica.        |
| Partners              | 90    | Cubierto                         | Cloud Partner Ficticio S.A. disponible si se requiere cloud propio.                   |
| Cobertura geografica  | 100   | Cubierto                         | Servicio remoto, usuarios en Andalucía, sin requerimientos de presencialidad.         |
| Transicion            | 90    | Cubierto                         | 3 semanas factible, requiere acceso y validación de herramientas.                     |
| SLA                   | 90    | Cubierto                         | SLA 8x5, 2h/1d cubierto con equipo y herramientas propuestas.                         |
| Continuidad           | 85    | Cubrible con acciones            | Bus factor 1 en BI, backup disponible, factor vacaciones a considerar.                |
| Dependencias cliente  | 80    | Cubrible con acciones            | Accesos, inventario y validación gateway/workspace a confirmar con cliente.           |
| **TOTAL**             | **89**| **Operable con acciones menores**|                                                                                       |

3. Alcance operativo real:
| Usuarios | Sedes      | Sistemas/Apps | Dispositivos/Activos | Horario | Modalidad | Tickets/mes | Cambios | Incidencias criticas | Cobertura geografica | Duracion | Go-live | Fuente |
|----------|------------|---------------|----------------------|---------|-----------|-------------|---------|----------------------|----------------------|----------|---------|--------|
| 35       | Remoto     | Power BI, ETL | N/A                  | 8x5     | Remoto    | ~10-20      | ~2-4    | 0-1                  | Andalucia/remoto     | 8 meses  | T+3sem  | Pliego |

4. Recursos humanos y dimensionamiento:
| Perfil                | Necesidad nominal | Necesidad operativa real | Disponible | Gap | Turnos/guardias | Bus factor | Accion                |
|-----------------------|-------------------|-------------------------|------------|-----|------------------|-----------|-----------------------|
| Especialista BI/datos | 1 FTE             | 1,25 FTE (vacaciones)   | 1 + backup | No  | 8x5             | 1         | Confirmar backup      |
| Analista funcional    | 0,5 FTE           | 0,6 FTE                 | 1          | No  | 8x5             | 1         | Confirmar backup      |
| Backend integraciones | 0,3 FTE           | 0,4 FTE                 | 1          | No  | 8x5             | 1         | Confirmar backup      |
| QA                    | 0,2 FTE           | 0,25 FTE                | 1          | No  | 8x5             | 1         | Confirmar backup      |

5. Cobertura de turnos y ubicaciones:
- 8x5 cubierto con equipo base.
- No se requiere 12x5, 16x5 ni 24x7.
- Servicio remoto, sin presencialidad obligatoria.
- Cobertura Andalucía y remoto nacional garantizada.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo         | Aporta           | Estado      | Necesario antes de | Impacto si falta      | Accion                |
|---------------------------|------------------|-------------|-------------------|----------------------|-----------------------|
| Power BI Pro (5 licencias)| Proveedor        | Pendiente   | Go-live           | No desarrollo BI     | Comprar               |
| Gateway Power BI          | Proveedor/Cliente| Pendiente   | Go-live           | No ETL productivo    | Validar, comprar      |
| Workspace Power BI        | Proveedor/Cliente| Pendiente   | Go-live           | No desarrollo BI     | Validar, contratar    |
| Repositorio Git           | Proveedor        | Disponible  | Go-live           | Bajo                 | Usar propio           |
| Herramienta calidad datos | Proveedor        | Pendiente   | Go-live           | Bajo/medio           | Seleccionar, provision|

7. Dependencias de Compras / Partners:
| Capacidad/Producto      | Estado A10 | Impacto operativo | SLA tercero vs SLA cliente | Riesgo | Accion                |
|------------------------|------------|-------------------|---------------------------|--------|-----------------------|
| Power BI Pro licencias | Pendiente  | Alto              | N/A                       | Bajo   | Compra anticipada     |
| Gateway Power BI       | Pendiente  | Medio             | N/A                       | Bajo   | Validar, comprar      |
| Workspace Power BI     | Pendiente  | Medio             | N/A                       | Bajo   | Validar, contratar    |
| Cloud Partner Ficticio | Cubierto   | Bajo              | 8x5                       | Bajo   | Solo si cloud propio  |

8. Modelo de soporte y escalados:
- L0: No aplica (usuarios gestores).
- L1: No aplica (usuarios finales cubiertos por cliente).
- L2: Equipo propio (Paula, Luis, Sofia) en 8x5.
- L3: Escalado a Microsoft solo para incidencias críticas de Power BI.
- Escalado a Cloud Partner solo si cloud propio.

9. Plan de transicion y go-live:
- Semana 1: Discovery, acceso a fuentes, validación herramientas.
- Semana 2: KT, shadowing, configuración Power BI, provisioning licencias.
- Semana 3: Pruebas ETL, validación conectores, formación inicial, runbooks.
- Go-live: War room, soporte intensivo, reporting diario.

10. Curva de incorporacion:
| Hito    | Recursos principales           | Herramientas           | Partners           | Bloqueos principales           |
|---------|-------------------------------|------------------------|--------------------|-------------------------------|
| T-45    | Service Manager, equipo base  | N/A                    | N/A                | N/A                           |
| T-30    | BI, backend, analista         | Validar herramientas   | N/A                | Accesos, licencias            |
| T-15    | QA, backup, formador          | Provisionar licencias  | N/A                | Gateway, workspace            |
| T-7     | Todos                        | Pruebas integracion    | Cloud Partner (si) | Validar conectores            |
| T0      | Todos                        | Operacion completa     | N/A                | N/A                           |
| T+30    | Todos                        | Reporting, mejora      | N/A                | N/A                           |

11. Dependencias de transicion:
| Dependencia           | Necesaria antes de | Responsable | Estado     | Riesgo | Mitigacion           |
|----------------------|-------------------|-------------|------------|--------|----------------------|
| Accesos fuentes      | T-14              | Cliente     | Pendiente  | Medio  | Solicitar T-30       |
| Licencias Power BI   | T-7               | Proveedor   | Pendiente  | Bajo   | Compra anticipada    |
| Gateway/workspace    | T-7               | Proveedor   | Pendiente  | Bajo   | Validar con cliente  |
| Inventario fuentes   | T-14              | Cliente     | Pendiente  | Medio  | Solicitar T-30       |
| Documentacion actual | T-14              | Cliente     | Pendiente  | Medio  | Solicitar T-30       |

12. Continuidad, capacidad y picos:
- Volumen bajo, picos asumibles con equipo base.
- Bus factor 1 en BI, backup disponible.
- Contingencia: backup remoto, teletrabajo, reporting diario.
- Riesgo bajo de rotación por duración corta.

13. Procedimientos operativos requeridos:
- Gestión de incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización ETL, inventario fuentes, reporting, reversibilidad.

14. Automatizacion y shift-left:
- Alertas automáticas de fallos ETL.
- Autoservicio de consultas frecuentes (Power BI).
- Runbooks para soporte y cambios menores.
- Reporting automatizado de calidad de datos.

15. Gap analysis operacional:
| Capacidad             | Necesidad         | Disponible | Gap | Probabilidad | Impacto | Riesgo | Accion                | Fecha limite |
|----------------------|-------------------|------------|-----|--------------|---------|--------|-----------------------|--------------|
| Licencias Power BI   | 5                 | No         | Sí  | Baja         | Alto    | Bajo   | Comprar               | T-7          |
| Gateway Power BI     | 1                 | No         | Sí  | Baja         | Medio   | Bajo   | Validar, comprar      | T-7          |
| Workspace Power BI   | 1                 | No         | Sí  | Baja         | Medio   | Bajo   | Validar, contratar    | T-7          |
| Accesos fuentes      | Completo          | No         | Sí  | Media        | Medio   | Medio  | Solicitar T-30        | T-14         |
| Inventario fuentes   | Completo          | No         | Sí  | Media        | Medio   | Medio  | Solicitar T-30        | T-14         |

16. Riesgos operativos principales:
1. Retraso en compra/licenciamiento Power BI Pro → No arranque desarrollo → Responsable: Compras → Mitigación: compra anticipada.
2. Ambigüedad gateway/workspace (cliente vs proveedor) → Bloqueo de ETL → Responsable: Preventa → Mitigación: validar antes de oferta.
3. Accesos a fuentes de datos retrasados → Bloqueo ETL/modelo → Responsable: Cliente → Mitigación: solicitar T-30.
4. Bus factor 1 en BI → Riesgo ausencia → Responsable: Operaciones → Mitigación: backup y formación cruzada.

17. Supuestos operativos:
- El cliente facilitará accesos a fuentes de datos y documentación técnica antes de T-14.
- El gateway y workspace Power BI pueden ser provisionados por el adjudicatario si el cliente no los aporta.
- El volumen de tickets y cambios es bajo y asumible por el equipo base.
- No se requiere presencialidad ni soporte fuera de 8x5.
- Validar estos supuestos antes de la oferta.

18. Preguntas al cliente:
- ¿El gateway de datos debe instalarse en infraestructura del cliente o del adjudicatario?
- ¿El workspace de desarrollo Power BI debe estar en cloud propio o se habilita en el entorno del cliente?
- ¿Se permite el uso de herramientas open source para calidad de datos?
- ¿Cuándo estarán disponibles los accesos a fuentes y documentación técnica?
- ¿Hay inventario actualizado de fuentes y diccionario de datos?

19. Decision operativa:
- OPERAR INTERNAMENTE con acciones menores: compra de licencias Power BI Pro, validación gateway/workspace, solicitud de accesos y documentación.
- Condiciones mínimas para pasar a oferta: confirmación de que el cliente facilitará accesos y documentación antes de T-14, y que la compra de licencias y herramientas puede ejecutarse antes de go-live.
- Condiciones mínimas para go-live: licencias Power BI Pro activas, gateway/workspace operativo, accesos a fuentes y documentación técnica recibidos.

20. Documentos revisados:
1. Pliego administrativo OPP-SW-005 BI expedientes
2. Pliego técnico OPP-SW-005 BI expedientes
3. Anexo solvencia OPP-SW-005 BI expedientes