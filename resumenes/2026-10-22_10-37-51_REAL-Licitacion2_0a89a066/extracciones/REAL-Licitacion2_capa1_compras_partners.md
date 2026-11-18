# 1. Resumen factual

La licitación para el servicio de Administración Workplace de Correos y CEX exige al adjudicatario la prestación de servicios de administración, gestión, mantenimiento, evolución y soporte de infraestructuras y plataformas tecnológicas de puesto de trabajo (físico, virtual y movilidad), incluyendo la administración de hardware, software, herramientas de gestión, plataformas de virtualización, dispositivos móviles y periféricos, así como la colaboración con fabricantes y la posibilidad de subcontratación de expertos bajo ciertas condiciones. No se exige la compra de hardware/software nuevo salvo para proyectos especiales, pero sí la administración y soporte de los existentes. Se establecen requisitos de experiencia, certificaciones deseables y soporte de fabricantes, pero no se exige carta de fabricante ni partnership formal. La subcontratación está permitida con límites y debe ser declarada. No se describen cadenas de suministro ni se exige stock, logística, staging, retirada o destrucción de equipos, salvo la gestión documental y de conocimiento. Los SLA y penalizaciones están definidos para la prestación del servicio, pero no se exigen SLA back-to-back con fabricantes ni garantías de fabricante específicas.

# 2. Mapa de suministros y terceros
| Elemento/necesidad | Tipo | Cantidad/volumen | Especificacion | Quien debe aportarlo | Fuente |
|--------------------|------|------------------|---------------|---------------------|--------|
| ThinClient HP | Hardware | >12.000 | Windows7/Windows IOT 10/Otros | Cliente (administrar) | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.34 |
| Servidores virtuales Citrix | Hardware | 100 infra, 600 servicio | DDCs, StoreFront, Licenserver, SystemCenter, SSOO W2008-2019 | Cliente (administrar) | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.35 |
| VDIs Azure WVD | Hardware/Cloud | 1.000 | SSOO W10 | Cliente (administrar) | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.35 |
| Chasis Cisco UCS, servidores UCS, switches Nexus | Hardware | 8 chasis, 32 B200 M5, 48 B200 M4, 4 Nexus 9300 | Cisco UCS 5108, WS-C3560X-48T-L, UCS 6248 | Cliente (administrar) | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.35 |
| Cabinas NetApp | Hardware | 4 cabinas | FAS8020, AFF8040, DS2246, DS4246 | Cliente (administrar) | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.35 |
| Equipos físicos de puesto de trabajo | Hardware | >16.000 | 68% sobremesa/thinclient, 25% portátiles, 5% dispensadores, 2% autoservicio | Cliente (administrar) | ANEXO I.pdf p.10, DOC20240806095753Pliegodefinitivofirmado.pdf p.41 |
| Dispositivos de movilidad (PDA, smartphones, tablets) | Hardware | 34.000 PDA Honeywell, 2.000/400 Zebra, 3.100 smartphones, 130 iPhone, 100 tablets | Modelos y SO especificados | Cliente (administrar) | ANEXO I.pdf p.14, DOC20240806095753Pliegodefinitivofirmado.pdf p.45 |
| Plataformas de gestión (SCCM, HPDM, MDT, DA, INTUNE, MDM) | Software | NO CONSTA | Herramientas de gestión centralizada | Cliente (administrar) | ANEXO I.pdf p.11, DOC20240806095753Pliegodefinitivofirmado.pdf p.42 |
| MDM Workspace One UEM OnPremise/SaaS | Software | 3 entornos | VmWare, versiones 2209 y 2302, migración a SaaS | Cliente (administrar) | ANEXO I.pdf p.14, DOC20240806095753Pliegodefinitivofirmado.pdf p.45 |
| PoST (Remedy ITSM) | Software | NO CONSTA | Herramienta de ticketing | Cliente (administrar) | ANEXO I.pdf p.25, DOC20240806095753Pliegodefinitivofirmado.pdf p.56 |
| Microsoft Teams, Office 365 | Software | NO CONSTA | Herramientas colaborativas | Cliente (administrar) | ANEXO I.pdf p.12, DOC20240806095753Pliegodefinitivofirmado.pdf p.43 |
| Panel de expertos/fabricante | Servicio externo | Bajo demanda | Soporte de fabricantes Microsoft, NetApp, Cisco, Citrix, etc. | Adjudicatario (subcontratar si no dispone) | ANEXO I.pdf p.34, DOC20240806095753Pliegodefinitivofirmado.pdf p.63 |

