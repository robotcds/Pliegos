## 1. Resumen factual Seguridad / DPO / ENS

La licitación para la solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para la operación ferroviaria de RENFE-Operadora exige el cumplimiento de requisitos avanzados en materia de seguridad, protección de datos y ENS. Se requiere certificación ENS nivel Medio, ISO 27001, medidas técnicas y organizativas alineadas con el ENS, gestión de identidades y accesos, cifrado, control de vulnerabilidades, logging, continuidad, planes de salida y destrucción segura, así como obligaciones específicas para subencargados, localización de datos y notificación de incidentes. El adjudicatario será encargado del tratamiento de datos personales y debe cumplir instrucciones documentadas del responsable (RENFE). Se establecen penalizaciones y causas de resolución contractual por incumplimiento de las obligaciones de seguridad, privacidad y ENS.

---

## 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito ENS | Categoria/nivel | Alcance | Acreditación | Momento | Fuente |
|---|---|---|---|---|---|
| Certificación ENS | Nivel Medio | Sistemas de información que soportan el servicio SaaS | Certificado ENS nivel Medio o compromiso de obtenerlo | Antes del inicio del servicio o en los primeros 10 meses si no se dispone; 12 meses si solo ISO 27001 | ANEXO I 2026 03393.pdf, p.28-29, CN.01; PCP 2026 03993.pdf, p.20 |
| Declaración responsable de cumplimiento de requisitos de seguridad | No aplica | Todos los requisitos de seguridad del Anexo I | Declaración responsable | Sobre A, presentación de oferta | ANEXO II 2026 03993.pdf, p.2; PCP 2026 03993.pdf, p.5, 7 |
| Análisis de riesgos conforme ENS (MAGERIT) | No aplica | Servicio contratado | Informe de análisis de riesgos | Tras adjudicación, antes de inicio | ANEXO I 2026 03393.pdf, p.25-26, PS.04 |
| Informe CLARA CCN (cumplimiento ENS ≥65%) | Nivel Medio | Equipos de usuario del adjudicatario | Informe individual por equipo | Antes de inicio de uso de equipos | ANEXO I 2026 03393.pdf, p.24, 34, SE.05 |
| Medidas técnicas y organizativas ENS | Nivel Medio | Servicio SaaS y equipos asociados | Documentación técnica, procedimientos, evidencias | Durante ejecución | ANEXO I 2026 03393.pdf, p.25-39 |

---

## 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|---|---|---|---|
| Encargado del tratamiento (adjudicatario) | Tratar datos solo según instrucciones documentadas del responsable (RENFE) | Durante la ejecución del contrato | PCP 2026 03993.pdf, p.25-28, cláusula 17 |
| Prohibición de uso para fines propios o distintos | Solo ejecución del contrato | Durante la ejecución | PCP 2026 03993.pdf, p.25-28 |
| Prohibición de comunicación a terceros sin autorización | Salvo autorización escrita del responsable | Durante la ejecución | PCP 2026 03993.pdf, p.25-28 |
| Confidencialidad del personal | Compromiso de confidencialidad, subsiste tras la relación | Durante y tras la ejecución | PCP 2026 03993.pdf, p.25-28 |
| Medidas técnicas y organizativas adecuadas | Según análisis de riesgos y ENS | Durante la ejecución | PCP 2026 03993.pdf, p.25-28; ANEXO I 2026 03393.pdf, p.25-39 |
| Subencargados: autorización previa escrita | Obligatorio | Antes de subcontratar | PCP 2026 03993.pdf, p.25-28 |
| Registro de actividades de tratamiento | Si el tratamiento entraña riesgo, no es ocasional o incluye categorías especiales | Durante la ejecución | PCP 2026 03993.pdf, p.27 |
| Supresión o devolución de datos al finalizar | A elección del responsable | Al finalizar el contrato | PCP 2026 03993.pdf, p.27-28; ANEXO I 2026 03393.pdf, p.29, CN.04 |
| Certificado de destrucción | Obligatorio para cada borrado/destrucción | Al finalizar el contrato o cuando se requiera | ANEXO I 2026 03393.pdf, p.29, CN.04.02 |
| Asistencia al responsable en ejercicio de derechos | Obligatorio | Inmediato tras solicitud | PCP 2026 03993.pdf, p.26 |
| Notificación de solicitudes de derechos | A dpd@renfe.es | Inmediato tras recepción | PCP 2026 03993.pdf, p.26 |
| Asistencia en notificación de brechas | Obligatorio | Según legislación vigente | PCP 2026 03993.pdf, p.26 |
| Principios de protección de datos por diseño y por defecto | Obligatorio | Durante la ejecución | PCP 2026 03993.pdf, p.28 |

