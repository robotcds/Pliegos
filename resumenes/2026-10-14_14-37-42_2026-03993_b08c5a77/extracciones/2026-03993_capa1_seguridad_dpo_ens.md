# 1. Resumen factual Seguridad / DPO / ENS

La licitación para la "Solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para la operación ferroviaria" de RENFE-Operadora exige el cumplimiento de requisitos avanzados en materia de seguridad de la información, protección de datos personales y Esquema Nacional de Seguridad (ENS). El adjudicatario debe acreditar certificación ENS nivel Medio, cumplir con ISO 27001, aplicar medidas técnicas y organizativas específicas, gestionar identidades y accesos, garantizar la trazabilidad y la gestión de incidentes, y colaborar en auditorías y supervisión. Se establecen obligaciones contractuales detalladas sobre subcontratación, localización de datos, cifrado, backup, continuidad, borrado seguro y confidencialidad, así como penalizaciones y causas de resolución por incumplimiento. El adjudicatario actúa como encargado del tratamiento de datos personales, con obligaciones contractuales específicas en materia de RGPD/LOPDGDD.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito ENS | Categoria/Nivel | Alcance | Acreditación | Momento | Fuente |
|---|---|---|---|---|---|
| Certificación ENS | Nivel MEDIO | Sistemas de información que den soporte a los servicios objeto de la licitación | Certificado ENS nivel MEDIO o compromiso de obtenerlo | Antes del inicio del servicio o en los primeros 10 meses de prestación; si solo ISO 27001, en los primeros 12 meses | ANEXO I 2026 03393.pdf, p.28, CN.01; PCP 2026 03993.pdf, p.20 |
| Cumplimiento ENS | Nivel MEDIO | Solución SaaS y servicios asociados | Declaración responsable y documentación técnica | Presentación de oferta y durante ejecución | ANEXO I 2026 03393.pdf, p.24-25, Parte I y II |
| Análisis de riesgos MAGERIT | Nivel MEDIO | Proyecto completo | Informe de análisis de riesgos conforme ENS/MAGERIT | Tras adjudicación, antes de inicio | ANEXO I 2026 03393.pdf, p.25, PS.04 |
| Informe CLARA CCN | Nivel MEDIO, ≥65% | Equipos de usuario del adjudicatario conectados a sistemas de Renfe | Informe individual por equipo | Antes de uso de equipos | ANEXO I 2026 03393.pdf, p.24, Parte I; p.34, SE.05 |
| Guías CCN-CERT | Aplicable según tecnología | Bases de datos, seguridad, etc. | Cumplimiento de guías CCN-CERT BP/22, BP/23, BP/24 | Durante ejecución | ANEXO I 2026 03393.pdf, p.30, SD.04.02 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|---|---|---|---|
| Encargado del tratamiento | El adjudicatario es encargado, RENFE responsable | Durante la ejecución del contrato | PCP 2026 03993.pdf, p.25-28, cláusula 17 |
| Tratamiento solo bajo instrucciones | Solo según instrucciones documentadas de RENFE | Durante contrato | PCP 2026 03993.pdf, p.25 |
| Prohibición de uso para fines propios | No puede usar datos para fines propios o distintos | Durante contrato | PCP 2026 03993.pdf, p.25 |
| Subencargados solo con autorización | Necesaria autorización previa y escrita de RENFE | Durante contrato | PCP 2026 03993.pdf, p.26 |
| Registro de actividades de tratamiento | Si el tratamiento entraña riesgo, no es ocasional o incluye categorías especiales | Durante contrato | PCP 2026 03993.pdf, p.27 |
| Supresión o devolución de datos | A elección de RENFE al finalizar el servicio | Al finalizar el contrato | PCP 2026 03993.pdf, p.27 |
| Certificado de destrucción | Para cada borrado/destrucción realizado | Al finalizar el contrato o cuando se requiera | ANEXO I 2026 03393.pdf, p.29, CN.04.02 |
| Comunicación de derechos de interesados | Comunicación inmediata a dpd@renfe.es | Inmediato tras recepción | PCP 2026 03993.pdf, p.27 |
| Asistencia en ejercicio de derechos | Asistencia técnica y organizativa | Durante contrato | PCP 2026 03993.pdf, p.27 |
| Notificación de incidentes/brechas | Asistencia en notificación a autoridad y afectados | Según legislación vigente | PCP 2026 03993.pdf, p.27 |
| Principios de protección de datos por diseño y por defecto | Obligación expresa | Durante contrato | PCP 2026 03993.pdf, p.28 |
| DPD/DPD de RENFE | El DPD de RENFE es el responsable final | Durante contrato | ANEXO I 2026 03393.pdf, p.31, SP.04 |

# 4. Subencargados, cloud, localización y transferencias

