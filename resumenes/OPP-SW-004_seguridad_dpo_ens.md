1. Veredicto ejecutivo Seguridad / DPO / ENS: CUMPLE CON GAPS

2. Los 8 puntos críticos:
- ENS: Se exige ENS BASICA (declaración de conformidad, no certificación). Capacidad interna superior (certificación ENS MEDIA), pero el pliego solo pide BASICA. Gap: No se exige certificación formal, pero sí declaración y medidas mínimas.
- Datos personales y rol: Se accede a datos de empleados, expedientes internos, logs y BBDD legacy. Rol: Encargado del tratamiento. Gap: No se detalla acuerdo de encargado ni categorías exactas de interesados.
- Ubicación/cloud/transferencias: No se permite soporte L2/L3 fuera de la UE. No se exige cloud ni se mencionan transferencias internacionales. Gap: No se detalla ubicación de backups ni servicios auxiliares.
- Medidas técnicas: Exige VPN, cuentas nominativas, MFA, segregación, registro de cambios, trazabilidad BBDD, cifrado de backups y confidencialidad. Gap: No se exige SIEM/SOC ni medidas avanzadas.
- Incidentes/brechas: Notificación de incidentes al cliente <= 4h, brechas RGPD <= 2h. Gap: No se detalla canal ni procedimiento forense.
- Subencargados/cadena de suministro: Subcontratación permitida solo para tareas especializadas, previa autorización. Gap: No se exige acuerdo de subencargado ni detalle de cadena de suministro.
- Auditorías/evidencias: No se exige auditoría ENS ni ISO, pero se valora ISO 27001. Gap: No se exige evidencia formal ni periodicidad.
- Gaps principales: Falta de detalle en acuerdo de encargado, subencargados, ubicación de datos, logging avanzado y reversibilidad.

3. ENS:
- Categoría exigida: BASICA.
- Certificación/declaración: Declaración de conformidad (no certificación formal).
- Momento de acreditación: No especificado, pero debe estar disponible al inicio del servicio.
- Alcance: Servicio de soporte y mantenimiento Java.
- Guías CCN-STIC: No citadas explícitamente.
- Evidencia: Declaración de conformidad ENS BASICA.
- Gap: Capacidad interna superior (ENS MEDIA), pero no se exige ni se puede aportar ENS ALTA.

4. RGPD/DPO:
- Datos tratados: Empleados, expedientes internos, logs, BBDD legacy.
- Finalidad: Soporte y mantenimiento, resolución de incidencias.
- Interesados: Empleados y usuarios internos.
- Rol: Encargado del tratamiento.
- Acuerdo de encargado: No detallado en pliego, pero obligatorio por RGPD.
- EIPD: No exigido.
- DPO/DPD: No exigido, pero recomendable.
- Conservación: Logs y cambios 12 meses.
- Acciones: Proponer acuerdo de encargado y registro de actividades.

5. Subcontratación, subencargados, cloud y cadena de suministro:
- Cadena: Cliente -> Adjudicatario (encargado) -> Subcontratistas (DBA, pruebas rendimiento, previa autorización, solo UE).
- Accesos: Solo tareas especializadas, no soporte principal. Gap: No se detalla acceso a logs ni credenciales.

6. Localización y transferencias internacionales:
- Ubicación: No se permite soporte principal fuera de la UE. No se detalla ubicación de datos ni backups.
- Regiones: No especificadas.
- Backups: Cifrado exigido, ubicación no detallada.
- Soporte remoto: Permitido por VPN.
- Telemetría/IA/SaaS: No mencionados.
- Riesgos: Falta de detalle en servicios auxiliares y backups.

7. Medidas técnicas de seguridad:
| Medida                | Tipo         | Pliego | Capacidad actual | Gap | Riesgo | Acción |
|-----------------------|--------------|--------|------------------|-----|--------|--------|
| VPN                   | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| Cuentas nominativas   | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| MFA                   | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| Segregación funciones | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| Registro de cambios   | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| Trazabilidad BBDD     | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| Cifrado backups       | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| Confidencialidad      | Obligatoria  | Sí     | Sí               | No  | Bajo   | Ninguna|
| SIEM/SOC              | Recomendada  | No     | Parcial          | Sí  | Medio  | Ofertar si se valora|