---

## 4. Subencargados, cloud, localización y transferencias

| Requisito | Condición | Fuente |
|---|---|---|
| Subencargados: autorización previa escrita del responsable | Obligatorio | PCP 2026 03993.pdf, p.25-28; ANEXO I 2026 03393.pdf, p.26, PS.07 |
| Subencargados deben asumir mismas obligaciones contractuales | Obligatorio | PCP 2026 03993.pdf, p.25-28; ANEXO I 2026 03393.pdf, p.26, PS.07 |
| Localización de datos: prestación desde EEE salvo autorización expresa | Obligatorio | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Autorización para cambios de ubicación geográfica | Obligatorio | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Información a RENFE de ubicación y países de tratamiento/almacenamiento | Obligatorio | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Transferencias internacionales: solo con autorización y conforme a Derecho UE | Obligatorio | PCP 2026 03993.pdf, p.25-28 |
| Cloud público: integración con CNAPP de Renfe si se solicita | Condicionado | ANEXO I 2026 03393.pdf, p.35, CD.05 |

---

## 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente

| Medida | Obligatoria/valorable/condicionada | Parámetro/plazo | Fuente |
|---|---|---|---|
| Cifrado en tránsito, uso y almacenamiento | Obligatoria | Protocolos seguros (https, TLS v1.2+), datos confidenciales cifrados | ANEXO I 2026 03393.pdf, p.30, SD.03 |
| Custodia de claves en HSM | Obligatoria salvo impedimento técnico autorizado | Durante la ejecución | ANEXO I 2026 03393.pdf, p.30, SD.03.04 |
| Control de accesos y gestión de identidades | Obligatoria | Integración con sistema de identidad de Renfe, SSO, SAML2/ADFS | ANEXO I 2026 03393.pdf, p.32, GI.05.01 |
| MFA/2FA para servicios expuestos a Internet | Obligatoria para servicios expuestos | Durante la ejecución | ANEXO I 2026 03393.pdf, p.35, CD.03.11 |
| RBAC, mínimo privilegio, perfiles diferenciados | Obligatoria | Definición y gestión de roles, control de privilegios | ANEXO I 2026 03393.pdf, p.32, GI.07 |
| PAM (gestión de accesos privilegiados) | Obligatoria | Gestión y control de accesos privilegiados | ANEXO I 2026 03393.pdf, p.32, GI.08-09 |
| VPN para accesos remotos | Obligatoria si hay acceso remoto | Durante la ejecución | ANEXO I 2026 03393.pdf, p.33, GI.10.03 |
| Bastionado, segmentación de red | Obligatoria | Segmentación adecuada, controles de acceso | ANEXO I 2026 03393.pdf, p.29, CN.03; p.35, CD.03.01, CD.03.02 |
| EDR/antimalware | Obligatoria | Instalación y mantenimiento en equipos adjudicatario | ANEXO I 2026 03393.pdf, p.33-34, SE.04 |
| WAF para servicios web | Obligatoria si aplica | Durante la ejecución | ANEXO I 2026 03393.pdf, p.35, CD.03.04 |
| SIEM, logs y monitorización 24x7 | Obligatoria | Integración con SIEM de Renfe, logs normalizados, retención según Renfe | ANEXO I 2026 03393.pdf, p.36, CD.06-07 |
| DLP | Obligatoria si hay datos personales/confidenciales | Descubrimiento cada 3 meses | ANEXO I 2026 03393.pdf, p.29, SD.01.03; p.35, CD.03.06 |
| Backups, restauración y pruebas | Obligatoria | Procesos de backup, restauración y pruebas | ANEXO I 2026 03393.pdf, p.29, SD.01.04; p.38, DS.01.03 |
| Defensa perimetral, IDS/IPS, proxys, CASB, CWPP | Obligatoria según arquitectura | Durante la ejecución | ANEXO I 2026 03393.pdf, p.35, CD.03 |
| Protección correo electrónico | Obligatoria si aplica | Antimalware, antispam, reputación | ANEXO I 2026 03393.pdf, p.35, CD.03.10 |

