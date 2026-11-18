1. Veredicto ejecutivo Compras / Partners: CUBIERTO CON PARTNERS

2. Resumen ejecutivo:
La licitación exige una plataforma de IA documental sobre cloud UE, con arquitectura RAG, NLP, trazabilidad, seguridad ENS media, retención de logs, pentest, SAST/SCA, SBOM, EIPD y formación. No hay fabricantes obligatorios, pero sí requisitos de cloud, IA, licencias, auditoría y anonimización. El adjudicatario debe comprar/contratar:
- Cloud IA en UE (Azure recomendado, vía Cloud Partner Ficticio S.A.)
- Licencias SAST/SCA (compra directa)
- Vector database gestionada (cloud/SaaS)
- Servicio de anonimización de datos (partner/autónomo)
- Pentest y EIPD (Pentest Lab Ficticio S.L.)
- Auditoría ENS media (interno/partner)
- Formación y acompañamiento experto (interno/autónomo)
Dependencias críticas: cloud UE, subencargados IA/SaaS, partners de seguridad, cumplimiento ENS, retención de logs, SLA cloud, y validación de equivalentes SaaS. Partners propuestos: Cloud Partner Ficticio S.A., Pentest Lab Ficticio S.L. No hay bloqueos, pero la viabilidad depende de cerrar compromisos cloud, seguridad y anonimización antes de ofertar.

3. Mapa de necesidades externas:
| Necesidad                        | Tipo         | Requisito literal/derivado | Cantidad/volumen | Especificación                  | Quien lo aporta                | Acción                |
|----------------------------------|--------------|---------------------------|------------------|-------------------------------|-------------------------------|-----------------------|
| Cloud IA UE                      | Compra/Partner| Literal                   | 14 meses         | Azure/alternativa UE           | Cloud Partner Ficticio S.A.   | BOM, carta fabricante |
| Licencias SAST/SCA               | Compra       | Literal                   | 5-10 usuarios    | SAST/SCA enterprise            | Adjudicatario                  | RFQ, validación       |
| Vector database gestionada       | Compra/Partner| Literal                   | 1 servicio       | SaaS UE, API, logs 24 meses    | Cloud Partner Ficticio S.A.   | BOM, validación SaaS  |
| Anonimización de datos           | Partner      | Derivado                  | 1 servicio       | SaaS/servicio, DPA, logs       | Partner/autónomo               | Buscar mercado        |
| Pentest/EIPD                     | Partner      | Literal                   | 1 servicio       | Pentest, EIPD, informe         | Pentest Lab Ficticio S.L.      | Compromiso firmado    |
| Auditoría ENS media              | Interno/Partner| Literal                  | 1 auditoría      | ENS media, alcance IA/RAG      | Interno/Pentest Lab Ficticio   | Validar alcance       |
| Formación/adopción               | Interno/Autónomo| Literal                 | 30h formación    | ITIL, IA, seguridad            | Interno/autónomo               | Plan de formación     |

4. Productos, hardware y materiales:
| Producto         | Cantidad | Características         | Fabricante obligatorio | Equivalente permitido | Garantía/soporte | Stock | Lead time | Responsable |
|------------------|---------|------------------------|------------------------|----------------------|------------------|-------|----------|-------------|
| No aplica (no hay hardware obligatorio en pliego)

5. Software, SaaS y licencias:
| Producto                | Fabricante | Licencias/metrica | Entornos | Duración | Aporta | Ambiguo | Acción |
|-------------------------|-----------|-------------------|----------|----------|--------|---------|--------|
| Cloud IA (Azure)        | Microsoft | consumo mensual   | PRE/PRO  | 14 meses | Adjudicatario | No      | BOM, carta fabricante |
| Vector DB SaaS          | Varios    | servicio SaaS     | PRE/PRO  | 14 meses | Adjudicatario | Sí      | Validar equivalencia  |
| SAST/SCA                | Varios    | usuario/anual     | PRE/PRO  | 14 meses | Adjudicatario | No      | RFQ, validación      |
| Pentest/EIPD            | Pentest Lab| servicio          | PRO      | 1 vez    | Partner        | No      | Compromiso firmado   |
| Anonimización SaaS      | Varios    | servicio          | PRE/PRO  | 14 meses | Partner/autónomo| Sí      | Buscar mercado       |

6. Fabricantes, canal y cartas:
| Fabricante   | Obligatorio/Referencia | Partner/canal disponible | Carta requerida | Estado | Fecha objetivo | Riesgo |
|--------------|-----------------------|--------------------------|-----------------|--------|---------------|--------|
| Microsoft    | No, pero recomendado  | Cloud Partner Ficticio   | Sí              | Disponible | T-7 días     | Bajo   |
| SAST/SCA     | No                    | Compra directa           | No              | N/A     | T-12 días     | Bajo   |
| Vector DB    | No                    | Cloud Partner Ficticio   | Sí/validación   | Validar  | T-10 días     | Medio  |
| Pentest Lab  | No, pero recomendado  | Pentest Lab Ficticio     | Sí              | Disponible | T-7 días     | Bajo   |
| Anonimización| No                    | Buscar mercado           | Sí/validación   | Buscar   | T-10 días     | Medio  |

7. Subcontratación, UTE y medios externos:
- Límite subcontratación: No especificado, pero preferencia interna 40%.
- Actividades no subcontratables: Gobierno del dato, dirección de proyecto.
- Subcontratistas a declarar: Si aportan solvencia o servicios críticos (cloud, pentest, anonimización).
- UTE permitida: Sí, socios preidentificados.
- Integración de solvencia: Cloud Partner Ficticio S.A. y Pentest Lab Ficticio S.L. pueden aportar solvencia cloud y seguridad.

