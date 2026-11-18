1. RESUMEN FACTUAL SEGURIDAD / DPO / ENS
- El contrato exige cumplimiento del Esquema Nacional de Seguridad (ENS) nivel BÁSICO, con medidas de seguridad del Anexo II del ENS y guías CCN-STIC aplicables. No se exige certificación ENS ni ISO 27001. No se exige DPO/DPD propio ni acuerdo de encargado de tratamiento, ya que el pliego indica expresamente que el adjudicatario no tratará datos personales por cuenta del Ayuntamiento. Se establecen requisitos de seguridad, ciberseguridad, gestión de riesgos, logging, control de accesos, desarrollo seguro, gestión de vulnerabilidades, incidentes y auditorías, así como obligaciones de confidencialidad y borrado seguro de datos. El despliegue cloud debe realizarse exclusivamente en regiones del EEE en Azure, AWS o GCP, bajo el modelo de gobierno cloud del Ayuntamiento de Madrid. No se permite la transferencia internacional fuera del EEE. El acceso a sistemas y privilegios está regulado por IAM. Se exige punto de contacto de seguridad y análisis de riesgos conforme ENS. Consecuencias contractuales: penalidades económicas y resolución por incumplimientos graves o muy graves, incluyendo incidentes de seguridad, indisponibilidad, destrucción o alteración de datos.

2. ENS: Requisito | Categoria/nivel | Alcance | Acreditacion | Momento | Fuente
- Cumplimiento ENS | Nivel BÁSICO | Servicios objeto del contrato y sistemas desarrollados/desplegados/mantenidos | No se exige certificación, solo cumplimiento de medidas del Anexo II ENS y guías CCN-STIC | Durante toda la ejecución | ID_188_3.PDF, pág. 45-46, 47

3. RGPD/DPO: Datos/rol/obligacion | Condicion | Plazo/retencion | Fuente
- Tratamiento de datos personales por cuenta del responsable: NO (el pliego indica que no se precisa tratamiento de datos personales por cuenta del Ayuntamiento) | No se exige acuerdo de encargado ni DPO/DPD propio | NO CONSTA PLAZO/RETENCIÓN | ID_188_3.PDF, pág. 48; ID_188_2.PDF, pág. 54
- Información sobre protección de datos de los licitadores (contratación municipal): Responsable: Dirección General de Contratación y Servicios; DPD: Coordinación General de Distritos, Transparencia y Participación Ciudadana; Finalidad: gestión contractual; Conservación: mientras sean necesarios para la ejecución del contrato | ID_188_2.PDF, Anexo IX, pág. 95-96

4. Subencargados, cloud, localizacion y transferencias: requisito | condicion | fuente
- Subcontratación permitida salvo tareas críticas (implantación y jefe de proyecto) | Obligación de informar y mantener garantías jurídicas | ID_188_3.PDF, pág. 29
- Cloud: Solo Azure, AWS, GCP en regiones EEE; prohibido fuera del EEE | Modelo de gobierno cloud IAM, políticas de seguridad y privacidad, localización en EEE | ID_188_3.PDF, pág. 29-34
- Transferencias internacionales: Prohibidas fuera del EEE | Art. 45 RGPD, decisión de adecuación | ID_188_3.PDF, pág. 30, 33

