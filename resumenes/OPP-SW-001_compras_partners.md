1. Veredicto ejecutivo Compras / Partners: CUBIERTO CON PARTNERS

2. Resumen ejecutivo:
El proyecto exige la compra/contratación de licencias software (Jira Service Management, SAST/SCA, Power BI Pro), cloud Azure (DEV/PRE/PRO), y la ejecución de un pentest web externo. No hay hardware físico a suministrar. El cloud Azure y las licencias pueden ser cubiertos mediante el partner homologado Cloud Partner Ficticio S.A. El pentest debe ser cubierto por Pentest Lab Ficticio S.L. No existen bloqueos críticos, pero la dependencia de partners para cloud y pentest es alta y requiere compromisos formales antes de ofertar. No se detectan gaps internos en perfiles, pero sí dependencias externas para cloud y pentest. Viabilidad: alta si se cierran compromisos de partners y cartas requeridas.

3. Mapa de necesidades externas:
| Necesidad                        | Tipo         | Requisito literal/derivado | Cantidad/volumen | Especificación                                    | Quien lo aporta                | Acción                         |
|----------------------------------|--------------|---------------------------|------------------|---------------------------------------------------|-------------------------------|-------------------------------|
| Cloud Azure DEV/PRE/PRO          | Cloud/SaaS   | Literal                   | 12 meses         | Alta disponibilidad, WAF, backups, logs 12m       | Cloud Partner Ficticio S.A.   | RFQ, carta compromiso         |
| Licencias Jira Service Mgmt      | Software     | Literal                   | 5 agentes        | SaaS, gestión tickets, reporting                  | Cloud Partner Ficticio S.A.   | Validar licenciamiento        |
| Licencias SAST/SCA               | Software     | Literal                   | 4 desarrolladores| Cobertura OWASP, SBOM, dependencias               | Adjudicatario/Partner         | RFQ, validar equivalentes     |
| Licencias Power BI Pro           | Software     | Literal                   | 3 usuarios       | Power BI Pro, reporting                           | Cloud Partner Ficticio S.A.   | Validar licenciamiento        |
| Pentest web externo              | Servicio     | Literal                   | 1 (previo prod)  | Pentest web, informe, retest                      | Pentest Lab Ficticio S.L.     | Compromiso firmado            |
| Carta compromiso cloud/partner   | Documento    | Literal                   | 1                | Carta partner Microsoft/Cloud Partner             | Cloud Partner Ficticio S.A.   | Solicitar carta               |

4. Productos, hardware y materiales:
No hay hardware físico, materiales ni stock a suministrar según pliego.

5. Software, SaaS y licencias:
| Producto                  | Fabricante   | Licencias/metrica | Entornos      | Duración | Aporta           | Ambiguo | Acción                  |
|--------------------------|--------------|-------------------|---------------|----------|------------------|---------|------------------------|
| Jira Service Management  | Atlassian    | 5 agentes         | PROD/Soporte  | 12 meses | Adjudicatario    | No      | Validar licenciamiento |
| SAST/SCA (SonarQube o eq)| SonarQube/?  | 4 desarrolladores | DEV/CI/CD     | 12 meses | Adjudicatario    | Sí*     | Validar equivalencia   |
| Power BI Pro             | Microsoft    | 3 usuarios        | Reporting     | 12 meses | Adjudicatario    | No      | Validar licenciamiento |
| Cloud Azure              | Microsoft    | Consumo mensual   | DEV/PRE/PRO   | 12 meses | Adjudicatario    | No      | RFQ, carta partner     |
*Ambiguo: se permite equivalente, pero debe cumplir OWASP, SBOM, dependencias. Preguntar si hay preferencia.

6. Fabricantes, canal y cartas:
| Fabricante   | Obligatorio/Referencia | Partner/canal disponible      | Carta requerida | Estado     | Fecha objetivo | Riesgo |
|--------------|-----------------------|------------------------------|----------------|------------|---------------|--------|
| Microsoft    | Sí (cloud, Power BI)  | Cloud Partner Ficticio S.A.  | Sí             | Disponible | T-7 días      | Medio  |
| Atlassian    | Sí (Jira)             | Cloud Partner Ficticio S.A.  | No habitual    | OK         | N/A           | Bajo   |
| SonarQube/?  | Referencia/equiv.     | Directo/Partner a buscar     | No             | Ambiguo    | T-12 días     | Bajo   |

7. Subcontratación, UTE y medios externos:
- Límite subcontratación: 30% (pliego).
- No subcontratable: dirección de proyecto.
- Subcontratistas a declarar: Cloud Partner Ficticio S.A. (cloud/licencias), Pentest Lab Ficticio S.L. (pentest).
- UTE: permitida, socios preidentificados.

