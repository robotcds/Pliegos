1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS

La empresa Sermicro Software Ficticio S.L. dispone de capacidades sólidas en Service Design e ITIL para la mayoría de los requisitos, pero existen gaps relevantes en cobertura 24x7 real, administración avanzada de ciertas herramientas (GLPI, ServiceNow), y en la gestión avanzada de CMDB y monitorización en entornos legacy. El dimensionamiento y la dispersión geográfica añaden complejidad y riesgo operativo.

2. Alcance y dimensionamiento del servicio:
- Servicios: Soporte a puesto de usuario (CAU), soporte de sistemas, comunicaciones, seguridad, gestión de inventario hardware.
- Sistemas: Infraestructura Microsoft (Windows Server, SQL Server, Active Directory, MDT, WSUS, Citrix, VMware, GLPI, Zabbix, Checkmk, WorkSpace One), eREGES/REGES, Sharepoint, Office365, VPN, WiFi, videoconferencia Teams, backup Legato Networker, cabinas NetApp/EMC.
- Usuarios: ~900 usuarios distribuidos en toda España, con concentración en Madrid (>50%).
- Sedes: Sede central Madrid + 9 zonas periféricas (todas las CCAA, Ceuta, Melilla, Baleares, Canarias).
- Horarios: Lunes a jueves 9-18h, viernes 8-15h. Cobertura extendida (mejora) hasta 24x5/24x7 para primer contacto (Nivel 0). Bolsas de horas para fuera de horario.
- Modalidad: Presencial en sedes clave, remoto y mixto. Desplazamientos puntuales (bolsa de 45 desplazamientos interprovinciales).
- Volumetría: 12.000 tickets/año (aprox.), 50% en Madrid. Impacto: requiere equipo estable, suplencias, y gestión de picos.

3. Modelo de servicio exigido:
- Estructura: N1 (CAU, presencial/remoto, pool coordinado), N2 (soporte sistemas, DBA, comunicaciones, seguridad), sin N3 explícito.
- Operación: Soporte a usuario, administración de sistemas, gestión de inventario, soporte comunicaciones, seguridad, DBA.
- Mantenimiento: Correctivo, preventivo, evolutivo (puesto, sistemas, comunicaciones).
- Monitorización: Zabbix, Checkmk, GLPI.
- Servicios especializados: Seguridad (ENS, CCN), continuidad, soporte eventos, formación.

4. Procesos ITIL requeridos:
| Proceso                | Explicito/Implicito | Evidencia textual | Exigencia | Capacidad actual | Gap |
|------------------------|---------------------|-------------------|----------|------------------|-----|
| Incident Management   | Explícito           | CAU, gestión incidencias | Obligatorio | Implantado | Bajo |
| Request Fulfilment    | Explícito           | Peticiones, catálogo | Obligatorio | Implantado | Bajo |
| Change Management     | Explícito           | Comité de Cambios | Obligatorio | Implantado (CAB ligero) | Bajo |
| Configuration Mgmt    | Implícito           | GLPI, inventario, CIs | Obligatorio | Parcial (diseño/carga) | Medio |
| Knowledge Mgmt        | Implícito           | Base documental, formación | Obligatorio | Implantado | Bajo |
| Service Level Mgmt    | Explícito           | ANS, penalizaciones | Obligatorio | Implantado | Bajo |
| Availability Mgmt     | Implícito           | 99% plataformas | Obligatorio | Parcial (cloud fuerte) | Medio |
| Capacity Mgmt         | Implícito           | Métricas, reporting | Recomendado | Parcial | Medio |
| Continuity Mgmt       | Implícito           | Planes contingencia | Recomendado | Parcial | Medio |
| Release/Deployment    | Implícito           | MDT, WSUS, Citrix | Recomendado | Implantado | Bajo |
| Event Management      | Implícito           | Zabbix, Checkmk | Obligatorio | Parcial | Medio |
| Continual Improvement | Implícito           | Plan mejora continua | Recomendado | Implantado | Bajo |

