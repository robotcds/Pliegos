1. Veredicto ejecutivo Seguridad / DPO / ENS: CUMPLE CON GAPS.

2. Los 8 puntos críticos:
- ENS: Exigido nivel BÁSICO, cumplimiento por declaración, no por certificación. Alcance: asistente virtual SaaS y servicios asociados. No se exige ENS media ni alta. Gap: la empresa tiene ENS media certificada, pero el pliego solo exige básico.
- Datos personales y rol: El pliego indica que NO se requiere tratamiento de datos personales por cuenta del responsable (apartado 1.8 Anexo I y 11.18 PPTP). Rol: No encargado ni subencargado. Gap: No aplica acuerdo de encargado ni EIPD.
- Ubicación/cloud/transferencias: Despliegue solo en Azure, AWS o GCP, regiones EEE. Prohibido fuera EEE. No se prevén transferencias internacionales. Gap: ninguno relevante si se usa cloud UE.
- Medidas técnicas: Exigidas las del ENS básico y guías CCN-STIC. IAM del Ayuntamiento controla acceso, red, logs, monitorización, backup, etc. Gap: la empresa cumple ENS media, pero debe adaptar procedimientos a la gobernanza IAM y ENS básico.
- Incidentes/brechas: Gestión de incidentes según ENS y CCN-STIC-817. No aplica brecha RGPD (no hay tratamiento de datos personales). Gap: ninguno relevante.
- Subencargados/cadena de suministro: Subcontratación permitida salvo tareas críticas. Clouders permitidos: Azure, AWS, GCP. Gap: informar y controlar subcontratistas, pero sin acceso a datos personales.
- Auditorías/evidencias: Derecho de auditoría del Ayuntamiento, obligación de evidencias de cumplimiento ENS básico. Gap: la empresa tiene evidencias y certificaciones superiores, pero debe preparar declaración y evidencias específicas para ENS básico.
- Gaps principales: No aplica ENS media/alta ni RGPD como encargado. El principal esfuerzo es documental y de adaptación a la gobernanza cloud y ENS básico del Ayuntamiento.

3. ENS:
- Categoría exigida: BÁSICA (PPTP 11.1, CCN-STIC-803).
- Certificación/declaración: Declaración de conformidad, no se exige certificación.
- Momento de acreditación: Antes de la puesta en producción, con evidencias y declaración.
- Alcance: Asistente virtual SaaS, panel de control, servicios asociados en cloud pública (Azure, AWS, GCP) bajo gobernanza IAM.
- Guías CCN-STIC: Aplican las de ENS básico y las específicas de cloud y desarrollo seguro.
- Evidencia: Declaración de conformidad, análisis de riesgos, plan de tratamiento, medidas técnicas, documentación de arquitectura y procedimientos.
- Gap frente a capacidad actual: Ninguno relevante, la empresa tiene ENS media certificada y puede cubrir ENS básico por declaración.

4. RGPD/DPO:
- Datos tratados: El pliego indica que NO se requiere tratamiento de datos personales por cuenta del responsable (Anexo I 1.8, PPTP 11.18).
- Finalidad: No aplica.
- Interesados: No aplica.
- Rol del adjudicatario: No encargado ni subencargado.
- Acuerdo de encargado: No aplica.
- EIPD: No aplica.
- DPO/DPD: No exigido para el adjudicatario.
- Conservación: No aplica.
- Acciones: Vigilar que no se introduzcan datos personales en el servicio SaaS; si se detecta, anonimizar y notificar al cliente.

5. Subcontratación, subencargados, cloud y cadena de suministro:
- Cadena: Cliente (Ayuntamiento) -> Adjudicatario (SaaS, operación, soporte) -> Cloud (Azure/AWS/GCP, regiones EEE) -> posibles subcontratistas para desarrollo, soporte, mantenimiento (sin acceso a datos personales).
- Accesos: IAM controla accesos, red, logs, monitorización. Subcontratistas solo pueden intervenir en tareas no críticas y sin acceso a datos personales.

