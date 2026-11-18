# 1. Resumen factual

La licitación AI240006 para el "servicio de Administración Workplace" de Correos y CEX exige al adjudicatario la prestación de servicios de administración, gestión, mantenimiento, evolución y soporte de infraestructuras y plataformas de virtualización, puesto de trabajo y movilidad, incluyendo hardware, software, herramientas de gestión y soporte de fabricantes. El adjudicatario debe administrar y mantener infraestructuras y plataformas ya existentes (con fabricantes y modelos concretos), pero no se exige expresamente el suministro de nuevos equipos o licencias salvo para cubrir necesidades derivadas de la administración, actualización, soporte y evolución de los sistemas durante la ejecución del contrato. Se permite la subcontratación parcial, con limitaciones para tareas críticas. Se exige soporte de fabricantes y posibilidad de recurrir a expertos externos, incluso subcontratados al fabricante, bajo demanda. No se localizan requisitos de canal, cartas de fabricante, ni compromisos de suministro de hardware/software nuevos, salvo los derivados de la administración y soporte de los sistemas existentes. No se describen cadenas de suministro ni condiciones logísticas específicas más allá de la gestión y soporte de los activos existentes. Los SLA y penalizaciones están definidos para la prestación del servicio, no para suministros de terceros.

# 2. Mapa de suministros y terceros
| Elemento/necesidad | Tipo | Cantidad/volumen | Especificación | Quién debe aportarlo | Fuente |
|--------------------|------|------------------|---------------|---------------------|--------|
| ThinClient HP | Hardware | >12.000 | HP, Windows7/IoT10/Otros | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.34 |
| Servidores virtuales Citrix | Hardware | 100+600 | DDCs, StoreFront, etc. | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.35 |
| VDIs Azure WVD | Hardware/Cloud | 1.000 | W10 | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.35 |
| Chasis Cisco UCS, servidores, switches | Hardware | 8 chasis, 32+48 servidores, 2+8+4 switches | Cisco UCS 5108, B200 M4/M5, WS-C3560X-48T-L, Nexus 9300 | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.35 |
| Cabinas NetApp | Hardware | 4 cabinas | FAS8020, AFF8040, DS2246, DS4246 | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.35 |
| Dispositivos movilidad (PDA, smartphones, tablets) | Hardware | 34.000+ | Honeywell EDA52, Zebra TC56/57, Samsung, Xiaomi, Apple, Zelenza | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.45 |
| Plataformas MDM Workspace One UEM | Software/Infra | 3 entornos | VmWare, versiones 2209/2302 | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.45 |
| Herramientas gestión (SCCM, HPDM, MDT, DA, INTUNE, MDM) | Software | No especificado | Microsoft, HP, VmWare | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.42 |
| Herramienta ticketing PoST (Remedy ITSM) | Software | 1 | Remedy | Cliente (uso obligatorio) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.56 |
| Panel de expertos/fabricante | Servicio externo | Bajo demanda | Microsoft, NetApp, Cisco, Citrix, etc. | Adjudicatario (subcontratar si no dispone) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.63, 71 |

# 3. Productos, hardware y materiales
| Producto | Cantidad | Características | Fabricante/referencia | Equivalente permitido | Garantía/soporte | Stock/plazo | Fuente |
|----------|----------|----------------|----------------------|----------------------|------------------|------------|--------|
| ThinClient HP | >12.000 | Windows7/IoT10/Otros | HP | NO CONSTA | NO CONSTA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.34 |
| Servidores Cisco UCS | 32+48 | B200 M4/M5 | Cisco | NO CONSTA | NO CONSTA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.35 |
| Cabinas NetApp | 4 | FAS8020, AFF8040 | NetApp | NO CONSTA | NO CONSTA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.35 |
| Dispositivos movilidad | 34.000+ | PDA Honeywell EDA52, Zebra TC56/57, etc. | Honeywell, Zebra, Samsung, Xiaomi, Apple, Zelenza | NO CONSTA | NO CONSTA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.45 |

