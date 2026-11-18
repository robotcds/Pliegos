1. Veredicto ejecutivo Service Design / ITIL: APTO CON GAPS

La empresa cumple la mayoría de los requisitos técnicos y organizativos exigidos, pero existen gaps relevantes en experiencia específica en asistentes virtuales con IA generativa, cobertura de agentes N1 en horario ampliado, y madurez en integración avanzada con plataformas cloud/MAIA y reporting de trazabilidad IA. Riesgo medio-alto en dimensionamiento de perfiles expertos y cumplimiento de SLAs en picos de demanda.

2. Alcance y dimensionamiento del servicio:
- Servicios: Diseño, desarrollo, implantación, operación, mantenimiento y evolución tecnológica de un asistente virtual (chatbot) para Decide Madrid, en modo SaaS, incluyendo panel de control, soporte N1 humano, formación y reporting.
- Sistemas afectados: Portal Decide Madrid (Ruby on Rails, multicloud), integración con buscador, panel de control, almacenamiento de logs y conversaciones.
- Usuarios: Ciudadanía (más de 555.000 usuarios registrados), personal DGPC (mínimo 5 usuarios panel control), agentes N1.
- Sedes: Servicio remoto desde dependencias adjudicataria; presencialidad solo excepcional.
- Horarios: Asistente virtual 24x7x365; N1 humano laborables 11:00-14:00 (ampliable como mejora).
- Modalidad: SaaS, operación remota, integración cloud (Azure, AWS, GCP).
- Cobertura: Madrid, acceso web nacional/internacional.
- Volumetrías: Mínimo 15.000 mensajes/mes, 50 conversaciones simultáneas, bolsa inicial 600h evolución tecnológica.
- Impacto: Dimensionamiento crítico en agentes N1, expertos IA, DevOps cloud, y soporte a picos de demanda. Riesgo si la demanda supera lo previsto o si la IA requiere tuning frecuente.

3. Modelo de servicio exigido:
- Estructura: No hay Service Desk tradicional, pero sí N1 (agente humano), N2 (expertos IA, cloud, dev), N3 (consultoría evolución tecnológica).
- Operación: Monitorización diaria, soporte correctivo/evolutivo, mantenimiento preventivo, reporting mensual.
- Mantenimiento: Correctivo, evolutivo, preventivo, soporte a incidencias y cambios.
- Monitorización: Supervisión diaria de calidad IA, logs, panel control, integración con herramientas IAM.
- Servicios especializados: IA generativa, RAG, fine-tuning, integración cloud, accesibilidad, cumplimiento IA-ACT/ENS.

4. Procesos ITIL requeridos:
| Proceso                | Explicito/Implicito | Evidencia textual | Exigencia | Capacidad actual | Gap |
|------------------------|---------------------|-------------------|-----------|------------------|-----|
| Incident Management   | Implícito           | Soporte N1, panel control, reporting incidencias | Alto | Implantado | Ninguno |
| Request Fulfilment    | Implícito           | Solicitudes a N1, formación, FAQs | Medio | Implantado | Ninguno |
| Change Management     | Implícito           | Evolución tecnológica, cambios IA, upgrades | Alto | Implantado | Ninguno |
| Problem Management    | Implícito           | Análisis logs, mejora continua, tuning IA | Medio | Parcial | Gap en KEDB y análisis IA |
| Configuration Mgmt    | Implícito           | Inventario cloud, panel control, logs | Medio | Parcial | Gap en CMDB avanzada |
| Knowledge Management  | Implícito           | FAQs, manuales, panel control, formación | Alto | Implantado | Ninguno |
| Service Level Mgmt    | Explícito           | SLAs en implantación, operación, penalizaciones | Alto | Implantado | Ninguno |
| Availability Mgmt     | Implícito           | 24x7 bot, penalizaciones por indisponibilidad | Alto | Parcial | Gap en HA y contingencia |
| Capacity Mgmt         | Implícito           | 50 sesiones simultáneas, 15.000 msg/mes | Medio | Parcial | Gap en métricas predictivas |
| Continuity Mgmt       | Implícito           | Backup, reversibilidad, contingencia | Medio | Parcial | Gap en RTO/RPO formal |
| Release/Deployment    | Implícito           | Fase implantación, upgrades, DevOps | Alto | Implantado | Ninguno |
| Event Management      | Implícito           | Monitorización diaria, logs, alertas | Medio | Parcial | Gap en integración IAM |
| Continual Improvement | Implícito           | Mejora continua, tuning IA, encuestas | Alto | Implantado | Ninguno |