8. Make / Buy / Partner:
| Capacidad                | Interno | Comprar | Partner | Autonomo | Recomendación | Justificación |
|--------------------------|---------|---------|---------|----------|---------------|--------------|
| Cloud IA UE              | No      | Sí      | Sí      | No       | Partner       | Cloud Partner Ficticio |
| SAST/SCA                 | No      | Sí      | No      | No       | Comprar       | Licencia obligatoria |
| Vector DB SaaS           | No      | Sí      | Sí      | No       | Partner/Comprar| Validar SaaS UE |
| Pentest/EIPD             | No      | No      | Sí      | No       | Partner       | Pentest Lab Ficticio |
| Anonimización            | No      | Sí      | Sí      | Sí       | Buscar mercado| No partner homologado |
| Auditoría ENS media      | Sí      | No      | Sí      | No       | Interno/Partner| Alcance IA/RAG |
| Formación/adopción       | Sí      | No      | No      | Sí       | Interno/autónomo| Capacidad interna/autónoma |

9. Mapa de partners propuestos:
| Necesidad                | Partner/autónomo candidato | Encaje | Documentación disponible | Gap | Criticidad | Acción |
|--------------------------|----------------------------|--------|-------------------------|-----|------------|--------|
| Cloud IA UE              | Cloud Partner Ficticio     | Sí     | Carta, solvencia        | No  | Alta       | BOM, carta fabricante |
| Pentest/EIPD             | Pentest Lab Ficticio       | Sí     | Compromiso, certificados| No  | Alta       | Compromiso firmado   |
| Anonimización            | Buscar mercado/autónomo    | Parcial| N/A                     | Sí  | Media      | Buscar mercado       |
| Auditoría ENS media      | Pentest Lab Ficticio       | Sí     | Certificados            | No  | Media      | Validar alcance      |

10. Cadena de suministro y dependencias:
Cliente > Adjudicatario > Cloud Partner Ficticio (Azure) > SaaS/Vector DB > Pentest Lab Ficticio > Autónomo/partner anonimización
| Dependencia              | Criticidad | Single point of failure | Alternativas | Riesgo |
|--------------------------|------------|------------------------|--------------|--------|
| Cloud IA UE              | Alta       | Sí (Azure)             | AWS UE, GCP UE| Medio  |
| Pentest/EIPD             | Alta       | No                     | Otros partners| Bajo   |
| Anonimización            | Media      | Sí                     | Buscar mercado| Medio  |
| SAST/SCA                 | Media      | No                     | Otros fabricantes| Bajo   |

11. SLA back-to-back:
| SLA cliente              | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|--------------------------|-----------------------------|-------------------------|-----|-----------------------|
| P1 respuesta <= 15 min   | Cloud Partner Ficticio      | 12x5, 24x7 extra        | Gap | Guardias, penalización |
| Pentest/EIPD             | Pentest Lab Ficticio        | Planificado             | No  | Compromiso firmado    |
| Logs 24 meses            | Cloud Partner Ficticio/SaaS | 12 meses base           | Gap | Presupuestar extra    |

12. Logística, staging, stock, garantía y retirada:
No aplica (no hay hardware ni materiales físicos en pliego).

13. Riesgos de compras y partners:
| Dependencia              | Riesgo    | Impacto | Probabilidad | Mitigación | Responsable |
|--------------------------|-----------|---------|-------------|------------|-------------|
| Cloud IA UE              | Coste, SLA| Alto    | Media       | BOM, carta | Compras     |
| Pentest/EIPD             | Retardo   | Medio   | Baja        | Compromiso | Preventa    |
| Anonimización            | Falta partner| Medio | Media       | Buscar mercado| Preventa   |
| Logs 24 meses            | Coste extra| Medio   | Media       | Validar SaaS | Preventa   |

14. Matriz de acciones de Compras/Preventa:
| Acción                   | Necesidad | Responsable sugerido | Prioridad | Fecha objetivo | Bloquea oferta |
|--------------------------|-----------|----------------------|-----------|---------------|---------------|
| BOM cloud IA             | Cloud IA  | Preventa/Compras     | Alta      | T-12 días     | Sí            |
| Carta fabricante Azure   | Cloud IA  | Preventa/Compras     | Alta      | T-7 días      | Sí            |
| RFQ SAST/SCA             | SAST/SCA  | Compras              | Media     | T-12 días     | Sí            |
| Compromiso Pentest/EIPD  | Pentest   | Preventa/Compras     | Alta      | T-7 días      | Sí            |
| Buscar anonimización     | Anonimización| Preventa/Compras   | Alta      | T-10 días     | Sí            |
| Validar logs 24 meses    | SaaS      | Preventa/Compras     | Media     | T-10 días     | No            |

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿Qué SaaS de vector database se consideran equivalentes válidos? ¿Requiere carta de fabricante?
- ¿La retención de logs 24 meses es obligatoria en todos los servicios SaaS? ¿Admite logs en almacenamiento propio?
- ¿El servicio de anonimización debe ser SaaS UE o se admite autónomo con DPA?
- ¿Se exige declaración de subcontratistas en oferta o solo si aportan solvencia?
- ¿Qué penalización aplica si el cloud IA supera el consumo estimado?

16. Opinión final:
La oferta es viable si se cierran compromisos con Cloud Partner Ficticio S.A. (Azure), Pentest Lab Ficticio S.L. (pentest/EIPD), y se valida el SaaS de vector database y anonimización. No hay bloqueos críticos, pero la dependencia de cloud UE y partners de seguridad es alta. Recomendado activar BOM, cartas, compromisos y buscar mercado para anonimización antes de ofertar.

17. Documentos revisados:
- Pliego administrativo OPP-SW-002 IA documental
- Pliego técnico OPP-SW-002 IA documental
- Anexo solvencia OPP-SW-002 IA documental