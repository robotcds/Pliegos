1. Veredicto ejecutivo Seguridad / DPO / ENS: CUMPLE CON GAPS

2. Los 8 puntos críticos:
- ENS: Exige BASICA (declaración) si alojamiento cliente; MEDIA (certificación) si cloud adjudicatario. Capacidad interna: ENS MEDIA certificada, pero solo para ciertos servicios cloud y desarrollo web. Gap: No cubre ENS ALTA ni servicios fuera de alcance actual.
- Datos personales y rol: Se tratan datos identificativos, usuarios gestores, trazas de acceso y datos económicos agregados. No categorías especiales. Rol: Encargado del tratamiento. 
- Ubicación/cloud/transferencias: Datos y backups dentro de UE. No SaaS fuera UE. Cloud permitido si ENS MEDIA. Gap: Validar subservicios cloud y telemetría.
- Medidas técnicas: TLS, RBAC, MFA admins, logs 12 meses, backup diario, restauración mensual, control de secretos, revisión permisos BI. Gap: Retención >12 meses y logs inmutables pueden requerir coste extra.
- Incidentes/brechas: Procedimiento exigido, notificación al cliente, registro de accesos. Gap: Plazos y escalado no detallados en pliego.
- Subencargados/cadena suministro: Cloud/SaaS/partners permitidos si dentro UE y comunicados con 30 días. Gap: Validar subencargados y cadena completa.
- Auditorías/evidencias: No se exige auditoría externa ENS, pero sí declaración/certificación según caso. Gap: Evidencia de alcance real y derecho de auditoría cliente.
- Gaps principales: Validar alcance ENS, subencargados cloud, logs y retención, reversibilidad y borrado, detalle de incidentes y transferencias indirectas.

3. ENS:
- Categoría exigida: BASICA (declaración) si alojamiento cliente; MEDIA (certificación) si cloud adjudicatario.
- Certificación/declaración: Declaración BASICA suficiente en on-premise cliente; certificación MEDIA obligatoria en cloud adjudicatario.
- Momento acreditación: Antes de inicio de servicio.
- Alcance: Sistema BI, ETL, almacenamiento, dashboards, logs y backups.
- Guías CCN-STIC: No citadas explícitamente, pero aplican por referencia ENS.
- Evidencia: Certificado ENS MEDIA vigente para cloud y desarrollo web. Gap: Validar si el entorno concreto está incluido.

4. RGPD/DPO:
- Datos tratados: Identificativos, usuarios gestores, trazas de acceso, datos económicos agregados. No datos especiales.
- Finalidad: Seguimiento de expedientes, soporte, ETL, mantenimiento.
- Interesados: Empleados públicos, usuarios gestores.
- Rol adjudicatario: Encargado del tratamiento.
- Acuerdo encargado: Exigido anexo con instrucciones, registro de accesos, medidas y reversibilidad.
- EIPD: No exigida salvo cambio de alcance.
- DPO/DPD: Exigido, capacidad interna disponible.
- Conservación: Logs 12 meses, backups diarios.
- Acciones: Validar acuerdo, registro de accesos y reversibilidad.

5. Subcontratación, subencargados, cloud y cadena de suministro:
- Cadena: Cliente -> Adjudicatario -> Cloud/SaaS/CPD/Partner (solo UE).
- Accesos: Adjudicatario y subencargados pueden acceder a datos, logs y credenciales bajo control y registro.
- Gap: Validar subencargados, telemetría, soporte y cadena completa.

6. Localización y transferencias internacionales:
- Ubicación: UE obligatoria para datos, backups y SaaS.
- Regiones: Cloud UE permitido si ENS MEDIA.
- Backups: Diarios, en UE.
- Soporte remoto: Permitido si en UE.
- Telemetría/IA: Prohibido fuera UE.
- Riesgos: Subservicios cloud, telemetría oculta, soporte fabricante.

7. Medidas técnicas de seguridad:
| Medida                | Tipo        | Pliego | Capacidad actual | Gap | Riesgo | Acción |
|-----------------------|-------------|--------|------------------|-----|--------|--------|
| TLS                   | Obligatoria | Sí     | Sí               | No  | Bajo   | Ninguna|
| RBAC                  | Obligatoria | Sí     | Sí               | No  | Bajo   | Ninguna|
| MFA admins            | Obligatoria | Sí     | Sí               | No  | Bajo   | Ninguna|
| Logs acceso/cambios   | Obligatoria | Sí     | Sí (12m)         | Retención >12m | Medio | Presupuestar si exige más|
| Backup diario         | Obligatoria | Sí     | Sí               | No  | Bajo   | Ninguna|
| Restauración mensual  | Obligatoria | Sí     | Sí               | No  | Bajo   | Ninguna|
| Control secretos      | Obligatoria | Sí     | Sí               | No  | Bajo   | Ninguna|
| Revisión permisos BI  | Obligatoria | Sí     | Sí               | No  | Bajo   | Ninguna|
| Separación datasets   | Recomendada | Sí     | Sí               | No  | Bajo   | Ninguna|
| Logs inmutables       | Valorable   | No     | Sí (si se presupuesta) | Coste | Bajo   | Valorar|

