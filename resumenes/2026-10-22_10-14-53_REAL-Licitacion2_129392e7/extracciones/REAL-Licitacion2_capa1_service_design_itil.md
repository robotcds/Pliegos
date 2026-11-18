# Resumen factual del servicio requerido

El contrato tiene por objeto la prestación del servicio de Administración Workplace para la Sociedad Estatal de Correos y Telégrafos S.A. S.M.E. y su filial Correos Express (CEX), durante al menos 24 meses, incluyendo la definición, diseño, construcción, mantenimiento, estandarización, auditoría, innovación y evolución de la administración del puesto de trabajo físico, virtual y de movilidad. El servicio se estructura en módulos: Virtualización, Puesto de Trabajo, Movilidad, Proyectos Especiales Correos y Proyectos Especiales CEX, con una capa de gestión común y modelo de gobierno. Se exige un servicio integral, con recursos técnicos compartidos o diferenciados según el módulo, y la cobertura de todas las prestaciones y tareas asociadas a la gestión del servicio, proyectos y modelo de gobierno, bajo parámetros de calidad comprometidos en los Acuerdos de Nivel de Servicio (ANS).

---

# 1. Alcance y volumetrías

| Dato | Valor/Unidad | Periodo | Fuente |
|---|---|---|---|
| Duración inicial | 24 meses | Contrato | DOC20240806095753Pliegodefinitivofirmado.pdf, p.5, Anexo I p.32 |
| Prórrogas | 2 (12 meses y 3 meses) | Eventual | DOC20240806095753Pliegodefinitivofirmado.pdf, p.5 |
| Empresas cubiertas | Correos y CEX | Contrato | DOC20240806095753Pliegodefinitivofirmado.pdf, p.4, Anexo I p.32 |
| Virtualización ThinClient | >12.000 dispositivos HP | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.35 |
| Virtualización Citrix | 100 servidores infra, 600 servidores escritorios, 500 VDIs, 15.000 sesiones/máquinas virtuales | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.35 |
| Virtualización WVD | 1.000 VDIs Azure WVD | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.35 |
| Virtualización física | 8 chasis Cisco UCS, 32 UCS B200 M5, 48 UCS B200 M4, etc. | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.35 |
| Puesto físico | >16.000 equipos (68% sobremesa/thinclient, 25% portátiles, 5% dispensadores, 2% autoservicio) | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.41 |
| Dispositivos movilidad | 34.000 PDA Honeywell EDA52, 2.000 Zebra TC56, 400 Zebra TC57, 100 Zelenza, 3.100 smartphones Samsung/Xiaomi/Huawei, 130 iPhone, 100 tablets Samsung TAB A8 LTE | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.45 |
| Plataformas movilidad | 9 host HP DL360, 1 host Veritas Backup, 2 vSphere/vCenter, 3 entornos MDM Workspace One UEM | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.45-46 |
| Horas estimadas por servicio | Virtualización: 14.400h, Puesto de trabajo: 10.800h, Movilidad: 7.200h, Gobierno: 480h, NetApp: 480h, Comunicaciones: 480h, BBDD SQL: 480h | 24 meses | DOC20240806095753Pliegodefinitivofirmado.pdf, p.73 |
| Modalidad de prestación | Presencial/remoto, mixto, con recursos presenciales mínimos y resto remoto | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.40, 44, 50, 72 |
| Horario habitual | L-V 07:00-18:30 (incluidos festivos no nacionales), mínimo 1 recurso presencial en Correos y 1 en CEX (09:00-18:30) | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.40, 44, 50 |
| Guardia 24x7 | Soporte incidencias relevantes y actividades fuera de horario | Vigencia | DOC20240806095753Pliegodefinitivofirmado.pdf, p.40, 44, 50 |

---

# 2. Modelo de servicio exigido

- Servicio integral, recursos técnicos compartidos o diferenciados según módulo (Virtualización, Puesto de Trabajo, Movilidad, Proyectos Especiales Correos, Proyectos Especiales CEX).
- Capa de gestión común y modelo de gobierno.
- Recursos mínimos dedicados diferenciados por servicio y compañía (ver detalle en organización y roles).
- Soporte de tercer nivel a equipos internos de Correos/CEX (Microinformática, CAU, TZ, etc.).
- Colaboración con equipos de desarrollo corporativos.
- Uso de herramientas corporativas de ticketing (PoST/Remedy) y documentación (Sharepoint o equivalente).
- Modalidad presencial/remoto, con guardias 24x7 para incidencias relevantes.

---

# 3. Procesos y actividades (ITIL/funcionales)

