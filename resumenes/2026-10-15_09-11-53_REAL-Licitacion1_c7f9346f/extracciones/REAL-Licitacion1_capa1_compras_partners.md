# 1. Resumen factual

La licitación para el "Asistente Virtual de Participación Ciudadana del Ayuntamiento de Madrid" exige que el adjudicatario aporte y gestione una solución tecnológica en modalidad SaaS, incluyendo todos los elementos de software, licencias, servicios cloud (salvo la infraestructura MultiCloud corporativa que aporta el Ayuntamiento), y medios materiales y personales necesarios para la ejecución del contrato. No se exige ningún fabricante concreto ni cartas de canal o partnership, pero sí se establecen restricciones de despliegue en cloud y obligaciones de soporte, mantenimiento, formación, y destrucción de datos. Se permite la subcontratación con límites y declaración previa, y se detallan obligaciones sobre la cadena de suministro cloud y la entrega/retirada de datos y documentación. No se localizan requisitos de hardware físico a suministrar al cliente ni obligaciones de stock, staging o logística física. No se exigen certificaciones de fabricante, ISO ni ENS. No se identifican SLA back-to-back con terceros ni garantías de fabricante.

# 2. Mapa de suministros y terceros
| Elemento/necesidad | Tipo | Cantidad/volumen | Especificación | Quién debe aportarlo | Fuente |
|--------------------|------|------------------|----------------|----------------------|--------|
| Solución Asistente Virtual | SaaS | 1 | BOT conversacional IA generativa y tradicional, integración Decide Madrid | Adjudicatario | ID_188_3.PDF, p.1, 13-14 |
| Panel de control | SaaS | 1 | Acceso web, métricas, gestión, mínimo 5 usuarios | Adjudicatario | ID_188_3.PDF, p.14-15 |
| Licencias software y herramientas | Software/licencias | Todas necesarias | Para desarrollo, operación y acceso a la solución | Adjudicatario | ID_188_3.PDF, p.13-14, 43 |
| Infraestructura MultiCloud (tenant, landing zone, servicios comunes) | Cloud infra | - | Google Cloud Platform, Microsoft Azure, Amazon AWS | Ayuntamiento | ID_188_3.PDF, p.29, 43 |
| Recursos cloud (SaaS/PaaS/IaaS) para la solución | Cloud servicios | Todos necesarios | Despliegue sobre Azure, GCP o AWS, bajo condiciones IAM | Adjudicatario | ID_188_3.PDF, p.29-31 |
| Personal técnico y agentes | Recursos humanos | Según perfiles mínimos | Ver perfiles y dedicación | Adjudicatario | ID_188_3.PDF, p.24-27 |
| Equipos de protección individual | Material | Según necesidad | Para personal propio en caso de riesgo | Adjudicatario | ID_188_3.PDF, p.23 |
| Formación a usuarios DGPC | Servicio | 20h mínimo, 20 asistentes | Formación inicial y continua | Adjudicatario | ID_188_3.PDF, p.16-17 |
| Destrucción de datos y documentación | Servicio | Al cierre | Borrado seguro, certificado | Adjudicatario | ID_188_3.PDF, p.9 |

# 3. Productos, hardware y materiales
| Producto | Cantidad | Características | Fabricante/referencia | Equivalente permitido | Garantía/soporte | Stock/plazo | Fuente |
|----------|---------|----------------|----------------------|----------------------|------------------|------------|--------|
| Equipos informáticos para personal propio | Según necesidad | Tecnología adecuada, usabilidad universal | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA | ID_188_3.PDF, p.50 |
| Equipos de protección individual | Según necesidad | Para riesgos laborales | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA | ID_188_3.PDF, p.23 |

No se exige suministro de hardware al cliente ni stock/logística física.

# 4. Software, SaaS y licencias
| Producto | Fabricante | Métrica/cantidad | Entornos | Duración | Quién lo aporta | Fuente |
|----------|-----------|------------------|----------|----------|----------------|--------|
| Asistente Virtual SaaS | NO CONSTA | 1 | Producción, preproducción (mínimo) | Vigencia contrato | Adjudicatario | ID_188_3.PDF, p.1, 13-14, 29 |
| Panel de control | NO CONSTA | 1 | Web | Vigencia contrato | Adjudicatario | ID_188_3.PDF, p.14-15 |
| Licencias software/herramientas | NO CONSTA | Todas necesarias | Según arquitectura | Vigencia contrato | Adjudicatario | ID_188_3.PDF, p.13-14, 43 |
| Licencias cloud (SaaS/PaaS/IaaS) | Microsoft/AWS/GCP | Todas necesarias | Producción, preproducción | Vigencia contrato | Adjudicatario | ID_188_3.PDF, p.29-31, 43 |

