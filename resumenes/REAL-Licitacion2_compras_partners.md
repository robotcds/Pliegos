1. Veredicto ejecutivo Compras / Partners: ALTO RIESGO

2. Resumen ejecutivo:
La licitación exige la prestación integral de servicios de administración workplace (virtualización, puesto de trabajo, movilidad) para Correos y CEX, con recursos dedicados y expertos en tecnologías muy específicas (Citrix, Hyper-V, NetApp, Cisco, SCCM, Workspace One UEM, SQL Server, etc.). El adjudicatario debe aportar todos los medios personales, materiales y licencias necesarias, salvo los sistemas y dispositivos ya existentes en el cliente. El análisis de solvencia de perfiles revela gaps críticos en todos los perfiles técnicos clave, que solo pueden cubrirse mediante contratación externa, partners o subcontratistas especializados. No hay en la red ficticia partners directos para Citrix, NetApp, SCCM, Workspace One UEM ni DBA SQL Server, y tampoco hay expertos acreditados en Cisco. La subcontratación está permitida salvo para la gestión y coordinación del servicio. El riesgo de dependencia de partners externos es crítico, y la viabilidad de la oferta depende de cerrar acuerdos con partners/freelance de alto nivel y obtener cartas de compromiso y solvencia externa. Sin estos acuerdos, la oferta sería excluida por incumplimiento de requisitos técnicos mínimos.

3. Mapa de necesidades externas:
| Necesidad                                 | Tipo         | Requisito literal/derivado | Cantidad/volumen | Especificación                                                                 | Quien lo aporta         | Acción                                    |
|-------------------------------------------|--------------|---------------------------|------------------|-------------------------------------------------------------------------------|------------------------|-------------------------------------------|
| Administrador de Sistemas Virtualizados   | Personal     | Literal                   | 3+1 recursos     | Experto en Hyper-V, Citrix Xenapp, SCVMM, Windows Server, scripting, clusters | Externo                | Contratar/partner urgente                 |
| Administrador de NetApp                   | Personal     | Literal                   | 1 recurso        | Experto ONTAP, SAN/NAS, scripting, 3 años exp.                                | Externo                | Contratar/partner urgente                 |
| Administrador de BBDD SQL                 | Personal     | Literal                   | 1 recurso        | DBA SQL Server, migraciones, HA, 3 años exp.                                  | Externo                | Contratar/partner urgente                 |
| Administrador de Comunicaciones Cisco     | Personal     | Literal                   | 1 recurso        | Cisco Catalyst/Nexus, routing, CCNA/CCNP, 5 años exp.                         | Externo                | Contratar/partner urgente                 |
| Administrador de Sistemas (Workplace)     | Personal     | Literal                   | 3 recursos       | SCCM, MDT, Workspace One UEM, Intune, HPDM, scripting, 3 años exp.            | Externo                | Contratar/partner urgente                 |
| Administrador de Sistemas de Movilidad    | Personal     | Literal                   | 2 recursos       | Android/iOS, Workspace One UEM, SOTI, MDM/MAM/MCM, 3 años exp.                | Externo                | Contratar/partner urgente                 |
| Bolsa de expertos en tecnologías clave    | Personal     | Literal                   | Variable         | 5 años exp. en tecnologías demandadas                                         | Externo                | Contratar/partner urgente                 |
| Certificaciones técnicas (Citrix, NetApp, Cisco, SCCM, Workspace One UEM) | Certificación | Literal/deseable           | Variable         | Certificados oficiales para perfiles clave                                     | Externo                | Contratar/partner urgente                 |
| Nivel de inglés técnico/conversacional    | Personal     | Literal                   | Todos técnicos   | Acreditación nivel conversación y lectura técnica                             | Externo                | Validar en contratación                   |
| Declaración y certificado de experiencia  | Documental   | Literal                   | Todos recursos   | Certificado de experiencia mínima 1 año en puesto similar                     | Externo                | Solicitar a candidatos/partners           |

4. Productos, hardware y materiales:
| Producto                  | Cantidad | Características                                                                 | Fabricante obligatorio/referencia | Equivalente permitido | Garantía/soporte | Stock | Lead time | Responsable |
|--------------------------|----------|-------------------------------------------------------------------------------|-------------------------------|----------------------|------------------|-------|-----------|-------------|
| Portátiles para equipo   | 8-10     | i5 9th gen+, SSD, 8-16GB RAM, Win10/11 Pro                                    | No (especificación mínima)    | Sí                   | 3 años NBD       | Sí    | 1-2 sem   | Adjudicatario|
| Smartphones para equipo  | 2-3      | Gama media, Android/iOS, compatible MDM                                       | No                          | Sí                   | 2 años           | Sí    | 1-2 sem   | Adjudicatario|
| Licencias Office/Teams   | 8-10     | Microsoft 365 Business/Teams                                                   | Microsoft                   | Sí                   | SaaS             | N/A   | Inmediato | Adjudicatario|
| Software de administración remota | 8-10 | Herramienta de acceso remoto, compatible con cliente | No | Sí | SaaS | N/A | Inmediato | Adjudicatario|