| Proceso/actividad | Expreso en pliego | Exigencia descrita | Fuente |
|---|---|---|---|
| Gestión de incidencias | ITIL citado expresamente (Remedy Help Desk) | Uso de PoST/Remedy para gestión de incidencias y peticiones | DOC20240806095753Pliegodefinitivofirmado.pdf, p.56 |
| Gestión de peticiones | ITIL citado expresamente (Remedy Help Desk) | Uso de PoST/Remedy para gestión de peticiones | DOC20240806095753Pliegodefinitivofirmado.pdf, p.56 |
| Gestión de cambios | ITIL citado expresamente (Remedy Change Management) | Uso de PoST/Remedy para gestión de cambios | DOC20240806095753Pliegodefinitivofirmado.pdf, p.56 |
| Gestión de activos | ITIL citado expresamente (Remedy Asset Management) | Uso de PoST/Remedy para gestión de activos | DOC20240806095753Pliegodefinitivofirmado.pdf, p.56 |
| Gestión de niveles de servicio | ITIL citado expresamente (Remedy SLM) | Uso de PoST/Remedy para gestión de ANS | DOC20240806095753Pliegodefinitivofirmado.pdf, p.56 |
| Gestión del conocimiento | ITIL citado expresamente (Remedy Help Desk) | Base de datos de conocimiento, registro y catalogación de soluciones y workarounds | DOC20240806095753Pliegodefinitivofirmado.pdf, p.56, 55 |
| Gestión de la capacidad | ITIL NO CITADO EXPRESAMENTE | Elaboración de informes periódicos para detección temprana de riesgos, optimización de recursos | DOC20240806095753Pliegodefinitivofirmado.pdf, p.37 |
| Gestión de la disponibilidad | ITIL NO CITADO EXPRESAMENTE | Monitorización continua, informes de disponibilidad, soporte 24x7 | DOC20240806095753Pliegodefinitivofirmado.pdf, p.37, 40, 44, 50 |
| Gestión de la seguridad | ITIL NO CITADO EXPRESAMENTE | Administración de servicios de seguridad, definición e implantación de políticas, integración con gestión de identidades | DOC20240806095753Pliegodefinitivofirmado.pdf, p.37, 42, 48 |
| Gestión de backups y recuperación | ITIL NO CITADO EXPRESAMENTE | Definición, implantación y ejecución de políticas de backup y pruebas de recuperación mensuales | DOC20240806095753Pliegodefinitivofirmado.pdf, p.37, 39 |
| Gestión de documentación | ITIL NO CITADO EXPRESAMENTE | Creación y mantenimiento de documentación técnica y de gestión, migración a nuevos sistemas si se requiere | DOC20240806095753Pliegodefinitivofirmado.pdf, p.38, 43, 49 |
| Gestión de la formación | ITIL NO CITADO EXPRESAMENTE | Formación a grupos de soporte y gestión, en caso necesario | DOC20240806095753Pliegodefinitivofirmado.pdf, p.40, 44, 50 |
| Gestión de proyectos especiales | ITIL NO CITADO EXPRESAMENTE | Propuestas, planificación, ejecución y reporting de proyectos especiales bajo bolsa económica | DOC20240806095753Pliegodefinitivofirmado.pdf, p.50-51 |
| Automatización de operaciones | ITIL NO CITADO EXPRESAMENTE | Automatización de procesos y tareas, desarrollo de scripts, autoservicio | DOC20240806095753Pliegodefinitivofirmado.pdf, p.38, 43, 48, 59 |

---

# 4. SLA/KPI/penalizaciones

