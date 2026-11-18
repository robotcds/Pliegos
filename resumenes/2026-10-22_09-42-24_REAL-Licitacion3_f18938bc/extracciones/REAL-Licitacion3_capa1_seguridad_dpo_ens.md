# 1. Resumen factual Seguridad / DPO / ENS

- El pliego exige certificación ENS nivel medio para el Lote 2 como obligación esencial, así como ISO 27001:2013 para ambos lotes. Se requiere cumplimiento de RGPD y LOPDGDD, con cláusulas específicas sobre confidencialidad, acceso y tratamiento accidental de datos personales. No se define rol de encargado ni responsable de tratamiento salvo en caso de acceso necesario a datos personales, en cuyo caso se formalizará acuerdo de encargo. Se regula la subcontratación y la ubicación de los servicios, exigiendo declaración sobre localización de servidores si se accede a datos personales. Se detallan medidas técnicas de seguridad, control de accesos, autenticación fuerte, logging, monitorización, backup, continuidad y confidencialidad. Se establecen penalizaciones y causas de resolución por incumplimiento de obligaciones esenciales, incluidas las de seguridad y protección de datos.

# 2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente

| Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente |
|---|---|---|---|---|---|
| Certificación ENS | Nivel medio | Lote 2 | Certificado por organismo independiente | Presentación a requerimiento tras adjudicación | DOC20240202141404130-24_PLIEGO.pdf, p.11-12 |

# 3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente

| Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente |
|---|---|---|---|
| Prohibido acceso o tratamiento de datos personales por el contratista | Salvo que sea necesario para la ejecución, en cuyo caso se formalizará acuerdo de encargo | No especificado | DOC20240202141404130-24_PLIEGO.pdf, p.47 |
| Comunicación de incidente de acceso accidental a datos personales | Obligación de notificar al responsable del contrato con la mayor diligencia y celeridad, para que el responsable del tratamiento pueda conocerlo en 72 horas | 72 horas desde conocimiento del incidente | DOC20240202141404130-24_PLIEGO.pdf, p.47 |
| Declaración de ubicación de servidores y servicios asociados si se accede a datos personales | Obligación esencial si se accede a datos personales | Durante la ejecución, comunicar cualquier cambio | DOC20240202141404130-24_PLIEGO.pdf, p.47-48 |
| Formación e información al personal en obligaciones de protección de datos | Obligación de la adjudicataria | Durante la ejecución | DOC2024020214010801+PPT+2023+VI.pdf, p.40 |

# 4. Subencargados, cloud, localizacion y transferencias: requisito | condicion | fuente

| Requisito | Condicion | Fuente |
|---|---|---|
| Subcontratación permitida | Debe notificarse y cumplir requisitos del art. 215 y 216 LCSP; declaración responsable de subcontratistas de no estar incursos en prohibición de contratar | DOC20240202141404130-24_PLIEGO.pdf, p.42, 60-62 |
| Declaración de ubicación de servidores y servicios asociados si se accede a datos personales | Obligación esencial; comunicar cualquier cambio durante la vida del contrato | DOC20240202141404130-24_PLIEGO.pdf, p.47-48 |
| Uso de cloud (AWS, Azure) en la infraestructura | Descrito en el Anexo III; no se establecen restricciones adicionales en el pliego | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf, p.4 |
| Transferencias internacionales | NO CONSTA EN LA DOCUMENTACION REVISADA |

# 5. Medidas tecnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente

| Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente |
|---|---|---|---|
| Autenticación fuerte (doble factor o certificado en tarjeta criptográfica) | Obligatoria si lo requiere el Ministerio | Durante la ejecución | DOC2024020214010801+PPT+2023+VI.pdf, p.7 |
| Control de acceso a entornos | Obligatoria | Durante la ejecución | DOC2024020214010801+PPT+2023+VI.pdf, p.7 |
| Seguridad perimetral con firewalls de nueva generación en alta disponibilidad | Descriptiva de la infraestructura | Permanente | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf, p.2 |
| VPN SSL para acceso remoto | Descriptiva de la infraestructura | Permanente | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf, p.4 |
| Monitorización y alertas en tiempo real | Obligatoria | Permanente | DOC2024020214010801+PPT+2023+VI.pdf, p.23, 28, 29, 33 |
| Backup con Veeam Backup & Replication | Descriptiva de la infraestructura | Permanente | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf, p.3 |
| Registro de actuaciones y logs en herramientas del Ministerio | Obligatoria | Permanente | DOC2024020214010801+PPT+2023+VI.pdf, p.17, 21, 25, 28, 30, 33 |
| Restricciones de acceso y uso de datos según políticas del Ministerio | Obligatoria | Permanente | DOC2024020214010801+PPT+2023+VI.pdf, p.40 |

# 6. Identidad, accesos y privilegios

