1. Veredicto ejecutivo Seguridad / DPO / ENS: CUMPLE CON GAPS. El pliego exige ENS categoría BÁSICA, rol de encargado, medidas técnicas y organizativas alineadas con ENS y RGPD, acuerdo de encargado, control de subencargados y confidencialidad, pero hay detalles operativos y de alcance que requieren aclaración y adaptación.

2. Los 8 puntos críticos:
- ENS: Exige categoría BÁSICA, cumplimiento por certificación o declaración, medidas según Anexo II RD 3/2010/311/2022, guías CCN-STIC. No se exige ENS MEDIA/ALTA.
- Datos personales y rol: Identificativos (nombre, apellidos, DNI, IP), usuarios AGE. Rol: encargado del tratamiento. Finalidad: soporte, incidencias, configuración y adaptación de puestos.
- Ubicación/cloud/transferencias: No se permite tratamiento fuera del EEE salvo autorización expresa. Infraestructura en CPD del Ministerio de Justicia. No se prevén transferencias internacionales.
- Medidas técnicas: Exige medidas ENS BÁSICA, control de accesos, confidencialidad, integridad, disponibilidad, logging, backups, gestión de incidentes, formación, NDA.
- Incidentes/brechas: Notificación a responsable en <72h, colaboración en análisis y remediación. Distinción incidente/brecha RGPD.
- Subencargados/cadena de suministro: Subcontratación permitida con autorización y contrato de subencargo. Obligación de informar y trasladar medidas ENS/RGPD.
- Auditorías/evidencias: Derecho de auditoría, evidencias de cumplimiento, formación, NDA, certificados.
- Gaps principales: No se exige ENS MEDIA/ALTA, no se detallan medidas avanzadas (SOC, SIEM, EDR), ni logging extendido, ni requisitos cloud específicos.

3. ENS:
- Categoría exigida: BÁSICA.
- Certificación/declaración: Admisible cualquiera de las dos.
- Momento de acreditación: Antes de inicio de tareas con datos personales.
- Alcance: Soporte a usuarios, sistemas, comunicaciones y seguridad de la AGE.
- Guías CCN-STIC: Referencia genérica, no se citan guías concretas.
- Evidencia: Anexo 5, PPT y PCAP.
- Gap: Capacidad interna es ENS MEDIA, por lo que se cumple sobradamente. No se exige MEDIA/ALTA.

4. RGPD/DPO:
- Datos tratados: Nombre, apellidos, DNI, IP, localización, dirección física de puesto.
- Finalidad: Soporte, incidencias, configuración, adaptación de puestos.
- Interesados: Usuarios de la AGE.
- Rol: Encargado del tratamiento.
- Acuerdo de encargado: Modelo detallado en Anexo 5, con instrucciones, medidas, subencargados, devolución/borrado, auditoría.
- EIPD: No exigida salvo que se amplíe el alcance a datos sensibles.
- DPO/DPD: No se menciona, pero es obligatorio para el responsable (AGE).
- Conservación: Durante la vigencia del contrato, devolución/borrado al finalizar.
- Acciones: Firmar acuerdo, garantizar medidas, informar de subencargados, cumplir plazos de notificación.

5. Subcontratación, subencargados, cloud y cadena de suministro:
- Cadena: Cliente (AGE) -> Adjudicatario (encargado) -> Subencargados (autorizados, con contrato) -> Proveedores (si acceden a datos).
- Accesos: Solo los necesarios para soporte, incidencias, configuración. Subencargados deben cumplir ENS/RGPD y ser autorizados.

6. Localización y transferencias internacionales:
- Ubicación: CPD Ministerio de Justicia, España. No se permite fuera del EEE salvo autorización.
- Backups: En la infraestructura AGE/Ministerio.
- Soporte remoto: Permitido si cumple ENS/RGPD.
- Telemetría/IA/SaaS: No previsto.
- Riesgos: Uso de subencargados no autorizados, soporte fuera de EEE, falta de control sobre backups.

7. Medidas técnicas de seguridad:
| Medida                | Tipo         | Obligatoria | Evidencia pliego | Capacidad actual | Gap | Riesgo | Acción |
|-----------------------|--------------|-------------|------------------|------------------|-----|--------|--------|
| Control de accesos    | ENS BÁSICA   | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Confidencialidad      | ENS BÁSICA   | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Logging               | ENS BÁSICA   | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Backups               | ENS BÁSICA   | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Gestión de incidentes | ENS BÁSICA   | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Formación             | ENS BÁSICA   | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| NDA/confidencialidad  | ENS BÁSICA   | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|