6. Localización y transferencias internacionales:
- Ubicación obligatoria: Regiones EEE de Azure, AWS o GCP.
- Regiones permitidas: Solo EEE.
- Backups: En cloud EEE, bajo control IAM.
- Soporte remoto: Permitido si es desde EEE.
- Telemetría, IA/SaaS: Solo en EEE.
- Riesgos: Bajo, si se respeta la restricción geográfica y no se introducen datos personales.

7. Medidas técnicas de seguridad:
| Medida                | Tipo        | Obligatoria | Evidencia pliego | Capacidad actual | Gap | Riesgo | Acción |
|-----------------------|-------------|-------------|------------------|------------------|-----|--------|--------|
| Cifrado en tránsito   | ENS básico  | Sí          | PPTP 11.6        | TLS 1.2+         | No  | Bajo   | Alinear|
| Cifrado en reposo     | ENS básico  | Sí          | PPTP 11.6        | Sí               | No  | Bajo   | Alinear|
| Gestión de accesos    | ENS básico  | Sí          | PPTP 11.7, 11.10 | Sí (RBAC, IAM)   | No  | Bajo   | Alinear|
| MFA                   | ENS básico  | Recomendado | PPTP 11.8        | Sí (admin)       | No  | Bajo   | Alinear|
| Logging y trazabilidad| ENS básico  | Sí          | PPTP 11.12       | Sí (logs 12-24m) | No  | Bajo   | Alinear|
| Monitorización        | ENS básico  | Sí          | PPTP 11.12       | Sí               | No  | Bajo   | Alinear|
| Parcheado             | ENS básico  | Sí          | PPTP 11.13       | Sí               | No  | Bajo   | Alinear|
| Análisis de riesgos   | ENS básico  | Sí          | PPTP 11.3        | Sí               | No  | Bajo   | Alinear|
| Desarrollo seguro     | ENS básico  | Sí          | PPTP 11.5        | Sí (OWASP, SAST) | No  | Bajo   | Alinear|

8. Identidad, accesos y privilegios:
- MFA: Recomendado para administración.
- SSO: Acceso gestionado por IAM, credenciales proporcionadas por el Ayuntamiento.
- Directorio: IAM controla identidades.
- Cuentas nominativas: Sí, para administración.
- PAM: No exigido explícitamente, pero IAM limita privilegios.
- RBAC: Sí, controlado por IAM.
- Mínimo privilegio: Sí, exigido.
- Altas/bajas: IAM controla.
- Revisiones: No detalladas, pero bajo control IAM.
- Acceso remoto: Solo mediante mecanismos autorizados por IAM.

9. Vulnerabilidades, parcheado y desarrollo seguro:
- SAST, DAST, SCA, SBOM: No exigidos explícitamente, pero buenas prácticas de desarrollo seguro y ENS básico aplican.
- Pentesting: No exigido, pero el Ayuntamiento puede auditar.
- CVE, EOL/EOS: Parcheado diligente exigido.
- Plazos de parcheado: No detallados, pero "diligente y continuado".
- CI/CD, secretos, OWASP: Recomendado, no obligatorio.

10. Incidentes de seguridad y brechas de datos:
- Incidente de seguridad: Cualquier evento que afecte a la confidencialidad, integridad o disponibilidad del sistema (PPTP 11.14).
- Brecha RGPD: No aplica (no hay tratamiento de datos personales).
- Plazos de notificación: Inmediata al responsable del contrato.
- 72 horas AEPD: No aplica.

11. Logging, SOC/SIEM, monitorización y retención:
- Logs exigidos: Sí, para trazabilidad y monitorización (PPTP 11.12).
- Integridad: No detallada, pero exigible por ENS básico.
- Sincronización horaria: No detallada, pero exigible por ENS básico.
- Retención: No especificada, pero mínimo 12 meses recomendable.
- SIEM/SOC: No exigido explícitamente, pero integración posible con herramientas IAM.
- Alertas: Sí, para incidentes.
- Coste/riesgo operativo: Bajo, si se usa cloud y herramientas IAM.

