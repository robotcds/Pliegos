### 1. Veredicto ejecutivo Seguridad / DPO / ENS
**CUMPLE CON GAPS**. El pliego exige ENS categoría media (certificación), cumplimiento RGPD, medidas técnicas avanzadas y control de subcontratistas. La empresa cumple en gran parte, pero hay gaps en ENS alta, SOC 24x7, alojamiento exclusivo en España, ISO 20000 y gestión de datos especialmente sensibles.

---

### 2. Los 8 puntos críticos
1. **ENS**: Exige certificación ENS media (no alta), acreditación obligatoria, alcance sobre toda la infraestructura y servicios gestionados, con guías CCN-STIC. Gap: no se cubre ENS alta ni servicios fuera de alcance actual.
2. **Datos personales y rol**: Se tratarán datos identificativos, empleados, usuarios, logs, correos, IPs, etc. El rol del adjudicatario es de encargado del tratamiento, no responsable. Acuerdo de encargado solo si hay acceso a datos personales.
3. **Ubicación/cloud/transferencias**: Datos y sistemas en CPD del Ministerio (Madrid) y cloud (Azure/AWS) en UE. No se permiten transferencias internacionales salvo autorización. Backups y soporte en España/UE. Gap: alojamiento exclusivo en España requiere revisión de todos los servicios cloud/SaaS.
4. **Medidas técnicas**: Exige MFA, control de accesos, logging, monitorización, backups, cifrado, VPN, segmentación, gestión de vulnerabilidades, etc. Gap: SOC 24x7 solo con partner, DLP parcial, PAM parcial.
5. **Incidentes/brechas**: Procedimiento de notificación inmediata al cliente, registro, informe, y colaboración en análisis forense. Gap: plazos internos más estrictos que los exigidos.
6. **Subencargados/cadena de suministro**: Subcontratación permitida con notificación y control. Cloud/SaaS/CPD deben estar en UE. Gap: revisión continua de subencargados y servicios auxiliares.
7. **Auditorías/evidencias**: Derecho de auditoría del cliente, evidencias de cumplimiento, certificaciones ISO 27001/9001/ENS media. Gap: no ISO 20000 ni 27701.
8. **Gaps principales**: No ENS alta, SOC 24x7 limitado, alojamiento exclusivo en España, ISO 20000/27701, gestión de datos especialmente sensibles, retención de logs >12 meses con coste extra.

---

### 3. ENS
- **Categoría exigida**: ENS categoría media (certificación obligatoria, no declaración de conformidad).
- **Momento de acreditación**: Antes de la adjudicación y durante toda la vigencia.
- **Alcance**: Toda la infraestructura, sistemas, redes, CPD, cloud y servicios gestionados para el Ministerio.
- **Guías CCN-STIC**: Referencia general, no se citan guías específicas.
- **Evidencia**: Certificado ENS media vigente, auditoría superada en 2025.
- **Gap**: No se cubre ENS alta ni servicios fuera de alcance actual (IoT, mobile nativo, datos sanitarios especiales).

---

### 4. RGPD/DPO
- **Datos tratados**: Identificativos, empleados, usuarios, logs, IPs, correos, credenciales técnicas, datos económicos no sensibles.
- **Finalidad**: Soporte, administración, operación, monitorización y gestión de sistemas y usuarios del Ministerio.
- **Interesados**: Empleados públicos, usuarios internos, ciudadanos (en menor medida).
- **Rol adjudicatario**: Encargado del tratamiento (no responsable ni corresponsable).
- **Acuerdo de encargado**: Solo si hay acceso a datos personales; debe formalizarse con instrucciones, medidas, subencargados, devolución/borrado, auditoría y confidencialidad.
- **EIPD**: No exigido salvo tratamiento de datos especialmente sensibles o perfilado masivo.
- **DPO/DPD**: Obligatorio tenerlo y colaborar con el responsable.
- **Conservación**: Según instrucciones del responsable; logs y backups sujetos a retención definida por el Ministerio.
- **Acciones**: Preparar modelo de acuerdo de encargado, revisar subencargados, asegurar reversibilidad y borrado seguro.

---

### 5. Subcontratación, subencargados, cloud y cadena de suministro
- **Cadena**: Cliente (Ministerio) → Adjudicatario → Subencargados (cloud/SaaS/CPD/fabricantes/partners).
- **Accesos**: Subencargados pueden acceder a sistemas, datos, logs y credenciales bajo control y autorización previa.
- **Obligaciones**: Notificación y autorización de subcontratistas, cumplimiento ENS/RGPD, evidencias de cumplimiento, NDA y control de pagos.
- **Gap**: Revisión continua de subencargados, especial atención a servicios cloud/SaaS auxiliares y soporte fuera de UE.

---

### 6. Localización y transferencias internacionales
- **Ubicación obligatoria**: CPD principal y respaldo en Madrid; cloud en UE (Azure/AWS). No se permiten transferencias internacionales salvo autorización expresa.
- **Backups**: En CPD y cloud UE; restauración y borrado bajo control del Ministerio.
- **Soporte remoto**: Permitido desde UE; fuera de UE requiere autorización.
- **Telemetría/IA/SaaS**: Revisar servicios auxiliares para evitar transferencias no autorizadas.
- **Riesgos**: Uso de SaaS/soporte/telemetría fuera de UE, cambios en la localización cloud, subencargados no controlados.

---

### 7. Medidas técnicas de seguridad (extracto)
| Medida                | Tipo         | Pliego | Capacidad actual | Gap | Riesgo | Acción |
|-----------------------|--------------|--------|------------------|-----|--------|--------|
| MFA                   | Obligatoria  | Sí     | Sí (admin)       | No  | Bajo   | Cumple |
| SSO                   | Recomendado  | Sí     | Sí               | No  | Bajo   | Cumple |
| Cifrado en tránsito   | Obligatoria  | Sí     | Sí (TLS 1.2+)    | No  | Bajo   | Cumple |
| Cifrado en reposo     | Obligatoria  | Sí     | Sí               | No  | Bajo   | Cumple |
| RBAC                  | Obligatoria  | Sí     | Sí               | No  | Bajo   | Cumple |
| PAM                   | Recomendado  | Sí     | Parcial          | Sí  | Medio  | Refuerzo|
| VPN                   | Obligatoria  | Sí     | Sí               | No  | Bajo   | Cumple |
| Bastionado            | Obligatoria  | Sí     | Sí               | No  | Bajo   | Cumple |
| Segmentación          | Obligatoria  | Sí     | Sí               | No  | Bajo   | Cumple |
| EDR/XDR               | Recomendado  | Sí     | Parcial          | Sí  | Medio  | Refuerzo|
| WAF                   | Recomendado  | Sí     | Sí               | No  | Bajo   | Cumple |
| SIEM/SOC              | Obligatoria  | Sí     | Parcial (SOC 24x7 solo con partner) | Sí | Medio | Refuerzo/partner |
| DLP                   | Recomendado  | Sí     | Parcial          | Sí  | Medio  | Refuerzo|
| Backups               | Obligatoria  | Sí     | Sí               | No  | Bajo   | Cumple |
| Logs                  | Obligatoria  | Sí     | Sí (12 meses)    | Sí  | Bajo   | Ampliar si exige >12m |
| Integridad logs       | Recomendado  | Sí     | Sí (opcional)    | Sí  | Bajo   | Presupuestar si exige |

---

### 8. Identidad, accesos y privilegios
- **MFA**: Obligatorio para administradores, disponible.
- **SSO**: Disponible (Entra ID/SAML/OIDC).
- **Directorio**: Microsoft Active Directory, cuentas nominativas, segregación de roles.
- **RBAC**: Implantado.
- **PAM**: Parcial, refuerzo necesario para cuentas críticas.
- **Altas/bajas**: Procedimiento disponible, integración con cliente.
- **Revisiones**: Revisiones periódicas, acceso remoto bajo control.

---

### 9. Vulnerabilidades, parcheado y desarrollo seguro
- **SAST/DAST/SCA/SBOM**: Disponibles en CI/CD y bajo demanda.
- **Pentesting**: Disponible con recursos internos o partner.
- **CVE/EOL/EOS**: Gestión activa, parcheado crítico <=48h (24h requiere refuerzo).
- **OWASP**: Aplicado en desarrollo web.
- **Secretos**: Gestión disponible.
- **Gaps**: Parcheado crítico <=24h solo con guardia/refuerzo; EOL/EOS en sistemas legacy.

---

### 10. Incidentes de seguridad y brechas de datos
- **Incidente de seguridad**: Cualquier evento que afecte a la confidencialidad, integridad o disponibilidad.
- **Brecha RGPD**: Acceso, pérdida o divulgación no autorizada de datos personales.
- **Plazos**: Notificación interna inmediata, comunicación al cliente objetivo <=2h. Relación con 72h AEPD: el responsable (Ministerio) notifica a AEPD/interesados.

---

### 11. Logging, SOC/SIEM, monitorización y retención
- **Logs**: Centralización obligatoria, retención base 12 meses (ampliable con coste).
- **Integridad**: Almacenamiento inmutable opcional.
- **SIEM/SOC**: Integración disponible, SOC 24x7 solo con partner.
- **Alertas**: Monitorización 24x7, alertas automáticas.
- **Coste/riesgo**: Retención >12 meses y almacenamiento inmutable implican coste extra.

---

### 12. Continuidad, backup, borrado y reversibilidad segura
- **RTO/RPO**: No definidos en pliego, pero se exige restauración rápida y backup diario.
- **Backups**: Cifrados, retención configurable, restauración bajo control del Ministerio.
- **Borrado**: Seguro, con certificado de destrucción lógica; backups sujetos a ciclo de retención.
- **Reversibilidad**: Entrega de datos y documentación en formatos abiertos.