- El acceso a los recursos se gestiona mediante el directorio activo de Microsoft, con más de 10.000 cuentas y servicio a unos 5.500 usuarios. (DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf, p.3)
- Se podrán requerir mecanismos avanzados de autenticación fuerte (doble factor o certificado en tarjeta criptográfica). (DOC2024020214010801+PPT+2023+VI.pdf, p.7)
- El adjudicatario debe garantizar que sus empleados dispongan de los medios físicos necesarios para cumplir los requisitos de seguridad marcados por el Ministerio. (DOC2024020214010801+PPT+2023+VI.pdf, p.7)
- Restricciones de utilización de sistemas y acceso a datos según políticas y mecanismos de seguridad del Ministerio. (DOC2024020214010801+PPT+2023+VI.pdf, p.40)

# 7. Vulnerabilidades, parcheado y desarrollo seguro

- Instalación de correcciones y ajustes precisos para el funcionamiento eficaz de equipos físicos y lógicos, incluyendo parches de seguridad. (DOC2024020214010801+PPT+2023+VI.pdf, p.21, 31)
- Soporte preventivo y evolutivo de hardware y software, incluyendo despliegue centralizado de software y parches de seguridad. (DOC2024020214010801+PPT+2023+VI.pdf, p.31)
- NO CONSTA EN LA DOCUMENTACION REVISADA: requisitos específicos de pentesting, CVE, SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD, SBOM.

# 8. Incidentes, brechas y plazos de notificacion expresamente indicados

- En caso de acceso o tratamiento accidental de datos personales, el contratista debe notificarlo al responsable del contrato con la mayor diligencia y celeridad, para que el responsable del tratamiento pueda conocerlo en 72 horas. (DOC20240202141404130-24_PLIEGO.pdf, p.47)
- El contratista debe poner a disposición del responsable del contrato toda la información necesaria para demostrar el cumplimiento de las obligaciones y para permitir auditorías, incluidas inspecciones. (DOC20240202141404130-24_PLIEGO.pdf, p.47)
- NO CONSTA EN LA DOCUMENTACION REVISADA: definición de incidente de seguridad, canales específicos de notificación distintos del responsable del contrato, plazos para otros incidentes no relacionados con datos personales.

# 9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retencion

- Registro de todas las actuaciones practicadas en las herramientas del Ministerio, incluyendo logs de incidencias, peticiones y operaciones. (DOC2024020214010801+PPT+2023+VI.pdf, p.17, 21, 25, 28, 30, 33)
- Monitorización proactiva de servicios y sistemas, con alertas en tiempo real. (DOC2024020214010801+PPT+2023+VI.pdf, p.23, 28, 29, 33)
- Backup de máquinas virtuales, carpetas de servidores de ficheros, SQL Server y Oracle, con Veeam Backup & Replication. (DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf, p.3)
- Clústeres de alta disponibilidad para ficheros y SQL Server. (DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf, p.3)
- NO CONSTA EN LA DOCUMENTACION REVISADA: requisitos de SOC/SIEM, RTO/RPO expresos, retención de logs o backups, pruebas de continuidad.

# 10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad

- Certificación ISO/IEC 27001:2013 exigida para ambos lotes. (DOC20240202141404130-24_PLIEGO.pdf, p.11)
- Certificación ENS nivel medio exigida para Lote 2. (DOC20240202141404130-24_PLIEGO.pdf, p.11-12)
- El contratista debe poner a disposición del responsable del contrato toda la información necesaria para auditorías, incluidas inspecciones. (DOC20240202141404130-24_PLIEGO.pdf, p.47)
- Formación e información al personal en obligaciones de protección de datos. (DOC2024020214010801+PPT+2023+VI.pdf, p.40)
- Obligación de confidencialidad y secreto profesional sobre toda la información, incluso tras la finalización del contrato. (DOC2024020214010801+PPT+2023+VI.pdf, p.40)
- Prohibición de conservar, copiar o ceder datos o documentos proporcionados por la Administración, salvo autorización expresa. (DOC2024020214010801+PPT+2023+VI.pdf, p.40)
- Retirada y destrucción de soportes inservibles, con entrega de documentos acreditativos de acuerdo a RAEE. (DOC2024020214010801+PPT+2023+VI.pdf, p.23)
- NO CONSTA EN LA DOCUMENTACION REVISADA: requisitos de borrado seguro de datos personales, contenido detallado de certificados de destrucción, designación de DPO/DPD, EIPD, frecuencia de auditorías.

# 11. Consecuencias contractuales expresamente asociadas al incumplimiento, si constan

- El incumplimiento de la certificación ENS nivel medio (Lote 2) y otras certificaciones es causa de resolución del contrato por ser obligación esencial. (DOC20240202141404130-24_PLIEGO.pdf, p.12)
- El incumplimiento de las obligaciones esenciales en materia de protección de datos y localización de servidores es causa de resolución del contrato. (DOC20240202141404130-24_PLIEGO.pdf, p.47-48)
- Penalizaciones económicas por incumplimiento de ANS, falta de recursos asignados, rotación no planificada del personal, y por incumplimiento de condiciones de subcontratación. (DOC20240202141404130-24_PLIEGO.pdf, p.43-45)

# 12. Datos no localizados o ambiguos, sin recomendaciones

