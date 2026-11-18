### 1. Veredicto ejecutivo Service Design / ITIL
**APTO CON GAPS**. La empresa cumple la mayoría de requisitos técnicos y organizativos, pero existen gaps relevantes en experiencia con ciertas herramientas (Remedy avanzado, NetApp, Workspace One UEM), cobertura 24x7 real, y capacidad de absorción de picos o expertos en tecnologías muy específicas. El riesgo operativo es gestionable si se refuerza con partners y se planifica la transición y la gestión de conocimiento.

---

### 2. Alcance y dimensionamiento del servicio
- **Servicios**: Administración integral de Workplace (físico, virtual, movilidad) para Correos y CEX. Incluye virtualización (Citrix, Hyper-V, Azure WVD), puesto físico (16.000+ equipos), movilidad (40.000+ dispositivos), proyectos especiales, gestión y gobierno.
- **Sistemas**: Citrix, Hyper-V, Azure WVD, NetApp, SQL Server, SCCM, HPDM, MDT, Intune, Workspace One UEM, Cisco UCS, dispositivos HP, Zebra, Honeywell, Samsung, Apple, etc.
- **Usuarios**: No se especifica número exacto, pero el parque gestionado es masivo (16.000+ puestos, 40.000+ dispositivos móviles).
- **Sedes**: Cobertura nacional, oficinas Correos y CEX, CPDs, almacenes, centros logísticos.
- **Horarios**: 07:00-18:30 (L-V, presencial/remoto), guardias 24x7 para incidencias críticas y tareas programadas.
- **Modalidad**: Mixta (presencial mínimo 1 recurso por sede principal, resto remoto/intercambiable).
- **Cobertura geográfica**: Nacional, con recursos en remoto y presencial según necesidad.
- **Volumetrías**: Se aportan estimaciones de equipos y dispositivos, pero no de tickets/incidencias/cambios. Impacto: dimensionamiento crítico, riesgo de subestimación de recursos.

---

### 3. Modelo de servicio exigido
- **Estructura**: No hay Service Desk N1 propio, sino administración y soporte N2/N3 especializado por dominios (virtualización, workplace, movilidad, proyectos especiales).
- **Operación**: Gestión integral extremo a extremo, soporte a CAU/Microinformática/TZ, colaboración con otros proveedores.
- **Mantenimiento**: Correctivo, evolutivo, preventivo, gestión de cambios, parches, backups, pruebas de recuperación.
- **Monitorización**: Proactiva, definición de métricas y alertas, informes periódicos.
- **Servicios especializados**: Panel de expertos bajo demanda (IoT, cloud, movilidad, etc.), consultoría y proyectos especiales.

---

### 4. Procesos ITIL requeridos
| Proceso                   | Explicito/Implicito | Evidencia textual | Exigencia | Capacidad actual | Gap |
|---------------------------|---------------------|-------------------|-----------|------------------|-----|
| Incident Management       | Explícito           | Gestión incidencias en PoST/Remedy | Obligatorio | Implantado | Ninguno |
| Request Fulfilment        | Explícito           | Peticiones en PoST/Remedy | Obligatorio | Implantado | Ninguno |
| Change Management         | Explícito           | Cambios en PoST/Remedy | Obligatorio | Implantado (CAB ligero) | Ninguno |
| Configuration Management  | Explícito           | Gestión activos en Remedy Asset | Obligatorio | Parcial (diseño/carga, no descubrimiento auto) | Gap en reconciliación/descubrimiento |
| Knowledge Management      | Explícito           | Base de conocimiento en Remedy | Obligatorio | Implantado | Ninguno |
| Service Level Management  | Explícito           | Gestión ANS en Remedy SLM | Obligatorio | Implantado | Ninguno |
| Availability Management   | Implícito           | Informes, monitorización, HA | Recomendado | Parcial (cloud fuerte, legacy limitado) | Gap en legacy |
| Capacity Management       | Implícito           | Informes de consumo, optimización | Recomendado | Parcial | Gap en métricas de entrada |
| Continuity Management     | Implícito           | Backups, pruebas recuperación | Recomendado | Parcial (DR/BCP bajo proyecto) | Gap en continuidad formal |
| Release/Deployment        | Implícito           | Subida de versiones, parches | Obligatorio | Implantado | Ninguno |
| Event Management          | Implícito           | Monitorización, alertas | Obligatorio | Parcial (Azure Monitor, no Remedy) | Gap en integración |
| Continual Improvement     | Implícito           | Propuestas de mejora, innovación | Obligatorio | Implantado | Ninguno |

---