---

### 13. Seguridad del personal, confidencialidad y auditorías
- **NDA/confidencialidad**: Obligatorio, incluido en pliego y procedimientos internos.
- **Formación**: ENS/RGPD/ciberseguridad obligatoria para personal asignado.
- **Roles de seguridad**: Responsable de seguridad, DPO/DPD designados.
- **Auditorías**: Derecho de auditoría del cliente, evidencias de cumplimiento, certificaciones ISO 27001/9001/ENS media.

---

### 14. Matriz de cumplimiento Seguridad / DPO / ENS
(Extracto, ver tabla completa en anexo)
| Requisito | Tipo | Obligatorio | Situación | Evidencia interna | Gap | Riesgo | Acción |
|-----------|------|-------------|-----------|-------------------|-----|--------|--------|
| ENS media | Certificación | Sí | Cumple | Certificado | No | Bajo | Mantener |
| ENS alta | Certificación | No | No cumple | N/A | Sí | Medio | No ofertar servicios ENS alta |
| ISO 20000 | Certificación | Sí (L2) | No cumple | N/A | Sí | Medio | Buscar partner/certificación |
| Logging >12m | Técnica | No | Parcial | 12m | Sí | Bajo | Presupuestar si exige |
| SOC 24x7 | Técnica | No | Parcial | Partner | Sí | Medio | Subcontratar |
| DLP/PAM | Técnica | No | Parcial | Parcial | Sí | Bajo | Refuerzo |

---

### 15. Costes o esfuerzos adicionales previsibles
- **Certificación ISO 20000** (si se exige en Lote 2).
- **SOC 24x7**: Subcontratación/partner.
- **Retención de logs >12 meses**: Coste de almacenamiento.
- **Alojamiento exclusivo en España**: Validación de todos los servicios cloud/SaaS.
- **Auditoría ENS**: Mantenimiento y renovación.
- **EIPD**: Si se tratan datos especialmente sensibles.
- **Refuerzo de personal**: Guardias para parcheado crítico <=24h, soporte 24x7.

---

### 16. Riesgos de incumplimiento contractual
1. No disponer de ENS alta si se exige para algún sistema.
2. No cumplir ISO 20000 en Lote 2.
3. No controlar subencargados/transferencias internacionales.
4. No cumplir plazos de notificación de incidentes/brechas.
5. No poder alojar todos los datos en España si se exige.
6. No poder ampliar retención de logs sin coste extra.
7. No poder cubrir SOC 24x7 sin partner.
8. No poder acreditar destrucción de backups fuera de ciclo.

---

### 17. Plan de acción recomendado
- **Antes de ofertar**: Confirmar alcance ENS media, revisar subencargados, preparar evidencias, aclarar dudas con el órgano de contratación.
- **Antes de adjudicación**: Formalizar acuerdos de encargado, revisar cadena de suministro, planificar refuerzos (SOC, logs, guardias).
- **Durante ejecución**: Mantener certificaciones, evidencias, formación, control de subencargados, reporting y auditorías periódicas.

---

### 18. Preguntas al órgano de contratación
1. ¿Se exige ENS alta para algún sistema concreto o solo media?
2. ¿Qué datos personales concretos se tratarán y en qué volumen?
3. ¿El adjudicatario tendrá acceso directo a datos personales o solo a sistemas?
4. ¿Se permite subcontratación de SOC, cloud, soporte o desarrollo?
5. ¿Se exige alojamiento exclusivo en España o basta con UE?
6. ¿Qué retención mínima de logs se exige (12, 24, 36 meses)?
7. ¿Qué plazos de notificación de incidentes/brechas se consideran críticos?
8. ¿Se exige EIPD para algún tratamiento?
9. ¿Qué auditorías externas se exigirán durante el contrato?
10. ¿Qué servicios cloud/SaaS auxiliares están permitidos?
11. ¿Qué procedimiento de reversibilidad y borrado de backups se exige?
12. ¿Qué controles sobre la cadena de suministro se consideran suficientes?

---

### 19. Documentos revisados
1. DOC2024020214010801+PPT+2023+VI.pdf
2. DOC20240202141404130-24_PLIEGO.pdf
3. DOC20240202144445012+Anexo+II+Lista+final+de+sedes+del+MITMA+7+nov+2023.pdf
4. DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf
5. DOC20240202144519014+Anexo+IV+Resumen+de+activos.pdf
6. DOC20240202144535015+Anexo+V+Conocimientos+equipo+de+trabajo.pdf
7. DOC20240202144619016+Anexo+VI+Datos+de+peticiones+de+servicio+e+incidencias.pdf
8. DOC_CD2024-000159639.pdf
9. DOC_CN2024-000157989.pdf
10. poc (detalle licitación)
11. poc (perfil contratante)
12. poc (perfil contratante duplicado)