---

## 6. Identidad, accesos y privilegios

- Integración con sistema de identidad de Renfe y federación (SAML2, ADFS, etc.).
- Prohibición de usuarios genéricos; detección y control de creación/uso.
- Validación de identidad, control de privilegios, registro de intentos de autenticación (fallidos y correctos) con información relevante (IP, usuario, etc.).
- Gestión de accesos privilegiados (PAM), controles de acceso, trazabilidad, auditoría y escalado de privilegios.
- Acceso remoto seguro (VPN).
- Gestión de altas/bajas de usuarios, integración con directorio corporativo.
- Listados nominales de autorizaciones y accesos a disposición del responsable.

Fuente: ANEXO I 2026 03393.pdf, p.32-33, GI.01-GI.11; p.29, SD.01.01-02

---

## 7. Vulnerabilidades, parcheado y desarrollo seguro

- Estrategia y plan de no obsolescencia, gestión de vulnerabilidades (identificación, remediación, SLA).
- Parcheo regular y seguro de productos, configuración segura, mantenimiento de documentación técnica actualizada, inventario de activos.
- Escaneos de vulnerabilidades periódicos, entrega de informes a Renfe, remediación según criticidad y políticas de Renfe.
- Pruebas de seguridad (pentesting, hacking ético) requieren autorización previa y entrega de resultados a Renfe.
- Cumplimiento de guías CCN-CERT para bases de datos (según tecnología).
- Desarrollo seguro: NO CONSTA EN LA DOCUMENTACION REVISADA referencia expresa a SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD o SBOM.

Fuente: ANEXO I 2026 03393.pdf, p.26, PS.06; p.29, CN.03; p.35-36, CD.04, CD.09; p.30, SD.04.02

---

## 8. Incidentes, brechas y plazos de notificación expresamente indicados

- Notificación de incidentes de seguridad con impacto Medio, Alto, Muy Alto y Crítico a la Gerencia de Área de Ciberseguridad de Renfe y al CERT de Renfe (notificaciones.pocterceros.ciberseguridad@renfe.es).
- El adjudicatario debe colaborar en la valoración, remediación, documentación y notificación del incidente.
- Prohibición de destrucción de pruebas durante la gestión del incidente.
- Plazos: NO CONSTA EN LA DOCUMENTACION REVISADA un plazo expreso de horas/días para la notificación de incidentes o brechas.
- Notificación de solicitudes de derechos de interesados a dpd@renfe.es de forma inmediata tras recepción.

Fuente: ANEXO I 2026 03393.pdf, p.36-37, CD.08; PCP 2026 03993.pdf, p.26

---

## 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención

- Logging: registro, auditoría y trazabilidad de eventos, operaciones y accesos; logs normalizados, integración con SIEM de Renfe o API autorizada.
- Custodia de logs por el periodo de retención que especifique Renfe.
- Monitorización 24x7 de la infraestructura para detección de incidencias e incidentes.
- Continuidad: planes de contingencia, crisis, continuidad de negocio, salida programada y sobrevenida, identificación de competencias críticas para retomar control.
- Backups: mecanismos adecuados y contrastados, pruebas de restauración.
- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA valores numéricos específicos.
- Pruebas de continuidad: se exige elaboración de planes, pero no se detallan frecuencias ni formatos de pruebas.

