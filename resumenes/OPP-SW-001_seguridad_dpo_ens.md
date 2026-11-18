1. Veredicto ejecutivo Seguridad / DPO / ENS: CUMPLE CON GAPS

La empresa cumple los requisitos esenciales de ENS, RGPD y medidas técnicas para la categoría MEDIA exigida, pero existen algunos gaps y riesgos operativos/coste que deben gestionarse antes de ofertar y durante la ejecución.

2. Los 8 puntos críticos:
- ENS: Se exige ENS categoría MEDIA, certificación previa a producción, cubriendo desarrollo, soporte y cloud. La empresa dispone de certificación ENS MEDIA en el alcance requerido.
- Datos personales y rol: Se tratan datos identificativos, empleados, ciudadanos, correos, IPs, logs y datos económicos. El adjudicatario es ENCARGADO del tratamiento.
- Ubicación/cloud/transferencias: Datos y backups en UE, cloud Azure permitido, no se permiten transferencias internacionales sin autorización. La empresa cumple, pero debe revisar servicios auxiliares y subencargados.
- Medidas técnicas: TLS 1.2+, cifrado en reposo, MFA admins, RBAC, cuentas nominativas, WAF, gestión de vulnerabilidades, backups diarios cifrados, logs 12 meses. Todo disponible, salvo retención >12 meses y SOC 24x7.
- Incidentes/brechas: Notificación incidente/brecha en <=2h, informe inicial 24h. Procedimiento disponible.
- Subencargados/cadena suministro: Cloud Azure, Jira, SAST/SCA, pentest, partners comunicados y autorizables. No se permite subcontratar dirección de proyecto.
- Auditorías/evidencias: Certificados ENS, ISO 27001, informes pentest, derecho de auditoría aceptable. Gap: no ISO 27701/22301.
- Gaps principales: No ENS ALTA, retención logs >12 meses, SOC 24x7, alojamiento exclusivo en España, ISO 27701/22301, EIPD si hay datos sensibles.

3. ENS:
- Categoría exigida: MEDIA.
- Certificación: Obligatoria antes de producción.
- Declaración: No basta, se exige certificación.
- Alcance: Desarrollo, soporte, cloud, APIs, web.
- CCN-STIC: No se citan guías concretas, pero se asume aplicación de guías ENS y CCN-STIC para categoría MEDIA.
- Evidencia: Certificado ENS MEDIA vigente, auditoría 2025 superada.
- Gap: No disponible ENS ALTA ni para sistemas fuera de alcance actual (IoT, mobile nativo, SOC 24x7).

4. RGPD/DPO:
- Datos tratados: Identificativos, empleados, ciudadanos, correos, IPs, logs, datos económicos.
- Finalidad: Tramitación electrónica, gestión de expedientes, pagos, soporte.
- Interesados: Ciudadanos, empleados públicos.
- Rol: Encargado del tratamiento.
- Acuerdo encargado: Exigido, modelo disponible.
- EIPD: No exigida salvo datos sensibles.
- DPO/DPD: Exigido, disponible (Laura Castillo).
- Conservación: No detallada, pero logs 12 meses mínimo.
- Acciones: Firmar acuerdo, revisar subencargados, asegurar reversibilidad y borrado.

5. Subcontratación, subencargados, cloud y cadena de suministro:
- Cadena: Cliente -> Adjudicatario -> Cloud Azure/Jira/SAST/Pentest/Partners.
- Accesos: Cloud y SaaS gestionan datos, logs y credenciales técnicas. Subencargados deben ser comunicados y autorizados.
- No se permite subcontratar dirección de proyecto.

6. Localización y transferencias internacionales:
- Ubicación: UE obligatoria para datos y backups.
- Regiones: Azure UE permitido.
- Backups: En UE, cifrados.
- Soporte remoto: Permitido, sin transferencias internacionales.
- Telemetría/IA/SaaS: Revisar que no impliquen transferencias fuera UE.
- Riesgos: Servicios auxiliares, soporte fabricante, telemetría cloud.

7. Medidas técnicas de seguridad:
| Medida                | Tipo         | Obligatoria | Pliego | Capacidad actual | Gap | Riesgo | Acción |
|-----------------------|--------------|-------------|--------|------------------|-----|--------|--------|
| TLS 1.2+              | Técnica      | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| Cifrado en reposo     | Técnica      | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| MFA admins            | Técnica      | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| RBAC                  | Técnica      | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| Cuentas nominativas   | Técnica      | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| WAF                   | Técnica      | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| Gestión vulnerabilidades| Técnica     | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| Backups diarios cifrados| Técnica    | Sí          | Sí     | Sí               | No  | Bajo   | Ninguna|
| Logs 12 meses         | Técnica      | Sí          | Sí     | Sí (base)        | No  | Bajo   | Ninguna|
| Retención >12 meses   | Técnica      | No          | No     | Parcial          | Sí  | Medio  | Presupuestar si se exige|
| SIEM/SOC 24x7         | Técnica      | No          | No     | Parcial          | Sí  | Medio  | Partner si se exige|