5. Software, SaaS y licencias:
| Producto                | Fabricante | Licencias/metrica | Entornos | Duración | Aporta | Ambiguo | Acción |
|------------------------|------------|-------------------|----------|----------|--------|---------|--------|
| Microsoft 365/Teams    | Microsoft  | Usuario           | Todos    | 24m      | Adjud. | No      | Comprar|
| SCCM, Intune           | Microsoft  | Usuario/dispositivo| Todos   | 24m      | Cliente| Sí      | Preguntar cliente si aporta licencias |
| Workspace One UEM      | VMware     | Usuario/dispositivo| Todos   | 24m      | Cliente| Sí      | Preguntar cliente si aporta licencias |
| Citrix Xenapp          | Citrix     | Usuario/concurrente| Todos   | 24m      | Cliente| Sí      | Preguntar cliente si aporta licencias |
| NetApp ONTAP           | NetApp     | Sistema           | Todos    | 24m      | Cliente| Sí      | Preguntar cliente si aporta licencias |
| Remedy ITSM            | BMC        | Usuario           | Todos    | 24m      | Cliente| No      | Validar acceso y formación |

6. Fabricantes, canal y cartas:
| Fabricante | Obligatorio/Referencia | Partner/canal disponible | Carta requerida | Estado | Fecha objetivo | Riesgo |
|------------|-----------------------|--------------------------|-----------------|--------|----------------|--------|
| Citrix     | Sí (tecnología clave) | No en red ficticia       | Sí              | No     | T-15 días      | Crítico |
| NetApp     | Sí (tecnología clave) | No en red ficticia       | Sí              | No     | T-15 días      | Crítico |
| Cisco      | Sí (tecnología clave) | No en red ficticia       | Sí              | No     | T-15 días      | Crítico |
| VMware     | Sí (Workspace One UEM)| No en red ficticia       | Sí              | No     | T-15 días      | Crítico |
| Microsoft  | Sí (SCCM, Intune)     | Cloud Partner Ficticio   | Sí (si compra licencias) | Parcial | T-15 días | Medio |

7. Subcontratación, UTE y medios externos:
- Límite subcontratación: Permitida salvo gestión/coordinación del servicio.
- Actividades no subcontratables: Gestión y coordinación del servicio.
- Subcontratistas a declarar: Si aportan solvencia o medios personales críticos.
- UTE: Permitida, socios preidentificados (Cloud Partner Ficticio, Mobile Studio Ficticio).
- Integración de solvencia: Necesaria para cubrir gaps de perfiles y experiencia.

8. Make / Buy / Partner:
| Capacidad                        | Interno | Comprar | Partner | Autonomo | Recomendación         | Justificación |
|----------------------------------|---------|---------|---------|----------|----------------------|--------------|
| Admin. Sistemas Virtualizados   | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |
| Admin. NetApp                  | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |
| Admin. BBDD SQL                | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |
| Admin. Comunicaciones Cisco    | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |
| Admin. Workplace (SCCM, UEM)   | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |
| Admin. Movilidad (UEM, SOTI)   | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |
| Certificaciones técnicas        | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |
| Inglés técnico                  | No      | No      | Sí      | Sí       | Partner/autónomo     | Gap crítico   |

9. Mapa de partners propuestos:
| Necesidad                        | Partner/autónomo candidato | Encaje | Documentación disponible | Gap | Criticidad | Acción |
|-----------------------------------|----------------------------|--------|-------------------------|-----|------------|--------|
| Admin. Virtualización/Citrix      | Buscar mercado             | No     | No                      | Sí  | Crítica     | Buscar partner/freelance |
| Admin. NetApp                    | Buscar mercado             | No     | No                      | Sí  | Crítica     | Buscar partner/freelance |
| Admin. SQL Server                | Buscar mercado             | No     | No                      | Sí  | Crítica     | Buscar partner/freelance |
| Admin. Cisco                     | Buscar mercado             | No     | No                      | Sí  | Crítica     | Buscar partner/freelance |
| Admin. SCCM/Workspace One        | Buscar mercado             | No     | No                      | Sí  | Crítica     | Buscar partner/freelance |

10. Cadena de suministro y dependencias:
Cadena: Cliente (Correos/CEX) → Adjudicatario (Sermicro Software Ficticio S.L.) → Partner/freelance especializado (Citrix, NetApp, Cisco, SCCM, UEM, SQL) → Fabricante (soporte de 3er nivel/licencias) → Distribuidor (si aplica).