| Requisito | Condición | Fuente |
|---|---|---|
| Subencargados | Autorización previa y escrita de RENFE; mismas obligaciones contractuales | PCP 2026 03993.pdf, p.26; ANEXO I 2026 03393.pdf, p.26, PS.07 |
| Cloud público | Si se usa, Renfe puede auditar con CNAPP; integración obligatoria | ANEXO I 2026 03393.pdf, p.36, CD.05 |
| Localización de datos | Prestación del servicio y almacenamiento solo en Espacio Económico Europeo salvo autorización expresa de Renfe | ANEXO I 2026 03393.pdf, p.25, PS.01 |
| Transferencias internacionales | Prohibidas salvo autorización expresa y cumplimiento legal | ANEXO I 2026 03393.pdf, p.25, PS.01; PCP 2026 03993.pdf, p.25 |

# 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente

| Medida | Obligatoria/Valorable/Condicionada | Parámetro/Plazo | Fuente |
|---|---|---|---|
| Cifrado de datos en tránsito, uso y almacenamiento | Obligatoria | Protocolos seguros (https, TLS v1.2+), información sobre servicios criptográficos, custodia de claves en HSM salvo excepción | ANEXO I 2026 03393.pdf, p.30, SD.03 |
| Control de accesos y gestión de identidades | Obligatoria | Integración con sistema de identidad de Renfe, SSO, SAML2/ADFS, prohibición de usuarios genéricos, control de privilegios | ANEXO I 2026 03393.pdf, p.31-32, GI.01-GI.11 |
| Backup y restauración | Obligatoria | Procesos de backup, restauración y pruebas periódicas | ANEXO I 2026 03393.pdf, p.29, SD.01.04; p.38, DS.01.03 |
| DLP (Data Loss Prevention) | Obligatoria si hay datos personales o tarjetas de pago | Solución comercial, descubrimiento cada 3 meses | ANEXO I 2026 03393.pdf, p.29, SD.01.03; p.35, CD.03.06 |
| WAF, IDS/IPS, FW, antimalware, proxy, CASB, CWPP | Obligatoria según naturaleza de la solución | Según arquitectura y servicios | ANEXO I 2026 03393.pdf, p.35, CD.03 |
| Segmentación de red | Obligatoria | Segmentación adecuada | ANEXO I 2026 03393.pdf, p.29, CN.03 |
| Administración remota segura, VPN | Obligatoria | Acceso seguro, controlado y auditado | ANEXO I 2026 03393.pdf, p.33, GI.10 |
| Gestión de vulnerabilidades y parcheado | Obligatoria | Proceso formal, escaneos periódicos, remediación según criticidad, entrega de informes | ANEXO I 2026 03393.pdf, p.35-36, CD.04 |
| Trazabilidad y logs | Obligatoria | Registro de actividad, acceso, IP origen/destino, usuario; entrega al SIEM de Renfe o API autorizada; retención según especifique Renfe | ANEXO I 2026 03393.pdf, p.36, CD.06 |
| Monitorización 24x7 (SOC/SIEM) | Obligatoria | Monitorización de incidencias e incidentes 24x7 | ANEXO I 2026 03393.pdf, p.36, CD.07 |
| Control de acceso físico/lógico | Obligatoria | Acceso restringido, prohibición de acceso no autorizado | ANEXO I 2026 03393.pdf, p.31, GI.01 |
| Gestión de usuarios privilegiados (PAM) | Obligatoria | Medios adecuados para gestión de accesos privilegiados, controles, trazabilidad | ANEXO I 2026 03393.pdf, p.32, GI.08-GI.09 |
| Bastionado de equipos | Obligatoria | Cumplimiento de requisitos ENS, informe CLARA ≥65% | ANEXO I 2026 03393.pdf, p.34, SE.05 |
| Protección de bases de datos | Obligatoria | Cifrado, ofuscación, pseudo-anonimización, auditoría, cumplimiento guías CCN-CERT | ANEXO I 2026 03393.pdf, p.30, SD.04 |
| Protección correo electrónico | Obligatoria si aplica | Antimalware, antispam, reputación, uso de sistemas de Renfe | ANEXO I 2026 03393.pdf, p.35, CD.03.10, CD.10 |
| 2FA/MFA | Obligatoria para servicios expuestos a Internet que lo requieran | Segundo factor de autenticación | ANEXO I 2026 03393.pdf, p.35, CD.03.11 |

# 6. Identidad, accesos y privilegios

- Integración obligatoria con el sistema de identidad de Renfe y federación (SAML2, ADFS, etc.).
- Prohibición de usuarios genéricos; detección y control de creación/uso.
- Gestión de altas/bajas de usuarios, perfiles diferenciados (administrador, operador, analista, consulta).
- Control de accesos privilegiados (PAM), trazabilidad, auditoría y escalado de privilegios.
- Acceso remoto seguro (VPN, autenticación fuerte).
- Registro de intentos de autenticación (fallidos y correctos) con información relevante (IP, usuario, etc.).
- Aplicación del principio de mínimo privilegio.