8. Identidad, accesos y privilegios:
- MFA: No exigido explícitamente.
- SSO: No exigido explícitamente.
- Directorio: Active Directory AGE.
- Cuentas nominativas: Sí, para acceso a sistemas.
- PAM: No exigido.
- RBAC: Sí, por roles.
- Mínimo privilegio: Sí, por diseño.
- Altas/bajas: Sí, por procedimiento.
- Revisiones: No detalladas.
- Acceso remoto: Permitido bajo control.

9. Vulnerabilidades, parcheado y desarrollo seguro:
- SAST/DAST/SCA/SBOM: No aplicable (no hay desarrollo).
- Pentesting: No exigido.
- CVE/EOL/EOS: No detallado.
- Plazos de parcheado: No detallado.
- CI/CD, secretos, OWASP: No aplicable.

10. Incidentes de seguridad y brechas de datos:
- Incidente de seguridad: Cualquier evento que afecte a la seguridad de la información.
- Brecha RGPD: Acceso, pérdida, alteración o divulgación no autorizada de datos personales.
- Plazos: Notificación a responsable (AGE) en <72h. Responsable notifica a AEPD/interesados si procede.

11. Logging, SOC/SIEM, monitorización y retención:
- Logs: Registro de accesos, incidencias, operaciones relevantes.
- Integridad: No detallada.
- Sincronización horaria: No detallada.
- Retención: Durante la vigencia del contrato.
- SIEM/SOC: No exigido.
- Alertas: No detalladas.
- Coste/riesgo: Bajo, salvo que se exijan logs avanzados.

12. Continuidad, backup, borrado y reversibilidad segura:
- RTO/RPO: No detallado.
- Backups: Sí, en infraestructura AGE.
- Copias inmutables/offline: No detallado.
- Restauración: Sí, por procedimiento.
- Borrado de datos/backups: Sí, al finalizar contrato, con certificado si se exige.
- Revocación de accesos: Sí, al finalizar.

13. Seguridad del personal, confidencialidad y auditorías:
- NDA: Sí, Anexo 3.
- Formación ENS/RGPD/ciber: Sí, exigida.
- Roles de seguridad: No detallados.
- Auditorías: Derecho de auditoría, evidencias de cumplimiento.
- Certificaciones: No exigidas, pero valorables.

14. Matriz de cumplimiento Seguridad / DPO / ENS:
(Ver tabla en punto 7)

15. Costes o esfuerzos adicionales previsibles:
- Formación ENS/RGPD.
- Adaptación de procedimientos a requisitos AGE.
- Certificados de destrucción/borrado.
- Gestión documental y evidencias.

16. Riesgos de incumplimiento contractual:
- Subcontratación sin autorización.
- Acceso a datos fuera del EEE.
- Incumplimiento de plazos de notificación de brechas.
- Falta de evidencias de cumplimiento ENS/RGPD.
- Falta de control sobre backups y borrado.

17. Plan de acción recomendado:
- Antes de ofertar: Revisar cadena de subencargados, confirmar ubicación de datos, preparar evidencias ENS/RGPD, plan de formación.
- Antes de adjudicación: Firmar acuerdos de encargado y subencargado, validar procedimientos de borrado y reversibilidad.
- Durante ejecución: Mantener evidencias, cumplir plazos de notificación, actualizar formación, controlar subcontratación.

18. Preguntas al órgano de contratación:
- ¿Se permite el uso de cloud público o solo CPD Ministerio?
- ¿Qué subencargados están autorizados?
- ¿Se exige logging avanzado o SIEM?
- ¿Qué plazos de retención de logs y backups se exigen?
- ¿Se permite soporte remoto desde fuera de España?
- ¿Qué evidencias de borrado/certificados se requieren?
- ¿Se exige formación/certificación específica ENS/RGPD?

19. Documentos revisados:
1. Anuncio.pdf
2. PCAP.pdf
3. PPT.pdf
4. poc (detalle licitación)
5. poc (perfil contratante)
6. poc (perfil contratante, datos de contacto)