8. Identidad, accesos y privilegios:
- MFA, cuentas nominativas, VPN, segregación de funciones y registro de accesos exigidos y cubiertos.
- SSO, PAM, RBAC, revisiones: No exigidos, pero disponibles internamente.
- Altas/bajas: No detallado, pero cubierto por procedimientos internos.

9. Vulnerabilidades, parcheado y desarrollo seguro:
- Parcheado crítico <= 5 días (pliego), capacidad interna <= 48h (mejor).
- SAST, DAST, SCA, SBOM, pentesting: No exigidos, pero disponibles internamente.
- EOL/EOS: Registrar como excepción de riesgo.
- Gap: No se exige desarrollo seguro, pero recomendable ofertar.

10. Incidentes de seguridad y brechas de datos:
- Incidente: Notificación al cliente <= 4h.
- Brecha RGPD: Notificación al cliente <= 2h.
- Canal, forense, RCA: No detallados.
- Relación con 72h AEPD: No mencionada, pero responsabilidad del cliente.

11. Logging, SOC/SIEM, monitorización y retención:
- Logs de soporte y cambios retenidos 12 meses.
- Integridad, SIEM/SOC, alertas: No exigidos, pero disponibles internamente.
- Sincronización horaria: No mencionada.
- Gap: No se exige retención superior ni logging avanzado.

12. Continuidad, backup, borrado y reversibilidad segura:
- RTO/RPO: No exigidos.
- Backups cifrados exigidos, ubicación no detallada.
- Borrado/reversibilidad: No detallados, pero disponibles internamente.
- Gap: No se exige certificado de destrucción ni plan de reversibilidad formal.

13. Seguridad del personal, confidencialidad y auditorías:
- NDA/confidencialidad exigida.
- Formación ENS/RGPD/ciber: No exigida, pero recomendable.
- Auditorías: No exigidas, pero ISO 27001 valorable.
- Evidencias/certificaciones: No exigidas, pero disponibles.

14. Matriz de cumplimiento Seguridad / DPO / ENS:
(Ver tabla en punto 7)

15. Costes o esfuerzos adicionales previsibles:
- Declaración ENS BASICA: coste bajo.
- Acuerdo de encargado: coste bajo.
- Logging 12 meses: coste bajo.
- No se prevén costes de certificación ENS ni SOC/SIEM.

16. Riesgos de incumplimiento contractual:
- Falta de acuerdo de encargado formal.
- Falta de detalle en subencargados y cadena de suministro.
- Ubicación de backups y servicios auxiliares no detallada.
- Penalización por incumplimiento de SLA o trazabilidad.

17. Plan de acción recomendado:
- Antes de ofertar: Preparar declaración ENS BASICA, modelo de acuerdo de encargado, evidencias de medidas técnicas y plan de reversibilidad.
- Antes de adjudicación: Validar subcontratistas y cadena de suministro, confirmar ubicación de datos y backups.
- Durante ejecución: Formalizar acuerdo de encargado, mantener logs 12 meses, cumplir medidas técnicas y notificar incidentes según pliego.

18. Preguntas al órgano de contratación:
- ¿Se requiere acuerdo de encargado de tratamiento formal?
- ¿Se permite el uso de cloud o solo on-premise?
- ¿Dónde se ubican los backups y servicios auxiliares?
- ¿Qué subcontratistas están autorizados?
- ¿Se exige logging avanzado o SIEM?
- ¿Qué canal se usará para notificación de incidentes/brechas?
- ¿Se requiere plan de reversibilidad y certificado de destrucción?

19. Documentos revisados:
1. Pliego administrativo OPP-SW-004 mantenimiento Java
2. Pliego técnico OPP-SW-004 mantenimiento Java
3. Anexo solvencia OPP-SW-004 mantenimiento Java