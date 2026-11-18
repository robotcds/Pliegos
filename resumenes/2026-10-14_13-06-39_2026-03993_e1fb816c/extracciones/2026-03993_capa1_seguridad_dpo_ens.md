## 1. Resumen factual Seguridad / DPO / ENS

La licitación exige el cumplimiento de requisitos de seguridad, privacidad y ENS para la solución SaaS de inteligencia meteorológica y gestión de riesgos naturales. Se requiere certificación ENS nivel Medio, cumplimiento de ISO 27001 o equivalente, análisis de riesgos conforme a MAGERIT, medidas técnicas y organizativas específicas, control de subcontratación, localización de datos en el EEE, cifrado, gestión de identidades y accesos, logging, monitorización, gestión de incidentes, planes de continuidad, auditorías y obligaciones de confidencialidad y protección de datos. El adjudicatario será encargado del tratamiento y debe cumplir instrucciones del responsable (RENFE), incluyendo obligaciones sobre subencargados, localización, transferencias, borrado y devolución de datos.

## 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito ENS | Categoria/nivel | Alcance | Acreditación | Momento | Fuente |
|---|---|---|---|---|---|
| Certificación ENS | Nivel Medio | Sistemas de información que soportan el servicio | Certificado ENS nivel Medio o compromiso de obtenerlo | Antes del inicio del servicio o en 10 meses si no se dispone, 12 meses si solo ISO 27001 | ANEXO I 2026 03393.pdf, p.24-28, CN.01 |
| Análisis de riesgos MAGERIT | Nivel Medio | Proyecto completo | Informe de análisis de riesgos | Tras adjudicación, antes de inicio | ANEXO I 2026 03393.pdf, p.25-26, PS.04 |
| Informe CLARA CCN | Nivel Medio | Equipos de usuario | Informe individual cumplimiento ENS 65%+ | Antes de inicio de uso de equipos | ANEXO I 2026 03393.pdf, p.24, SE.05 |
| Medidas técnicas ENS | Nivel Medio | Toda la solución | Declaración responsable y evidencias | Presentación y ejecución | ANEXO I 2026 03393.pdf, p.24-28 |

## 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|---|---|---|---|
| Encargado del tratamiento | El adjudicatario es encargado, RENFE responsable | Durante la ejecución del contrato | PCP 2026 03993.pdf, p.25-27 |
| Instrucciones documentadas | Solo según instrucciones de RENFE | Durante contrato | PCP 2026 03993.pdf, p.25-27 |
| Subencargados | Solo con autorización previa y escrita de RENFE | Durante contrato | PCP 2026 03993.pdf, p.26; ANEXO I 2026 03393.pdf, p.27, PS.07 |
| Localización de datos | Solo EEE salvo autorización expresa | Durante contrato | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Transferencias internacionales | Solo con autorización expresa de RENFE | Durante contrato | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Borrado/devolución | A elección de RENFE al finalizar el servicio | Al cierre del contrato | PCP 2026 03993.pdf, p.27; ANEXO I 2026 03393.pdf, p.28, CN.04 |
| Registro de actividades | Si el tratamiento entraña riesgo/no es ocasional | Durante contrato | PCP 2026 03993.pdf, p.27 |
| Asistencia a derechos ARCO | Comunicación inmediata a dpd@renfe.es | Inmediato | PCP 2026 03993.pdf, p.27 |
| Notificación de incidentes | Según legislación y directrices RENFE | Inmediato | PCP 2026 03993.pdf, p.27; ANEXO I 2026 03393.pdf, p.28, CD.08 |

## 4. Subencargados, cloud, localización y transferencias

| Requisito | Condición | Fuente |
|---|---|---|
| Subencargados | Autorización previa y escrita de RENFE, mismas obligaciones | PCP 2026 03993.pdf, p.26; ANEXO I 2026 03393.pdf, p.27, PS.07 |
| Cloud público | Integración con CNAPP de Renfe si se solicita | ANEXO I 2026 03393.pdf, p.36, CD.05 |
| Localización de datos | Solo EEE salvo autorización expresa | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Transferencias internacionales | Solo con autorización expresa de RENFE | ANEXO I 2026 03393.pdf, p.25, PS.01 |

## 5. Medidas técnicas

