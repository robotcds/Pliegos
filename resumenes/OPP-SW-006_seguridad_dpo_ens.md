1. Veredicto ejecutivo Seguridad / DPO / ENS: CUMPLE CON GAPS

2. Los 8 puntos críticos:
- ENS: Exigido ENS MEDIA para backend, APIs y panel gestor. Apps mobile deben aplicar medidas equivalentes. Se requiere certificación, no solo declaración. Gap: la certificación interna ENS media no cubre mobile nativo ni panel gestor específico.
- Datos personales y rol: Se tratan datos identificativos, fotografías, geolocalización, IP, identificadores de dispositivo y notificaciones push. Rol: encargado del tratamiento. Acuerdo de encargado obligatorio.
- Ubicación/cloud/transferencias: Almacenamiento y crash reporting en UE. Prohibidas transferencias internacionales salvo autorización. Gap: validar servicios push/crash reporting y subencargados cloud.
- Medidas técnicas: TLS, pinning valorable, cifrado local, minimización geolocalización, MFA, RBAC, logs 12 meses, gestión segura certificados push, almacenamiento fotos en UE. Gap: pinning, cifrado local mobile, logs mobile, gestión certificados push.
- Incidentes/brechas: Comunicación al cliente ≤2h, alto impacto si afecta fotos/geolocalización. Borrado seguro y revocación cuentas store. Gap: proceso mobile específico y evidencias de borrado/retorno.
- Subencargados/cadena suministro: Apple, Google, servicio push, crash reporting, cloud. Cadena: Cliente → Adjudicatario → Mobile Studio/Pentest Lab/Azure/Apple/Google. Gap: declaración y control de subencargados, validación UE.
- Auditorías/evidencias: ENS media, ISO 27001, pentest mobile y backend, logs, acuerdos de encargado, NDA. Gap: evidencias mobile nativo y panel gestor.
- Gaps principales: ENS media no cubre mobile nativo, subencargados no validados UE, logs mobile, cifrado local, pinning, proceso incidentes mobile, borrado seguro mobile, evidencias específicas mobile.

3. ENS:
- Categoría exigida: MEDIA (backend, APIs, panel gestor). Apps mobile: medidas equivalentes.
- Certificación/declaración: Certificación ENS media exigida, no solo declaración. Apps mobile: equivalencia, no certificación formal.
- Momento acreditación: Antes de inicio de servicio.
- Alcance: Backend, APIs, panel gestor. Apps mobile fuera de alcance formal ENS, pero deben aplicar medidas equivalentes.
- Guías CCN-STIC: No citadas explícitamente, pero aplican por ENS media.
- Evidencia: Certificado ENS media (desarrollo web/cloud), autoevaluación básica. Gap: mobile nativo y panel gestor no cubiertos.

4. RGPD/DPO:
- Datos tratados: Identificativos, fotos, geolocalización, IP, identificadores dispositivo, notificaciones push.
- Finalidad: Gestión de incidencias ciudadanas.
- Interesados: Ciudadanos, gestores municipales.
- Rol adjudicatario: Encargado del tratamiento.
- Acuerdo encargado: Obligatorio, con instrucciones, categorías, subencargados, conservación, borrado.
- EIPD: No exigida, pero recomendable si se amplía a datos sensibles o perfilado.
- DPO/DPD: Obligatorio, debe figurar en acuerdo.
- Conservación: No detallada, aplicar principio de minimización y borrado seguro al finalizar.
- Acciones: Firmar acuerdo, validar subencargados, definir conservación y borrado.

5. Subcontratación, subencargados, cloud y cadena de suministro:
- Cadena: Cliente → Adjudicatario (Sermicro) → Mobile Studio Ficticio (desarrollo mobile) → Azure (cloud backend) → Apple/Google (stores) → Crash reporting/push (UE).
- Accesos: Mobile Studio accede a código y datos mobile; Azure a backend y datos; Apple/Google a stores y metadatos; crash reporting/push a logs y notificaciones.
- Gap: Declaración y control de subencargados, validación UE, acuerdos de subencargado.

6. Localización y transferencias internacionales:
- Ubicación obligatoria: UE para datos, crash reporting, push, fotos.
- Regiones permitidas: UE. España preferible, no obligatoria.
- Backups: No detallados, deben estar en UE.
- Soporte remoto: Permitido, sin transferencias internacionales.
- Telemetría/IA/SaaS: Deben validarse y declararse.
- Riesgos: Crash reporting/push fuera UE, soporte Apple/Google, telemetría no controlada.

7. Medidas técnicas de seguridad:
| Medida                        | Tipo         | Obligatoria | Evidencia pliego | Capacidad actual | Gap | Riesgo | Acción |
|-------------------------------|--------------|-------------|------------------|------------------|-----|--------|--------|
| TLS                           | Obligatoria  | Sí          | Sí               | Sí               | No  | Bajo   | Cumple |
| Pinning certificado           | Valorable    | No          | Sí               | Parcial          | Sí  | Medio  | Evaluar |
| Cifrado local mobile          | Obligatoria  | Sí          | Parcial          | Sí/No            | Sí  | Medio  | Implementar |
| Minimización geolocalización  | Obligatoria  | Sí          | Parcial          | Sí               | No  | Bajo   | Cumple |
| MFA gestores                  | Obligatoria  | Sí          | Sí               | Sí               | No  | Bajo   | Cumple |
| RBAC                          | Obligatoria  | Sí          | Sí               | Sí               | No  | Bajo   | Cumple |
| Logs administración 12 meses  | Obligatoria  | Sí          | Sí               | Sí               | No  | Bajo   | Cumple |
| Gestión certificados push     | Obligatoria  | Sí          | Parcial          | Parcial          | Sí  | Medio  | Mejorar |
| Almacenamiento fotos UE       | Obligatoria  | Sí          | Sí               | Sí               | No  | Bajo   | Cumple |
| Pentest mobile/backend        | Obligatoria  | Sí          | Sí               | Sí               | No  | Bajo   | Cumple |