| Servicio | Prioridad | Respuesta | Resolución | Horario | Objetivo | Penalización | Fuente |
|---|---|---|---|---|---|---|---|
| Perfil no cumple requisitos | N/A | N/A | N/A | N/A | 100% perfiles cumplen requisitos | 15% facturación mensual del servicio, sustitución en 15 días | DOC20240806095753Pliegodefinitivofirmado.pdf, p.111-112 |
| Perfil no cubierto en plazo | N/A | N/A | N/A | N/A | 100% perfiles cubiertos en 15 días naturales, 5 días traspaso | 25% facturación mensual del servicio, 100% si >30 días | DOC20240806095753Pliegodefinitivofirmado.pdf, p.112 |
| Disponibilidad recursos dedicados | N/A | N/A | N/A | N/A | 100% sin indisponibilidad >3 días laborables | 20% facturación mensual por perfil, acumulativo | DOC20240806095753Pliegodefinitivofirmado.pdf, p.113 |
| Tasa de renovación equipos | N/A | N/A | N/A | N/A | 1 o menos rotaciones por año y servicio | 20% facturación mensual de todos los servicios | DOC20240806095753Pliegodefinitivofirmado.pdf, p.113 |
| Respuesta a proyectos especiales | N/A | <15 días naturales | N/A | N/A | 100% respuestas en plazo | 15% facturación mensual de todos los servicios de la empresa peticionaria | DOC20240806095753Pliegodefinitivofirmado.pdf, p.114 |
| Resolución incidencias alta | Alta | N/A | <4h | L-V 8:00-21:00 | 100% | 25% facturación mensual del servicio | DOC20240806095753Pliegodefinitivofirmado.pdf, p.115-116 |
| Resolución incidencias media | Media | N/A | <12h (L-V 8:00-18:30) | L-V 8:00-21:00 | 100% | 5% facturación mensual del servicio | DOC20240806095753Pliegodefinitivofirmado.pdf, p.115-116 |
| Resolución incidencias baja | Baja | N/A | <72h (L-V 8:00-18:30) | L-V 8:00-21:00 | 100% | 1% facturación mensual del servicio | DOC20240806095753Pliegodefinitivofirmado.pdf, p.115-116 |
| Resolución peticiones alta | Alta | N/A | <4h | L-V 8:00-21:00 | 100% | 25% facturación mensual del servicio | DOC20240806095753Pliegodefinitivofirmado.pdf, p.117 |
| Resolución peticiones media | Media | N/A | <12h (L-V 8:00-18:30) | L-V 8:00-21:00 | 100% | 5% facturación mensual del servicio | DOC20240806095753Pliegodefinitivofirmado.pdf, p.117 |
| Resolución peticiones baja | Baja | N/A | <72h (L-V 8:00-18:30) | L-V 8:00-21:00 | 100% | 1% facturación mensual del servicio | DOC20240806095753Pliegodefinitivofirmado.pdf, p.117 |
| Plan de parcheo virtualización | N/A | N/A | 2 veces/año | N/A | 100% | 100% facturación de 1 mes del servicio de virtualización | DOC20240806095753Pliegodefinitivofirmado.pdf, p.118 |

- Penalizaciones acumulativas, posibilidad de resolución anticipada si se penaliza 3 meses consecutivos o 4 veces en 12 meses (DOC20240806095753Pliegodefinitivofirmado.pdf, p.111).

---

# 5. Reglas de priorización e impacto/urgencia

- Incidencias y peticiones categorizadas en alta, media y baja según impacto en entornos productivos, número de tickets y horario (DOC20240806095753Pliegodefinitivofirmado.pdf, p.115-117).
- Definición detallada de cada nivel de severidad/prioridad en el Anexo XVII.

---

# 6. Organización y roles exigidos

- Recursos mínimos dedicados diferenciados:
  - Virtualización: 3 recursos Correos, 1 recurso CEX
  - Puesto de trabajo: 3 recursos Correos
  - Movilidad: 1 recurso Correos, 1 recurso CEX
  - Gobierno/gestión: 1 recurso Correos/CEX
- Perfiles detallados: Responsable de gestión y seguimiento, Administrador de sistemas virtualizados, Administrador de NetApp, Administrador de BBDD SQL, Administrador de comunicaciones Cisco, Administrador de sistemas, Administrador de sistemas de movilidad, expertos bajo demanda (DOC20240806095753Pliegodefinitivofirmado.pdf, p.64-71).
- Experiencia mínima: 3-5 años según perfil, inglés técnico, certificaciones deseables.
- Modalidad mixta presencial/remoto, intercambiables, con medios técnicos propios (portátil, software, comunicaciones, teléfono directo, etc.) (DOC20240806095753Pliegodefinitivofirmado.pdf, p.72).
- Cobertura de ausencias: sustitución en 3 días laborables, penalización si no se cumple (p.113).

---

# 7. Gobierno y reporting exigidos

- Modelo de gobierno colaborativo, con roles y responsabilidades definidos, matrices RACI, comités de gestión (estratégico, táctico, operativo) con periodicidad definida (DOC20240806095753Pliegodefinitivofirmado.pdf, p.52-53, 84-85).
- Entregables de gestión: plan de servicio, plan de gobierno, modelo de relación, informes de estado, cuadro de mando mensual, gestión de cambios, informes de cumplimiento de ANS, plan de riesgos, plan de calidad, plan de capacidad, informe de cierre, actas de reunión (p.54-55).
- Documentación técnica: inventarios, catálogos, procedimientos, integración con ticketing y CMDB, base de conocimiento (p.55).