Fuente: ANEXO I 2026 03393.pdf, p.27, PS.08; p.36, CD.06-07; p.38-39, DS.01-03

---

## 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad

- Auditorías: Renfe podrá solicitar informes técnicos, auditorías, revisiones de seguridad y continuidad, acceso a locales y sistemas, colaboración obligatoria del adjudicatario.
- Auditoría bi-anual autoimpuesta, auditorías de terceros (IGAE, Tribunal de Cuentas, etc.), auditorías extraordinarias.
- Evidencias: entrega de documentación, registros, informes de seguridad, certificados de destrucción.
- Certificaciones: ENS nivel Medio (obligatoria), ISO 27001 (obligatoria), otras certificaciones relevantes pueden ser solicitadas.
- Seguridad del personal: formación, concienciación y capacitación obligatoria en tecnologías, seguridad de la información y legislación aplicable.
- Borrado y destrucción: procedimiento seguro conforme ENS, entrega de certificado con fecha, personal, procedimiento.
- Confidencialidad: acuerdo de confidencialidad firmado por personal propio y subcontratado, obligación subsiste tras la relación.

Fuente: ANEXO I 2026 03393.pdf, p.27-28, PS.10-11; p.29, CN.04; p.37-38, AU.01-04

---

## 11. Consecuencias contractuales expresamente asociadas al incumplimiento

- Penalización hasta el 10% del contrato por no entrega de documentación de ciberseguridad (análisis de riesgos, acuerdos de confidencialidad, informes de seguridad, etc.).
- Penalización de 1000-3000€ por demora en completar el cuestionario de evaluación de seguridad de la cadena de suministro (PS.07).
- Penalización hasta el 10% del contrato por falta de certificación ENS nivel Medio (CN.01).
- Penalización de 1000€ por no notificar el Punto de Contacto de Seguridad en plazo, incrementándose por cada mes adicional; penalización por falta de respuesta del POC de Seguridad en 48h y sucesivos periodos de 24h.
- Penalización hasta el 20% del contrato por incumplimiento de obligaciones de confidencialidad, protección de datos y propiedad intelectual.
- Resolución contractual por incumplimiento de SP.01, PS.07, CN.01, entrega de documentación de ciberseguridad, confidencialidad, protección de datos, propiedad intelectual y ética y cumplimiento.

Fuente: PCP 2026 03993.pdf, p.30-34, cláusulas 19 y 29

---

## 12. Datos no localizados o ambiguos, sin recomendaciones

- NO CONSTA EN LA DOCUMENTACION REVISADA: valores numéricos de RTO/RPO.
- NO CONSTA EN LA DOCUMENTACION REVISADA: detalle de SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD, SBOM.
- NO CONSTA EN LA DOCUMENTACION REVISADA: categorías concretas de datos personales tratados, interesados o finalidades específicas más allá de la ejecución del contrato.
- NO CONSTA EN LA DOCUMENTACION REVISADA: plazos expresos (en horas/días) para notificación de incidentes de seguridad o brechas de datos personales.

---

## 13. Documentos revisados

1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393.pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Plataforma de Contratación del Sector Público, información general)
7. poc (Perfil de contratante RENFE-Operadora, información general)
8. poc (Perfil de contratante RENFE-Operadora, información general)

---