5. SLA, KPI y penalizaciones:
| Servicio | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo |
|----------|----------|-----------|------------|----------|---------|--------------|------------------|-----|--------|
| CAU      | Crítica  | 10 min    | 2h         | 90%      | Laboral | Sí           | Parcial (no 24x7 real) | Alto | Muy alto |
| CAU      | Alta     | 30 min    | 4h         | 90%      | Laboral | Sí           | Disponible        | Bajo | Bajo |
| CAU      | Media    | 1h        | 8h         | 90%      | Laboral | Sí           | Disponible        | Bajo | Bajo |
| CAU      | Baja     | 2h        | 24h        | 90%      | Laboral | Sí           | Disponible        | Bajo | Bajo |
| Peticiones | Normal/Alta | Según catálogo | Según catálogo | 90% | Laboral | Sí | Disponible | Bajo | Bajo |
| Cambios  | N/A      | Comité    | Según tipo | 99% disp | Laboral | Sí           | Parcial           | Medio | Medio |

6. Modelo de priorización:
- P1 (Crítica): Paralización total o pérdida de información.
- P2 (Alta): Interrupción relevante a muchos usuarios.
- P3 (Media): No interrumpe pero requiere atención en jornada.
- P4 (Baja): No interrumpe, puede esperar.
- No se detalla matriz impacto x urgencia, pero la definición es clara. Riesgo: subjetividad en escalado y categorización, especialmente en sedes periféricas.

7. Organización y modelo operativo:
- Roles exigidos: Coordinador técnico, técnicos de sistemas (admin, DBA), técnicos de soporte (central y periferia).
- Dedicaciones: 17 recursos base (1 coordinador, 2 admin sistemas, 1 DBA, 4 soporte Madrid, 9 soporte periferia).
- Guardias: No explícitas, pero bolsa de horas para fuera de horario.
- Presencialidad: Sedes clave, resto remoto/mixto.
- Sustituciones: Plan de cobertura y actualización obligatorio, suplencias equivalentes.
- Idiomas: No exigidos explícitamente, pero relevante para Cataluña, Galicia, País Vasco.
- Certificaciones: MCSA, ITIL Intermediate, Citrix, VMware, Linux LPIC-2, CISSP/CISM, Power BI, Microsoft 365 Fundamentals (valorables, no obligatorias).
- Perfiles internos: Ana Torres (gobierno), Claudia Benitez (soporte), Ivan Lopez (sistemas), Paula Navarro (reporting), Javier Prieto (seguridad). Faltan DBA senior y técnicos con certificaciones avanzadas.

8. Gobierno del servicio:
- Comités: No detallados, pero se espera comité operativo (semanal), seguimiento (mensual), dirección (trimestral).
- Entregables: Informes mensuales, cuadros de mando, reporting ANS, incidencias, peticiones, cambios, problemas recurrentes.
- Escalados: A través del coordinador técnico y jefe de proyecto.

9. Herramientas ITSM, CMDB y monitorización:
- ITSM: GLPI (obligatoria, para incidencias, peticiones, inventario, CMDB básica).
- Integraciones: No detalladas, pero se espera integración con Zabbix, Checkmk, MDT, WSUS, Citrix, WorkSpace One.
- Portal: No explícito, pero GLPI permite portal usuario.
- Inventario: GLPI, actualizado en procesos de alta/baja/modificación.
- CMDB: GLPI, CIs básicos, sin descubrimiento automático avanzado.
- Auditorías: Revisión periódica, reporting a la AGE.
- Reporting: Informes mensuales/trimestrales, cuadros de mando.

10. Transición, toma de control y reversibilidad:
- Fases: Asunción (1 mes, shadowing), Ejecución, Devolución (1 mes, reverse shadowing).
- Shadowing: Sí, transferencia de conocimiento, documentación, credenciales.
- Migración de tickets: No detallada, pero se espera migración de histórico relevante.
- Configuración SLA: En fase de asunción.
- Formación: Plan inicial y continua (50h/año/recursos).
- Entrega de documentación: Obligatoria, inventario, procedimientos, configuraciones.
- Salida: Entrega de documentación, datos, soporte a nuevo adjudicatario.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos, pero se exige 99% disponibilidad plataformas.
- Backups: Legato Networker, SnapManager, procedimientos definidos.
- Alta disponibilidad: Clusters, SAN replicada, Citrix, eREGES.
- Accesos: MFA, control de usuarios privilegiados, Active Directory.
- Vulnerabilidades: Apoyo en análisis, uso de CCN microClaudia, ADA.
- ENS/RGPD: Cumplimiento obligatorio, medidas de seguridad, confidencialidad, protección de datos.
- Incidentes de seguridad: Apoyo en investigación, documentación, reporting.