### 5. SLA, KPI y penalizaciones
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo operativo |
|------------------|----------|-----------|------------|----------|---------|--------------|------------------|-----|-----------------|
| Incidencias Alta | P1       | -         | <4h        | 100%     | L-V 8-21| 25% facturación | Disponible en apps conocidas | Riesgo en 24x7 y picos | Alto si no hay refuerzo |
| Incidencias Media| P2       | -         | <12h       | 100%     | L-V 8-18:30| 5% facturación | Disponible | Bajo | Bajo |
| Incidencias Baja | P3       | -         | <72h       | 100%     | L-V 8-18:30| 1% facturación | Disponible | Bajo | Bajo |
| Peticiones Alta  | P1       | -         | <4h        | 100%     | L-V 8-21| 25% facturación | Disponible | Bajo | Bajo |
| Peticiones Media | P2       | -         | <12h       | 100%     | L-V 8-18:30| 5% facturación | Disponible | Bajo | Bajo |
| Peticiones Baja  | P3       | -         | <72h       | 100%     | L-V 8-18:30| 1% facturación | Disponible | Bajo | Bajo |
| Sustitución perfil| -       | 15 días   | -          | 100%     | -       | 25-100% facturación | Riesgo si rotación alta | Gap si rotación inesperada | Medio |
| Plan de parches  | -        | -         | 2/año      | 100%     | -       | 100% facturación 1 mes | Disponible | Bajo | Bajo |

---

### 6. Modelo de priorización
- **Niveles**: P1 (Alta, >40 tickets, caída total/parcial, horario 8-21h), P2 (Media, degradación parcial, <40 tickets), P3 (Baja, disfunción menor).
- **Impacto x urgencia**: No se detalla matriz, pero la definición es clara para P1/P2/P3. No se menciona P4.
- **Ambigüedades**: Riesgo en interpretación de "crítica" y en escalado fuera de horario.
- **Riesgos**: Subjetividad en categorización, riesgo de escalado insuficiente en 24x7.

---

### 7. Organización y modelo operativo
- **Roles exigidos**: Responsable de gestión, administradores de sistemas virtualizados, NetApp, SQL, comunicaciones Cisco, sistemas, movilidad, expertos bajo demanda.
- **Dedicaciones**: Recursos dedicados diferenciados por servicio y compañía (mínimos: 3 virtualización, 3 puesto trabajo, 2 movilidad, 1 gestión, expertos bajo demanda).
- **Guardias**: 24x7 solo para incidencias críticas y tareas programadas, en modo guardia.
- **Presencialidad**: Mínimo 1 recurso presencial por sede principal, resto remoto/intercambiable.
- **Sustituciones**: Máx. 15 días, con 5 días de solape.
- **Idiomas**: Español, inglés técnico para soporte fabricantes.
- **Certificaciones**: Microsoft, Citrix, NetApp, Cisco, VMware, deseables en Workspace One UEM.
- **Perfiles internos**: Encajan en gestión, sistemas, cloud, QA, BI, ciberseguridad. Gap en NetApp, Workspace One UEM, expertos movilidad avanzada.

---

### 8. Gobierno del servicio
- **Comités**: Estratégico (dirección, trimestral), Táctico (seguimiento, mensual), Operativo (semanal).
- **Entregables**: Informes de estado, cuadros de mando, actas, planes de calidad, gestión de riesgos, informes ANS, propuestas de mejora.
- **Escalados**: Definidos por niveles, con roles claros y matriz RACI.

---

### 9. Herramientas ITSM, CMDB y monitorización
- **Obligatoria**: Remedy (PoST) para ticketing, gestión de activos, cambios, ANS, conocimiento.
- **Integraciones**: Con Directorio Activo, acceso remoto, reporting.
- **Portal**: PoST, acceso intranet y remoto.
- **Inventario/CMDB**: Remedy Asset Management, gestión de ciclo de vida, gap en descubrimiento automático.
- **Auditorías**: Acceso, cambios, reporting, cumplimiento ANS.
- **Reporting**: Informes periódicos, cuadros de mando.

---

### 10. Transición, toma de control y reversibilidad
- **Fases**: Transición (1 mes, shadowing, plan de conocimiento, configuración equipos y comités), prestación/mejora continua, reversión (1 mes, reverse shadowing, entrega documentación, acceso a sistemas, soporte a nuevo adjudicatario).
- **Shadowing**: Equipo mixto saliente/entrante, transferencia de conocimiento, no facturable.
- **Migración tickets**: No detallada, pero se asume continuidad en PoST.
- **Configuración SLA**: En transición, con validación y reporting.
- **Formación**: A cargo del adjudicatario, con soporte de Correos.
- **Documentación**: Entrega y actualización obligatoria, propiedad de Correos/CEX.

---