8. Identidad, accesos y privilegios:
- MFA: Obligatorio admins, disponible.
- SSO: Disponible.
- Directorio: Disponible (Azure Entra ID/SAML).
- Cuentas nominativas: Sí.
- PAM: Parcial, para cuentas críticas.
- RBAC: Sí.
- Mínimo privilegio: Política implantada.
- Altas/bajas: Procedimiento disponible.
- Revisiones: Disponibles.
- Acceso remoto: Permitido bajo control.

9. Vulnerabilidades, parcheado y desarrollo seguro:
- SAST, DAST, SCA, SBOM: Disponibles.
- Pentesting: Disponible.
- CVE/EOL/EOS: Gestión disponible.
- Plazos parcheado: <=48h crítico, <=24h requiere refuerzo.
- CI/CD: Implantado.
- Secretos: Gestión disponible.
- OWASP: Aplicado.

10. Incidentes de seguridad y brechas de datos:
- Incidente seguridad: Procedimiento disponible, escalado y RCA.
- Brecha RGPD: Notificación cliente <=2h, registro, informe inicial 24h, final tras cierre.
- 72h AEPD: Responsable cliente, pero soporte disponible.

11. Logging, SOC/SIEM, monitorización y retención:
- Logs acceso/cambios: Obligatorio, 12 meses.
- Integridad logs: Disponible con almacenamiento inmutable (coste extra).
- Sincronización horaria: NTP disponible.
- SIEM/SOC: Integración disponible, 24x7 solo con partner.
- Alertas: Disponibles.
- Coste/riesgo: Retención >12m y logs inmutables pueden requerir presupuesto.

12. Continuidad, backup, borrado y reversibilidad segura:
- RTO/RPO: No exigidos explícitamente.
- Backups: Diarios, cifrados, retención configurable.
- Restauración: Prueba mensual.
- Borrado datos/backups: Disponible, certificado destrucción lógica.
- Revocación accesos: Disponible.

13. Seguridad del personal, confidencialidad y auditorías:
- NDA: Disponible.
- Formación ENS/RGPD/ciber: Sí.
- Roles seguridad: Javier Prieto.
- Auditorías: Derecho cliente aceptable.
- Evidencias: Certificados, políticas, informes.
- Certificaciones: ENS MEDIA, ISO 27001.

14. Matriz de cumplimiento Seguridad / DPO / ENS:
(Ver tabla en punto 7 y resumen en cada apartado)

15. Costes o esfuerzos adicionales previsibles:
- Certificación ENS MEDIA para entorno concreto si no está incluido.
- Logs inmutables y retención >12 meses.
- SIEM/SOC 24x7 si se exige.
- Validación subencargados y cadena suministro.
- Auditoría ENS si cambia alcance.

16. Riesgos de incumplimiento contractual:
- No inclusión del entorno concreto en ENS MEDIA.
- Subencargados cloud fuera UE o sin comunicación previa.
- Logs o backups fuera de UE.
- Retención logs insuficiente.
- Brecha RGPD no notificada en plazo.
- Falta de evidencia de reversibilidad/borrado.

17. Plan de acción recomendado:
- Antes de ofertar: Validar alcance ENS MEDIA, subencargados cloud, retención logs, reversibilidad y borrado.
- Antes de adjudicación: Solicitar detalle de entorno, confirmar subencargados y cadena suministro.
- Durante ejecución: Mantener evidencias, cumplir plazos notificación, actualizar registro accesos y validar backups.

18. Preguntas al órgano de contratación:
- ¿El entorno cloud concreto está incluido en ENS MEDIA? ¿Se aceptan logs 12 meses o se exige más?
- ¿Se requiere logs inmutables? ¿Qué subencargados cloud/SaaS están permitidos?
- ¿Se exige auditoría ENS externa o basta declaración/certificación?
- ¿Qué procedimiento de reversibilidad y borrado se exige?
- ¿Se permite soporte remoto desde fuera de España pero dentro UE?

19. Documentos revisados:
1. Pliego administrativo OPP-SW-005 BI expedientes
2. Pliego técnico OPP-SW-005 BI expedientes
3. Anexo solvencia OPP-SW-005 BI expedientes