12. Automatización, self-service y mejora continua:
- Exigencias: No explícitas, pero se espera uso de MDT, WSUS, WorkSpace One, scripts, automatización de despliegues, reporting automatizado.
- Oportunidades: Chatbot/FAQ en portal GLPI, scripts de auto-remediation, base de conocimiento, reducción de incidencias por formación y documentación.

13. Reporting y gestión del conocimiento:
- Informes: Mensuales, cuadros de mando, ANS, incidencias, peticiones, cambios, problemas.
- Base de conocimiento: Documentación de incidencias, peticiones, procedimientos, FAQs.
- Runbooks: No explícitos, pero recomendables.
- KEDB: No exigida, pero recomendable para problemas recurrentes.
- Manuales: Obligatorios, propiedad de la AGE.

14. Matriz de evaluación Service Design:
(Se muestra extracto, tabla completa en entrega extendida)
| Requisito | Exigencia | Impacto | Capacidad actual | Gap | Riesgo | Acción recomendada | Diferenciación |
|-----------|-----------|---------|------------------|-----|--------|--------------------|---------------|
| Cobertura 24x7 | Valorada | Muy alto | Parcial | Alto | Muy alto | Subcontratar/guardias | Ofrecer 24x5 sólido |
| GLPI ITSM | Obligatoria | Medio | Media | Bajo | Bajo | Formación/refuerzo | Integración avanzada |
| Certificaciones | Valoradas | Medio | Parcial | Medio | Medio | Plan de formación | Certificados extra |
| CMDB avanzada | No exigida | Bajo | Parcial | Bajo | Bajo | No ofertar discovery | - |
| Seguridad ENS | Obligatoria | Medio | Media | Bajo | Bajo | Refuerzo ENS | Certificación ISO/ENS |

15. Riesgos operativos principales:
- Incapacidad de cumplir SLA críticos (P1 10min/2h) en 24x7 real sin refuerzo externo.
- Rotación de personal en sedes periféricas, dificultad de suplencias y transferencia de conocimiento.
- Falta de DBA senior y técnicos con certificaciones avanzadas.
- Dependencia de GLPI para ITSM/CMDB, limitaciones en reporting y automatización.
- Ambigüedad en volumetrías de cambios, peticiones complejas y eventos fuera de horario.
- Riesgo de penalizaciones por incumplimiento de ANS en picos de demanda o bajas no cubiertas.

16. Modelo operativo recomendado para ofertar:
- Estructura: 1 coordinador técnico (Madrid), 2 admin sistemas, 1 DBA, 4 soporte Madrid, 9 soporte periferia, plan de suplencias y bolsa de horas para picos.
- Procesos: ITIL Incident, Request, Change, Knowledge, Service Level, Problem (básico), Configuration (GLPI).
- Herramientas: GLPI (ITSM, CMDB, inventario, portal), Zabbix/Checkmk (monitorización), scripts automatización, reporting Power BI.
- Gobierno: Comité operativo semanal, seguimiento mensual, dirección trimestral, informes ANS, incidencias, peticiones, cambios, problemas.
- Transición: 1 mes asunción (shadowing), 1 mes devolución (reverse shadowing), plan de formación inicial y continua, entrega de documentación y datos.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Se exige cobertura 24x7 real para incidencias críticas o solo para primer contacto (Nivel 0)?
- ¿Qué herramienta ITSM exacta se usará (GLPI, otra)? ¿Se permite integración con herramientas propias?
- ¿Se requiere descubrimiento automático de CIs en CMDB o solo inventario manual?
- ¿Qué volumetría de cambios y peticiones complejas se prevé?
- ¿Qué RTO/RPO se exige para sistemas críticos?
- ¿Qué penalizaciones exactas se aplican por incumplimiento de ANS en cada prioridad?
- ¿Se exige soporte en idiomas cooficiales en sedes periféricas?
- ¿Qué nivel de reporting y cuadros de mando se espera (Power BI, GLPI, Excel)?

18. Documentos revisados:
1. Anuncio.pdf
2. PCAP.pdf
3. PPT.pdf
4. poc (detalle licitación)
5. poc (perfil contratante)
6. poc (perfil contratante ampliado)

(Para detalle ampliado de cada punto, solicitar desglose por apartado o tabla extendida.)