## 14. Tabla de trazabilidad

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Certificación ENS nivel Medio | Obligación contractual | Certificado ENS nivel Medio o compromiso de obtenerlo | ANEXO I 2026 03393.pdf | p.28-29, CN.01 | TEXTO EXTRAIDO |
| ISO 27001 | Obligación contractual | Certificación ISO 27001 o equivalente | PCP 2026 03993.pdf | p.20 | TEXTO EXTRAIDO |
| Declaración responsable requisitos seguridad | Requisito de admisión | Declaración responsable | ANEXO II 2026 03993.pdf | p.2 | TEXTO EXTRAIDO |
| Análisis de riesgos MAGERIT | Obligación contractual | Informe de análisis de riesgos conforme ENS | ANEXO I 2026 03393.pdf | p.25-26, PS.04 | TEXTO EXTRAIDO |
| Informe CLARA CCN | Obligación contractual | Informe individual por equipo, cumplimiento ENS ≥65% | ANEXO I 2026 03393.pdf | p.24, 34, SE.05 | TEXTO EXTRAIDO |
| Medidas técnicas ENS | Obligación contractual | Medidas técnicas y organizativas alineadas ENS | ANEXO I 2026 03393.pdf | p.25-39 | TEXTO EXTRAIDO |
| Encargado del tratamiento | Obligación contractual | Tratar datos solo según instrucciones de RENFE | PCP 2026 03993.pdf | p.25-28 | TEXTO EXTRAIDO |
| Subencargados: autorización previa | Obligación contractual | Autorización escrita de RENFE | PCP 2026 03993.pdf | p.25-28 | TEXTO EXTRAIDO |
| Localización de datos | Obligación contractual | Prestación desde EEE salvo autorización expresa | ANEXO I 2026 03393.pdf | p.25, PS.01 | TEXTO EXTRAIDO |
| Cifrado en tránsito y almacenamiento | Obligación contractual | Protocolos seguros, datos confidenciales cifrados | ANEXO I 2026 03393.pdf | p.30, SD.03 | TEXTO EXTRAIDO |
| Control de accesos, RBAC, SSO | Obligación contractual | Integración con sistema de identidad de Renfe | ANEXO I 2026 03393.pdf | p.32, GI.05.01 | TEXTO EXTRAIDO |
| MFA/2FA | Obligación contractual | Para servicios expuestos a Internet | ANEXO I 2026 03393.pdf | p.35, CD.03.11 | TEXTO EXTRAIDO |
| PAM | Obligación contractual | Gestión de accesos privilegiados | ANEXO I 2026 03393.pdf | p.32, GI.08-09 | TEXTO EXTRAIDO |
| VPN | Obligación contractual | Acceso remoto seguro | ANEXO I 2026 03393.pdf | p.33, GI.10.03 | TEXTO EXTRAIDO |
| Logging, SIEM | Obligación contractual | Integración con SIEM de Renfe, logs normalizados | ANEXO I 2026 03393.pdf | p.36, CD.06-07 | TEXTO EXTRAIDO |
| Backups | Obligación contractual | Procesos de backup, restauración y pruebas | ANEXO I 2026 03393.pdf | p.29, SD.01.04 | TEXTO EXTRAIDO |
| Planes de continuidad y salida | Obligación contractual | Planes de contingencia, crisis, continuidad, salida | ANEXO I 2026 03393.pdf | p.38-39, DS.01-03 | TEXTO EXTRAIDO |
| Auditorías | Obligación contractual | Colaboración obligatoria, acceso a sistemas y locales | ANEXO I 2026 03393.pdf | p.37-38, AU.01-04 | TEXTO EXTRAIDO |
| Borrado y destrucción segura | Obligación contractual | Procedimiento seguro, certificado de destrucción | ANEXO I 2026 03393.pdf | p.29, CN.04 | TEXTO EXTRAIDO |
| Penalizaciones por incumplimiento | Consecuencia contractual | Hasta 10%/20% del contrato, penalizaciones específicas | PCP 2026 03993.pdf | p.30-34 | TEXTO EXTRAIDO |
| RTO/RPO | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA |
| Desarrollo seguro (SDLC, DevSecOps, etc.) | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA |
| Plazos de notificación de incidentes | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA |
| Categorías de datos personales/interesados | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | NO CONSTA | NO CONSTA |

---

## Discrepancias y pendientes de aclaración

No se han identificado discrepancias en la documentación revisada. No se localizan valores numéricos de RTO/RPO, detalles de SDLC/DevSecOps/SAST/DAST/SCA/OWASP/CI-CD/SBOM, ni plazos expresos para notificación de incidentes o brechas. No se detallan categorías concretas de datos personales tratados ni interesados.