# 3. Productos, hardware y materiales
| Producto | Cantidad | Caracteristicas | Fabricante/referencia | Equivalente permitido | Garantia/soporte | Stock/plazo | Fuente |
|----------|----------|----------------|----------------------|----------------------|------------------|------------|--------|
| ThinClient HP | >12.000 | Windows7/Windows IOT 10/Otros | HP | NO CONSTA | NO CONSTA | NO CONSTA | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.34 |
| Servidores UCS B200 M5/M4 | 32/48 | Blade servers | Cisco | NO CONSTA | NO CONSTA | NO CONSTA | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.35 |
| Cabinas NetApp FAS8020/AFF8040 | 2/2 | Almacenamiento | NetApp | NO CONSTA | NO CONSTA | NO CONSTA | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.35 |
| PDA Honeywell EDA52 | 34.000 | Android 11 | Honeywell | NO CONSTA | NO CONSTA | NO CONSTA | ANEXO I.pdf p.14, DOC20240806095753Pliegodefinitivofirmado.pdf p.45 |
| Smartphones Samsung/Xiaomi/Huawei/Apple | 3.100/130 | Modelos y SO especificados | Samsung/Xiaomi/Huawei/Apple | NO CONSTA | NO CONSTA | NO CONSTA | ANEXO I.pdf p.14, DOC20240806095753Pliegodefinitivofirmado.pdf p.45 |
| Tablets Samsung TAB A8 LTE | 100 | Android >8 | Samsung | NO CONSTA | NO CONSTA | NO CONSTA | ANEXO I.pdf p.14, DOC20240806095753Pliegodefinitivofirmado.pdf p.45 |

# 4. Software, SaaS y licencias
| Producto | Fabricante | Metrica/cantidad | Entornos | Duracion | Quien lo aporta | Fuente |
|---------|-----------|------------------|----------|----------|----------------|--------|
| Citrix Xenapp | Citrix | NO CONSTA | Virtualización | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.5, DOC20240806095753Pliegodefinitivofirmado.pdf p.36 |
| Hyper-V | Microsoft | NO CONSTA | Virtualización | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.5, DOC20240806095753Pliegodefinitivofirmado.pdf p.36 |
| NetApp ONTAP | NetApp | NO CONSTA | Almacenamiento | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.5, DOC20240806095753Pliegodefinitivofirmado.pdf p.36 |
| SQL Server | Microsoft | NO CONSTA | BBDD | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.5, DOC20240806095753Pliegodefinitivofirmado.pdf p.36 |
| Windows Virtual Desktop (WVD) | Microsoft/Azure | 1.000 VDIs | Cloud | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.4, DOC20240806095753Pliegodefinitivofirmado.pdf p.35 |
| Workspace One UEM | VmWare | 3 entornos | OnPremise/SaaS | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.14, DOC20240806095753Pliegodefinitivofirmado.pdf p.45 |
| Remedy ITSM (PoST) | BMC | NO CONSTA | Ticketing | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.25, DOC20240806095753Pliegodefinitivofirmado.pdf p.56 |
| Microsoft Teams, Office 365 | Microsoft | NO CONSTA | Colaboración | NO CONSTA | Cliente (administrar) | ANEXO I.pdf p.12, DOC20240806095753Pliegodefinitivofirmado.pdf p.43 |

# 5. Fabricantes, canal y cartas
| Fabricante | Requisito | Nivel/certificacion/carta exigida | Momento | Fuente |
|-----------|----------|-------------------------------|---------|--------|
| Microsoft, NetApp, Cisco, Citrix | Soporte de fabricante a técnicos | NO CONSTA carta/partner obligatoria, solo "deseable" certificación | Ejecución (soporte a técnicos) | ANEXO I.pdf p.34, DOC20240806095753Pliegodefinitivofirmado.pdf p.63 |
| NetApp | Certificación deseable | Certificación NetApp (deseable) | Ejecución (perfil) | ANEXO I.pdf p.35, DOC20240806095753Pliegodefinitivofirmado.pdf p.66 |
| Cisco | Certificación deseable | CCNA/CCNP (deseable) | Ejecución (perfil) | ANEXO I.pdf p.36, DOC20240806095753Pliegodefinitivofirmado.pdf p.68 |
| Citrix | Certificación deseable | Certificación Citrix (deseable) | Ejecución (perfil) | ANEXO I.pdf p.34, DOC20240806095753Pliegodefinitivofirmado.pdf p.65 |
| Microsoft | Certificación deseable | Certificación Microsoft (deseable) | Ejecución (perfil) | ANEXO I.pdf p.34, DOC20240806095753Pliegodefinitivofirmado.pdf p.65 |
| VmWare | Certificación deseable | Certificación Workspace One UEM/AirWatch (deseable) | Ejecución (perfil) | ANEXO I.pdf p.39, DOC20240806095753Pliegodefinitivofirmado.pdf p.70 |