| Medida | Obligatoria/valorable/condicionada | Parámetro/plazo | Fuente |
|---|---|---|---|
| Cifrado en tránsito, uso y almacenamiento | Obligatoria | Protocolos seguros (https, TLS 1.2+), HSM para claves | ANEXO I 2026 03393.pdf, p.29-30, SD.03 |
| Control de accesos, RBAC, mínimo privilegio | Obligatoria | Roles definidos y autorizados por RENFE | ANEXO I 2026 03393.pdf, p.31-32, GI.01-GI.08 |
| MFA/2FA | Obligatoria para servicios expuestos a Internet | 2FA | ANEXO I 2026 03393.pdf, p.35, CD.03.11 |
| PAM (gestión de accesos privilegiados) | Obligatoria | Procedimientos y herramientas | ANEXO I 2026 03393.pdf, p.32, GI.08-GI.09 |
| VPN, acceso remoto seguro | Obligatoria | Acceso seguro para conexiones remotas | ANEXO I 2026 03393.pdf, p.33, GI.10 |
| Bastionado, segmentación de red | Obligatoria | Segmentación adecuada | ANEXO I 2026 03393.pdf, p.29, CN.03 |
| EDR/XDR, antimalware | Obligatoria | Instalación y mantenimiento actualizado | ANEXO I 2026 03393.pdf, p.34, SE.04 |
| WAF, IDS/IPS, defensa perimetral | Obligatoria según naturaleza del servicio | Comercial, alineado con Renfe | ANEXO I 2026 03393.pdf, p.35, CD.03 |
| SIEM, logs, monitorización 24x7 | Obligatoria | Integración con SIEM de Renfe, logs normalizados | ANEXO I 2026 03393.pdf, p.36, CD.06-CD.07 |
| DLP | Obligatoria si hay datos personales/confidenciales | Solución comercial, descubrimiento trimestral | ANEXO I 2026 03393.pdf, p.29, SD.01.03; p.35, CD.03.06 |
| Backups, restauración, pruebas | Obligatoria | Procesos de backup y restauración, pruebas periódicas | ANEXO I 2026 03393.pdf, p.29, SD.01.04; p.39, DS.01.03 |
| Logs, trazabilidad, retención | Obligatoria | Entrega a SIEM, retención según Renfe | ANEXO I 2026 03393.pdf, p.36, CD.06 |

## 6. Identidad, accesos y privilegios

- Autenticación segura, integración con sistema de identidad de Renfe, federación SAML2/ADFS (ANEXO I 2026 03393.pdf, p.24, GI.05.01).
- Prohibido uso de usuarios genéricos (p.32, GI.06).
- Gestión de altas/bajas, privilegios, perfiles, mínimo privilegio (p.31-32, GI.01-GI.08).
- Acceso remoto seguro, VPN (p.33, GI.10).
- Registro de intentos de autenticación, logs de acceso (p.32, GI.07.06).

## 7. Vulnerabilidades, parcheado y desarrollo seguro

- Estrategia y plan de no obsolescencia, gestión de vulnerabilidades, identificación, remediación, SLA (p.26, PS.06; p.35, CD.04).
- Parcheo regular y seguro, proceso formal de gestión de vulnerabilidades (p.29, CN.03; p.35, CD.04.01).
- Escaneos de vulnerabilidades periódicos, entrega de informes a Renfe, remediación según criticidad (p.35, CD.04.02).
- Pruebas de seguridad/pentesting autorizadas por Renfe, resultados compartidos (p.37, CD.09).
- Desarrollo seguro: NO CONSTA EN LA DOCUMENTACION REVISADA.

## 8. Incidentes, brechas y plazos de notificación expresamente indicados

- Notificación de incidentes de seguridad a Gerencia de Ciberseguridad de Renfe para niveles Medio, Alto, Muy Alto y Crítico, según Guía CCN-STIC 817 (p.36, CD.08).
- Canal: notificaciones.pocterceros.ciberseguridad@renfe.es (p.36, CD.08).
- Plazo: Inmediato tras identificación como posible incidente (p.36, CD.08).
- Colaboración con CERT de Renfe, evitar destrucción de pruebas (p.36-37, CD.08).
- Obligación de confidencialidad en la gestión de incidentes (p.37, CD.08).

## 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención

- Logging: registro, trazabilidad, entrega a SIEM de Renfe, logs normalizados, retención según Renfe (p.36, CD.06).
- Monitorización 24x7 de la infraestructura (p.36, CD.07).
- Continuidad: planes de contingencia, crisis, continuidad de negocio, salida programada y sobrevenida, devolución/destrucción de datos (p.28, PS.09; p.39, DS.01-DS.03).
- Backups: procesos de backup, restauración, pruebas periódicas (p.29, SD.01.04; p.39, DS.01.03).
- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Retención de logs: según periodo especificado por Renfe (p.36, CD.06).

## 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad

- Auditorías: derecho de Renfe a auditar, acceso a instalaciones, colaboración en auditorías externas, bi-anuales, extraordinarias (p.37-38, AU.01-AU.04).
- Evidencias: entrega de informes técnicos, SSAE16, IASE 3402 Soc 2 Tipo II, etc. si se solicitan (p.37, AU.01).
- Certificaciones: ENS nivel Medio, ISO 27001 o equivalente (p.24, CN.01).
- Seguridad del personal: formación, concienciación, acuerdos de confidencialidad firmados (p.27, PS.10-PS.11).
- Borrado: procedimiento seguro conforme ENS, certificado de destrucción con campos detallados (p.28, CN.04).
- Confidencialidad: obligación contractual, penalización hasta 20% del contrato por incumplimiento (PCP 2026 03993.pdf, p.24-25, 30-31).

