### 1. Veredicto ejecutivo Seguridad / DPO / ENS
**CUMPLE CON GAPS**. El pliego exige ENS, ISO 27001, medidas técnicas y acuerdo de encargado RGPD, pero no especifica nivel ENS ni detalla todos los datos tratados ni la ubicación cloud. Hay requisitos de subcontratación, reversibilidad, logging, incidentes y penalizaciones. La capacidad interna cubre ENS media, RGPD, medidas técnicas y subencargados, pero hay gaps en ENS alta, reversibilidad inmediata de backups, SOC 24x7 y alojamiento exclusivo en España.

### 2. 8 puntos críticos
- **ENS**: Exige cumplimiento, no especifica nivel. Certificación ISO 27001 e ISO 20000 obligatoria. Declaración de cumplimiento y evidencias periódicas.
- **Datos personales y rol**: Identificativos, empleados, contactos, logs, credenciales. Rol: encargado del tratamiento.
- **Ubicación/cloud/transferencias**: No se exige ubicación exclusiva en España, pero sí declaración de ubicación y cambios. Transferencias internacionales prohibidas salvo autorización.
- **Medidas técnicas**: Cifrado, control de accesos, backup, logging, gestión de identidades, monitorización, reversibilidad, NDA, formación.
- **Incidentes/brechas**: Notificación inmediata al responsable, colaboración en análisis y notificación RGPD.
- **Subencargados/cadena de suministro**: Subcontratación permitida salvo tareas críticas. Subencargados sujetos a autorización y acuerdo de encargado.
- **Auditorías/evidencias**: Derecho de auditoría, evidencias periódicas, certificaciones ISO y ENS.
- **Gaps principales**: Nivel ENS no definido, alcance cloud, reversibilidad de backups, SOC 24x7, alojamiento exclusivo España, EIPD si hay datos sensibles.

### 3. ENS
- **Categoría exigida**: No especificada (debe consultarse). Exige cumplimiento ENS y certificación ISO 27001/20000.
- **Certificación/declaración**: Certificación ISO 27001/20000 obligatoria. Declaración de cumplimiento ENS y evidencias periódicas.
- **Momento de acreditación**: Antes de adjudicación y durante ejecución (auditorías periódicas).
- **Alcance de sistemas/servicios**: Todos los servicios de administración workplace, virtualización, movilidad y puesto de trabajo.
- **Guías CCN-STIC**: Referencia genérica a cumplimiento de normativa y buenas prácticas.
- **Evidencia y gap**: Capacidad interna cubre ENS media, pero no alta. Gap si se exige ENS alta o alojamiento exclusivo en España.

### 4. RGPD/DPO
- **Datos tratados**: Identificativos, empleados, contactos, logs, credenciales, posiblemente datos de clientes/proveedores.
- **Finalidad**: Gestión y prestación de servicios workplace, soporte, administración, incidencias, proyectos especiales.
- **Interesados**: Empleados, usuarios, contactos de cliente, subcontratistas.
- **Rol del adjudicatario**: Encargado del tratamiento.
- **Acuerdo de encargado**: Modelo incluido en pliego (Anexo XVI), con instrucciones, medidas, subencargados, devolución/borrado, auditoría.
- **EIPD**: No exigida salvo que se traten datos sensibles o de alto riesgo (no especificado en pliego).
- **DPO/DPD**: Obligatorio, contacto de DPO de Correos incluido.
- **Conservación**: Según instrucciones del responsable, borrado tras fin de contrato, certificado de destrucción.
- **Acciones**: Confirmar categorías de datos y necesidad de EIPD.

### 5. Subcontratación, subencargados, cloud y cadena de suministro
- **Cadena**: Cliente (Correos) → Adjudicatario → Subencargados (cloud, SaaS, soporte, fabricantes, partners).
- **Accesos**: Subencargados solo con autorización y acuerdo de encargado. Acceso a datos, sistemas, logs y credenciales bajo control y registro.

### 6. Localización y transferencias internacionales
- **Ubicación obligatoria**: No exige España, pero sí declaración de ubicación y cambios.
- **Regiones permitidas**: No especificadas, pero transferencias internacionales prohibidas salvo autorización.
- **Backups**: Deben estar bajo control y sujetos a reversibilidad y borrado seguro.
- **Soporte remoto, telemetría, IA/SaaS**: No detallado, pero sujetos a autorización y acuerdo de encargado si acceden a datos.
- **Riesgos**: Gap si se exige alojamiento exclusivo en España o si hay servicios cloud/SaaS fuera de la UE.

### 7. Medidas técnicas de seguridad
| Medida                | Tipo         | Obligatoria | Evidencia pliego | Capacidad actual | Gap | Riesgo | Acción |
|-----------------------|-------------|-------------|------------------|------------------|-----|--------|--------|
| Cifrado               | Técnica     | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Control de accesos    | Técnica     | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Backup                | Técnica     | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Logging               | Técnica     | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Gestión de identidades| Técnica     | Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Monitorización        | Técnica     | Sí          | Sí               | Parcial           | Parcial | Medio | Refuerzo|
| Reversibilidad        | Técnica     | Sí          | Sí               | Parcial           | Parcial | Medio | Refuerzo|
| NDA/confidencialidad  | Organizativa| Sí          | Sí               | Sí               | No  | Bajo   | Mantener|
| Formación ENS/RGPD    | Organizativa| Sí          | Sí               | Sí               | No  | Bajo   | Mantener|

### 8. Identidad, accesos y privilegios
- **MFA**: No exigido explícitamente, pero recomendable para administradores.
- **SSO**: Integración con directorio activo de Correos obligatoria.
- **Cuentas nominativas**: Sí, acceso personal e intransferible.
- **PAM**: No exigido explícitamente, recomendable para cuentas privilegiadas.
- **RBAC**: Sí, control de accesos y privilegios.
- **Mínimo privilegio**: Sí, buenas prácticas.
- **Altas/bajas**: Gestión activa por el adjudicatario, verificación periódica.
- **Revisiones**: No detalladas, pero recomendadas.
- **Acceso remoto**: Permitido bajo control y medidas de seguridad.

### 9. Vulnerabilidades, parcheado y desarrollo seguro
- **SAST/DAST/SCA/SBOM**: No exigidos explícitamente, pero buenas prácticas recomendadas.
- **Pentesting**: No exigido, pero recomendable en proyectos especiales.
- **CVE/EOL/EOS**: Parcheo y actualización obligatoria, mínimo bianual.
- **Plazos de parcheado**: Bianual como mínimo, recomendable refuerzo para críticos.
- **CI/CD, secretos, OWASP**: No exigidos, pero recomendados en desarrollos.

### 10. Incidentes de seguridad y brechas de datos
- **Incidente de seguridad**: Cualquier evento que afecte a la seguridad de la información.
- **Brecha RGPD**: Acceso, pérdida o divulgación no autorizada de datos personales.
- **Plazos de notificación**: Inmediata al responsable (Correos), colaboración en análisis y notificación a AEPD en 72h si aplica.

### 11. Logging, SOC/SIEM, monitorización y retención
- **Logs exigidos**: Sí, registro de accesos, incidencias y operaciones relevantes.
- **Integridad**: No detallada, recomendable almacenamiento inmutable.
- **Sincronización horaria**: No detallada, recomendable NTP.
- **Retención**: No especificada, pero mínimo 12 meses recomendable.
- **SIEM/SOC**: No exigido, pero recomendable para monitorización avanzada.
- **Alertas**: Sí, para incidentes críticos.
- **Coste/riesgo operativo**: Refuerzo si se exige retención superior o SIEM/SOC 24x7.

### 12. Continuidad, backup, borrado y reversibilidad segura
- **RTO/RPO**: No especificados, pero exigible cumplimiento de ANS y restauración rápida.
- **Backups**: Sí, periódicos y restaurables.
- **Copias inmutables/offline**: No exigidas, recomendable para datos críticos.
- **Restauración**: Pruebas periódicas obligatorias.
- **Borrado de datos/backups**: Obligatorio tras fin de contrato, certificado de destrucción.
- **Revocación de accesos**: Obligatoria en reversibilidad.