8. Identidad, accesos y privilegios:
- MFA: Obligatorio admins, disponible.
- SSO: Disponible con Entra ID/SAML/OIDC.
- Directorio: Disponible.
- Cuentas nominativas: Sí.
- PAM: Parcial, para cuentas críticas.
- RBAC: Sí.
- Mínimo privilegio: Política implantada.
- Altas/bajas: Procedimiento disponible.
- Revisiones: Disponibles.
- Acceso remoto: VPN disponible.

9. Vulnerabilidades, parcheado y desarrollo seguro:
- SAST/SCA: Obligatorio, disponible.
- DAST: Disponible bajo demanda.
- SBOM: Exigido, disponible en proyectos nuevos.
- Pentesting: Obligatorio previo a producción, disponible.
- CVE/EOL/EOS: Gestión disponible.
- Plazo parcheado: <=48h crítico, disponible.
- CI/CD: Implantado.
- Secretos: Gestión disponible.
- OWASP: Aplicado.

10. Incidentes de seguridad y brechas de datos:
- Incidente seguridad: Notificación al cliente <=2h.
- Brecha RGPD: Notificación DPO cliente <=2h, informe inicial 24h.
- Relación 72h AEPD: El responsable (cliente) debe notificar, el encargado colabora.

11. Logging, SOC/SIEM, monitorización y retención:
- Logs: Accesos, eventos críticos, retención 12 meses.
- Integridad: Disponible con almacenamiento inmutable si se presupuesta.
- Sincronización horaria: NTP disponible.
- SIEM: Integración disponible, SOC 24x7 solo con partner.
- Alertas: Disponibles.
- Coste/riesgo: Retención >12 meses y SOC 24x7 implican coste extra.

12. Continuidad, backup, borrado y reversibilidad segura:
- RTO/RPO: No exigidos explícitamente, pero backups diarios y restauración disponible.
- Copias inmutables/offline: Disponibles si se presupuesta.
- Borrado datos/backups: Disponible, certificado destrucción lógica.
- Revocación accesos: Disponible.

13. Seguridad del personal, confidencialidad y auditorías:
- NDA: Exigido, disponible.
- Formación ENS/RGPD/ciber: Disponible.
- Roles seguridad: Javier Prieto (ciber), Laura Castillo (DPO).
- Auditorías: ENS, ISO 27001, pentest, derecho auditoría aceptable.
- Evidencias: Certificados, informes, políticas.

14. Matriz de cumplimiento Seguridad / DPO / ENS:
(Se adjunta tabla en documento completo)

15. Costes o esfuerzos adicionales previsibles:
- Certificación ENS MEDIA: Ya disponible.
- SOC 24x7: Coste extra si se exige.
- Retención logs >12 meses: Coste extra.
- Auditoría ENS: Incluida en ciclo actual.
- EIPD: Solo si hay datos sensibles.
- Cloud Azure: Presupuestado.
- Licencias SAST/SCA/Jira: Presupuestadas.

16. Riesgos de incumplimiento contractual:
- No disponer de ENS ALTA si se eleva la categoría.
- Transferencias internacionales no autorizadas por servicios auxiliares.
- Incumplimiento de plazos de notificación de incidentes/brechas.
- Falta de evidencia de borrado/backups.
- No comunicar subencargados o cambios en la cadena de suministro.

17. Plan de acción recomendado:
- Antes de ofertar: Revisar subencargados, confirmar regiones cloud, validar que no hay transferencias internacionales, preparar evidencias ENS/RGPD.
- Antes de adjudicación: Firmar acuerdo encargado, comunicar subencargados, validar arquitectura cloud y backups.
- Durante ejecución: Monitorizar cumplimiento ENS, RGPD, medidas técnicas, mantener evidencias y reporting, gestionar incidentes y brechas según procedimiento.

18. Preguntas al órgano de contratación:
- ¿Se prevé algún tratamiento de datos sensibles (salud, biométricos, menores)?
- ¿Se exige alojamiento exclusivo en España o basta con UE?
- ¿Qué servicios cloud/SaaS del cliente pueden implicar transferencias internacionales (soporte, telemetría, IA)?
- ¿Se exige retención de logs superior a 12 meses?
- ¿Se requiere SOC 24x7 o solo SIEM integrado?
- ¿Qué periodicidad de auditoría ENS se exige?
- ¿Se exige EIPD para algún tratamiento?
- ¿Qué subencargados cloud/SaaS están autorizados?
- ¿Qué procedimiento de reversibilidad y borrado de backups se exige?

19. Documentos revisados:
1. Pliego administrativo OPP-SW-001 portal ciudadano
2. Pliego técnico OPP-SW-001 portal ciudadano
3. Anexo solvencia OPP-SW-001 portal ciudadano