- NO CONSTA EN LA DOCUMENTACION REVISADA: requisitos de RTO/RPO, retención de logs, SOC/SIEM, desarrollo seguro (SDLC, DevSecOps, SAST, DAST, SCA, OWASP, CI/CD, SBOM), designación de DPO/DPD, EIPD, frecuencia de auditorías, transferencias internacionales de datos, contenido detallado de acuerdos de encargo, requisitos de borrado seguro de datos personales.

# 13. Documentos revisados: enumera todos los documentos del indice, uno por uno

1. DOC2024020214010801+PPT+2023+VI.pdf
2. DOC20240202141404130-24_PLIEGO.pdf
3. DOC20240202144445012+Anexo+II+Lista+final+de+sedes+del+MITMA+7+nov+2023.pdf
4. DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf
5. DOC20240202144519014+Anexo+IV+Resumen+de+activos.pdf
6. DOC20240202144535015+Anexo+V+Conocimientos+equipo+de+trabajo.pdf
7. DOC20240202144619016+Anexo+VI+Datos+de+peticiones+de+servicio+e+incidencias.pdf
8. DOC_CD2024-000159639.pdf
9. DOC_CN2024-000157989.pdf
10. poc (enlazado desde DOC_CD2024-000159639.pdf)
11. poc (enlazado desde DOC_CD2024-000159639.pdf)
12. poc (enlazado desde DOC_CD2024-000159639.pdf)

# Tabla de trazabilidad

| Requisito/dato | Tipo | Valor/condicion | Documento | Pagina/apartado | Estado de lectura |
|---|---|---|---|---|---|
| Certificación ENS nivel medio Lote 2 | Obligación esencial | Certificado por organismo independiente | DOC20240202141404130-24_PLIEGO.pdf | p.11-12 | Leído |
| Certificación ISO/IEC 27001:2013 ambos lotes | Obligación | Certificado por organismo independiente | DOC20240202141404130-24_PLIEGO.pdf | p.11 | Leído |
| Prohibición acceso/tratamiento datos personales | Obligación | Salvo necesidad, en cuyo caso acuerdo de encargo | DOC20240202141404130-24_PLIEGO.pdf | p.47 | Leído |
| Notificación incidente acceso accidental datos personales | Obligación | Notificar con diligencia para conocimiento en 72h | DOC20240202141404130-24_PLIEGO.pdf | p.47 | Leído |
| Declaración ubicación servidores si acceso a datos personales | Obligación esencial | Comunicar cambios durante la vida del contrato | DOC20240202141404130-24_PLIEGO.pdf | p.47-48 | Leído |
| Subcontratación permitida | Condición | Notificación y requisitos art. 215 y 216 LCSP | DOC20240202141404130-24_PLIEGO.pdf | p.42, 60-62 | Leído |
| Uso de cloud (AWS, Azure) | Descriptivo | No restricciones adicionales en pliego | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf | p.4 | Leído |
| Autenticación fuerte | Obligación | Si lo requiere el Ministerio | DOC2024020214010801+PPT+2023+VI.pdf | p.7 | Leído |
| Control de acceso a entornos | Obligación | Durante la ejecución | DOC2024020214010801+PPT+2023+VI.pdf | p.7 | Leído |
| Seguridad perimetral firewalls | Descriptivo | Permanente | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf | p.2 | Leído |
| VPN SSL acceso remoto | Descriptivo | Permanente | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf | p.4 | Leído |
| Monitorización y alertas en tiempo real | Obligación | Permanente | DOC2024020214010801+PPT+2023+VI.pdf | p.23, 28, 29, 33 | Leído |
| Backup con Veeam | Descriptivo | Permanente | DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf | p.3 | Leído |
| Registro de actuaciones/logs | Obligación | Permanente | DOC2024020214010801+PPT+2023+VI.pdf | p.17, 21, 25, 28, 30, 33 | Leído |
| Restricciones de acceso y uso de datos | Obligación | Según políticas del Ministerio | DOC2024020214010801+PPT+2023+VI.pdf | p.40 | Leído |
| Instalación de parches/correcciones | Obligación | Durante la ejecución | DOC2024020214010801+PPT+2023+VI.pdf | p.21, 31 | Leído |
| Formación en protección de datos | Obligación | Durante la ejecución | DOC2024020214010801+PPT+2023+VI.pdf | p.40 | Leído |
| Confidencialidad y secreto profesional | Obligación | Durante y tras el contrato | DOC2024020214010801+PPT+2023+VI.pdf | p.40 | Leído |
| Retirada y destrucción de soportes | Obligación | Entrega de documentos acreditativos | DOC2024020214010801+PPT+2023+VI.pdf | p.23 | Leído |
| Penalizaciones por incumplimiento ANS, recursos, subcontratación | Consecuencia | Económica y posible resolución | DOC20240202141404130-24_PLIEGO.pdf | p.43-45 | Leído |
| Causas de resolución por incumplimiento ENS, protección de datos | Consecuencia | Resolución del contrato | DOC20240202141404130-24_PLIEGO.pdf | p.12, 47-48 | Leído |
| RTO/RPO, SOC/SIEM, desarrollo seguro, DPO/DPD, EIPD, transferencias internacionales, borrado seguro, retención de logs/backups, frecuencia de auditorías | NO CONSTA | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |