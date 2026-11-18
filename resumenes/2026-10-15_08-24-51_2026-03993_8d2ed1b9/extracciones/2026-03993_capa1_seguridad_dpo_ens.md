## 1. Resumen factual Seguridad / DPO / ENS

La licitación para la solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para la operación ferroviaria de RENFE-Operadora exige el cumplimiento de requisitos avanzados en materia de seguridad, protección de datos y ENS. Se requiere certificación ENS nivel Medio, ISO 27001, análisis de riesgos MAGERIT, medidas técnicas y organizativas específicas, control de subcontratación, localización de datos en el EEE, cifrado, gestión de identidades, logging, continuidad, auditorías, borrado seguro y colaboración con el DPD y CISO de RENFE. Se establecen penalizaciones y causas de resolución contractual por incumplimiento de estas obligaciones.

---

## 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito ENS | Categoria/Nivel | Alcance | Acreditación | Momento | Fuente |
|---|---|---|---|---|---|
| Certificación ENS | Nivel MEDIO | Sistemas de información que soportan el servicio | Certificado ENS nivel MEDIO o compromiso de obtenerlo | Antes del inicio del servicio o en los primeros 10 meses si no se dispone; 12 meses si solo ISO 27001 | ANEXO I 2026 03393.pdf, p.28, CN.01 |
| Análisis de riesgos MAGERIT | No aplica | Alcance del proyecto | Informe de análisis de riesgos | Tras adjudicación, antes de inicio | ANEXO I 2026 03393.pdf, p.25, PS.04 |
| Informe CLARA CCN | Nivel MEDIO, ≥65% cumplimiento | Equipos de usuario del adjudicatario | Informe individual por equipo | Antes de inicio de uso de equipos | ANEXO I 2026 03393.pdf, p.34, SE.05 |
| Cumplimiento guías CCN-CERT BP/22, BP/23, BP/24 | No aplica | Bases de datos Oracle, DB2, otras | Declaración de cumplimiento | Durante ejecución | ANEXO I 2026 03393.pdf, p.30, SD.04.02 |

---

## 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|---|---|---|---|
| Encargado del tratamiento | El adjudicatario es encargado, RENFE responsable | Durante la ejecución del contrato | PCP 2026 03993.pdf, p.25-27, cláusula 17 |
| Tratamiento solo bajo instrucciones | Prohibido uso para fines propios o distintos | Durante ejecución | PCP 2026 03993.pdf, p.25-27 |
| Subencargados solo con autorización escrita | Obligación de imponer mismas condiciones | Durante ejecución | PCP 2026 03993.pdf, p.26 |
| Registro de actividades si aplica | Si tratamiento no es ocasional o incluye datos especiales | Durante ejecución | PCP 2026 03993.pdf, p.27 |
| Supresión o devolución de datos al finalizar | A elección de RENFE | Al finalizar el servicio | PCP 2026 03993.pdf, p.27 |
| Comunicación de solicitudes de derechos | Inmediata a dpd@renfe.es | Inmediata tras recepción | PCP 2026 03993.pdf, p.27 |
| Asistencia en EIPD, notificación de brechas | Obligatoria | Sin plazo expreso | PCP 2026 03993.pdf, p.27 |
| Medidas técnicas y organizativas adecuadas | Obligatoria | Durante ejecución | PCP 2026 03993.pdf, p.26 |

---

## 4. Subencargados, cloud, localización y transferencias

| Requisito | Condición | Fuente |
|---|---|---|
| Subencargados | Solo con autorización previa escrita de RENFE; mismas obligaciones contractuales | PCP 2026 03993.pdf, p.26; ANEXO I 2026 03393.pdf, p.26, PS.07 |
| Cloud público | Permitido, sujeto a ENS y localización EEE | ANEXO I 2026 03393.pdf, p.25, PS.01; p.28, CN.01 |
| Localización de datos | Obligatorio informar ubicación geográfica y países; solo EEE salvo autorización expresa | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Transferencias internacionales | Prohibidas salvo autorización expresa de RENFE | ANEXO I 2026 03393.pdf, p.25, PS.01 |

---

## 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente

| Medida | Obligatoria/Valorable/Condicionada | Parámetro/Plazo | Fuente |
|---|---|---|---|
| Cifrado en tránsito, uso y almacenamiento | Obligatoria | Protocolos seguros (https, TLS v1.2+), HSM para claves | ANEXO I 2026 03393.pdf, p.30, SD.03 |
| Control de accesos y gestión de identidades | Obligatoria | Integración con identidad RENFE, SAML2/ADFS, no usuarios genéricos | ANEXO I 2026 03393.pdf, p.31-32, GI.01-GI.07 |
| Backup y restauración | Obligatoria | Pruebas periódicas, retención según RENFE | ANEXO I 2026 03393.pdf, p.29, SD.01.04; p.38, DS.01.03 |
| DLP | Obligatoria si hay datos personales o confidenciales | Descubrimiento cada 3 meses | ANEXO I 2026 03393.pdf, p.29, SD.01.03 |
| WAF, IDS/IPS, FW, antimalware | Obligatoria según naturaleza del servicio | Durante ejecución | ANEXO I 2026 03393.pdf, p.34, CD.03 |
| 2FA | Obligatoria para servicios expuestos a Internet que lo requieran | Durante ejecución | ANEXO I 2026 03393.pdf, p.34, CD.03.11 |
| Segmentación de red | Obligatoria | Durante ejecución | ANEXO I 2026 03393.pdf, p.29, CN.03 |
| Gestión de vulnerabilidades y parcheado | Obligatoria | Proceso formal, escaneos periódicos, plazos según política RENFE | ANEXO I 2026 03393.pdf, p.35, CD.04 |
| Logging y trazabilidad | Obligatoria | Logs normalizados, entrega a SIEM RENFE, retención según RENFE | ANEXO I 2026 03393.pdf, p.36, CD.06 |
| Monitorización 24x7 | Obligatoria | SOC/SIEM, detección de incidentes | ANEXO I 2026 03393.pdf, p.36, CD.07 |
| Pruebas de seguridad/pentesting | Obligatoria, previa autorización RENFE | Resultados a Seguridad RENFE | ANEXO I 2026 03393.pdf, p.37, CD.09 |
| Borrado seguro y certificado | Obligatoria al finalizar servicio | Certificado de destrucción | ANEXO I 2026 03393.pdf, p.29, CN.04 |

---

## 6. Identidad, accesos y privilegios

- Integración con sistema de identidad de RENFE, soporte de federación (SAML2, ADFS, etc.).
- Prohibición de usuarios genéricos.
- Gestión de altas/bajas de usuarios, control de privilegios, mínimo privilegio.
- Gestión de accesos privilegiados (PAM), controles, trazabilidad y auditoría.
- Acceso remoto seguro (VPN, autenticación fuerte).
- Registro de intentos de autenticación, logs de acceso y privilegios.

Fuente: ANEXO I 2026 03393.pdf, p.31-33, GI.01-GI.11

---

## 7. Vulnerabilidades, parcheado y desarrollo seguro

- Proceso formal de gestión de vulnerabilidades y parcheado, escaneos periódicos, entrega de informes a RENFE, remediación según criticidad y política RENFE.
- Prohibición de software en EOL/EOS.
- Pruebas de seguridad (pentesting) autorizadas por RENFE, resultados compartidos.
- Plan de no obsolescencia.
- Cumplimiento de guías CCN-CERT para bases de datos.

Fuente: ANEXO I 2026 03393.pdf, p.28, PS.06; p.35, CD.04; p.30, SD.04.02

---

## 8. Incidentes, brechas y plazos de notificación expresamente indicados

- Comunicación de incidentes de seguridad a CERT RENFE (notificaciones.pocterceros.ciberseguridad@renfe.es) para niveles Medio, Alto, Muy Alto y Crítico, según Guía CCN-STIC 817.
- Incorporación de la dirección de notificación en la plataforma del adjudicatario.
- Colaboración en valoración, remediación, documentación y notificación.
- Prohibición de destrucción de pruebas.
- No consta plazo expreso de notificación en horas o días.

Fuente: ANEXO I 2026 03393.pdf, p.36-37, CD.08

---

## 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención

- Logs normalizados, campos mínimos: actividad, acceso, IP origen/destino, usuario.
- Entrega de logs al SIEM de RENFE o API autorizada.
- Custodia de logs por periodo de retención que especifique RENFE.
- Monitorización 24x7 de la infraestructura.
- Planes de continuidad, contingencia, crisis, salida programada y sobrevenida.
- Backup y restauración periódica, pruebas de restauración.
- No consta RTO/RPO numérico.

Fuente: ANEXO I 2026 03393.pdf, p.36, CD.06-CD.07; p.38-39, DS.01-DS.03

---

## 10. Auditorías, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad

- RENFE puede solicitar informes técnicos, auditorías, acceso a locales y sistemas, colaboración obligatoria.
- Auditoría bi-anual, auditorías de terceros y extraordinarias.
- Certificados de destrucción de datos al finalizar el servicio.
- Acuerdo de confidencialidad obligatorio para personal propio y subcontratado.
- Formación y concienciación en seguridad y privacidad para el personal.
- Certificación ISO 27001 obligatoria.
- Certificación ENS nivel MEDIO obligatoria.

Fuente: ANEXO I 2026 03393.pdf, p.37-38, AU.01-AU.04; p.29, CN.04; p.28, PS.10-PS.11; PCP 2026 03993.pdf, p.24-25, 15

---

## 11. Consecuencias contractuales expresamente asociadas al incumplimiento

- Penalización hasta el 10% del contrato por no entrega de documentación de ciberseguridad (análisis de riesgos, acuerdos de confidencialidad, informes de seguridad, etc.).
- Penalización de 1000-3000€ por demora en el cuestionario de evaluación de seguridad de la cadena de suministro.
- Penalización hasta el 10% del contrato por falta de certificación ENS nivel MEDIO.
- Penalización de 1000€/mes por no notificar el Punto de Contacto de Seguridad; 1000€/24h por falta de respuesta.
- Penalización hasta el 20% del contrato por incumplimiento de obligaciones de confidencialidad, protección de datos y propiedad intelectual.
- Resolución del contrato por incumplimiento grave de SP.01, PS.07, CN.01 o entrega de documentación de ciberseguridad.

Fuente: PCP 2026 03993.pdf, p.30-31, 19.6-19.8; p.33, 29

---

## 12. Datos no localizados o ambiguos, sin recomendaciones

- No consta definición de RTO/RPO numérico.
- No consta listado exhaustivo de categorías de datos personales ni interesados.
- No consta detalle de plazos de retención de logs o backups (se remite a lo que especifique RENFE).
- No consta exigencia de DPO/DPD propio para el adjudicatario, solo colaboración con el DPD de RENFE.
- No consta exigencia de SBOM, SAST, DAST, SCA, DevSecOps, CI/CD, OWASP, salvo medidas generales de desarrollo seguro y pruebas de seguridad.

---

## 13. Documentos revisados

1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393.pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Plataforma de Contratación del Sector Público, sin contenido relevante adicional)
7. poc (Plataforma de Contratación del Sector Público, sin contenido relevante adicional)
8. poc (Plataforma de Contratación del Sector Público, sin contenido relevante adicional)

---

## 14. Trazabilidad de requisitos y fuentes

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Certificación ENS nivel MEDIO | Obligatorio | Certificado o compromiso, 10-12 meses | ANEXO I 2026 03393.pdf | p.28, CN.01 | TEXTO EXTRAIDO |
| ISO 27001 | Obligatorio | Certificado vigente | PCP 2026 03993.pdf | p.20 | TEXTO EXTRAIDO |
| Análisis de riesgos MAGERIT | Obligatorio | Informe, compartir con RENFE | ANEXO I 2026 03393.pdf | p.25, PS.04 | TEXTO EXTRAIDO |
| Subencargados | Obligatorio | Autorización previa escrita, mismas condiciones | PCP 2026 03993.pdf | p.26 | TEXTO EXTRAIDO |
| Localización de datos | Obligatorio | Solo EEE salvo autorización expresa | ANEXO I 2026 03393.pdf | p.25, PS.01 | TEXTO EXTRAIDO |
| Cifrado en tránsito y almacenamiento | Obligatorio | Protocolos seguros, HSM | ANEXO I 2026 03393.pdf | p.30, SD.03 | TEXTO EXTRAIDO |
| Gestión de identidades | Obligatorio | Integración con RENFE, SAML2/ADFS | ANEXO I 2026 03393.pdf | p.31-32, GI.05 | TEXTO EXTRAIDO |
| Logging y SIEM | Obligatorio | Logs normalizados, entrega a SIEM RENFE | ANEXO I 2026 03393.pdf | p.36, CD.06 | TEXTO EXTRAIDO |
| Monitorización 24x7 | Obligatorio | SOC/SIEM | ANEXO I 2026 03393.pdf | p.36, CD.07 | TEXTO EXTRAIDO |
| Backup y restauración | Obligatorio | Pruebas periódicas | ANEXO I 2026 03393.pdf | p.29, SD.01.04 | TEXTO EXTRAIDO |
| Pruebas de seguridad/pentesting | Obligatorio | Autorización previa, resultados a RENFE | ANEXO I 2026 03393.pdf | p.37, CD.09 | TEXTO EXTRAIDO |
| Borrado seguro y certificado | Obligatorio | Certificado de destrucción | ANEXO I 2026 03393.pdf | p.29, CN.04 | TEXTO EXTRAIDO |
| Penalizaciones por incumplimiento | Consecuencia | Hasta 20% del contrato, resolución | PCP 2026 03993.pdf | p.30-31, 19.6-19.8 | TEXTO EXTRAIDO |
| Comunicación de incidentes | Obligatorio | A CERT RENFE, niveles Medio+ | ANEXO I 2026 03393.pdf | p.36-37, CD.08 | TEXTO EXTRAIDO |
| Registro de actividades de tratamiento | Condicionado | Si aplica, según RGPD | PCP 2026 03993.pdf | p.27 | TEXTO EXTRAIDO |
| Devolución o supresión de datos | Obligatorio | A elección de RENFE al finalizar | PCP 2026 03993.pdf | p.27 | TEXTO EXTRAIDO |
| Formación y concienciación | Obligatorio | Personal propio y subcontratado | ANEXO I 2026 03393.pdf | p.28, PS.10 | TEXTO EXTRAIDO |

---

## 15. Discrepancias y pendientes de aclaración

No se han identificado discrepancias en la documentación revisada. No se localizan RTO/RPO numéricos, detalle de categorías de datos personales, ni exigencia de DPO propio para el adjudicatario. No consta exigencia de SBOM, SAST, DAST, SCA, DevSecOps, CI/CD, OWASP, salvo medidas generales de desarrollo seguro y pruebas de seguridad.