# 5. Fabricantes, canal y cartas
| Fabricante | Requisito | Nivel/certificación/carta exigida | Momento | Fuente |
|------------|----------|-------------------------------|---------|--------|
| NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |

No se exige fabricante concreto, ni carta de canal, ni partnership, ni certificación de fabricante.

# 6. Subcontratación, UTE y medios externos
| Regla | Límite/condición | Declaración/autorización | Fuente |
|-------|------------------|-------------------------|--------|
| Subcontratación permitida | No se pueden subcontratar tareas críticas de implantación ni jefe de proyecto | Declarar en oferta parte a subcontratar, importe y nombre/perfil subcontratista | ID_188_2.PDF, p.75-76; ID_188_3.PDF, p.29 |
| UTE permitida | Sí, con compromiso y constitución formal si adjudicataria | Compromiso en oferta, escritura tras adjudicación | ID_188_2.PDF, p.19 |
| Medios externos para solvencia | Permitido | Compromiso de medios y documentación de la entidad externa | ID_188_2.PDF, p.18, 30, 92-93 |

# 7. Cadena de suministro y dependencias contractuales descritas
- El adjudicatario debe desplegar la solución sobre la infraestructura cloud (Azure, GCP, AWS) proporcionada por el Ayuntamiento, pero todos los recursos, servicios, licencias y costes asociados a la solución son a cargo del adjudicatario (ID_188_3.PDF, p.29-31, 43).
- El adjudicatario debe mantener la solución actualizada, sustituir recursos obsoletos y garantizar la integración con las plataformas y herramientas del Ayuntamiento (ID_188_3.PDF, p.29-31).
- El adjudicatario debe transferir conocimiento y entregar toda la información, datos y documentación generada al cierre del contrato, y realizar la destrucción certificada de datos (ID_188_3.PDF, p.9, 43).

# 8. SLA de proveedor/fabricante, garantías y soporte exigidos
- No se exige SLA back-to-back con fabricantes ni soporte de fabricante específico.
- El adjudicatario debe garantizar el soporte y mantenimiento de la solución durante toda la vigencia del contrato, incluyendo mantenimiento preventivo, correctivo y evolutivo (ID_188_3.PDF, p.17).
- El adjudicatario debe garantizar la disponibilidad 24x7x365 del asistente virtual, salvo paradas planificadas (ID_188_3.PDF, p.13).
- Penalizaciones por indisponibilidad: grave si supera 48h, muy grave si supera 5 días (ID_188_2.PDF, p.76).
- No se exige garantía de fabricante ni condiciones NBD/4h/onsite.

# 9. Logística, staging, stock, entrega, retirada y destrucción
- No se exige stock físico ni staging de hardware.
- El adjudicatario debe garantizar la entrega de toda la información, datos y documentación generada, en formato abierto y reutilizable, al cierre del contrato (ID_188_3.PDF, p.9, 43, 55-56).
- El adjudicatario debe realizar la destrucción certificada de datos y documentación al cierre del contrato (ID_188_3.PDF, p.9, 43).
- No se exige retirada física de equipos ni logística inversa.

# 10. Ambigüedades y datos no localizados
- No se exige ningún fabricante, referencia, ni equivalencia mínima de producto.
- No se exige carta de canal, partnership, ni certificación de fabricante.
- No se exige stock, logística física, staging, ni retirada de hardware.
- No se exige garantía de fabricante ni soporte NBD/4h/onsite.
- No se identifican SLA de terceros ni back-to-back.
- No se describen condiciones de cadena de suministro física, solo digital/cloud.
- No se exige homologación, sostenibilidad ni EOL/EOS de productos.
- No se exige ISO, ENS ni otra certificación de calidad o seguridad.
- No se exige declaración de fabricantes ni de canal en la oferta.
- No se exige carta de compromiso de fabricantes ni de proveedores cloud.
- No se exige declaración de stock ni de logística física.
- No se exige staging ni pruebas de pre-entrega física.

# 11. Documentos revisados
1. ID_188_1.PDF (Documento licitación real)
2. ID_188_2.PDF (Pliego de Cláusulas Administrativas Particulares)
3. ID_188_3.PDF (Pliego de Prescripciones Técnicas)
4. poc (Documento enlazado, detalle licitación)
5. poc (Documento enlazado, perfil contratante)
6. poc (Documento enlazado, perfil contratante)
7. 147409-2026 (Documento enlazado, sin texto extraíble; pendiente de lectura/OCR)
8. perfilContratante (Documento enlazado, perfil contratante)