5. Medidas tecnicas: Medida | Obligatoria/valorable/condicionada | Parametro/plazo | Fuente
- Medidas ENS nivel básico (Anexo II) | Obligatoria | Durante toda la ejecución | ID_188_3.PDF, pág. 45-46
- Guías CCN-STIC para configuración segura | Obligatoria | Durante toda la ejecución | ID_188_3.PDF, pág. 47
- Cifrado de información no pública en tránsito por redes ajenas | Obligatoria | Según valoración del responsable | ID_188_3.PDF, pág. 47
- Identificación y autenticación: Delegación en IAM (personal municipal) y CL@VE (ciudadanía) | Obligatoria | Durante toda la ejecución | ID_188_3.PDF, pág. 47
- Doble factor de autenticación municipal (si aplica) | Obligatoria | Adjudicatario proporciona medios | ID_188_3.PDF, pág. 48
- Acceso remoto: Solo mediante servicio de acceso remoto del Ayuntamiento | Obligatoria | Condiciones de uso facilitadas por el Ayuntamiento | ID_188_3.PDF, pág. 48
- Control de acceso: Principio de mínimo privilegio y necesidad de conocer | Obligatoria | Durante toda la ejecución | ID_188_3.PDF, pág. 48
- Logging: Registro de actividad de usuarios, entrega a requerimiento | Obligatoria | Durante toda la ejecución | ID_188_3.PDF, pág. 49
- Parcheado y actualizaciones de seguridad | Obligatoria | Periódica y continuada | ID_188_3.PDF, pág. 49
- Gestión de vulnerabilidades | Obligatoria | Subsanación a requerimiento | ID_188_3.PDF, pág. 49
- Gestión de incidentes: Detección, notificación inmediata, colaboración en resolución | Obligatoria | Notificación tan pronto como se tenga conocimiento | ID_188_3.PDF, pág. 49
- Auditorías de seguridad por el Ayuntamiento | Obligatoria | Durante la ejecución | ID_188_3.PDF, pág. 49
- Desarrollo seguro y orientado a la privacidad | Obligatoria | Metodologías y buenas prácticas verificables | ID_188_3.PDF, pág. 47
- Borrado seguro de datos a la finalización del contrato, con certificado | Obligatoria | Al finalizar el contrato | ID_188_3.PDF, pág. 9

6. Identidad, accesos y privilegios
- Gestión de credenciales y accesos por IAM; usuarios externos con credenciales IAM; acceso mínimo privilegio y necesidad de conocer; roles de administración restringidos; autenticación delegada en IAM/CL@VE; doble factor si aplica | ID_188_3.PDF, pág. 33-34, 47-48

7. Vulnerabilidades, parcheado y desarrollo seguro
- Subsanación de vulnerabilidades comunicadas por el responsable; aplicación diligente de actualizaciones de seguridad; desarrollo seguro y orientado a la privacidad, metodologías y buenas prácticas verificables | ID_188_3.PDF, pág. 47, 49

8. Incidentes, brechas y plazos de notificacion expresamente indicados
- Gestión de ciberincidentes en todo su ciclo de vida conforme guía CCN-STIC-817; notificación inmediata al responsable del contrato; colaboración activa en resolución | ID_188_3.PDF, pág. 49
- No se especifican plazos concretos de notificación en horas/días, salvo "tan pronto como tenga conocimiento"

9. Logging, SOC/SIEM, continuidad, backup, RTO/RPO y retencion
- Logging: Registro de actividad de usuarios, entrega a requerimiento | ID_188_3.PDF, pág. 49
- Integración con herramientas de observabilidad y monitorización de IAM si se solicita | ID_188_3.PDF, pág. 31
- Backups: Proporcionados por IAM | ID_188_3.PDF, pág. 31
- Continuidad: No se especifican RTO/RPO ni pruebas de continuidad en el pliego | NO CONSTA EN LA DOCUMENTACION REVISADA

10. Auditorias, evidencias, certificaciones, seguridad del personal, borrado y confidencialidad
- Auditorías de seguridad por el Ayuntamiento | Obligatoria | Durante la ejecución | ID_188_3.PDF, pág. 49
- Borrado seguro de datos a la finalización del contrato, con certificado | Obligatoria | Al finalizar el contrato | ID_188_3.PDF, pág. 9
- Confidencialidad: Obligación de confidencialidad y secreto, subsiste tras el contrato | ID_188_3.PDF, pág. 53
- Seguridad del personal: Obligación de proveer EPIs y cumplir normativa de prevención de riesgos laborales | ID_188_3.PDF, pág. 23, 51
- No se exige certificación ENS ni ISO 27001 | ID_188_3.PDF, pág. 45-46

11. Consecuencias contractuales expresamente asociadas al incumplimiento
- Penalidades económicas del 5% o 10% del precio del contrato por incumplimientos graves o muy graves, incluyendo destrucción, pérdida o alteración de datos, indisponibilidad del servicio, incumplimiento de órdenes, retrasos, etc. | ID_188_2.PDF, pág. 75-77
- Resolución del contrato por reiteración de incumplimientos muy graves | ID_188_2.PDF, pág. 78