8. Identidad, accesos y privilegios:
- MFA: Obligatorio para gestores, disponible.
- SSO: Disponible con Entra ID/SAML/OIDC.
- Directorio: Disponible.
- Cuentas nominativas: Sí.
- PAM: Parcial, para cuentas críticas.
- RBAC: Sí.
- Mínimo privilegio: Sí.
- Altas/bajas: Sí.
- Revisiones: Sí.
- Acceso remoto: Sí, controlado.

9. Vulnerabilidades, parcheado y desarrollo seguro:
- SAST/SCA: Obligatorio, disponible.
- DAST: Recomendado, disponible bajo demanda.
- SBOM: Disponible en proyectos nuevos.
- Pentesting: Obligatorio antes de publicación, disponible.
- CVE/EOL/EOS: No detallado, pero aplicable.
- Plazos parcheado: Críticas ≤48h.
- CI/CD: Sí.
- Secretos: Sí.
- OWASP MASVS: Recomendado, aplicar.

10. Incidentes de seguridad y brechas de datos:
- Incidente seguridad: Cualquier evento que afecte confidencialidad, integridad o disponibilidad.
- Brecha RGPD: Acceso no autorizado a datos personales.
- Plazos notificación: Cliente ≤2h; AEPD ≤72h (responsable).
- Proceso: Clasificación, escalado, RCA, plan remediación, registro, borrado seguro, revocación accesos.

11. Logging, SOC/SIEM, monitorización y retención:
- Logs administración: 12 meses.
- Integridad: Disponible, inmutable si se presupuesta.
- Sincronización horaria: NTP corporativo.
- SIEM/SOC: Integración disponible, 24x7 solo con partner.
- Alertas: Sí.
- Coste/riesgo: Retención >12 meses y SOC 24x7 implican coste extra.

12. Continuidad, backup, borrado y reversibilidad segura:
- RTO/RPO: No detallados, aplicar mejores prácticas.
- Backups: Diarios, cifrados, retención configurable, en UE.
- Copias inmutables/offline: Disponibles si se presupuesta.
- Restauración: Sí.
- Borrado datos/backups: Disponible, certificado destrucción lógica.
- Revocación accesos: Sí.

13. Seguridad del personal, confidencialidad y auditorías:
- NDA: Sí, 4 años.
- Formación ENS/RGPD/ciber: Sí.
- Roles seguridad: Responsable de seguridad y DPO disponibles.
- Auditorías: ENS media, ISO 27001, pentest, derecho auditoría cliente.
- Evidencias: Certificados, políticas, informes, acuerdos.

14. Matriz de cumplimiento Seguridad / DPO / ENS: (ver tabla en punto 7 y resumen de gaps)

15. Costes o esfuerzos adicionales previsibles:
- Certificación ENS media para panel gestor y mobile nativo (gap).
- Validación y posible cambio de crash reporting/push a UE.
- Logging mobile y retención 12 meses.
- Pentest mobile y backend.
- Borrado seguro mobile y backups.
- Control y acuerdos de subencargados.
- SOC 24x7 si se exige.

16. Riesgos de incumplimiento contractual:
- No certificación ENS media para mobile/panel gestor.
- Crash reporting/push fuera UE.
- Subencargados no declarados o sin acuerdo.
- Logs mobile insuficientes.
- Incumplimiento plazos notificación incidentes.
- Borrado seguro no evidenciado.
- Falta de evidencias mobile nativo.

17. Plan de acción recomendado:
- Antes de ofertar: Validar subencargados, crash reporting/push UE, compromiso Mobile Studio, plan logs mobile, acuerdo encargado, evidencias ENS media.
- Antes de adjudicación: Firmar acuerdos subencargados, definir logging mobile, plan borrado seguro, evidencias pentest.
- Durante ejecución: Monitorizar cumplimiento ENS, RGPD, logs, incidentes, backups, formación, auditorías.

18. Preguntas al órgano de contratación:
- ¿Se acepta equivalencia ENS media para mobile nativo o se exige certificación formal?
- ¿Qué crash reporting/push cumplen ubicación UE y requisitos ENS/RGPD?
- ¿Se exige logging mobile 12 meses y con qué detalle?
- ¿Qué subencargados cloud/SaaS deben declararse y con qué periodicidad?
- ¿Se requiere EIPD si se amplía a datos sensibles o perfilado?
- ¿Qué evidencias de borrado seguro y reversibilidad se exigen?
- ¿Se aceptan backups en UE fuera de España?

19. Documentos revisados:
- Pliego administrativo OPP-SW-006 app móvil
- Pliego técnico OPP-SW-006 app móvil
- Anexo solvencia OPP-SW-006 app móvil