## 11. Consecuencias contractuales expresamente asociadas al incumplimiento

- Penalización hasta 10% del contrato por no entrega de documentación de ciberseguridad (PCP 2026 03993.pdf, p.30).
- Penalización por no completar cuestionario de cadena de suministro: 1000€/mes de retraso, hasta 3000€ (PCP 2026 03993.pdf, p.31).
- Penalización hasta 10% del contrato por falta de certificación ENS (PCP 2026 03993.pdf, p.31).
- Penalización por no notificar Punto de Contacto de Seguridad: 1000€/mes de retraso, 1000€/24h por falta de respuesta (PCP 2026 03993.pdf, p.31).
- Penalización hasta 20% del contrato por incumplimiento de confidencialidad, protección de datos o propiedad intelectual (PCP 2026 03993.pdf, p.30).
- Resolución del contrato por incumplimiento grave de SP.01, PS.07, CN.01 o entrega de documentación de ciberseguridad (PCP 2026 03993.pdf, p.33).

## 12. Datos no localizados o ambiguos, sin recomendaciones

- Desarrollo seguro (SDLC, DevSecOps, SAST, DAST, SCA, secretos, OWASP, CI/CD, SBOM): NO CONSTA EN LA DOCUMENTACION REVISADA.
- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Categorías concretas de datos personales/interesados: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Detalle de formatos de portabilidad: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Plazos de retención de datos personales: NO CONSTA EN LA DOCUMENTACION REVISADA.
- DPO/DPD del adjudicatario: NO CONSTA EN LA DOCUMENTACION REVISADA.

## 13. Documentos revisados

1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393.pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Plataforma de Contratación del Sector Público, sin contenido relevante extraído)
7. poc (Plataforma de Contratación del Sector Público, sin contenido relevante extraído)
8. poc (Plataforma de Contratación del Sector Público, sin contenido relevante extraído)

## Tabla de trazabilidad

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Certificación ENS | Obligación contractual | Nivel Medio, sistemas de información, certificado ENS | ANEXO I 2026 03393.pdf | p.24-28, CN.01 | TEXTO EXTRAIDO |
| Análisis de riesgos MAGERIT | Obligación contractual | Informe MAGERIT, compartir con Renfe | ANEXO I 2026 03393.pdf | p.25-26, PS.04 | TEXTO EXTRAIDO |
| Subencargados | Obligación contractual | Autorización previa y escrita, mismas obligaciones | PCP 2026 03993.pdf; ANEXO I 2026 03393.pdf | p.26; p.27, PS.07 | TEXTO EXTRAIDO |
| Localización de datos | Obligación contractual | Solo EEE salvo autorización expresa | ANEXO I 2026 03393.pdf | p.25, PS.01 | TEXTO EXTRAIDO |
| Cifrado | Medida técnica obligatoria | En tránsito, uso y almacenamiento, HSM para claves | ANEXO I 2026 03393.pdf | p.29-30, SD.03 | TEXTO EXTRAIDO |
| Control de accesos | Medida técnica obligatoria | RBAC, mínimo privilegio, integración identidad Renfe | ANEXO I 2026 03393.pdf | p.31-32, GI.01-GI.08 | TEXTO EXTRAIDO |
| MFA/2FA | Medida técnica obligatoria | Para servicios expuestos a Internet | ANEXO I 2026 03393.pdf | p.35, CD.03.11 | TEXTO EXTRAIDO |
| Logging/SIEM | Medida técnica obligatoria | Entrega a SIEM de Renfe, logs normalizados | ANEXO I 2026 03393.pdf | p.36, CD.06 | TEXTO EXTRAIDO |
| Monitorización 24x7 | Medida técnica obligatoria | SOC/SIEM, detección de incidentes | ANEXO I 2026 03393.pdf | p.36, CD.07 | TEXTO EXTRAIDO |
| Notificación de incidentes | Obligación contractual | Inmediata, canal designado, colaboración CERT | ANEXO I 2026 03393.pdf | p.36, CD.08 | TEXTO EXTRAIDO |
| Auditorías | Obligación contractual | Derecho de Renfe, acceso a instalaciones, colaboración | ANEXO I 2026 03393.pdf | p.37-38, AU.01-AU.04 | TEXTO EXTRAIDO |
| Borrado/destrucción | Obligación contractual | Procedimiento seguro, certificado de destrucción | ANEXO I 2026 03393.pdf | p.28, CN.04 | TEXTO EXTRAIDO |
| Penalizaciones | Consecuencia contractual | Hasta 20% del contrato, resolución por incumplimiento grave | PCP 2026 03993.pdf | p.30-33 | TEXTO EXTRAIDO |
| Desarrollo seguro | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| RTO/RPO | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| Categorías de datos personales | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| DPO/DPD adjudicatario | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |

## Discrepancias y pendientes de aclaración

No se han identificado discrepancias en la documentación revisada.