12. Datos no localizados o ambiguos, sin recomendaciones
- No se exige certificación ENS ni ISO 27001
- No se exige DPO/DPD propio ni acuerdo de encargado de tratamiento
- No se exige RTO/RPO ni pruebas de continuidad
- No se exige SOC/SIEM dedicado, solo integración con monitorización IAM si se solicita
- No se exige SBOM, SAST, DAST, CI/CD, ni guías OWASP específicas
- No se exige EDR/XDR, WAF, DLP, PAM, VPN, segmentación, ni MFA salvo lo indicado para doble factor municipal
- No se exige plan de continuidad ni DR específico
- No se exige acuerdo de subencargado ni reglas específicas para SaaS fuera de lo indicado para cloud y subcontratación

13. Documentos revisados: 
- ID_188_1.PDF (Documento licitación real)
- ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares)
- ID_188_3.PDF (Pliego de Prescripciones Técnicas)
- poc (enlazado desde ID_188_1.PDF, detalle licitación y perfil contratante)
- perfilContratante (enlazado desde ID_188_2.PDF)
- 147409-2026 (Sin texto extraíble; documento pendiente de lectura/OCR)

TABLA DE TRAZABILIDAD
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|----------------|-----------|------------------|-------------------|
| ENS cumplimiento | Obligatorio | Nivel básico, medidas Anexo II ENS, guías CCN-STIC | ID_188_3.PDF | 45-46, 47 | Leído |
| Certificación ENS/ISO | No exigido | No se exige | ID_188_3.PDF | 45-46 | Leído |
| DPO/DPD propio | No exigido | No se exige | ID_188_3.PDF | 48 | Leído |
| Acuerdo encargado | No exigido | No se exige | ID_188_3.PDF | 48 | Leído |
| Subcontratación | Permitida | Salvo tareas críticas, informar y mantener garantías | ID_188_3.PDF | 29 | Leído |
| Cloud/localización | Obligatorio | Solo Azure, AWS, GCP en EEE | ID_188_3.PDF | 29-34 | Leído |
| Transferencias internacionales | Prohibidas | Solo EEE | ID_188_3.PDF | 30, 33 | Leído |
| Medidas técnicas ENS | Obligatorio | Anexo II ENS, guías CCN-STIC | ID_188_3.PDF | 45-47 | Leído |
| Cifrado | Obligatorio | Información no pública en tránsito por redes ajenas | ID_188_3.PDF | 47 | Leído |
| Identidad/accesos | Obligatorio | IAM/CL@VE, mínimo privilegio | ID_188_3.PDF | 33-34, 47-48 | Leído |
| Logging | Obligatorio | Registro de actividad, entrega a requerimiento | ID_188_3.PDF | 49 | Leído |
| Parcheado | Obligatorio | Periódico y continuado | ID_188_3.PDF | 49 | Leído |
| Vulnerabilidades | Obligatorio | Subsanación a requerimiento | ID_188_3.PDF | 49 | Leído |
| Incidentes | Obligatorio | Notificación inmediata, gestión ciclo completo | ID_188_3.PDF | 49 | Leído |
| Auditoría seguridad | Obligatorio | Por el Ayuntamiento | ID_188_3.PDF | 49 | Leído |
| Borrado seguro | Obligatorio | Al finalizar el contrato, con certificado | ID_188_3.PDF | 9 | Leído |
| Confidencialidad | Obligatorio | Durante y tras el contrato | ID_188_3.PDF | 53 | Leído |
| Penalidades | Obligatorio | 5%/10% precio contrato, resolución por reiteración | ID_188_2.PDF | 75-78 | Leído |
| RTO/RPO, DR, SOC/SIEM dedicado | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| SAST, DAST, CI/CD, SBOM, EDR/XDR, WAF, DLP, PAM, VPN, segmentación | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| Acuerdo subencargado | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| Acuerdo SaaS específico | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| DPO/DPD licitador | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| Pruebas de continuidad, RTO/RPO | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| SBOM, OWASP, DevSecOps | No exigido | NO CONSTA EN LA DOCUMENTACION REVISADA | - | - | - |
| 147409-2026 | PENDIENTE DE VERIFICAR | Sin texto extraíble | 147409-2026 | - | No leído |