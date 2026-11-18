# 1. Resumen factual Seguridad / DPO / ENS

La licitación para la solución SaaS de inteligencia meteorológica y gestión de riesgos naturales para la operación ferroviaria de RENFE-Operadora exige el cumplimiento de requisitos avanzados en materia de seguridad, protección de datos y ENS. Se requiere certificación ENS nivel Medio, ISO 27001, cumplimiento RGPD/LOPDGDD, medidas técnicas y organizativas específicas, control de subencargados, localización de datos en el EEE, gestión de identidades y accesos, logging, continuidad, backup, gestión de vulnerabilidades, notificación de incidentes, auditorías, borrado seguro y confidencialidad. Se establecen penalizaciones y causas de resolución contractual por incumplimiento de estas obligaciones.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
| Requisito ENS | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente |
|---|---|---|---|---|---|
| Certificación ENS | Nivel Medio | Sistemas de información que soportan el servicio | Certificado ENS nivel Medio | Antes del inicio del servicio o en los primeros 10 meses si no se dispone al inicio | ANEXO I 2026 03393.pdf, p. 25-28 (CN.01, PS.01, Parte I y II) |
| Declaración responsable de cumplimiento ENS | Nivel Medio | Solución ofertada | Declaración responsable | Presentación de oferta (Sobre A) | ANEXO II 2026 03993.pdf, p. 2; ANEXO I 2026 03393.pdf, p. 23 |
| Informe CLARA CCN (cumplimiento ENS 65%+) | Nivel Medio | Equipos de usuario del adjudicatario | Informe individual por equipo | Antes de conexión a red/sistemas RENFE | ANEXO I 2026 03393.pdf, p. 24, 34 (SE.05) |
| Análisis de riesgos MAGERIT | Nivel Medio | Servicio contratado | Análisis de riesgos compartido con RENFE | Tras adjudicación, antes de inicio | ANEXO I 2026 03393.pdf, p. 23, 25-26 (PS.04) |
| Medidas técnicas ENS | Nivel Medio | Toda la solución SaaS | Implementación y documentación | Durante ejecución | ANEXO I 2026 03393.pdf, p. 25-39 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
| Datos/rol/obligación | Condición | Plazo/retención | Fuente |
|---|---|---|---|
| Encargado del tratamiento | El adjudicatario es encargado, RENFE responsable | Durante la ejecución del contrato | PCP 2026 03993.pdf, p. 25-28 (cláusula 17); ANEXO I 2026 03393.pdf, p. 25 (PS.01) |
| Tratamiento solo bajo instrucciones documentadas | Obligación contractual | Durante la ejecución | PCP 2026 03993.pdf, p. 25-28 |
| Prohibición de uso para fines propios o distintos | Obligación contractual | Durante la ejecución | PCP 2026 03993.pdf, p. 25-28 |
| Prohibición de comunicación a terceros sin autorización | Obligación contractual | Durante la ejecución | PCP 2026 03993.pdf, p. 25-28 |
| Subencargados solo con autorización previa escrita | Obligación contractual | Durante la ejecución | PCP 2026 03993.pdf, p. 25-28; ANEXO I 2026 03393.pdf, p. 26 (PS.07) |
| Registro de actividades de tratamiento | Si el tratamiento entraña riesgo/no es ocasional/incluye categorías especiales | Durante la ejecución | PCP 2026 03993.pdf, p. 25-28 |
| Supresión o devolución de datos al finalizar | A elección de RENFE | Al finalizar el servicio | PCP 2026 03993.pdf, p. 25-28; ANEXO I 2026 03393.pdf, p. 28 (CN.04) |
| Certificado de destrucción | Obligación contractual | Al finalizar el servicio | ANEXO I 2026 03393.pdf, p. 28 (CN.04.02) |
| Asistencia en ejercicio de derechos | Obligación contractual | Inmediato a solicitud | PCP 2026 03993.pdf, p. 25-28 |
| Notificación de solicitudes de derechos a dpd@renfe.es | Obligación contractual | Inmediato | PCP 2026 03993.pdf, p. 25-28 |
| Asistencia en EIPD y consulta previa | Obligación contractual | Cuando aplique | PCP 2026 03993.pdf, p. 25-28 |
| Medidas técnicas y organizativas adecuadas | Obligación contractual | Durante la ejecución | PCP 2026 03993.pdf, p. 25-28; ANEXO I 2026 03393.pdf, p. 25-39 |
| DPD RENFE como responsable final | Obligación contractual | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 31 (SP.04) |
| Localización de datos en EEE | Obligación contractual | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 25 (PS.01) |
| Transferencias internacionales solo con autorización | Obligación contractual | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 25 (PS.01) |

