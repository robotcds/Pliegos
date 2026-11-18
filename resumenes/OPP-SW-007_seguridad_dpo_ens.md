1. Veredicto ejecutivo Seguridad / DPO / ENS: CUMPLE CON GAPS

2. Los 8 puntos críticos:
- ENS: Exige ENS categoría MEDIA e ISO 27001 vigentes antes de oferta. No se exige ENS ALTA. Alcance: auditoría, pentesting y securización de aplicaciones web y APIs. Gap: sólo un pentester senior interno, se requieren dos.
- Datos personales y rol: Se tratan datos identificativos, logs, credenciales temporales, IPs y evidencias técnicas. Rol: No se explicita, pero por objeto y medidas, el adjudicatario actúa como encargado de tratamiento.
- Ubicación/cloud/transferencias: Evidencias y datos deben almacenarse cifrados en la UE. Prohibido extraer evidencias fuera de UE. Gap: Validar que todas las herramientas SaaS cumplen.
- Medidas técnicas: MFA, cifrado extremo a extremo, segregación de funciones, control de accesos, borrado seguro, registro de actividad, retención 24 meses. Gap: Custodia cifrada 24 meses y borrado seguro de credenciales temporales.
- Incidentes/brechas: Comunicación de hallazgo crítico <= 1 hora, informe inicial <= 8 horas, brecha de datos personales comunicación inmediata al DPO cliente. Gap: Procedimiento interno cumple, pero requiere refuerzo para notificación urgente.
- Subencargados/cadena de suministro: Prohibida subcontratación de pentesting. Herramientas SaaS sólo si aprobadas y sin extracción fuera UE. Gap: Validar cadena de suministro SaaS.
- Auditorías/evidencias: Cliente puede auditar metodología, controles, CVs, certificaciones y trazabilidad de accesos. Gap: Ninguno relevante.
- Gaps principales: Segundo pentester senior, validación SaaS, refuerzo notificación incidentes, custodia cifrada 24 meses.

3. ENS:
- Categoría exigida: MEDIA.
- Certificación: Obligatoria, vigente antes de oferta.
- Declaración: No se admite, sólo certificación.
- Alcance: Auditoría, pentesting, securización de aplicaciones web y APIs.
- Guías CCN-STIC: No se citan, pero se asume aplicación de guías de auditoría, pentesting y custodia de evidencias.
- Evidencia: Certificado ENS media vigente, referencias de proyectos ENS media.
- Gap: Ninguno en certificación, sólo en personal (segundo pentester senior).

4. RGPD/DPO:
- Datos tratados: Identificativos, logs, credenciales temporales, IPs, evidencias técnicas.
- Finalidad: Auditoría, pentesting, custodia de evidencias y remediación.
- Interesados: Empleados, usuarios de aplicaciones auditadas, técnicos.
- Rol: Encargado del tratamiento (no explícito, pero deducible por objeto y medidas).
- Acuerdo de encargado: No se adjunta modelo, pero es obligatorio. Instrucciones, medidas, devolución/borrado, subencargados, auditoría.
- EIPD: No exigido, pero recomendable si se detectan datos sensibles.
- DPO/DPD: Comunicación inmediata en caso de brecha.
- Conservación: Evidencias 24 meses salvo instrucción contraria.
- Acciones: Confirmar acuerdo de encargado y procedimiento de brechas.

5. Subcontratación, subencargados, cloud y cadena de suministro:
- Cadena: Cliente -> Adjudicatario (no puede subcontratar pentesting) -> Herramientas SaaS (sólo si aprobadas, sin extracción fuera UE).
- Accesos: Equipo propio, acceso a sistemas, logs, credenciales temporales. SaaS sólo para análisis, nunca para custodia de evidencias.

6. Localización y transferencias internacionales:
- Ubicación: UE obligatoria para evidencias y datos.
- Regiones: UE, no se exige España exclusiva.
- Backups: No detallados, pero se asume en UE.
- Soporte remoto: Permitido si cumple ubicación.
- Telemetría/IA/SaaS: Prohibido extraer evidencias fuera UE. Validar telemetría y logs de herramientas.
- Riesgos: Uso de SaaS no validado, soporte de fabricantes fuera UE.

7. Medidas técnicas de seguridad:
| Medida                        | Tipo         | Obligatoria | Evidencia pliego | Capacidad actual | Gap | Riesgo | Acción |
|-------------------------------|--------------|-------------|------------------|------------------|-----|--------|--------|
| MFA                           | Técnica      | Sí          | Sí               | Sí               | No  | Bajo   | Ninguna|
| Cifrado extremo a extremo     | Técnica      | Sí          | Sí               | Sí               | No  | Bajo   | Ninguna|
| Segregación de funciones      | Técnica      | Sí          | Sí               | Sí               | No  | Bajo   | Ninguna|
| Control de accesos            | Técnica      | Sí          | Sí               | Sí               | No  | Bajo   | Ninguna|
| Borrado seguro credenciales   | Técnica      | Sí          | Sí               | Sí               | No  | Bajo   | Ninguna|
| Registro de actividad         | Técnica      | Sí          | Sí               | Sí               | No  | Bajo   | Ninguna|
| Custodia cifrada 24 meses     | Técnica      | Sí          | Sí               | Parcial          | Sí  | Medio  | Presupuestar almacenamiento seguro 24 meses|
| Herramientas SaaS UE          | Técnica      | Sí          | Sí               | Parcial          | Sí  | Medio  | Validar SaaS y ubicación|

8. Identidad, accesos y privilegios:
- MFA: Obligatorio para acceso a evidencias y sistemas.
- SSO: No exigido, pero recomendable.
- Directorio: No detallado.
- Cuentas nominativas: Implícito por control de accesos y trazabilidad.
- PAM: No exigido.
- RBAC: Recomendado.
- Mínimo privilegio: Sí, por "necesidad de conocer".
- Altas/bajas: No detallado.
- Revisiones: No detallado.
- Acceso remoto: Permitido si cumple medidas y ubicación.

9. Vulnerabilidades, parcheado y desarrollo seguro:
- SAST/DAST/SCA: No exigidos, pero valorables en metodología.
- SBOM: No exigido.
- Pentesting: Obligatorio, metodología OWASP.
- CVE/EOL/EOS: No detallado.
- Plazos de parcheado: No detallado, pero retest crítico <= 5 días.
- CI/CD, secretos, OWASP: No exigidos, pero recomendables.

10. Incidentes de seguridad y brechas de datos:
- Incidente de seguridad: Hallazgo crítico, comunicación <= 1 hora, informe inicial <= 8 horas.
- Brecha RGPD: Comunicación inmediata al DPO cliente. No se detalla plazo AEPD (72h), pero es responsabilidad del cliente.

11. Logging, SOC/SIEM, monitorización y retención:
- Logs: Registro de actividad obligatorio.
- Integridad: No detallada, pero se asume por custodia cifrada.
- Sincronización horaria: No detallada.
- Retención: 24 meses para evidencias.
- SIEM/SOC: No exigido.
- Alertas: No detalladas.
- Coste/riesgo: Custodia cifrada 24 meses puede requerir almacenamiento dedicado.

12. Continuidad, backup, borrado y reversibilidad segura:
- RTO/RPO: No detallados.
- Backups: No detallados, pero se asume en UE.
- Copias inmutables/offline: No detalladas.
- Restauración: No detallada.
- Borrado de datos/backups: Borrado seguro de credenciales temporales obligatorio.
- Certificados de destrucción: No detallados, pero recomendables.
- Revocación de accesos: Implícito en reversibilidad.

13. Seguridad del personal, confidencialidad y auditorías:
- NDA: Obligatorio.
- Formación ENS/RGPD/ciber: No detallada, pero recomendable.
- Roles de seguridad: Responsable de seguridad, pentesters, auditor.
- Auditorías: Cliente puede auditar controles, CVs, certificaciones y trazabilidad.
- Evidencias: Custodia cifrada, informes, matriz de riesgos.
- Certificaciones: ENS media, ISO 27001, valorable ISO 20000, Lead Auditor, CEH.
- Derecho de auditoría: Sí.

14. Matriz de cumplimiento Seguridad / DPO / ENS:
(Ver tabla en punto 7 y resumen de gaps: segundo pentester, validación SaaS, custodia cifrada 24 meses, refuerzo notificación incidentes.)

15. Costes o esfuerzos adicionales previsibles:
- Contratación/refuerzo de segundo pentester senior.
- Validación y posible cambio de herramientas SaaS para custodia de evidencias.
- Almacenamiento cifrado seguro 24 meses.
- Refuerzo de procedimiento de notificación urgente de incidentes.

16. Riesgos de incumplimiento contractual:
- Exclusión por falta de segundo pentester senior.
- Penalización grave por filtración de evidencias o incumplimiento de confidencialidad.
- Incumplimiento ENS media o ISO 27001 vigente.
- Uso de SaaS que extraiga datos fuera de UE.
- No notificar incidentes críticos en plazo.

17. Plan de acción recomendado:
- Antes de ofertar: Identificar y contratar segundo pentester senior, validar herramientas SaaS, planificar almacenamiento cifrado 24 meses, revisar procedimiento de notificación urgente.
- Antes de adjudicación: Confirmar acuerdo de encargado, validar cadena de suministro SaaS, preparar evidencias de certificaciones y CVs.
- Durante ejecución: Cumplir plazos de notificación, mantener custodia cifrada, documentar accesos y evidencias, preparar para auditoría del cliente.

18. Preguntas al órgano de contratación:
- ¿Se admite declaración de conformidad ENS media o sólo certificación?
- ¿Qué datos personales pueden aparecer en evidencias? ¿Se requiere EIPD?
- ¿Modelo de acuerdo de encargado disponible?
- ¿Se permite uso de herramientas SaaS para análisis si no custodian evidencias?
- ¿Ubicación de backups y logs? ¿Se exige España o basta UE?
- ¿Se exige logging inmutable o sólo cifrado?
- ¿Plazo máximo de notificación de brecha RGPD al cliente?
- ¿Se permite soporte remoto desde fuera de España si es UE?
- ¿Requiere formación/certificación específica del personal?

19. Documentos revisados:
- Pliego administrativo OPP-SW-007 ciberseguridad
- Pliego técnico OPP-SW-007 ciberseguridad
- Anexo solvencia OPP-SW-007 ciberseguridad