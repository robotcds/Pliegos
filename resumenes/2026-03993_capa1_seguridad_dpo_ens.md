## 1. Resumen factual Seguridad / DPO / ENS

La licitación para la solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para RENFE-Operadora exige el cumplimiento de requisitos de seguridad, privacidad y ENS de forma detallada y contractual. Se requiere certificación ENS nivel Medio, cumplimiento de ISO 27001, medidas técnicas y organizativas específicas, gestión de identidades y accesos, control de vulnerabilidades, logging, continuidad, auditoría, confidencialidad y obligaciones RGPD/LOPDGDD para el tratamiento de datos personales como encargado. Se regulan subencargados, localización de datos, transferencias, medidas de cifrado, backups, logging, SOC/SIEM, gestión de incidentes y planes de salida. El incumplimiento de estas obligaciones puede conllevar penalizaciones y resolución contractual.

---

## 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito ENS | Categoria/Nivel | Alcance | Acreditación | Momento | Fuente |
|---|---|---|---|---|---|
| Certificación ENS | Nivel Medio | Sistemas de información que soportan el servicio | Certificado ENS nivel Medio o compromiso de obtenerlo | Antes del inicio del servicio o en los primeros 10 meses si no se dispone; 12 meses si solo ISO 27001 | ANEXO I 2026 03393.pdf, p.24-28, CN.01 |
| Cumplimiento ENS | Nivel Medio | Solución SaaS y equipos conectados | Informe CLARA CCN ≥65% cumplimiento ENS Medio | Antes de inicio y durante ejecución | ANEXO I 2026 03393.pdf, p.24, SE.05 |
| Análisis de riesgos ENS | Nivel Medio | Servicio contratado | Análisis de riesgos MAGERIT (Pilar) | Tras adjudicación, antes de inicio | ANEXO I 2026 03393.pdf, p.25, PS.04 |
| Medidas técnicas ENS | Nivel Medio | Toda la plataforma y equipos | Declaración responsable y evidencias | Presentación y ejecución | ANEXO I 2026 03393.pdf, p.24-28 |
| Guías CCN | Aplicable según tecnología | Bases de datos, seguridad | CCN-CERT BP/22, BP/23, BP/24 | Ejecución | ANEXO I 2026 03393.pdf, p.30 |

---

## 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|---|---|---|---|
| Encargado del tratamiento | El adjudicatario es encargado, RENFE responsable | Durante la ejecución del contrato | PCP 2026 03993.pdf, p.25-28 |
| Instrucciones documentadas | Solo según instrucciones de RENFE | Durante ejecución | PCP 2026 03993.pdf, p.25-28 |
| Subencargados | Solo con autorización previa escrita de RENFE | Durante ejecución | PCP 2026 03993.pdf, p.26 |
| Localización de datos | Solo EEE salvo autorización expresa RENFE | Durante ejecución | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Supresión/devolución de datos | A elección de RENFE al finalizar el servicio | Al cierre del contrato | PCP 2026 03993.pdf, p.27; ANEXO I 2026 03393.pdf, p.28, CN.04 |
| Registro de actividades | Si el tratamiento entraña riesgo/no es ocasional | Durante ejecución | PCP 2026 03993.pdf, p.27 |
| Asistencia a derechos ARCO | Comunicación inmediata a dpd@renfe.es | Inmediato tras solicitud | PCP 2026 03993.pdf, p.27 |
| Medidas técnicas y organizativas | Adecuadas al riesgo, conforme ENS y RGPD | Durante ejecución | PCP 2026 03993.pdf, p.26; ANEXO I 2026 03393.pdf, p.24-28 |

---

## 4. Subencargados, cloud, localización y transferencias

| Requisito | Condición | Fuente |
|---|---|---|
| Subencargados | Autorización previa escrita de RENFE, mismas obligaciones que el adjudicatario | PCP 2026 03993.pdf, p.26; ANEXO I 2026 03393.pdf, p.25, PS.07 |
| Cloud/CPD | Localización en EEE salvo autorización expresa; informar ubicación y cambios | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Transferencias internacionales | Prohibidas salvo autorización expresa de RENFE | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Evaluación de seguridad de la cadena de suministro | Cuestionario obligatorio, entrega en 30 días y anual | ANEXO I 2026 03393.pdf, p.24, PS.12 |

---

## 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente

| Medida | Obligatoria/Valorable/Condicionada | Parámetro/Plazo | Fuente |
|---|---|---|---|
| Cifrado en tránsito, uso y almacenamiento | Obligatoria | Protocolos seguros (https, TLS v1.2+), claves en HSM | ANEXO I 2026 03393.pdf, p.30, SD.03 |
| Control de accesos, RBAC, mínimo privilegio | Obligatoria | Roles definidos, control de privilegios | ANEXO I 2026 03393.pdf, p.31-32, GI.01-GI.09 |
| MFA/2FA | Obligatoria para servicios expuestos a Internet | Implementación 2FA | ANEXO I 2026 03393.pdf, p.35, CD.03.11 |
| DLP | Obligatoria | Solución comercial, revisión trimestral | ANEXO I 2026 03393.pdf, p.29, SD.01.03 |
| Backups y restauración | Obligatoria | Procesos de backup, restauración y pruebas | ANEXO I 2026 03393.pdf, p.29, SD.01.04; p.38, DS.01.03 |
| Logs y trazabilidad | Obligatoria | Registro de actividad, acceso, IP, usuario, entrega a SIEM RENFE | ANEXO I 2026 03393.pdf, p.36, CD.06 |
| WAF, IDS/IPS, FW, antimalware | Obligatoria según naturaleza del servicio | Implementación y alineación con marcas RENFE | ANEXO I 2026 03393.pdf, p.35, CD.03 |
| Segmentación de red | Obligatoria | Segmentación adecuada | ANEXO I 2026 03393.pdf, p.29, CN.03 |
| Administración remota segura, VPN | Obligatoria | Acceso seguro, controlado y auditado | ANEXO I 2026 03393.pdf, p.33, GI.10 |
| Gestión de identidades y federación | Obligatoria | SAML2, ADFS, integración con directorio RENFE | ANEXO I 2026 03393.pdf, p.24, GI.05.01 |
| Prohibición de usuarios genéricos | Obligatoria | Medios para detectar y evitar | ANEXO I 2026 03393.pdf, p.32, GI.06 |
| Protección de bases de datos | Obligatoria | Cifrado, ofuscación, guías CCN | ANEXO I 2026 03393.pdf, p.30, SD.04 |
| Monitorización 24x7, SOC/SIEM | Obligatoria | Monitorización continua, entrega de logs | ANEXO I 2026 03393.pdf, p.36-37, CD.07 |

---

## 6. Identidad, accesos y privilegios

- Autenticación segura, integración con sistema de identidad de RENFE, federación SAML2/ADFS (ANEXO I 2026 03393.pdf, p.24, GI.05.01).
- Control de accesos por roles, mínimo privilegio, prohibición de usuarios genéricos (ANEXO I 2026 03393.pdf, p.31-32, GI.01-GI.09).
- Gestión de altas/bajas, trazabilidad de accesos, registro de intentos de autenticación (ANEXO I 2026 03393.pdf, p.32, GI.07.06).
- Acceso remoto seguro, VPN, controlado y auditado (ANEXO I 2026 03393.pdf, p.33, GI.10).

---

## 7. Vulnerabilidades, parcheado y desarrollo seguro

- Estrategia y plan de no obsolescencia, gestión de vulnerabilidades (identificación, remediación, SLA) obligatoria (ANEXO I 2026 03393.pdf, p.25, PS.06; p.35, CD.04.01-CD.04.03).
- Escaneos de vulnerabilidades periódicos, entrega de informes a RENFE, remediación según criticidad y políticas RENFE (ANEXO I 2026 03393.pdf, p.35, CD.04.02).
- Pruebas de seguridad/pentesting: autorización previa de RENFE, entrega de resultados (ANEXO I 2026 03393.pdf, p.37, CD.09).
- Desarrollo seguro: NO CONSTA EN LA DOCUMENTACION REVISADA ninguna referencia expresa a SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD o SBOM.

---

## 8. Incidentes, brechas y plazos de notificación expresamente indicados