---

# 8. Herramientas ITSM, CMDB, monitorización e integraciones exigidas

- Herramienta de ticketing PoST (Remedy ITSM): gestión de incidencias, peticiones, cambios, activos, ANS, conocimiento (p.56).
- Integración con Directorio Activo de Correos (p.56).
- Documentación en Sharepoint corporativo o equivalente (p.38, 43, 49).
- Monitorización continua, métricas y alertas definidas por el adjudicatario, acceso a responsables Correos/CEX, preferible plataforma única (p.37).

---

# 9. Transición, continuidad y reversibilidad exigidas

- Fase de transición: 1 mes desde firma, periodo de solapamiento con equipo saliente, transferencia de conocimiento, documentación, procedimientos, etc. (p.57-59).
- Fase de prestación: inicio tras transición, aplicación de ANS, gestión de esfuerzo y reporting (p.59).
- Fase de reversión: periodo de traspaso mínimo 15 días (recomendado 1 mes), equipo mixto, entrega de toda la documentación actualizada, acceso a servicios, soporte a nuevo adjudicatario, mínimo 5 personas en instalaciones para reversión, no se factura último mes hasta aceptación (p.61-62).
- Garantía técnica: 3 meses desde recepción conforme (p.28).

---

# 10. Automatización, self-service y gestión del conocimiento

- Automatización: administración y operación lo más automatizada posible, scripts en powershell, Basic, Bash, Visual Basic, etc. (p.38, 43, 48, 59).
- Autoservicio: evaluación y puesta a disposición de solicitudes/peticiones automatizables para autoservicio (p.38, 43, 48).
- Base de datos de conocimiento: registro, catalogación y mantenimiento de soluciones y workarounds, integración con PoST/Remedy (p.55-56).

---

# 11. Datos no localizados o ambiguos

- NO CONSTA EN LA DOCUMENTACION REVISADA: definición de N1/N2/N3 fuera de soporte de tercer nivel, detalle de Service Desk como punto único de contacto, detalle de CMDB fuera de Remedy Asset Management, detalle de reporting de satisfacción de usuario final, detalle de integración con otras herramientas ITSM externas, detalle de RTO/RPO, detalle de licencias de software a aportar por el adjudicatario, detalle de mecanismos de escalado fuera de los comités y reporting, detalle de mecanismos de continuidad de negocio (más allá de backup y pruebas de recuperación), detalle de mecanismos de borrado seguro de datos al cierre, detalle de formación mínima (horas, asistentes, modalidad), detalle de encuestas de satisfacción, detalle de mecanismos de autoevaluación o auditoría interna, detalle de gestión de cambios de arquitectura fuera de la documentación y reporting.

---

# 12. Documentos revisados

1. ANEXO I.pdf
2. Anuncio.pdf
3. DOC20240806095753Pliegodefinitivofirmado.pdf
4. DOC_CD2024-000901195.pdf
5. poc (detalle licitación)
6. poc (perfil contratante)
7. CORREOS-Codigo-General-de-Conducta.pdf (NO DISPONIBLE, error 404)
8. perfil-contratante
9. PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf

---

# Discrepancias y pendientes de aclaración

- No se han identificado discrepancias en la documentación revisada.
- Remisión a CORREOS-Codigo-General-de-Conducta.pdf pendiente de verificar por error 404.
- Algunos detalles de procesos, reporting y mecanismos de continuidad quedan pendientes de aclaración por ausencia de información específica en los documentos revisados.

---

# Trazabilidad (extracto)

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Gestión de incidencias | Proceso ITIL | Remedy Help Desk | DOC20240806095753Pliegodefinitivofirmado.pdf | p.56 | Leído |
| Resolución incidencias alta | SLA | <4h, 25% penalización | DOC20240806095753Pliegodefinitivofirmado.pdf | p.115-116 | Leído |
| Automatización | Obligación | Scripts, autoservicio | DOC20240806095753Pliegodefinitivofirmado.pdf | p.38, 43, 48, 59 | Leído |
| Fase de reversión | Reversibilidad | 15 días mínimo, entrega documentación | DOC20240806095753Pliegodefinitivofirmado.pdf | p.61-62 | Leído |
| Base de conocimiento | Gestión conocimiento | Integrada en PoST/Remedy | DOC20240806095753Pliegodefinitivofirmado.pdf | p.55-56 | Leído |
| ... | ... | ... | ... | ... | ... |

(El detalle completo se encuentra en el registro documental de preventa.)