Fuente: ANEXO I 2026 03393.pdf, p.31-33, GI.01-GI.11

# 7. Vulnerabilidades, parcheado y desarrollo seguro

- Proceso formal de gestión de vulnerabilidades y parcheado de sistemas, plataformas e infraestructuras.
- Escaneos de vulnerabilidades periódicos, habilitación de accesos para escaneos de Renfe.
- Entrega de informes de escaneo a Renfe; remediación en plazos según criticidad y políticas de Renfe.
- Prohibición de uso de software próximo a EOL/EOS.
- Pruebas de seguridad (pentesting, hacking ético) solo con autorización de Renfe; resultados obligatoriamente compartidos.
- Plan de no obsolescencia y actualización continua.
- Cumplimiento de guías CCN-CERT para bases de datos.

Fuente: ANEXO I 2026 03393.pdf, p.28, PS.06; p.35-36, CD.04, CD.09; p.30, SD.04.02

# 8. Incidentes, brechas y plazos de notificación expresamente indicados

- Comunicación de incidentes de seguridad con impacto Medio, Alto, Muy Alto y Crítico a la Gerencia de Área de Ciberseguridad de Renfe y al CERT de Renfe (notificaciones.pocterceros.ciberseguridad@renfe.es).
- El adjudicatario debe colaborar en la valoración, remediación, documentación y notificación del incidente.
- Prohibición de destrucción de pruebas durante la gestión del incidente.
- Plazo de notificación: NO CONSTA PLAZO EXPRESO EN HORAS/MINUTOS, salvo penalizaciones por falta de respuesta del POC de Seguridad (ver sección 11).
- Comunicación inmediata a dpd@renfe.es de solicitudes de derechos de interesados.

Fuente: ANEXO I 2026 03393.pdf, p.36-37, CD.08; PCP 2026 03993.pdf, p.27

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención

- Registro, auditoría y trazabilidad de eventos, operaciones y actividades en aplicaciones, sistemas e infraestructuras.
- Logs con actividad, acceso, IP origen/destino, usuario; entrega al SIEM de Renfe o API autorizada.
- Custodia de logs por el periodo de retención que especifique Renfe.
- Monitorización 24x7 de la infraestructura (SOC/SIEM).
- Copias de seguridad, restauración y pruebas periódicas.
- Planes de contingencia, crisis, continuidad de negocio y salida (devolución/destrucción de datos).
- Identificación de competencias básicas para retomar control directo en caso de contingencia.
- Certificados de destrucción de información al finalizar el servicio.
- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA.

Fuente: ANEXO I 2026 03393.pdf, p.27, PS.08; p.36, CD.06-CD.07; p.38-39, DS.01-DS.03

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad

- Renfe puede solicitar informes técnicos, auditorías, SSAE16, ISAE 3402 Soc 2 Tipo II, etc.
- Renfe puede auditar sistemas, procesos y locales del adjudicatario y subcontratistas.
- El adjudicatario debe colaborar en auditorías internas y externas (bi-anuales, IGAE, Tribunal de Cuentas, UIC, CNPIC, extraordinarias).
- Certificación ENS nivel MEDIO obligatoria; si solo ISO 27001, compromiso de obtener ENS en 10-12 meses.
- Certificados de destrucción de datos al finalizar el servicio.
- Acuerdo de confidencialidad obligatorio para personal propio y subcontratado.
- Formación y concienciación en seguridad y protección de datos para el personal.
- Prohibición de uso de información confidencial para fines distintos a los del contrato.

Fuente: ANEXO I 2026 03393.pdf, p.28, CN.01; p.27, PS.11; p.37-38, AU.01-AU.04; PCP 2026 03993.pdf, p.24-25, 15

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento

- Penalización de hasta el 10% del contrato por no entrega de documentación de ciberseguridad (análisis de riesgos, acuerdos de confidencialidad, informes de seguridad, etc.).
- Penalización de 1000-3000€ por demora en completar el cuestionario de evaluación de seguridad de la cadena de suministro (PS.07).
- Penalización de hasta el 10% del contrato por falta de certificación ENS nivel MEDIO (CN.01).
- Penalización de 1000€ por no notificar el Punto de Contacto de Seguridad en plazo; 1000€ adicionales por cada mes de retraso; 1000€ por cada 24h de falta de respuesta del POC de Seguridad.
- Penalización de hasta el 20% del contrato por incumplimiento de obligaciones de confidencialidad, protección de datos o propiedad intelectual.
- Resolución del contrato por incumplimiento de SP.01, PS.07, CN.01, entrega de documentación de ciberseguridad, confidencialidad, protección de datos, propiedad intelectual, ética y cumplimiento.