- Comunicación de incidentes de seguridad con impacto Medio, Alto, Muy Alto y Crítico a la Gerencia de Ciberseguridad de RENFE y al CERT de RENFE, a través de notificaciones.pocterceros.ciberseguridad@renfe.es (ANEXO I 2026 03393.pdf, p.37, CD.08).
- Plazo de notificación: NO CONSTA EN LA DOCUMENTACION REVISADA un plazo expreso en horas o días para la notificación de incidentes.
- Colaboración en valoración, remediación, documentación y notificación del incidente (ANEXO I 2026 03393.pdf, p.37, CD.08).
- Prohibición de destrucción de pruebas durante la gestión del incidente (ANEXO I 2026 03393.pdf, p.37, CD.08).

---

## 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención

- Logging: registro de actividad, acceso, IP, usuario, logs normalizados, entrega a SIEM RENFE o API autorizada, retención según especifique RENFE (ANEXO I 2026 03393.pdf, p.36, CD.06).
- SOC/SIEM: monitorización 24x7, detección de incidentes, integración con SIEM RENFE (ANEXO I 2026 03393.pdf, p.36-37, CD.07).
- Continuidad: arquitecturas redundadas, balanceadas, planes de contingencia, crisis, continuidad y salida, pruebas de restauración de backups (ANEXO I 2026 03393.pdf, p.38-39, DS.01-DS.03).
- Backups: procesos de backup, restauración y pruebas, mecanismos adecuados y contrastados (ANEXO I 2026 03393.pdf, p.29, SD.01.04; p.38, DS.01.03).
- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA valores numéricos de RTO/RPO.
- Retención de logs: según especifique RENFE para cada fuente (ANEXO I 2026 03393.pdf, p.36, CD.06).

---

## 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad

- Auditorías: derecho de RENFE a auditar, acceso a locales, sistemas, procesos, colaboración obligatoria, auditoría bi-anual, auditorías de terceros, entrega de evidencias (ANEXO I 2026 03393.pdf, p.37-38, AU.01-AU.04).
- Evidencias: entrega de informes técnicos, SSAE16, IASE 3402 Soc 2 Tipo II, etc., si se solicitan (ANEXO I 2026 03393.pdf, p.37, AU.01).
- Certificaciones: ENS nivel Medio obligatoria, ISO 27001 o equivalente obligatoria (PCP 2026 03993.pdf, p.20; ANEXO I 2026 03393.pdf, p.24-28).
- Seguridad del personal: formación, concienciación, acuerdos de confidencialidad, cumplimiento de procedimientos de seguridad (ANEXO I 2026 03393.pdf, p.27, PS.10-PS.11).
- Borrado y destrucción: procedimiento seguro conforme ENS, entrega de certificado con fecha, personal, procedimiento (ANEXO I 2026 03393.pdf, p.28, CN.04).
- Confidencialidad: obligación contractual, acuerdo de confidencialidad, exclusiones detalladas (PCP 2026 03993.pdf, p.24-25; ANEXO I 2026 03393.pdf, p.27, PS.11).

---

## 11. Consecuencias contractuales expresamente asociadas al incumplimiento

- Penalizaciones de hasta el 10% del contrato por no entrega de documentación de ciberseguridad (análisis de riesgos, acuerdos de confidencialidad, informes de seguridad, etc.) (PCP 2026 03993.pdf, p.30-31).
- Penalización de 1000-3000€ por demora en el cuestionario de evaluación de seguridad de la cadena de suministro (PCP 2026 03993.pdf, p.31).
- Penalización de hasta el 10% del contrato por falta de certificación ENS nivel exigido (PCP 2026 03993.pdf, p.31).
- Penalización de 1000€/mes por no notificar el Punto de Contacto de Seguridad, 1000€/24h por falta de respuesta (PCP 2026 03993.pdf, p.31).
- Penalización de hasta el 20% del contrato por incumplimiento de obligaciones de confidencialidad, protección de datos o propiedad intelectual (PCP 2026 03993.pdf, p.30).
- Resolución contractual por incumplimiento de SP.01, PS.07, CN.01 o entrega de documentación de ciberseguridad (PCP 2026 03993.pdf, p.33).

---

## 12. Datos no localizados o ambiguos, sin recomendaciones

- NO CONSTA EN LA DOCUMENTACION REVISADA: valores numéricos de RTO/RPO, detalle de SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD, SBOM.
- NO CONSTA EN LA DOCUMENTACION REVISADA: categorías concretas de datos personales tratados, interesados, finalidades específicas más allá de la ejecución del contrato.
- NO CONSTA EN LA DOCUMENTACION REVISADA: plazos expresos en horas/días para notificación de incidentes de seguridad.