# Tabla de trazabilidad
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|----------------|-----------|-----------------|-------------------|
| Solución SaaS | Software/SaaS | Obligatorio, BOT IA generativa y tradicional | ID_188_3.PDF | p.1, 13-14 | Leído |
| Panel de control | Software/SaaS | Obligatorio, acceso web, 5 usuarios | ID_188_3.PDF | p.14-15 | Leído |
| Licencias software | Licencias | Todas necesarias, a cargo adjudicatario | ID_188_3.PDF | p.13-14, 43 | Leído |
| Infraestructura MultiCloud | Cloud infra | Tenant/landing zone, IAM | ID_188_3.PDF | p.29, 43 | Leído |
| Recursos cloud | Cloud servicios | Azure/GCP/AWS, SaaS/PaaS/IaaS | ID_188_3.PDF | p.29-31 | Leído |
| Subcontratación | Regla | Permitida, salvo tareas críticas | ID_188_2.PDF | p.75-76 | Leído |
| UTE | Regla | Permitida, compromiso y escritura | ID_188_2.PDF | p.19 | Leído |
| SLA disponibilidad | SLA | 24x7x365, penalizaciones por indisponibilidad | ID_188_3.PDF, ID_188_2.PDF | p.13, 76 | Leído |
| Garantía fabricante | Garantía | NO CONSTA | - | - | - |
| Carta de canal | Canal | NO CONSTA | - | - | - |
| Stock/logística | Logística | NO CONSTA | - | - | - |
| Hardware físico | Producto | NO CONSTA | - | - | - |
| Certificación fabricante | Certificación | NO CONSTA | - | - | - |
| ISO/ENS | Certificación | NO CONSTA | - | - | - |
| SLA back-to-back | SLA | NO CONSTA | - | - | - |
| Cadena de suministro física | Cadena | NO CONSTA | - | - | - |
| Homologación/sostenibilidad | Requisito | NO CONSTA | - | - | - |
| EOL/EOS | Requisito | NO CONSTA | - | - | - |
| Declaración de fabricante | Declaración | NO CONSTA | - | - | - |
| Declaración de canal | Declaración | NO CONSTA | - | - | - |
| Carta de compromiso fabricante | Compromiso | NO CONSTA | - | - | - |
| Staging/pruebas físicas | Logística | NO CONSTA | - | - | - |

# Requisitos obligatorios del documento IA - fuentes para proyecto viabilidad
| Parámetro | Subcampos pedidos | Estado del pliego | Dato/literal localizado | Documento y apartado/página |
|-----------|-------------------|-------------------|-----------------------|-----------------------------|
| Volumen anual de negocios | Umbral, ámbito, mejor ejercicio, ventana, moneda, acreditación | ENCONTRADO EN EL PLIEGO | 181.595,44 € (mejor ejercicio 2023-2025, declaración responsable) | ID_188_2.PDF, p.63 |
| Patrimonio neto/ratios | Ejercicio, activos, pasivos, fórmula, umbral, acreditación | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | ID_188_2.PDF, p.63 |
| Seguro RC/riesgos profesionales | Importe, actividad, asegurador, inicio, fin, vigencia, cobertura, renovación | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | ID_188_2.PDF, p.67 |
| Certificados de buena ejecución | Objeto, similitud/CPV, importe, fechas, destinatario, prueba | ENCONTRADO EN EL PLIEGO | Servicios igual/similar naturaleza, 3 últimos años, importe igual/superior presupuesto sin IVA | ID_188_2.PDF, p.64 |
| ISO/ENS | Norma, versión, alcance, certificadora, caducidad, acreditación, equivalencias | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | ID_188_2.PDF, p.65; ID_188_3.PDF, p.45-46 |
| Fabricantes/partnerships | Fabricante, nivel, especialización, carta, expiración, acreditación | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | ID_188_3.PDF, p.13-14, 43 |
| Perfiles | Puesto, cantidad, titulación, experiencia, sector, certificaciones, dedicación, jornada, presencialidad, ubicación, idiomas, funciones, sustitución | ENCONTRADO EN EL PLIEGO | Ver tabla perfiles mínimos y requisitos | ID_188_3.PDF, p.24-27 |
| ROLECE/clasificación | Exigencia/alternativa, grupo, subgrupo, categoría, vigencia, inscripción, acreditación | ENCONTRADO EN EL PLIEGO | No exigida, pero inscripción en ROLECE acredita solvencia | ID_188_2.PDF, p.63 |

# Discrepancias y pendientes de aclaración
- No se han identificado discrepancias en la documentación revisada.
- Documento 147409-2026 pendiente de lectura/OCR; no se puede verificar si contiene condiciones adicionales.