# 4. Software, SaaS y licencias
| Producto | Fabricante | Metrica/cantidad | Entornos | Duración | Quién lo aporta | Fuente |
|---------|-----------|-----------------|----------|----------|----------------|--------|
| Citrix Xenapp | Citrix | No especificado | Virtualización | No especificado | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.36 |
| Hyper-V | Microsoft | No especificado | Virtualización | No especificado | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.36 |
| NetApp ONTAP | NetApp | No especificado | Almacenamiento | No especificado | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.36 |
| SQL Server | Microsoft | No especificado | BBDD | No especificado | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.36 |
| Workspace One UEM | VmWare | 3 entornos | MDM | No especificado | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.45 |
| SCCM, HPDM, MDT, DA, INTUNE, MDM | Microsoft, HP, VmWare | No especificado | Gestión puestos | No especificado | Cliente (administrar) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.42 |
| Remedy ITSM (PoST) | BMC | 1 | Ticketing | No especificado | Cliente (uso obligatorio) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.56 |

# 5. Fabricantes, canal y cartas
| Fabricante | Requisito | Nivel/certificación/carta exigida | Momento | Fuente |
|------------|----------|-------------------------------|---------|--------|
| Microsoft, NetApp, Cisco, Citrix, etc. | Soporte experto bajo demanda | NO CONSTA carta/certificación obligatoria, pero "deseables" certificaciones en perfiles | Ejecución (cuando se requiera soporte experto) | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.63, 71 |
| NO CONSTA | Carta de canal/fabricante | NO CONSTA | NO CONSTA | NO CONSTA |

# 6. Subcontratación, UTE y medios externos
| Regla | Límite/condición | Declaración/autorización | Fuente |
|-------|------------------|------------------------|--------|
| Subcontratación permitida | No tareas críticas (gestión y coordinación del servicio) | Declarar parte subcontratada, importe y subcontratista en oferta; autorización previa para subcontratación posterior | DOC20240806095753Pliegodefinitivofirmado.pdf, p.25 |
| Subcontratación de expertos/fabricante | Permitida si no se dispone de perfil experto | Declarar en oferta si se conoce; autorización previa si afecta a datos personales | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.71; p.21 |
| UTE | Permitida | Declaración de compromiso en oferta | DOC20240806095753Pliegodefinitivofirmado.pdf, p.11 |

# 7. Cadena de suministro y dependencias contractuales descritas
NO CONSTA EN LA DOCUMENTACION REVISADA una descripción o condicionamiento contractual específico de la cadena de suministro (fabricantes, mayoristas, logística, etc.) más allá de la obligación de recurrir a soporte de fabricante bajo demanda y la gestión de activos existentes.

# 8. SLA de proveedor/fabricante, garantías y soporte exigidos
- Los SLA y penalizaciones están definidos para la prestación del servicio del adjudicatario a Correos/CEX, no para suministros de terceros ni para soporte back-to-back con fabricantes. (DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo XVII, p.111-118)
- Se exige que el adjudicatario tenga capacidad de recurrir a soporte de fabricante y expertos externos bajo demanda, pero no se exige un SLA contractual con fabricantes ni garantías de hardware/software nuevas. (DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.63, 71)

# 9. Logística, staging, stock, entrega, retirada y destrucción
- El adjudicatario debe preparar, empaquetar y enviar material de movilidad a centros de Correos/CEX según necesidades corporativas (DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.49).
- No se exige stock mínimo, ni plazos de suministro de hardware/software, ni condiciones de retirada o destrucción de equipos, salvo la obligación de mantener la documentación y realizar la migración de información a otros sistemas si lo requiere Correos/CEX (DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.38, 44, 49).
- No se describen condiciones de staging, logística de entrega inicial, ni destrucción de hardware/software.

# 10. Ambigüedades y datos no localizados
- No se localiza obligación expresa de suministro de hardware/software/licencias nuevos por parte del adjudicatario, salvo para cubrir necesidades de administración, actualización y soporte de los sistemas existentes.
- No se exige carta de fabricante, canal o partnership obligatorio.
- No se describen condiciones de cadena de suministro, stock, lead time, EOL/EOS, homologaciones, sostenibilidad, ni logística de retirada/destrucción.
- No se exige SLA back-to-back con fabricantes.
- No se exige garantía de hardware/software nueva.
- No se exige compromiso de suministro de piezas o repuestos.
- No se exige staging ni logística de entrega inicial.

# 11. Documentos revisados
1. ANEXO I.pdf
2. Anuncio.pdf
3. DOC20240806095753Pliegodefinitivofirmado.pdf
4. DOC_CD2024-000901195.pdf
5. poc (detalle licitación)
6. poc (perfil contratante)
7. CORREOS-Codigo-General-de-Conducta.pdf (NO DISPONIBLE, 404)
8. perfil-contratante
9. PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf

# 12. Trazabilidad de requisitos y datos
| Requisito/dato | Tipo | Valor/condición | Documento | Página/apartado | Estado de lectura |
|----------------|------|-----------------|-----------|------------------|-------------------|
| ThinClient HP | Hardware | >12.000, administrar | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.34 | Leído |
| Servidores Cisco UCS | Hardware | 32+48, administrar | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.35 | Leído |
| Cabinas NetApp | Hardware | 4, administrar | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.35 | Leído |
| Dispositivos movilidad | Hardware | 34.000+, administrar | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.45 | Leído |
| Citrix Xenapp | Software | administrar | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.36 | Leído |
| Workspace One UEM | Software | administrar | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.45 | Leído |
| Panel de expertos/fabricante | Servicio externo | subcontratar si no dispone | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.63, 71 | Leído |
| Subcontratación permitida | Regla | No tareas críticas | DOC20240806095753Pliegodefinitivofirmado.pdf | p.25 | Leído |
| SLA de servicio | SLA | definido para adjudicatario, no para terceros | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo XVII, p.111-118 | Leído |
| Logística movilidad | Logística | preparación/envío material movilidad | DOC20240806095753Pliegodefinitivofirmado.pdf | Anexo I, p.49 | Leído |
| Carta de fabricante/canal | Requisito | NO CONSTA | NO CONSTA | NO CONSTA | Leído |
| Stock mínimo | Requisito | NO CONSTA | NO CONSTA | NO CONSTA | Leído |
| Garantía hardware/software | Requisito | NO CONSTA | NO CONSTA | NO CONSTA | Leído |
| Cadena de suministro | Requisito | NO CONSTA | NO CONSTA | NO CONSTA | Leído |

# 13. Requisitos obligatorios del documento IA - fuentes para proyecto viabilidad
| Parámetro | Subcampos pedidos | Estado del pliego | Dato/literal localizado | Documento y apartado/página |
|-----------|--------------------|------------------|-----------------------|-----------------------------|
| Volumen anual de negocios | Umbral, ámbito, mejor ejercicio, ventana, moneda, acreditación | ENCONTRADO EN EL PLIEGO | 1.190.000 €, ámbito del contrato, mejor ejercicio de los 3 últimos, euros, cuentas anuales aprobadas y depositadas | DOC20240806095753Pliegodefinitivofirmado.pdf, p.7, Anexo V |
| Patrimonio neto/ratios | Ejercicio, activos, pasivos, fórmula, umbral, acreditación | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, p.7, Anexo V |
| Seguro RC/riesgos profesionales | Importe, actividad, asegurador, inicio, fin, vigencia, cobertura, renovación | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, p.7, Anexo V |
| Certificados de buena ejecución | Objeto, similitud, importe, fechas, destinatario, prueba | ENCONTRADO EN EL PLIEGO | 3 servicios igual/similar, 1.190.000 € anual, últimos 3 años, certificado de correcta ejecución | DOC20240806095753Pliegodefinitivofirmado.pdf, p.7, Anexo V |
| ISO/ENS | Norma, versión, alcance, certificadora, caducidad, acreditación | ENCONTRADO EN EL PLIEGO | ISO 27001 e ISO 20000 o equivalentes, durante ejecución, certificado | DOC20240806095753Pliegodefinitivofirmado.pdf, p.7, Anexo V |
| Fabricantes/partnerships | Fabricante, nivel, especialización, carta, expiración, acreditación | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I |
| Perfiles | Puesto, cantidad, titulación, experiencia, certificaciones, dedicación, funciones, sustitución | ENCONTRADO EN EL PLIEGO | Detallados por perfil, experiencia mínima, deseables certificaciones, dedicación, funciones, sustitución por panel de expertos o subcontratación | DOC20240806095753Pliegodefinitivofirmado.pdf, Anexo I, p.63-71 |
| ROLECE/clasificación | Exigencia, grupo, subgrupo, categoría, vigencia, inscripción, acreditación | NO CONSTA EN LA DOCUMENTACION REVISADA | NO CONSTA | DOC20240806095753Pliegodefinitivofirmado.pdf, p.7, Anexo V |

# 14. Discrepancias y pendientes de aclaración
- No se han identificado discrepancias en la documentación revisada.
- Pendiente de verificar: CORREOS-Codigo-General-de-Conducta.pdf (no disponible, 404).