### 11. Continuidad, disponibilidad y seguridad operativa
- **RTO/RPO**: No definidos explícitamente, pero se exige plan de backups, pruebas mensuales de recuperación, alta disponibilidad en plataformas críticas.
- **Backups**: Definición, implantación, pruebas mensuales, documentación.
- **Contingencia**: Planes de recuperación, documentación, pruebas periódicas.
- **Accesos**: Gestión de identidades, integración con AD, MFA no explícito pero recomendable.
- **Usuarios privilegiados**: Control, auditoría, baja/alta, cumplimiento ENS/ISO 27001.
- **Vulnerabilidades**: Parcheo bianual mínimo, reporting, colaboración con equipos de seguridad.
- **ENS/RGPD**: Cumplimiento obligatorio, soporte a auditorías, documentación.
- **Incidentes de seguridad**: Notificación, soporte a investigación, reporting.

---

### 12. Automatización, self-service y mejora continua
- **Exigencias**: Automatización máxima en administración, scripts (PowerShell, Bash, etc.), autoservicio, evaluación periódica de tareas automatizables.
- **Oportunidades**: RPA ligero, auto-remediation, chatbot FAQ, base de conocimiento, propuestas de innovación periódicas.

---

### 13. Reporting y gestión del conocimiento
- **Informes**: Estado del servicio, ANS, calidad, riesgos, capacidad, calidad, cierre, actas.
- **Cuadros de mando**: Mensuales, por niveles (operativo, táctico, estratégico).
- **Base de conocimiento**: Obligatoria, Remedy, registro de soluciones, workarounds, problemas conocidos.
- **Runbooks/FAQs**: Documentación técnica, procedimientos, videotutoriales.
- **Propiedad documental**: Correos/CEX, entrega y actualización obligatoria.

---

### 14. Matriz de evaluación Service Design
(Ver siguiente respuesta por límite de espacio)

---

### 15. Riesgos operativos principales
1. Subestimación de recursos por falta de volumetrías de tickets/incidencias.
2. Gaps en experiencia con herramientas específicas (Remedy avanzado, NetApp, Workspace One UEM).
3. Riesgo en cobertura 24x7 real y picos de trabajo.
4. Rotación de perfiles críticos y penalizaciones asociadas.
5. Integración y uso correcto de PoST/Remedy y reporting ANS.
6. Transferencia de conocimiento insuficiente en transición.
7. Falta de métricas de capacidad y disponibilidad en entornos legacy.
8. Riesgo de penalizaciones acumulativas por incumplimiento de ANS.

---

### 16. Modelo operativo recomendado para ofertar
- **Estructura**: Equipo dedicado por dominio (virtualización, workplace, movilidad), responsable de gestión, expertos bajo demanda, soporte a CAU/Microinformática.
- **Procesos**: ITIL completo, con especial refuerzo en gestión de cambios, incidentes, conocimiento y activos.
- **Herramientas**: Uso estricto de Remedy/PoST, reporting automatizado, integración con AD y monitorización.
- **Gobierno**: Comités operativo (semanal), táctico (mensual), estratégico (trimestral), reporting y escalados claros.
- **Transición**: Plan detallado de shadowing, transferencia de conocimiento, formación, documentación, validación de ANS.
- **Automatización**: Scripts, RPA, auto-remediation, propuestas de innovación periódicas.
- **Mejora continua**: Backlog de mejoras, propuestas trimestrales, base de conocimiento viva.

---

### 17. Preguntas o aclaraciones al órgano de contratación
1. ¿Volumetrías históricas de tickets, incidencias, cambios y peticiones por servicio y prioridad?
2. ¿Detalle de integración y uso de Remedy/PoST: APIs, reporting, acceso externo?
3. ¿Requisitos de descubrimiento automático y reconciliación en CMDB?
4. ¿RTO/RPO exigidos por servicio crítico y pruebas de contingencia?
5. ¿Detalle de penalizaciones acumulativas y ejemplos de aplicación?
6. ¿Definición de "incidencia crítica" fuera de horario y escalado 24x7?
7. ¿Detalle de proyectos especiales y tecnologías previstas?
8. ¿Requisitos de formación/certificación en Workspace One UEM y NetApp?
9. ¿Matriz de priorización impacto x urgencia y ejemplos prácticos?
10. ¿Detalle de reporting y cuadros de mando requeridos (formatos, periodicidad)?

---

### 18. Documentos revisados
1. ANEXO I.pdf
2. Anuncio.pdf
3. DOC20240806095753Pliegodefinitivofirmado.pdf
4. DOC_CD2024-000901195.pdf
5. poc (detalle licitación)
6. poc (perfil contratante)
7. CORREOS-Codigo-General-de-Conducta.pdf (no accesible)
8. perfil-contratante
9. PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf