1. Veredicto ejecutivo Compras / Partners: ALTO RIESGO

2. Resumen ejecutivo:
El pliego exige desarrollo y soporte de aplicaciones móviles nativas iOS y Android, backend, QA mobile, UX mobile y hardware de pruebas. La subcontratación del desarrollo mobile principal está prohibida, y la empresa no dispone de perfiles internos nativos iOS/Android ni referencias recientes válidas. QA mobile sí queda cubierto por Elena Garcia, aunque con bus factor 1. Es imprescindible contratar o incorporar desarrolladores iOS, Android y UX mobile antes de la oferta. Se requiere compra de hardware de pruebas (mínimo 12 dispositivos y 2 tablets), cuentas Apple/Google, servicios push y crash reporting en UE. Mobile Studio Ficticio S.L. es el único partner de la red con capacidad mobile, pero su uso directo para desarrollo principal está vetado por el pliego. El riesgo de dependencia crítica y bloqueo es muy alto si no se resuelve la incorporación de perfiles mobile nativos internos o mediante contratación directa.

3. Mapa de necesidades externas:
| Necesidad                                 | Tipo         | Requisito literal/derivado | Cantidad/volumen | Especificación                                      | Quién lo aporta                | Acción                         |
|-------------------------------------------|--------------|---------------------------|------------------|-----------------------------------------------------|-------------------------------|-------------------------------|
| Desarrollador iOS nativo                  | Personal     | Literal                   | 1                | 4 años exp. Swift, App Store, push                  | No disponible interno/partner  | Contratar/incorporar directo  |
| Desarrollador Android nativo              | Personal     | Literal                   | 1                | 4 años exp. Kotlin, Play Store, geolocalización     | No disponible interno/partner  | Contratar/incorporar directo  |
| QA mobile                                 | Personal     | Literal                   | 1                | 3 años exp. pruebas reales, automatización mobile   | Elena Garcia                   | Cubierto con bus factor 1; prever backup |
| UX mobile                                 | Personal     | Literal                   | 1                | 3 años exp. apps ciudadanas                         | No disponible interno/partner  | Contratar/incorporar directo  |
| Hardware de pruebas (smartphones/tablets) | Hardware     | Literal                   | 12+2             | Dispositivos iOS/Android, tablets                   | Comprar                       | BOM/RFQ                      |
| Cuentas Apple/Google                      | Licencia     | Literal                   | 1+1              | Apple Developer, Google Play                        | Comprar                       | Solicitar/gestionar           |
| Servicio push/crash reporting UE          | SaaS         | Literal/derivado          | 1                | Datos en UE, alternativa a Firebase si no cumple    | Comprar                       | Validar/alternativa           |
| Pentest mobile y backend                  | Servicio     | Literal                   | 1                | Antes de publicación, SAST/SCA, OWASP MASVS         | Pentest Lab Ficticio S.L.      | Solicitar compromiso          |
| MDM para pruebas                          | SaaS         | Literal                   | 1                | Gestión 30 dispositivos                             | Comprar/contratar              | BOM/RFQ                      |

4. Productos, hardware y materiales:
| Producto                | Cantidad | Características                        | Fabricante obligatorio/referencia | Equivalente permitido | Garantía/soporte | Stock | Lead time | Responsable           |
|-------------------------|----------|----------------------------------------|-----------------------------------|----------------------|------------------|-------|-----------|----------------------|
| Smartphone iOS          | 6        | Gama media/alta, iOS última versión    | Apple                            | Sí                   | 1 año mínimo     | No    | 2-3 sem   | Compras              |
| Smartphone Android      | 6        | Gama media/alta, Android última versión| Samsung/Google/Lenovo            | Sí                   | 1 año mínimo     | No    | 2-3 sem   | Compras              |
| Tablet iOS              | 1        | iPad, iOS última versión               | Apple                            | Sí                   | 1 año mínimo     | No    | 2-3 sem   | Compras              |
| Tablet Android          | 1        | Android última versión                 | Samsung/Lenovo                   | Sí                   | 1 año mínimo     | No    | 2-3 sem   | Compras              |
| MDM SaaS                | 1        | Gestión 30 dispositivos                | No especificado                   | Sí                   | SaaS             | N/A   | 1 sem     | Compras              |

5. Software, SaaS y licencias:
| Producto                | Fabricante | Licencias/métrica | Entornos | Duración | Aporta | Ambiguo | Acción |
|-------------------------|------------|-------------------|----------|----------|--------|---------|--------|
| Apple Developer         | Apple      | 1 cuenta          | PROD     | 1 año    | Adj.   | No      | Comprar|
| Google Play Developer   | Google     | 1 cuenta          | PROD     | 1 año    | Adj.   | No      | Comprar|
| Push/crash reporting    | Firebase/? | 1 SaaS            | PROD     | 1 año    | Adj.   | Sí      | Validar|
| MDM SaaS                | Varios     | 1 SaaS            | DEV/QA   | 1 año    | Adj.   | No      | Comprar|
| Jira Service Management | Atlassian  | 1-5 usuarios      | DEV/QA   | 1 año    | Adj.   | No      | Comprar|

6. Fabricantes, canal y cartas:
| Fabricante | Obligatorio/Referencia | Partner/canal disponible      | Carta requerida | Estado     | Fecha objetivo | Riesgo |
|------------|-----------------------|-------------------------------|----------------|------------|----------------|--------|
| Apple      | Sí                    | Compra directa                | No             | N/A        | N/A            | Bajo   |
| Google     | Sí                    | Compra directa                | No             | N/A        | N/A            | Bajo   |
| Atlassian  | No                    | Compra directa                | No             | N/A        | N/A            | Bajo   |
| Firebase/? | No                    | N/A                           | No             | Ambiguo    | N/A            | Medio  |