8. Make / Buy / Partner:
| Capacidad         | Interno | Comprar | Partner | Autónomo | Recomendación         | Justificación                  |
|-------------------|---------|---------|---------|----------|-----------------------|-------------------------------|
| Cloud Azure       | No      | Sí      | Sí      | No       | Partner               | Solo vía partner homologado    |
| Jira Service Mgmt | No      | Sí      | Sí      | No       | Partner               | Licencias SaaS vía partner     |
| SAST/SCA          | Parcial | Sí      | Sí      | No       | Comprar/Partner       | Validar si SonarQube directo   |
| Power BI Pro      | No      | Sí      | Sí      | No       | Partner               | Licencias vía partner          |
| Pentest web       | No      | No      | Sí      | No       | Partner               | Solo vía Pentest Lab Ficticio  |

9. Mapa de partners propuestos:
| Necesidad         | Partner/autónomo candidato   | Encaje | Documentación disponible | Gap | Criticidad | Acción                |
|-------------------|-----------------------------|--------|-------------------------|-----|------------|----------------------|
| Cloud Azure       | Cloud Partner Ficticio S.A. | Alto   | Carta, compromiso       | No  | Alta       | Solicitar carta      |
| Jira/Power BI     | Cloud Partner Ficticio S.A. | Alto   | Licencias, compromiso   | No  | Media      | Validar licencias    |
| Pentest web       | Pentest Lab Ficticio S.L.   | Alto   | Compromiso, CV, NDA     | No  | Alta       | Solicitar compromiso |

10. Cadena de suministro y dependencias:
Cadena: Cliente > Adjudicatario > Cloud Partner Ficticio S.A. (cloud/licencias) > Microsoft (cloud/Power BI) > Atlassian (Jira) > Pentest Lab Ficticio S.L. (pentest).
| Dependencia                    | Criticidad | Single point of failure | Alternativas | Riesgo |
|-------------------------------|------------|------------------------|--------------|--------|
| Cloud Partner Ficticio S.A.   | Alta       | Sí                     | Buscar otro  | Medio  |
| Pentest Lab Ficticio S.L.     | Alta       | Sí                     | Buscar otro  | Medio  |
| Microsoft (cloud/Power BI)    | Media      | No                     | No           | Bajo   |
| Atlassian (Jira)              | Media      | No                     | No           | Bajo   |

11. SLA back-to-back:
| SLA cliente                | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|----------------------------|-----------------------------|-------------------------|-----|-----------------------|
| Cloud alta disponibilidad  | Cloud Partner Ficticio S.A. | 99,5% Azure             | No  | Carta compromiso      |
| Pentest previo a producción| Pentest Lab Ficticio S.L.   | Bajo planificación      | No  | Compromiso firmado    |
| Licencias SaaS operativas  | Cloud Partner Ficticio S.A. | 12x5 soporte            | No  | SLA partner           |

12. Logística, staging, stock, garantía y retirada:
No aplica: no hay hardware ni materiales físicos a suministrar.

13. Riesgos de compras y partners:
| Dependencia                  | Riesgo         | Impacto | Probabilidad | Mitigación             | Responsable           |
|-----------------------------|----------------|---------|--------------|------------------------|----------------------|
| Cloud Partner Ficticio S.A. | Ruptura canal  | Alto    | Media        | Carta, acuerdo formal  | Compras/Preventa     |
| Pentest Lab Ficticio S.L.   | No disponibilidad| Alto  | Baja         | Compromiso firmado     | Compras/Preventa     |
| Licencias SaaS              | Error metrica   | Medio   | Baja         | Validar con partner    | Compras/Preventa     |

14. Matriz de acciones de Compras/Preventa:
| Acción                  | Necesidad         | Responsable sugerido | Prioridad | Fecha objetivo | Bloquea oferta |
|-------------------------|-------------------|----------------------|-----------|----------------|---------------|
| RFQ cloud/licencias     | Cloud/licencias   | Compras              | Alta      | T-12 días      | Sí            |
| Solicitar carta partner | Cloud             | Preventa             | Alta      | T-7 días       | Sí            |
| Validar licencias SaaS  | Jira/Power BI     | Preventa             | Media     | T-6 días       | Sí            |
| Solicitar compromiso    | Pentest           | Compras              | Alta      | T-7 días       | Sí            |
| Validar SAST/SCA        | SAST/SCA          | Preventa             | Media     | T-12 días      | Sí            |

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿Se admite SonarQube Community/Enterprise o hay preferencia de fabricante para SAST/SCA?
- ¿Se permite que el cloud Azure esté en tenant del partner o debe ser en tenant del cliente?
- ¿Se exige carta de fabricante Microsoft o basta con carta de partner cloud?
- ¿Se permite subcontratar el pentest web a partner homologado?

16. Opinión final:
La estrategia recomendada es cerrar compromisos formales con Cloud Partner Ficticio S.A. para cloud/licencias y con Pentest Lab Ficticio S.L. para pentest antes de ofertar. No hay gaps internos en perfiles, pero la dependencia de partners es crítica para cloud y pentest. Se recomienda validar licenciamiento y equivalentes SAST/SCA antes de la oferta. Viabilidad: alta si se cierran compromisos y cartas antes de la presentación.

17. Documentos revisados:
1. Pliego administrativo OPP-SW-001 portal ciudadano
2. Pliego técnico OPP-SW-001 portal ciudadano
3. Anexo solvencia OPP-SW-001 portal ciudadano