| Dependencia                  | Criticidad | Single point of failure | Alternativas | Riesgo |
|------------------------------|------------|------------------------|--------------|--------|
| Partner Citrix/NetApp/Cisco  | Crítica    | Sí                     | No           | Muy alto|
| Freelance experto            | Crítica    | Sí                     | No           | Muy alto|
| Licencias cliente            | Alta       | Sí (si no aporta)      | No           | Alto    |
| Soporte fabricante           | Alta       | Sí                     | No           | Alto    |

11. SLA back-to-back:
| SLA cliente                  | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|------------------------------|-----------------------------|-------------------------|-----|-----------------------|
| Resolución P1 <4h            | Partner/freelance           | No evidenciado          | Sí  | Contrato penalizable  |
| Disponibilidad 99,5%         | Partner/freelance           | No evidenciado          | Sí  | Contrato penalizable  |
| Cobertura 24x7 guardias      | Partner/freelance           | No evidenciado          | Sí  | Contrato penalizable  |

12. Logística, staging, stock, garantía y retirada:
- Entregas: No hay suministro masivo de hardware al cliente, solo para el equipo propio.
- Staging y asset tagging: No aplica salvo para el equipo propio.
- Instalación: No aplica (servicio sobre infraestructuras existentes).
- Sustitución/RAEE: No aplica.
- Destrucción: No aplica.
- Certificaciones: No aplica.

13. Riesgos de compras y partners:
| Dependencia                  | Riesgo      | Impacto | Probabilidad | Mitigación                | Responsable |
|------------------------------|------------|---------|-------------|---------------------------|-------------|
| Partner/freelance experto    | Crítico     | Muy alto| Muy alta     | Contrato, carta compromiso| Compras     |
| Licencias cliente            | Crítico     | Alto    | Alta         | Preguntar, carta cliente  | Preventa    |
| Certificaciones técnicas     | Crítico     | Alto    | Alta         | Validar CV/certificados   | RRHH        |
| SLA back-to-back             | Crítico     | Alto    | Alta         | Contrato penalizable      | Compras     |

14. Matriz de acciones de Compras/Preventa:
| Acción                        | Necesidad                        | Responsable sugerido | Prioridad | Fecha objetivo | Bloquea oferta |
|-------------------------------|----------------------------------|---------------------|-----------|---------------|----------------|
| Buscar partners/freelance     | Todos perfiles técnicos clave     | Compras             | Alta      | T-15 días      | Sí             |
| Solicitar cartas compromiso   | Partners/freelance               | Compras             | Alta      | T-12 días      | Sí             |
| Validar licencias cliente     | SCCM, Citrix, NetApp, UEM, SQL    | Preventa            | Alta      | T-10 días      | Sí             |
| Validar CV/certificados       | Todos perfiles técnicos           | RRHH                | Alta      | T-10 días      | Sí             |
| Contrato penalizable partner  | SLA críticos                      | Compras             | Alta      | T-7 días       | Sí             |
| Declarar subcontratistas      | Si aportan solvencia              | Preventa            | Media     | T-7 días       | Sí             |

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿Aporta el cliente las licencias de Citrix, NetApp, SCCM, Workspace One UEM, SQL Server, o debe el adjudicatario suministrarlas?
- ¿Se aceptan partners/freelance como recursos adscritos si acreditan experiencia y certificaciones?
- ¿Se aceptan cartas de compromiso de partners/freelance para cubrir solvencia técnica?
- ¿Qué nivel de detalle se exige en la acreditación de experiencia y certificaciones?
- ¿Se aceptan equivalentes a Citrix, NetApp, SCCM, Workspace One UEM si cumplen requisitos funcionales?

16. Opinión final:
La estrategia de compras/partners debe centrarse en la búsqueda y cierre urgente de acuerdos con partners/freelance expertos en Citrix, NetApp, Cisco, SCCM, Workspace One UEM y SQL Server, con acreditación documental y cartas de compromiso. Es imprescindible validar con el cliente la titularidad y provisión de licencias clave. Sin estos acuerdos, la oferta es inviable y sería excluida. Se recomienda activar la búsqueda de mercado y priorizar la formalización de compromisos contractuales penalizables y cartas de solvencia externa antes de presentar oferta. La dependencia de partners externos es crítica y no está resuelta con la red actual.

17. Documentos revisados:
1. ANEXO I.pdf
2. Anuncio.pdf
3. DOC20240806095753Pliegodefinitivofirmado.pdf
4. DOC_CD2024-000901195.pdf
5. poc (Anuncio.pdf)
6. poc (Anuncio.pdf)
7. CORREOS-Codigo-General-de-Conducta.pdf (sin texto extraíble)
8. perfil-contratante
9. PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf