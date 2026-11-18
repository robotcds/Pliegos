1. Veredicto ejecutivo Delivery / Operacion: ALTO RIESGO OPERATIVO

No es posible arrancar ni operar el servicio en las condiciones exigidas por el pliego con los recursos internos actuales ni con la red de partners en el modelo requerido. El gap de perfiles mobile nativos (iOS, Android, UX mobile) es crítico y la subcontratación directa está prohibida. El go-live y la operación dependen de la contratación previa de personal propio especializado, lo que no está garantizado a día de hoy.

2. Operational Readiness Score:
| Área                | Score | Semáforo                  | Razón                                                                 |
|---------------------|-------|---------------------------|-----------------------------------------------------------------------|
| Personal            | 30    | Gap crítico               | Faltan todos los perfiles mobile nativos y UX mobile.                 |
| Turnos              | 60    | Cubrible con acciones     | 12x5 cubrible si se contrata personal; guardias posibles.             |
| Herramientas        | 80    | Cubierto                  | Jira, MDM, hardware, SaaS cubribles con compras.                      |
| Infraestructura     | 80    | Cubierto                  | Operación remota, cloud y panel gestor cubribles.                     |
| Partners            | 40    | Gap crítico               | Mobile Studio no puede cubrir desarrollo principal por pliego.         |
| Cobertura geográfica| 80    | Cubierto                  | Remoto y pruebas en España cubribles.                                 |
| Transición          | 40    | Gap crítico               | Sin equipo mobile propio no se puede iniciar transición real.          |
| SLA                 | 50    | Gap crítico               | SLA P1 y soporte mobile dependen de perfiles no disponibles.           |
| Continuidad         | 30    | Gap crítico               | Bus factor 1 en QA y backend, 0 en mobile; sin backup.                |
| Dependencias cliente| 60    | Cubrible con acciones     | Accesos, cuentas stores y documentación gestionables.                 |
| **Global**          | **53**| **ALTO RIESGO OPERATIVO** | Gap crítico en personal y transición, resto cubrible con acciones.     |

3. Alcance operativo real:
| Elemento           | Valor / Detalle                                      | Fuente           |
|--------------------|------------------------------------------------------|------------------|
| Usuarios           | 60.000 ciudadanos, 120 gestores                      | Pliego técnico   |
| Sedes              | Remoto, Comunitat Valenciana                         | Pliego técnico   |
| Sistemas           | Apps iOS/Android, backend, panel gestor              | Pliego técnico   |
| Dispositivos       | 12 smartphones, 2 tablets (pruebas)                  | Pliego técnico   |
| Horario            | 12x5, guardia publicación/caída backend              | Pliego técnico   |
| Modalidad          | Remoto, pruebas físicas                              | Pliego técnico   |
| Tickets/mes        | 350 (15% mobile, 20% dudas, 65% peticiones menores)  | Pliego técnico   |
| Cambios            | No especificado                                      | Supuesto         |
| Incidencias críticas| P1 backend, P1 publicación stores                    | Pliego técnico   |
| Cobertura geográfica| España, remoto                                      | Pliego técnico   |
| Duración           | 9 meses                                              | Pliego admin.    |
| Go-live            | Semana 3 tras cuentas stores y equipo activo         | Pliego técnico   |

4. Recursos humanos y dimensionamiento:
| Perfil                  | Necesidad nominal | Necesidad real | Disponible | Gap | Turnos/guardias | Bus factor | Acción                  |
|-------------------------|-------------------|----------------|------------|-----|------------------|------------|------------------------|
| Jefe de proyecto        | 1                 | 1              | 1          | No  | 12x5             | 2          | Cubierto               |
| Backend APIs            | 1                 | 1              | 1          | No  | 12x5             | 1          | Riesgo continuidad     |
| QA mobile               | 1                 | 1              | 1          | No  | 12x5             | 1          | Riesgo continuidad     |
| iOS nativo              | 1                 | 1              | 0          | Sí  | 12x5             | 0          | Contratar              |
| Android nativo          | 1                 | 1              | 0          | Sí  | 12x5             | 0          | Contratar              |
| UX mobile               | 1                 | 1              | 0          | Sí  | 12x5             | 0          | Contratar              |

5. Cobertura de turnos y ubicaciones:
- 12x5 cubrible solo si se contrata equipo mobile propio antes de inicio.
- Guardias posibles para incidencias críticas, pero sin equipo propio no hay cobertura real.
- Remoto y pruebas físicas en España cubribles si se adquiere hardware.
- No hay cobertura 24x7 ni presencial continua.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/Activo      | Aporta           | Estado     | Necesario antes de | Impacto si falta | Acción           |
|------------------------|------------------|------------|--------------------|------------------|------------------|
| Jira Service Management| Proveedor        | Listo      | T-15               | Medio            | Configurar       |
| Hardware pruebas       | Compras          | Pendiente  | T-15               | Alto             | Comprar          |
| Cuentas Apple/Google   | Compras          | Pendiente  | T-15               | Crítico          | Comprar          |
| MDM SaaS               | Compras          | Pendiente  | T-15               | Medio            | Comprar          |
| Crash reporting UE     | Compras          | Ambiguo    | T-15               | Medio            | Validar          |
| Repositorio Git        | Proveedor        | Listo      | T-15               | Medio            | Configurar       |
| CI/CD mobile           | Proveedor        | Listo      | T-15               | Medio            | Configurar       |

7. Dependencias de Compras / Partners:
| Capacidad/Producto      | Estado           | Impacto operativo | SLA tercero vs cliente | Riesgo   | Acción           |
|------------------------|------------------|-------------------|-----------------------|----------|------------------|
| Personal mobile propio | No disponible    | Crítico           | N/A                   | Muy alto | Contratar        |
| Hardware pruebas       | Pendiente compra | Alto              | N/A                   | Medio    | Comprar          |
| Pentest mobile/backend | Partner disponible| Medio             | Cubrible              | Bajo     | Solicitar        |
| Crash reporting UE     | Ambiguo          | Medio             | Validar               | Medio    | Validar          |

8. Modelo de soporte y escalados:
- L0/L1: Cliente (ciudadanos, dudas básicas)
- L2: Adjudicatario (incidencias mobile, backend, QA)
- L3: Especialistas mobile (internos, deben ser contratados)
- Escalado a Pentest Lab para pentest, a fabricantes para cuentas stores.
- Gap: Sin equipo mobile propio, no hay escalado real posible.

9. Plan de transición y go-live:
- T-45: Contratación perfiles mobile, solicitud cuentas stores, BOM hardware.
- T-30: Configuración herramientas, onboarding equipo, compra hardware.
- T-15: Pruebas dispositivos, shadowing, runbooks, formación.
- T-7: Simulacro P1, validación SLA, war room.
- T0: Go-live condicionado a equipo completo y cuentas stores activas.

10. Curva de incorporación:
| Hito    | Recursos clave                | Herramientas/partners | Bloqueos principales           |
|---------|-------------------------------|-----------------------|-------------------------------|
| T-60    | Planificación                 | -                     | Contratación mobile           |
| T-45    | Contratación mobile           | Solicitud cuentas     | Hardware, cuentas stores      |
| T-30    | Onboarding mobile             | Jira, Git, MDM        | Hardware                      |
| T-15    | QA mobile, pruebas            | Dispositivos          | Crash reporting               |
| T-7     | Simulacro, war room           | -                     | Validación SLA                |
| T0      | Operación                     | -                     | Go-live condicionado          |

11. Dependencias de transición:
| Dependencia             | Necesaria antes de | Responsable | Estado     | Riesgo   | Mitigación           |
|------------------------|--------------------|-------------|------------|----------|----------------------|
| Contratación mobile    | T-45               | RRHH        | Pendiente  | Crítico  | Contratar antes oferta|
| Cuentas stores         | T-30               | Compras     | Pendiente  | Alto     | Solicitar urgente    |
| Hardware pruebas       | T-30               | Compras     | Pendiente  | Medio    | BOM y compra         |
| Crash reporting UE     | T-15               | Compras     | Ambiguo    | Medio    | Validar alternativa  |