Fuente: PCP 2026 03993.pdf, p.30-34, 19.6-19.8, 29

# 12. Datos no localizados o ambiguos, sin recomendaciones

- RTO/RPO: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Categorías concretas de datos personales tratados: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Detalle de medidas de desarrollo seguro (SDLC, DevSecOps, SAST, DAST, SCA, secretos, OWASP, CI/CD, SBOM): NO CONSTA EN LA DOCUMENTACION REVISADA.
- Plazos expresos de notificación de incidentes/brechas en horas/minutos: NO CONSTA EN LA DOCUMENTACION REVISADA.
- Detalle de formatos de portabilidad de datos personales: NO CONSTA EN LA DOCUMENTACION REVISADA.

# 13. Documentos revisados

1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393.pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Plataforma de Contratación del Sector Público, información general)
7. poc (Perfil de contratante RENFE-Operadora, información general)
8. poc (Perfil de contratante RENFE-Operadora, información general)

# Tabla de trazabilidad

| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Certificación ENS | Obligación contractual | Nivel MEDIO, sistemas de información, certificado o compromiso | ANEXO I 2026 03393.pdf | p.28, CN.01 | TEXTO EXTRAIDO |
| ISO 27001 | Obligación contractual | Certificación o equivalente, si no ENS, compromiso de obtener ENS | PCP 2026 03993.pdf | p.20 | TEXTO EXTRAIDO |
| Análisis de riesgos MAGERIT | Obligación contractual | Informe conforme ENS/MAGERIT, compartir con Renfe | ANEXO I 2026 03393.pdf | p.25, PS.04 | TEXTO EXTRAIDO |
| Subencargados | Obligación contractual | Autorización previa y escrita, mismas obligaciones | PCP 2026 03993.pdf | p.26 | TEXTO EXTRAIDO |
| Localización de datos | Obligación contractual | Solo EEE salvo autorización expresa | ANEXO I 2026 03393.pdf | p.25, PS.01 | TEXTO EXTRAIDO |
| Cifrado de datos | Obligación contractual | En tránsito, uso y almacenamiento, protocolos seguros, HSM | ANEXO I 2026 03393.pdf | p.30, SD.03 | TEXTO EXTRAIDO |
| Control de accesos | Obligación contractual | Integración con identidad Renfe, SSO, SAML2/ADFS, mínimo privilegio | ANEXO I 2026 03393.pdf | p.31-32, GI.01-GI.11 | TEXTO EXTRAIDO |
| Backup y restauración | Obligación contractual | Procesos de backup, restauración, pruebas periódicas | ANEXO I 2026 03393.pdf | p.29, SD.01.04 | TEXTO EXTRAIDO |
| DLP | Obligación contractual | Solución comercial, descubrimiento cada 3 meses | ANEXO I 2026 03393.pdf | p.29, SD.01.03 | TEXTO EXTRAIDO |
| Gestión de vulnerabilidades | Obligación contractual | Proceso formal, escaneos, remediación según criticidad | ANEXO I 2026 03393.pdf | p.35-36, CD.04 | TEXTO EXTRAIDO |
| Logging y SIEM | Obligación contractual | Registro de actividad, entrega a SIEM Renfe, retención según Renfe | ANEXO I 2026 03393.pdf | p.36, CD.06 | TEXTO EXTRAIDO |
| Monitorización 24x7 | Obligación contractual | SOC/SIEM, detección de incidentes | ANEXO I 2026 03393.pdf | p.36, CD.07 | TEXTO EXTRAIDO |
| Auditorías | Obligación contractual | Renfe puede auditar sistemas, procesos, locales | ANEXO I 2026 03393.pdf | p.37-38, AU.01-AU.04 | TEXTO EXTRAIDO |
| Borrado y destrucción de datos | Obligación contractual | Procedimiento seguro, certificado de destrucción | ANEXO I 2026 03393.pdf | p.29, CN.04.02 | TEXTO EXTRAIDO |
| Penalizaciones por incumplimiento | Consecuencia contractual | Hasta 10-20% del contrato, penalizaciones específicas | PCP 2026 03993.pdf | p.30-34, 19.6-19.8 | TEXTO EXTRAIDO |
| RTO/RPO | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| Desarrollo seguro (SDLC, DevSecOps, etc.) | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| Categorías de datos personales | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| Plazos de notificación de incidentes | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |

# Discrepancias y pendientes de aclaración

No se han identificado discrepancias en la documentación revisada. No se localizan plazos expresos de notificación de incidentes en horas/minutos, ni detalle de RTO/RPO, ni desarrollo seguro (SDLC, DevSecOps, etc.), ni categorías concretas de datos personales tratados. Si estos datos son relevantes, quedan pendientes de verificación en caso de que se publiquen documentos adicionales o aclaraciones oficiales.