7. Subcontratación, UTE y medios externos:
- Límite subcontratación: 20% (pliego), prohibida para desarrollo iOS/Android principal.
- Subcontratistas a declarar: QA, pentest, MDM, hardware, si superan límite.
- UTE: Permitida, socios preidentificados (Mobile Studio Ficticio S.L.), pero no resuelve gap de personal propio para desarrollo principal.

8. Make / Buy / Partner:
| Capacidad           | Interno | Comprar | Partner | Autónomo | Recomendación           | Justificación                                 |
|---------------------|---------|---------|---------|----------|------------------------|-----------------------------------------------|
| iOS nativo          | No      | Sí      | No      | No       | Contratar directo      | Subcontratación prohibida                     |
| Android nativo      | No      | Sí      | No      | No       | Contratar directo      | Subcontratación prohibida                     |
| QA mobile           | Sí      | No      | No      | No       | Interno con backup     | Elena Garcia cubre el requisito; bus factor 1 |
| UX mobile           | No      | Sí      | No      | No       | Contratar directo      | Subcontratación prohibida                     |
| Backend             | Sí      | No      | No      | No       | Interno                | Cubierto                                      |
| Pentest             | No      | No      | Sí      | No       | Partner                | Permitido, Pentest Lab Ficticio S.L.          |
| Hardware pruebas    | No      | Sí      | No      | No       | Comprar                | Requisito literal                             |
| MDM                 | No      | Sí      | No      | No       | Comprar                | Requisito literal                             |

9. Mapa de partners propuestos:
| Necesidad           | Partner/autónomo candidato | Encaje | Documentación disponible | Gap | Criticidad | Acción                |
|---------------------|----------------------------|--------|-------------------------|-----|-----------|----------------------|
| Pentest             | Pentest Lab Ficticio S.L.  | Sí     | Sí                      | No  | Media     | Solicitar compromiso |
| Mobile refuerzo     | Mobile Studio Ficticio S.L.| Parcial | Sí                      | Sí  | Crítica   | No permitido directo |

10. Cadena de suministro y dependencias:
Cliente > Adjudicatario > (Personal mobile contratado) > Hardware/MDM/Jira > Pentest Lab Ficticio S.L. (pentest)
| Dependencia                  | Criticidad | Single point of failure | Alternativas | Riesgo |
|------------------------------|------------|------------------------|--------------|--------|
| Personal mobile contratado   | Crítica    | Sí                     | No           | Muy alto|
| Hardware pruebas             | Media      | No                     | Sí           | Medio  |
| Pentest Lab Ficticio S.L.    | Media      | No                     | Sí           | Bajo   |

11. SLA back-to-back:
| SLA cliente                  | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|------------------------------|-----------------------------|-------------------------|-----|-----------------------|
| P1 backend <=15min/2h        | Personal contratado         | No definido             | Sí  | Contrato laboral      |
| Pentest previo a publicación | Pentest Lab Ficticio S.L.   | Sí                      | No  | Compromiso firmado    |

12. Logística, staging, stock, garantía y retirada:
- Entrega de hardware a equipo mobile antes de inicio.
- No se requiere logística compleja ni RAEE relevante.
- Garantía estándar de dispositivos suficiente.
- Staging y gestión de dispositivos por equipo propio.

13. Riesgos de compras y partners:
| Dependencia                  | Riesgo     | Impacto | Probabilidad | Mitigación                | Responsable |
|------------------------------|------------|---------|--------------|---------------------------|-------------|
| Personal mobile contratado   | Muy alto   | Crítico | Alta         | Contratar antes de oferta | RRHH        |
| Hardware pruebas             | Medio      | Medio   | Media        | BOM y compra anticipada   | Compras     |
| Pentest Lab Ficticio S.L.    | Bajo       | Bajo    | Baja         | Compromiso firmado        | Compras     |

14. Matriz de acciones de Compras/Preventa:
| Acción                       | Necesidad                  | Responsable sugerido | Prioridad | Fecha objetivo | Bloquea oferta |
|------------------------------|----------------------------|---------------------|-----------|---------------|---------------|
| Contratar personal mobile    | iOS, Android, QA, UX       | RRHH                | Alta      | T-20 días     | Sí            |
| BOM y RFQ hardware           | Dispositivos, tablets, MDM | Compras             | Alta      | T-12 días     | Sí            |
| Validar crash reporting UE   | Crash reporting            | Preventa            | Media     | T-10 días     | No            |
| Compromiso pentest           | Pentest                    | Preventa            | Media     | T-7 días      | No            |

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿Se admite la contratación directa de personal mobile antes de inicio como cumplimiento del requisito de equipo propio?
- ¿Se acepta Firebase/Crashlytics si los datos se alojan en UE? ¿Alternativas recomendadas?
- ¿Es obligatorio que las cuentas Apple/Google estén a nombre del adjudicatario o pueden ser del cliente?

16. Opinión final:
La viabilidad depende de la contratación directa de personal mobile nativo (iOS, Android y UX) antes de la oferta. QA mobile está cubierto por Elena Garcia, pero requiere backup operativo. La subcontratación o uso de partner para desarrollo principal está prohibida. El resto de necesidades (hardware, licencias, pentest) son cubribles con compras y partners existentes. Si no se cierra la incorporación de personal mobile propio, la oferta es inviable y el riesgo es bloqueante.

17. Documentos revisados:
1. Pliego administrativo OPP-SW-006 app móvil
2. Pliego técnico OPP-SW-006 app móvil
3. Anexo solvencia OPP-SW-006 app móvil