12. Continuidad, capacidad y picos:
- Sin equipo mobile propio, bus factor 0 en desarrollo mobile y UX.
- QA y backend con bus factor 1, riesgo alto de continuidad.
- Picos tras campañas municipales no cubribles sin equipo completo.
- Caída de herramienta, VPN o sede: mitigable con cloud y remoto.

13. Procedimientos operativos requeridos:
- Gestión de incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad. Todos deben adaptarse a mobile nativo y apps stores.

14. Automatización y shift-left:
- Oportunidad de auto-remediation en backend y crash reporting.
- Chatbot para FAQs ciudadanas (shift-left).
- Automatización CI/CD mobile y despliegue apps.

15. Gap analysis operacional:
| Capacidad              | Necesidad         | Disponible | Gap | Probabilidad | Impacto | Riesgo   | Acción           | Fecha límite |
|------------------------|-------------------|------------|-----|--------------|---------|----------|------------------|--------------|
| iOS nativo             | 1                 | 0          | Sí  | Alta         | Crítico | Muy alto | Contratar        | T-45         |
| Android nativo         | 1                 | 0          | Sí  | Alta         | Crítico | Muy alto | Contratar        | T-45         |
| UX mobile              | 1                 | 0          | Sí  | Alta         | Crítico | Muy alto | Contratar        | T-45         |
| QA mobile              | 1                 | 1          | No  | Media        | Alto    | Alto     | Backup           | T-30         |
| Backend APIs           | 1                 | 1          | No  | Media        | Alto    | Alto     | Backup           | T-30         |
| Hardware pruebas       | 14                | 0          | Sí  | Alta         | Alto    | Alto     | Comprar          | T-30         |
| Cuentas stores         | 2                 | 0          | Sí  | Alta         | Crítico | Muy alto | Solicitar        | T-30         |
| Crash reporting UE     | 1                 | 0          | Sí  | Media        | Medio   | Medio    | Validar          | T-15         |

16. Riesgos operativos principales:
1. Falta de contratación mobile nativo: bloquea oferta y go-live. (Propietario: RRHH)
2. Subcontratación prohibida: no se puede cubrir con partner. (Propietario: Dirección)
3. Hardware pruebas no adquirido a tiempo: retrasa QA y publicación. (Propietario: Compras)
4. Cuentas stores no activas: bloquea publicación y go-live. (Propietario: Compras)
5. Bus factor 1 en QA/backend: riesgo de continuidad. (Propietario: Operaciones)

17. Supuestos operativos:
- Se podrá contratar personal mobile nativo antes de la oferta y estarán disponibles antes de T-30.
- El cliente facilitará acceso a cuentas stores y documentación técnica antes de T-15.
- El hardware de pruebas estará disponible antes de T-15.
- Crash reporting UE será aceptado o se validará alternativa.

18. Preguntas al cliente:
- ¿Se admite la contratación directa de personal mobile antes de inicio como cumplimiento del requisito de equipo propio?
- ¿Se acepta Firebase/Crashlytics si los datos se alojan en UE? ¿Alternativas recomendadas?
- ¿Es obligatorio que las cuentas Apple/Google estén a nombre del adjudicatario o pueden ser del cliente?
- ¿Se puede presentar plan de backup para perfiles críticos (QA, backend) o se exige bus factor 2 real?
- ¿Se puede ampliar el plazo de transición si la contratación de perfiles mobile se retrasa?

19. Decisión operativa:
NO OFERTAR SIN REDISEÑO. No es posible arrancar ni operar el servicio en las condiciones exigidas por el pliego con los recursos internos y partners actuales. Es imprescindible contratar desarrolladores iOS, Android y UX mobile antes de la oferta y garantizar su disponibilidad antes de T-30. El resto de dependencias (hardware, licencias, pentest) son cubribles con compras y partners. Condiciones mínimas para pasar a oferta: contratación directa de personal mobile nativo y UX mobile, compromiso de hardware y cuentas stores antes de T-30. Condiciones mínimas para go-live: equipo completo, hardware y cuentas stores activas, herramientas configuradas y formación realizada.

20. Documentos revisados:
1. Pliego administrativo OPP-SW-006 app móvil
2. Pliego técnico OPP-SW-006 app móvil
3. Anexo solvencia OPP-SW-006 app móvil