# 4. Subencargados, cloud, localización y transferencias
| Requisito | Condición | Fuente |
|---|---|---|
| Subencargados solo con autorización previa escrita de RENFE | Obligación contractual | PCP 2026 03993.pdf, p. 25-28; ANEXO I 2026 03393.pdf, p. 26 (PS.07) |
| Subencargados deben asumir mismas obligaciones | Obligación contractual | PCP 2026 03993.pdf, p. 25-28; ANEXO I 2026 03393.pdf, p. 26 (PS.07) |
| Localización de datos en EEE | Obligación contractual | ANEXO I 2026 03393.pdf, p. 25 (PS.01) |
| Transferencias internacionales solo con autorización expresa | Obligación contractual | ANEXO I 2026 03393.pdf, p. 25 (PS.01) |
| Cloud público: integración con CNAPP de Renfe si se solicita | Obligación contractual | ANEXO I 2026 03393.pdf, p. 36 (CD.05) |

# 5. Medidas técnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente
| Medida | Tipo | Parámetro/Plazo | Fuente |
|---|---|---|---|
| Cifrado en tránsito, uso y almacenamiento | Obligatoria | Protocolos seguros (https, TLS v1.2+), datos confidenciales cifrados | ANEXO I 2026 03393.pdf, p. 29-30 (SD.03) |
| Custodia de claves en HSM | Obligatoria salvo impedimento técnico autorizado | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 30 (SD.03.04) |
| Control de accesos, RBAC, mínimo privilegio | Obligatoria | Gestión de perfiles, mínimo privilegio | ANEXO I 2026 03393.pdf, p. 31-32 (GI.07) |
| MFA/2FA para servicios expuestos a Internet | Obligatoria | Cuando aplique | ANEXO I 2026 03393.pdf, p. 35 (CD.03.11) |
| Integración con identidad corporativa RENFE (SSO, SAML2, ADFS) | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 24, 32 (GI.05.01) |
| Prohibición de usuarios genéricos | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 32 (GI.06) |
| DLP para datos personales y tarjetas de pago | Obligatoria | Descubrimiento cada 3 meses | ANEXO I 2026 03393.pdf, p. 29 (SD.01.03) |
| Backups, restauración y pruebas | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 29, 38 (SD.01.04, DS.01.03) |
| Segmentación de red | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 29 (CN.03) |
| Administración remota segura, VPN | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 33 (GI.10) |
| WAF, IDS/IPS, antimalware, defensa perimetral | Obligatoria según naturaleza del servicio | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 34-35 (CD.03) |
| SIEM, logs normalizados, entrega a SIEM RENFE | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 36 (CD.06) |
| Monitorización 24x7, SOC | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 36 (CD.07) |
| Detección y remediación de vulnerabilidades | Obligatoria | Escaneos periódicos, plazos según criticidad RENFE | ANEXO I 2026 03393.pdf, p. 35 (CD.04.01-03) |
| Parcheo regular y seguro | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 29, 35 (CN.03, CD.04) |
| Inventario de activos y software | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 29, 33 (CN.03, SE.03) |
| Protección de bases de datos (cifrado, ofuscación, pseudoanonimización) | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 30 (SD.04) |
| Guías CCN-CERT para bases de datos | Obligatoria según tecnología | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 30 (SD.04.02) |
| WAF para servicios web | Obligatoria si aplica | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 35 (CD.03.04) |
| DLP si hay datos personales/confidenciales | Obligatoria si aplica | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 35 (CD.03.06) |
| Proxys, CASB, CWPP, según arquitectura | Obligatoria si aplica | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 35 (CD.03.05-09) |
| Protección correo (antimalware, antispam, reputación) | Obligatoria si aplica | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 35 (CD.03.10) |
| Pruebas de restauración de backup | Obligatoria | Durante la ejecución | ANEXO I 2026 03393.pdf, p. 38 (DS.01.03) |

# 6. Identidad, accesos y privilegios
- Autenticación segura, perfiles y trazabilidad de accesos (ANEXO I 2026 03393.pdf, p. 15, 31-32).
- Integración con sistema de identidad corporativo RENFE, SSO, federación SAML2/ADFS (ANEXO I 2026 03393.pdf, p. 24, 32).
- Prohibición de usuarios genéricos, detección de su uso (ANEXO I 2026 03393.pdf, p. 32).
- Gestión de accesos privilegiados, controles, trazabilidad, escalado, acceso seguro local y remoto, VPN (ANEXO I 2026 03393.pdf, p. 33).
- Registro de intentos de autenticación, IP, usuario, información de negocio (ANEXO I 2026 03393.pdf, p. 32).
- Gestión de perfiles, mínimo privilegio, documentación de modelos de autorización (ANEXO I 2026 03393.pdf, p. 31-32).