### 13. Seguridad del personal, confidencialidad y auditorias
- **NDA/confidencialidad**: Obligatoria para todo el personal y subcontratistas.
- **Formación ENS/RGPD/ciber**: Obligatoria.
- **Roles de seguridad**: Responsable de seguridad y DPO designados.
- **Auditorías**: Derecho de auditoría para Correos, evidencias periódicas.
- **Certificaciones**: ISO 27001, ISO 20000 obligatorias, ENS según nivel.
- **Derecho de auditoría**: Sí, acceso físico y documental.

### 14. Matriz de cumplimiento Seguridad / DPO / ENS
(Ver tabla en punto 7 y resumen en cada apartado anterior)

### 15. Costes o esfuerzos adicionales previsibles
- Certificación ENS si se exige nivel superior a media.
- Refuerzo de logging, SIEM/SOC, retención de logs.
- Reversibilidad inmediata de backups y borrado seguro.
- Auditorías periódicas y evidencias adicionales.
- Refuerzo de personal para cumplimiento ANS y formación.

### 16. Riesgos de incumplimiento contractual
- Exclusión si no se acredita nivel ENS exigido o certificaciones ISO.
- Penalización por incumplimiento de ANS, reversibilidad, confidencialidad o plazos de respuesta.
- Incumplimiento RGPD por brecha, subencargados no autorizados o transferencias internacionales.
- Falta de evidencia de medidas técnicas o de reversibilidad.

### 17. Plan de acción recomendado
- **Antes de ofertar**: Consultar nivel ENS exigido, confirmar datos tratados y ubicación, validar subencargados y cloud, preparar evidencias de certificaciones y medidas técnicas.
- **Antes de adjudicación**: Presentar declaración de ubicación, acuerdo de encargado firmado, plan de reversibilidad y borrado, listado de subencargados y medidas técnicas.
- **Durante ejecución**: Mantener evidencias, actualizar documentación, realizar auditorías, monitorizar subencargados y transferencias, reforzar formación y pruebas de restauración/borrado.

### 18. Preguntas al órgano de contratación
- ¿Qué nivel ENS es exigido (básico, medio, alto)?
- ¿Se exige alojamiento exclusivo en España o UE para todos los datos y backups?
- ¿Qué categorías de datos personales se tratarán exactamente (sensibles, menores, salud, etc)?
- ¿Se prevé uso de cloud/SaaS fuera de la UE o subencargados internacionales?
- ¿Qué retención de logs y backups es obligatoria?
- ¿Se exige SIEM/SOC 24x7 o retención inmutable de logs?
- ¿Se requiere EIPD para algún tratamiento?
- ¿Qué periodicidad de auditoría y evidencias se exige?
- ¿Qué requisitos de reversibilidad y borrado inmediato de backups se aplican?
- ¿Qué servicios cloud, SaaS o soporte pueden acceder a datos o logs?

### 19. Documentos revisados
1. ANEXO I.pdf
2. Anuncio.pdf
3. DOC20240806095753Pliegodefinitivofirmado.pdf
4. DOC_CD2024-000901195.pdf
5. poc (detalle licitación)
6. poc (perfil contratante)
7. CORREOS-Codigo-General-de-Conducta.pdf (no accesible)
8. perfil-contratante
9. PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf

---

**Resumen ejecutivo:** El pliego exige cumplimiento ENS, ISO 27001/20000, medidas técnicas, acuerdo de encargado y control de subencargados, pero no especifica nivel ENS ni ubicación cloud. La capacidad interna cubre ENS media, RGPD y medidas técnicas, pero hay gaps en ENS alta, reversibilidad de backups, SOC 24x7 y alojamiento exclusivo en España. Se recomienda aclarar nivel ENS, ubicación, datos tratados y subencargados antes de ofertar.