5. SLA, KPI y penalizaciones:
| Servicio         | Prioridad | Respuesta | Resolución | Objetivo | Horario | Penalización | Capacidad actual | Gap | Riesgo operativo |
|------------------|----------|-----------|------------|---------|--------|--------------|------------------|-----|-----------------|
| Bot 24x7         | P1       | N/A       | 48h/5d max indisponibilidad | 24x7 | 24x7 | 5-10% contrato | Disponible en cloud | Gap en HA | Alto si fallo IA/cloud |
| N1 humano        | P1       | Inmediata | Durante horario | 11-14h L-V | Laboral | 5% contrato | Disponible 8x5 | Gap en ampliación | Medio si baja cobertura |
| Implantación     | P1       | N/A       | 2 meses | 2 meses | Laboral | 5-10% contrato | Disponible | Ninguno | Bajo |
| Mantenimiento    | P2       | 1 día     | 2-5 días | Laboral | Laboral | 5% contrato | Disponible | Ninguno | Bajo |
| Evolución tech   | P3       | 1-2 días  | Según plan | Laboral | Laboral | N/A | Disponible | Ninguno | Bajo |

6. Modelo de priorización:
- No se definen P1/P2/P3/P4 explícitos. Prioridad implícita: indisponibilidad bot (>48h grave, >5d muy grave), retrasos en implantación (>1 semana grave, >2 semanas muy grave), incidencias N1 fuera de horario no cubiertas.
- No hay matriz impacto x urgencia. Riesgo de ambigüedad en escalado de incidencias complejas o picos de demanda.

7. Organización y modelo operativo:
- Roles exigidos: Jefe/a de Proyecto (2), Técnico/a cloud, Analista programador, Experto IA, Lingüista computacional, Agente N1 (2), Consultor evolución tecnológica.
- Dedicaciones: Equipo mínimo, cobertura vacaciones/ausencias obligatoria, suplente para Jefe Proyecto.
- Guardias: No exigidas fuera de horario N1.
- Presencialidad: Remoto, salvo excepciones.
- Sustituciones: 7 días para cubrir bajas.
- Idiomas: Castellano.
- Certificaciones: Titulación universitaria para técnicos, experiencia específica en IA y asistentes virtuales.
- Perfiles internos: Ana Torres (Jefe Proyecto), Ivan Lopez (Cloud), El Joldan (IA), Claudia Benitez (N1), Luis Romero (Consultor). Gap en Lingüista computacional y experiencia específica en asistentes virtuales IA generativa.

8. Gobierno del servicio:
- Comités: Mensual (seguimiento técnico), operativo (ad hoc), dirección (trimestral, opcional).
- Entregables: Informe mensual seguimiento, memoria actuaciones, informes adicionales bajo demanda, informe final proyecto.
- Escalados: Responsable contrato DGPC, interlocutor único adjudicatario, reuniones mensuales, validación entregables.

9. Herramientas ITSM, CMDB y monitorización:
- Herramienta ITSM: No se exige una concreta, pero panel de control propio obligatorio, integración con IAM y reporting.
- CMDB: Inventario cloud, logs, panel control; integración con IAM, no se exige reconciliación automática.
- Monitorización: Logs, panel control, integración con herramientas IAM, reporting de actividad y calidad IA.
- Portal usuario: No aplica, interfaz bot y panel control.
- APIs: Integración con buscador, IAM, exportación informes.

10. Transición, toma de control y reversibilidad:
- Fases: Implantación (2 meses), operación, transferencia conocimiento (2 meses finales), reversibilidad.
- Shadowing: No explícito, pero transferencia y formación obligatoria.
- Migración tickets: No aplica, pero entrega de logs, modelos, código, documentación, encuestas, etc.
- Configuración SLA: Validación por DGPC/IAM antes de producción.
- Formación: 20h iniciales, actualizaciones durante contrato.
- Entrega documentación: Manuales, informes, logs, modelos, datos, scripts, etc.
- Salida: Borrado seguro, entrega de todo lo generado, certificado destrucción.

11. Continuidad, disponibilidad y seguridad operativa:
- RTO/RPO: No definidos, nivel ENS básico, backups cloud, contingencia cloud, acceso IAM, MFA, logs, auditoría, análisis de riesgos inicial, desarrollo seguro, cifrado en tránsito, control de accesos IAM, reporting incidentes seguridad, auditorías posibles.

12. Automatización, self-service y mejora continua:
- Exigencias: Chatbot IA generativa, RAG, fine-tuning, panel control, encuestas satisfacción, análisis logs, tuning IA, reporting, integración cloud, APIs, exportación datos.
- Oportunidades: Auto-remediation IA, scripts tuning, reporting avanzado, integración con herramientas IAM, mejora continua basada en logs y encuestas.

13. Reporting y gestión del conocimiento:
- Informes: Mensual seguimiento, memoria actuaciones, informes adicionales bajo demanda, informe final.
- Cuadros de mando: Panel control, exportación csv/xlsx/pdf.
- Base de conocimiento: FAQs, manuales, logs, documentación técnica, propiedad Ayuntamiento.
- Runbooks: No explícitos, pero manuales y procedimientos obligatorios.
- KEDB: No exigido, gap en problem management avanzado.

14. Matriz de evaluación Service Design:
(Ver siguiente respuesta por límite de espacio)

15. Riesgos operativos principales:
- Falta de experiencia específica en asistentes virtuales IA generativa y tuning continuo.
- Dimensionamiento insuficiente de agentes N1 para picos de demanda.
- Riesgo de incumplimiento de SLAs en disponibilidad bot y soporte N1.
- Gap en perfiles de lingüista computacional y expertos en integración cloud/MAIA.
- Ambigüedad en escalado de incidencias complejas.
- Riesgo de penalizaciones por indisponibilidad o retrasos en implantación.
- Integración avanzada con IAM y reporting de trazabilidad IA no probada.

16. Modelo operativo recomendado para ofertar:
- Estructura: Equipo mínimo exigido, refuerzo en IA y cloud con partners si es necesario, subcontratación de lingüista computacional.
- Roles: Jefe Proyecto (Ana Torres), Cloud (Ivan Lopez), IA (El Joldan), N1 (Claudia Benitez), Consultor (Luis Romero), Lingüista (partner).
- Procesos: ITIL implantados, reporting mensual, mejora continua, tuning IA semanal.
- Herramientas: Panel control propio, integración IAM, reporting csv/xlsx/pdf, logs, APIs.
- Gobierno: Comité mensual, informes, escalado directo a DGPC.
- Transición: 2 meses, formación inicial, entrega documentación, validación DGPC/IAM.

17. Preguntas o aclaraciones al órgano de contratación:
- ¿Se puede detallar la volumetría máxima esperada de conversaciones simultáneas y mensajes mensuales en picos?
- ¿Se exige integración con alguna herramienta ITSM/CMDB concreta del Ayuntamiento?
- ¿Qué herramientas de monitorización y reporting espera la DGPC (Power BI, panel propio, integración IAM)?
- ¿Se requiere RTO/RPO formal o plan de continuidad específico?
- ¿Qué nivel de detalle se espera en la documentación de logs, modelos y scripts entregados?
- ¿Se permite subcontratación de perfiles críticos (lingüista, IA, cloud) y en qué porcentaje?
- ¿Qué mecanismos de escalado y soporte fuera de horario N1 se esperan en caso de incidencias críticas?

18. Documentos revisados:
1. ID_188_1.PDF
2. ID_188_2.PDF
3. ID_188_3.PDF
4. poc (detalle licitación)
5. poc (perfil contratante)
6. poc (perfil contratante)
7. 147409-2026
8. perfilContratante