---

## 13. Documentos revisados

1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393 .pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Plataforma de Contratación del Sector Público, sin contenido relevante de seguridad)
7. poc (Perfil de contratante RENFE, sin contenido relevante de seguridad)
8. poc (Perfil de contratante RENFE, sin contenido relevante de seguridad)

---

## 14. Tabla de trazabilidad

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Certificación ENS | Obligación contractual | Nivel Medio, sistemas de información, certificado o compromiso | ANEXO I 2026 03393.pdf | p.24-28, CN.01 | TEXTO EXTRAIDO |
| ISO 27001 | Obligación contractual | Certificación obligatoria | PCP 2026 03993.pdf | p.20 | TEXTO EXTRAIDO |
| Análisis de riesgos ENS | Obligación contractual | MAGERIT (Pilar), compartir con RENFE | ANEXO I 2026 03393.pdf | p.25, PS.04 | TEXTO EXTRAIDO |
| Subencargados | Obligación contractual | Autorización previa escrita, mismas obligaciones | PCP 2026 03993.pdf | p.26 | TEXTO EXTRAIDO |
| Localización de datos | Obligación contractual | EEE salvo autorización expresa | ANEXO I 2026 03393.pdf | p.25, PS.01 | TEXTO EXTRAIDO |
| Cifrado | Obligación contractual | En tránsito, uso y almacenamiento, claves en HSM | ANEXO I 2026 03393.pdf | p.30, SD.03 | TEXTO EXTRAIDO |
| Control de accesos | Obligación contractual | RBAC, mínimo privilegio, prohibición usuarios genéricos | ANEXO I 2026 03393.pdf | p.31-32, GI.01-GI.09 | TEXTO EXTRAIDO |
| DLP | Obligación contractual | Solución comercial, revisión trimestral | ANEXO I 2026 03393.pdf | p.29, SD.01.03 | TEXTO EXTRAIDO |
| Backups | Obligación contractual | Procesos de backup, restauración y pruebas | ANEXO I 2026 03393.pdf | p.29, SD.01.04 | TEXTO EXTRAIDO |
| Logging/SIEM | Obligación contractual | Registro, entrega a SIEM RENFE, retención según RENFE | ANEXO I 2026 03393.pdf | p.36, CD.06 | TEXTO EXTRAIDO |
| SOC/monitorización | Obligación contractual | 24x7, integración con SIEM RENFE | ANEXO I 2026 03393.pdf | p.36-37, CD.07 | TEXTO EXTRAIDO |
| Incidentes | Obligación contractual | Comunicación a CERT RENFE, sin plazo expreso | ANEXO I 2026 03393.pdf | p.37, CD.08 | TEXTO EXTRAIDO |
| Auditoría | Obligación contractual | Derecho de RENFE, colaboración obligatoria | ANEXO I 2026 03393.pdf | p.37-38, AU.01-AU.04 | TEXTO EXTRAIDO |
| Borrado/destrucción | Obligación contractual | Procedimiento seguro, certificado | ANEXO I 2026 03393.pdf | p.28, CN.04 | TEXTO EXTRAIDO |
| Consecuencias incumplimiento | Penalización/resolución | Hasta 20%/10%/resolución según obligación | PCP 2026 03993.pdf | p.30-33 | TEXTO EXTRAIDO |
| Desarrollo seguro | NO CONSTA | NO CONSTA | ANEXO I 2026 03393.pdf | - | TEXTO EXTRAIDO |
| RTO/RPO | NO CONSTA | NO CONSTA | ANEXO I 2026 03393.pdf | - | TEXTO EXTRAIDO |
| Categorías de datos personales | NO CONSTA | NO CONSTA | PCP 2026 03993.pdf | - | TEXTO EXTRAIDO |
| Plazos notificación incidentes | NO CONSTA | NO CONSTA | ANEXO I 2026 03393.pdf | - | TEXTO EXTRAIDO |

---

## 15. Discrepancias y pendientes de aclaración

No se han identificado discrepancias en la documentación revisada. No se localizan valores de RTO/RPO, detalle de SDLC/DevSecOps, ni plazos expresos de notificación de incidentes. No se detallan categorías de datos personales ni finalidades específicas más allá de la ejecución contractual.