# 6. Subcontratacion, UTE y medios externos
| Regla | Limite/condicion | Declaracion/autorizacion | Fuente |
|-------|------------------|------------------------|--------|
| Subcontratación permitida | No tareas críticas (gestión y coordinación del servicio no subcontratable) | Declarar parte subcontratada, importe, nombre/perfil subcontratista en oferta; comunicar cambios | DOC20240806095753Pliegodefinitivofirmado.pdf p.25 |
| Subcontratación de expertos de fabricante | Permitida bajo demanda si no hay perfil propio | Declarar en oferta y comunicar | ANEXO I.pdf p.40, DOC20240806095753Pliegodefinitivofirmado.pdf p.71 |
| UTE | Permitida | Declaración compromiso constitución UTE en oferta | DOC20240806095753Pliegodefinitivofirmado.pdf p.11 |

# 7. Cadena de suministro y dependencias contractuales descritas
NO CONSTA EN LA DOCUMENTACION REVISADA ninguna descripción o condicionamiento contractual específico sobre la cadena de suministro, logística de aprovisionamiento, reposición, lead time, EOL/EOS, homologaciones, sostenibilidad, ni restricciones de canal o reposición.

# 8. SLA de proveedor/fabricante, garantias y soporte exigidos
| Elemento | SLA/garantía/soporte | Condición | Fuente |
|----------|---------------------|-----------|--------|
| Servicio adjudicatario | SLA definidos en ANS (Anexo XVII): tiempos de respuesta, resolución, disponibilidad, sustitución perfiles, penalizaciones económicas | Penalizaciones por incumplimiento, posibilidad de resolución anticipada | DOC20240806095753Pliegodefinitivofirmado.pdf p.111-118 |
| Fabricante | NO CONSTA SLA back-to-back ni garantía fabricante exigida | NO CONSTA | NO CONSTA |

# 9. Logistica, staging, stock, entrega, retirada y destruccion
NO CONSTA EN LA DOCUMENTACION REVISADA ninguna obligación de stock mínimo, logística de entrega, staging, retirada o destrucción de equipos, ni condiciones de almacenamiento, transporte o reciclaje.

# 10. Ambiguedades y datos no localizados
- No se exige carta de fabricante ni partnership formal obligatorio, solo certificaciones "deseables" para perfiles.
- No se exige compra ni suministro de hardware/software nuevo salvo para proyectos especiales, que se presupuestan aparte.
- No se describen condiciones de cadena de suministro, stock, logística, lead time, EOL/EOS, homologaciones, sostenibilidad, ni restricciones de canal.
- No se exige garantía de fabricante ni soporte back-to-back.
- No se exige staging, retirada ni destrucción de equipos.
- No se exige declaración de canal autorizado ni compromiso de suministro de fabricante.
- No se exige declaración de medios externos salvo para subcontratación de expertos.

# 11. Documentos revisados
1. ANEXO I.pdf
2. Anuncio.pdf
3. DOC20240806095753Pliegodefinitivofirmado.pdf
4. DOC_CD2024-000901195.pdf
5. poc (enlace a licitación)
6. poc (perfil contratante)
7. CORREOS-Codigo-General-de-Conducta.pdf (no leído, error 404)
8. perfil-contratante
9. PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf

# 12. Trazabilidad
| Requisito/dato | Tipo | Valor/condicion | Documento | Pagina/apartado | Estado de lectura |
|----------------|------|----------------|-----------|-----------------|------------------|
| ThinClient HP | Hardware | >12.000, administrar | ANEXO I.pdf | p.4 | Leído |
| Certificación NetApp | Certificación deseable | Deseable, no obligatoria | ANEXO I.pdf | p.35 | Leído |
| Subcontratación permitida | Regla | No tareas críticas, declarar | DOC20240806095753Pliegodefinitivofirmado.pdf | p.25 | Leído |
| SLA servicio | SLA | ANS definidos, penalizaciones | DOC20240806095753Pliegodefinitivofirmado.pdf | p.111-118 | Leído |
| Cadena de suministro | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |
| Garantía fabricante | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |
| Stock/logística | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA | NO CONSTA |

# Discrepancias y pendientes de aclaración
No se han identificado discrepancias en la documentación revisada. No se localizan obligaciones de suministro, canal, partnership, stock, logística, garantías de fabricante, ni condiciones de cadena de suministro más allá de la administración de los activos existentes del cliente y la subcontratación de expertos bajo demanda.