# 7. Vulnerabilidades, parcheado y desarrollo seguro
- Estrategia y plan de no obsolescencia, gestión de vulnerabilidades, identificación, remediación, SLA (ANEXO I 2026 03393.pdf, p. 23, 26, 35).
- Parcheo regular y seguro de productos, configuración segura, mantenimiento de documentación técnica (ANEXO I 2026 03393.pdf, p. 29, 35).
- Escaneos de vulnerabilidades periódicos, entrega de informes a RENFE, remediación según criticidad (ANEXO I 2026 03393.pdf, p. 35).
- Pruebas de seguridad (pentesting, hacking ético) solo con autorización previa, resultados a Seguridad RENFE (ANEXO I 2026 03393.pdf, p. 37).
- NO CONSTA EN LA DOCUMENTACION REVISADA: requisitos específicos de SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD, SBOM.

# 8. Incidentes, brechas y plazos de notificación expresamente indicados
- Notificación de incidentes de seguridad con impacto Medio, Alto, Muy Alto y Crítico a CERT RENFE (notificaciones.pocterceros.ciberseguridad@renfe.es) (ANEXO I 2026 03393.pdf, p. 36-37).
- Comunicación inmediata tras identificación como posible incidente (ANEXO I 2026 03393.pdf, p. 36-37).
- Colaboración en valoración, remediación, documentación y notificación del incidente (ANEXO I 2026 03393.pdf, p. 36-37).
- Prohibición de destrucción de pruebas, preservación durante triage y recuperación (ANEXO I 2026 03393.pdf, p. 36-37).
- Confidencialidad en actuaciones derivadas de la gestión del incidente (ANEXO I 2026 03393.pdf, p. 36-37).
- NO CONSTA EN LA DOCUMENTACION REVISADA: plazo máximo en horas/días para notificación inicial salvo lo indicado para el POC de seguridad (penalización por no respuesta en 48h, ver PCP 2026 03993.pdf, p. 31).

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retención
- Logging: registro, auditoría y trazabilidad de eventos, operaciones, acciones y actividades (ANEXO I 2026 03393.pdf, p. 27, 36).
- Logs entregados al SIEM de RENFE o API para captura, custodia por periodo de retención especificado por RENFE (ANEXO I 2026 03393.pdf, p. 36).
- Monitorización 24x7, SOC (ANEXO I 2026 03393.pdf, p. 36).
- Copias de seguridad, restauración, pruebas, retención según indique RENFE (ANEXO I 2026 03393.pdf, p. 29, 38).
- Planes de contingencia, crisis, continuidad de negocio, salida programada y sobrevenida, devolución y destrucción segura de información (ANEXO I 2026 03393.pdf, p. 38-39).
- Certificado de destrucción tras borrado (ANEXO I 2026 03393.pdf, p. 28).
- NO CONSTA EN LA DOCUMENTACION REVISADA: valores numéricos de RTO/RPO.

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Derecho de auditoría por RENFE y terceros designados, acceso completo a locales, sistemas, redes y datos (ANEXO I 2026 03393.pdf, p. 37-38).
- Colaboración en auditorías externas, bi-anuales, extraordinarias, sectoriales, regulatorias (ANEXO I 2026 03393.pdf, p. 37-38).
- Certificación ENS nivel Medio obligatoria, ISO 27001 obligatoria (PCP 2026 03993.pdf, p. 20; ANEXO I 2026 03393.pdf, p. 25-28).
- Formación, concienciación y capacitación del personal en seguridad y legislación aplicable (ANEXO I 2026 03393.pdf, p. 27, 39).
- Acuerdo de confidencialidad firmado por personal propio y subcontratado (ANEXO I 2026 03393.pdf, p. 27, 39).
- Procedimiento seguro de borrado y destrucción conforme ENS, certificado de destrucción (ANEXO I 2026 03393.pdf, p. 28).
- Devolución o destrucción de datos a elección de RENFE al finalizar el servicio (ANEXO I 2026 03393.pdf, p. 28, 39).

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Penalización hasta el 10% del contrato por no entrega de documentación de ciberseguridad (PCP 2026 03993.pdf, p. 31).
- Penalización de 1000-3000€ por demora en completar el cuestionario de evaluación de seguridad de la cadena de suministro (PCP 2026 03993.pdf, p. 31).
- Penalización hasta el 10% del contrato por falta de certificación ENS nivel exigido (PCP 2026 03993.pdf, p. 31).
- Penalización de 1000€/mes por no notificar el POC de Seguridad, y 1000€/24h por falta de respuesta (PCP 2026 03993.pdf, p. 31).
- Penalización hasta el 20% del contrato por incumplimiento de obligaciones de confidencialidad, protección de datos y propiedad intelectual (PCP 2026 03993.pdf, p. 30).
- Resolución del contrato por incumplimiento de SP.01, PS.07, CN.01 o entrega de documentación de ciberseguridad (PCP 2026 03993.pdf, p. 33).

# 12. Datos no localizados o ambiguos, sin recomendaciones
- NO CONSTA EN LA DOCUMENTACION REVISADA: requisitos específicos de SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD, SBOM.
- NO CONSTA EN LA DOCUMENTACION REVISADA: valores numéricos de RTO/RPO.
- NO CONSTA EN LA DOCUMENTACION REVISADA: categorías concretas de datos personales, interesados o finalidades específicas del tratamiento.
- NO CONSTA EN LA DOCUMENTACION REVISADA: plazos de retención de logs o datos salvo referencia a lo que indique RENFE.

# 13. Documentos revisados
1. PCP 2026 03993.pdf (Pliego administrativo)
2. ANEXO I 2026 03393 .pdf (Pliego técnico)
3. ANEXO III 2026 03993.pdf (Modelo oferta económica)
4. ANEXO II 2026 03993.pdf (Modelo declaración responsable)
5. ANEXO IV 2026 03993.pdf (Modelo garantía definitiva)
6. poc (Plataforma de Contratación del Sector Público, perfil RENFE)
7. poc (Plataforma de Contratación del Sector Público, perfil RENFE)
8. poc (Plataforma de Contratación del Sector Público, perfil RENFE)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Certificación ENS nivel Medio | Obligación contractual | Certificado ENS nivel Medio, antes del inicio o en 10 meses | ANEXO I 2026 03393.pdf | p. 25-28 (CN.01) | TEXTO EXTRAIDO |
| ISO 27001 | Obligación contractual | Certificado ISO 27001 | PCP 2026 03993.pdf | p. 20 | TEXTO EXTRAIDO |
| Declaración responsable cumplimiento ENS | Requisito de admisión | Declaración responsable en Sobre A | ANEXO II 2026 03993.pdf | p. 2 | TEXTO EXTRAIDO |
| Análisis de riesgos MAGERIT | Obligación contractual | Análisis de riesgos compartido con RENFE | ANEXO I 2026 03393.pdf | p. 23, 25-26 (PS.04) | TEXTO EXTRAIDO |
| Subencargados solo con autorización | Obligación contractual | Autorización previa escrita de RENFE | PCP 2026 03993.pdf, ANEXO I 2026 03393.pdf | p. 25-28, 26 (PS.07) | TEXTO EXTRAIDO |
| Localización de datos en EEE | Obligación contractual | Solo EEE salvo autorización expresa | ANEXO I 2026 03393.pdf | p. 25 (PS.01) | TEXTO EXTRAIDO |
| Cifrado en tránsito, uso y almacenamiento | Obligación contractual | Protocolos seguros, datos confidenciales cifrados | ANEXO I 2026 03393.pdf | p. 29-30 (SD.03) | TEXTO EXTRAIDO |
| DLP para datos personales | Obligación contractual | Descubrimiento cada 3 meses | ANEXO I 2026 03393.pdf | p. 29 (SD.01.03) | TEXTO EXTRAIDO |
| Integración con identidad corporativa RENFE | Obligación contractual | SSO, SAML2, ADFS | ANEXO I 2026 03393.pdf | p. 24, 32 (GI.05.01) | TEXTO EXTRAIDO |
| Prohibición de usuarios genéricos | Obligación contractual | Detección y prohibición | ANEXO I 2026 03393.pdf | p. 32 (GI.06) | TEXTO EXTRAIDO |
| Logging y entrega a SIEM RENFE | Obligación contractual | Logs normalizados, entrega a SIEM o API | ANEXO I 2026 03393.pdf | p. 36 (CD.06) | TEXTO EXTRAIDO |
| Monitorización 24x7, SOC | Obligación contractual | Durante la ejecución | ANEXO I 2026 03393.pdf | p. 36 (CD.07) | TEXTO EXTRAIDO |
| Notificación de incidentes a CERT RENFE | Obligación contractual | Impacto Medio/Alto/Muy Alto/Crítico, comunicación inmediata | ANEXO I 2026 03393.pdf | p. 36-37 (CD.08) | TEXTO EXTRAIDO |
| Penalización por incumplimiento ENS | Consecuencia contractual | Hasta 10% del contrato | PCP 2026 03993.pdf | p. 31 | TEXTO EXTRAIDO |
| Resolución por incumplimiento ENS, POC, cadena suministro | Consecuencia contractual | Resolución del contrato | PCP 2026 03993.pdf | p. 33 | TEXTO EXTRAIDO |
| NO CONSTA: SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD, SBOM | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| NO CONSTA: RTO/RPO numéricos | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| NO CONSTA: categorías de datos personales, interesados, finalidades | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| NO CONSTA: plazos de retención de logs/datos | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |

# Discrepancias y pendientes de aclaración
No se han identificado discrepancias en la documentación revisada.