12. Continuidad, backup, borrado y reversibilidad segura:
- RTO/RPO: No especificados.
- Backups: Sí, en cloud EEE, bajo control IAM.
- Copias inmutables/offline: No exigidas.
- Restauración: Sí, bajo control IAM.
- Borrado de datos/backups: Sí, certificado de destrucción exigido al final del contrato.
- Revocación de accesos: Sí, bajo control IAM.

13. Seguridad del personal, confidencialidad y auditorías:
- NDA: Sí, exigido.
- Formación ENS/ciber: No detallada, pero recomendable.
- Roles de seguridad: POC de seguridad exigido (PPTP 11.2).
- Auditorías: Derecho de auditoría del Ayuntamiento.
- Evidencias: Declaración de conformidad ENS básico, análisis de riesgos, plan de tratamiento, logs, informes.
- Certificaciones: No exigidas, pero la empresa dispone de ENS media e ISO 27001.

14. Matriz de cumplimiento Seguridad / DPO / ENS:
(Ver tabla en punto 7 para medidas técnicas. Para otros requisitos:)
| Requisito ENS básico | Obligatorio | Sí | Declaración, análisis de riesgos, medidas técnicas | Sí | No | Bajo | Preparar documentación específica |
| Declaración de conformidad | Obligatorio | Sí | Declaración firmada | Sí | No | Bajo | Preparar y firmar |
| POC de seguridad | Obligatorio | Sí | Designación de responsable | Sí | No | Bajo | Nombrar y comunicar |
| Subcontratación controlada | Obligatorio | Sí | Comunicación y control | Sí | No | Bajo | Informar y controlar |
| Cloud EEE | Obligatorio | Sí | Arquitectura cloud | Sí | No | Bajo | Validar regiones |
| No tratamiento datos personales | Obligatorio | Sí | Anexo I, PPTP | Sí | No | Bajo | Vigilar que no se introduzcan |

15. Costes o esfuerzos adicionales previsibles:
- Preparación de declaración de conformidad ENS básico y evidencias.
- Adaptación documental y procedimientos a la gobernanza IAM.
- Control y comunicación de subcontratistas.
- Formación específica ENS básico si se requiere.

16. Riesgos de incumplimiento contractual:
- No presentar declaración de conformidad ENS básico.
- No adaptar arquitectura/procedimientos a la gobernanza IAM.
- Subcontratación no comunicada o fuera de límites.
- Uso de regiones cloud fuera del EEE.
- Introducción accidental de datos personales en el SaaS.

17. Plan de acción recomendado:
- Antes de ofertar: Revisar arquitectura cloud, preparar declaración de conformidad ENS básico, identificar subcontratistas, validar regiones cloud, preparar evidencias de cumplimiento.
- Antes de adjudicación: Designar POC de seguridad, preparar documentación de análisis de riesgos y plan de tratamiento, revisar procedimientos de acceso y logging.
- Durante ejecución: Mantener evidencias, cumplir con la gobernanza IAM, informar de subcontratistas, mantener logs y backups, preparar certificados de destrucción al cierre.

18. Preguntas al órgano de contratación:
- ¿Se prevé en algún momento el tratamiento de datos personales por cuenta del Ayuntamiento (por ejemplo, logs, grabaciones, tickets)?
- ¿Qué evidencias concretas de cumplimiento ENS básico se deben aportar y en qué plazos?
- ¿Qué periodicidad y formato se exige para la entrega de logs y evidencias?
- ¿Se permite el uso de subcontratistas para soporte, desarrollo o mantenimiento fuera de la UE si no acceden a datos?
- ¿Qué mecanismos de reversibilidad y borrado de datos se consideran suficientes?
- ¿Se exige alguna auditoría externa o solo declaración de conformidad?
- ¿Qué formación en ENS/ciberseguridad se espera del personal asignado?

19. Documentos revisados:
1. ID_188_1.PDF
2. ID_188_2.PDF
3. ID_188_3.PDF
4. poc (detalle licitación)
5. poc (perfil contratante)
6. poc (perfil contratante)
7. 147409-2026
8. perfilContratante