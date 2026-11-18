1. Veredicto ejecutivo Compras / Partners: BLOQUEANTE

2. Resumen ejecutivo:
El análisis de la licitación OPP-SW-003 desde la perspectiva de compras, fabricantes, partners y dependencias externas revela un bloqueo crítico: la imposibilidad de cubrir internamente el requisito de dos DevOps/cloud senior con 5 años de experiencia en Azure, Kubernetes, Docker, CI/CD y observabilidad. Solo se dispone de un perfil adecuado (Ivan Lopez). El resto de necesidades tecnológicas (cloud temporal Azure, herramientas SAST/SCA, monitorización, guardias, soporte de fabricante/partner, cartas de compromiso) pueden cubrirse mediante compras y partners de la red ficticia, principalmente con Cloud Partner Ficticio S.A. y compras de licencias/herramientas. Sin embargo, la carencia de un segundo DevOps senior es un bloqueo literal del pliego y no subsanable con los recursos actuales, lo que impide presentar oferta viable salvo contratación/alianza urgente.

3. Mapa de necesidades externas:
| Necesidad                                 | Tipo         | Requisito literal/derivado | Cantidad | Especificación                                                      | Quien lo aporta                | Acción                                    |
|-------------------------------------------|--------------|---------------------------|----------|---------------------------------------------------------------------|-------------------------------|-------------------------------------------|
| DevOps/cloud senior (2º perfil)           | Personal     | Literal                   | 1        | 5 años Azure, K8s, Docker, CI/CD, observabilidad                    | No disponible                  | Contratar/partner externo urgente         |
| Cloud temporal Azure                      | Cloud        | Literal                   | 6 meses  | 4.200 EUR/mes, regiones UE, ENS media                               | Cloud Partner Ficticio S.A.    | RFQ, deal registration, carta compromiso  |
| Herramienta SAST/SCA                      | Software     | Literal                   | 5 users  | SAST/SCA, integración CI/CD                                         | Compra a fabricante/distribuidor| BOM, RFQ, validación licencias            |
| Monitorización Grafana/Prometheus         | SaaS/Software| Literal                   | 1        | Gestionado, integración AKS, dashboards                             | Compra/partner                 | BOM, RFQ, validación                      |
| Escaneo de contenedores                   | Software     | Literal                   | 1        | Integración pipelines, alertas CVE                                  | Compra/partner                 | BOM, RFQ, validación                      |
| Guardias DevOps migración                 | Servicio     | Literal                   | 8 fines  | Guardias localizadas, soporte 12x5/24x7 en ventanas                 | Interno + Cloud Partner Ficticio| Compromiso back-to-back                   |
| Carta compromiso partner cloud             | Documento    | Literal                   | 1        | Soporte AKS, regiones UE, ENS media                                 | Cloud Partner Ficticio S.A.    | Solicitar carta antes de oferta           |
| Soporte fabricante/partner en migración   | Servicio     | Literal                   | 1        | Soporte Azure/AKS, incidencias críticas                             | Cloud Partner Ficticio S.A.    | Compromiso firmado, SLA                   |
| Jira Service Management                   | Software     | Derivado                  | 1        | ITSM, CMDB, integración migración                                   | Compra directa                 | Validar licencias, integración            |

4. Productos, hardware y materiales:
No se detectan requisitos de hardware físico (portátiles, servidores, etc.) en el pliego. Todo el aprovisionamiento es cloud/software.

5. Software, SaaS y licencias:
| Producto                  | Fabricante   | Licencias/metrica | Entornos | Duración | Aporta         | Ambiguo | Acción                       |
|--------------------------|--------------|-------------------|----------|----------|---------------|---------|------------------------------|
| Azure cloud temporal      | Microsoft    | Consumo mensual   | PRE/PRO  | 6 meses  | Adjudicatario | No      | RFQ, deal registration       |
| SAST/SCA                  | A definir    | 5 usuarios        | CI/CD    | 10 meses | Adjudicatario | Sí      | Validar fabricante/alcance   |
| Grafana/Prometheus        | Grafana      | Equipo/instancia  | AKS      | 10 meses | Adjudicatario | No      | BOM, RFQ                     |
| Escaneo contenedores      | A definir    | 1 integración     | CI/CD    | 10 meses | Adjudicatario | Sí      | Validar fabricante/alcance   |
| Jira Service Management   | Atlassian    | 1 instancia       | ITSM     | 10 meses | Adjudicatario | No      | Compra directa/licencias     |

6. Fabricantes, canal y cartas:
| Fabricante   | Obligatorio/Referencia | Partner/canal disponible      | Carta requerida | Estado     | Fecha objetivo | Riesgo |
|--------------|-----------------------|------------------------------|----------------|------------|---------------|--------|
| Microsoft    | Sí (Azure)            | Cloud Partner Ficticio S.A.  | Sí             | Disponible | T-7 días      | Bajo   |
| Grafana      | Referencia            | Compra directa/partner       | No             | N/A        | N/A           | Bajo   |
| Atlassian    | Referencia            | Compra directa               | No             | N/A        | N/A           | Bajo   |
| SAST/SCA     | No definido           | Buscar mercado               | Sí (si exige)  | N/A        | T-12 días     | Medio  |

7. Subcontratación, UTE y medios externos:
- Límite subcontratación: 25% (excepto dirección de proyecto y arquitectura cloud, que deben ser internos).
- Subcontratistas a declarar: Cloud Partner Ficticio S.A. para cloud/guardias, otros para software si se requiere.
- UTE: Permitida, socios preidentificados.
- Integración de solvencia: Necesaria para cubrir el gap DevOps/cloud senior.

8. Make / Buy / Partner:
| Capacidad                  | Interno | Comprar | Partner | Autonomo | Recomendación         | Justificación                                 |
|----------------------------|---------|---------|---------|----------|----------------------|-----------------------------------------------|
| DevOps/cloud senior (2º)   | No      | No      | Sí      | No       | Partner/contratación | Gap literal, imprescindible para ofertar      |
| Cloud Azure/AKS            | No      | Sí      | Sí      | No       | Partner              | Cloud Partner Ficticio S.A.                   |
| SAST/SCA                   | No      | Sí      | Sí      | No       | Comprar/partner      | No definido fabricante, buscar mercado        |
| Monitorización Grafana     | Parcial | Sí      | Sí      | No       | Comprar/partner      | Integración cloud, posible compra directa     |
| Guardias DevOps            | Parcial | No      | Sí      | No       | Partner              | Refuerzo en ventanas críticas                 |

9. Mapa de partners propuestos:
| Necesidad                  | Partner/autónomo candidato | Encaje                    | Documentación disponible | Gap | Criticidad | Acción                  |
|----------------------------|----------------------------|---------------------------|-------------------------|-----|------------|-------------------------|
| DevOps/cloud senior (2º)   | Cloud Partner Ficticio S.A.| Sí (si aporta perfil)     | CV, carta compromiso    | Sí  | Crítica    | Validar disponibilidad  |
| Cloud Azure/AKS            | Cloud Partner Ficticio S.A.| Total                     | Carta, referencias      | No  | Alta       | Solicitar carta         |
| SAST/SCA                   | Buscar mercado             | N/A                       | N/A                    | Sí  | Media      | RFQ urgente             |
| Guardias DevOps            | Cloud Partner Ficticio S.A.| Sí                        | Compromiso              | No  | Alta       | Compromiso firmado      |

10. Cadena de suministro y dependencias:
- Cliente → Adjudicatario → Cloud Partner Ficticio S.A. (Azure, guardias, soporte) → Microsoft (cloud)
- Adjudicatario → Fabricante SAST/SCA (a definir)
- Adjudicatario → Atlassian (Jira Service Management)

| Dependencia                | Criticidad | Single point of failure | Alternativas | Riesgo |
|----------------------------|------------|------------------------|--------------|--------|
| DevOps/cloud senior (2º)   | Crítica    | Sí                     | No           | Muy alto|
| Cloud Partner Ficticio S.A.| Alta       | Parcial                | Buscar mercado| Medio  |
| Microsoft Azure            | Alta       | Sí                     | No           | Medio  |
| SAST/SCA fabricante        | Media      | No                     | Sí           | Bajo   |

11. SLA back-to-back:
| SLA cliente                | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|----------------------------|----------------------------|-------------------------|-----|-----------------------|
| Soporte migración 12x5     | Cloud Partner Ficticio S.A.| 12x5, 24x7 extra        | No  | Compromiso firmado    |
| Guardias fines de semana   | Cloud Partner Ficticio S.A.| Sí                      | No  | Compromiso firmado    |
| Respuesta P1 30 min        | Cloud Partner Ficticio S.A.| Sí                      | No  | Compromiso firmado    |

12. Logística, staging, stock, garantía y retirada:
No aplica hardware físico. Cloud y software gestionados. No hay RAEE ni logística física relevante.

13. Riesgos de compras y partners:
| Dependencia                | Riesgo     | Impacto | Probabilidad | Mitigación           | Responsable           |
|----------------------------|------------|---------|--------------|----------------------|----------------------|
| DevOps/cloud senior (2º)   | Bloqueante | Máximo  | Alta         | Contratar/partner    | Compras/Recursos     |
| Cloud Partner Ficticio S.A.| Medio      | Alto    | Media        | Carta compromiso     | Preventa/Compras     |
| SAST/SCA fabricante        | Medio      | Medio   | Media        | RFQ urgente          | Preventa/Compras     |

14. Matriz de acciones de Compras/Preventa:
| Acción                     | Necesidad                  | Responsable sugerido     | Prioridad | Fecha objetivo | Bloquea oferta |
|----------------------------|----------------------------|-------------------------|-----------|---------------|----------------|
| Contratar DevOps/cloud     | Gap DevOps senior          | RRHH/Compras            | Máxima    | T-15 días      | Sí             |
| Solicitar carta partner    | Cloud Azure/guardias       | Preventa/Compras        | Alta      | T-10 días      | Sí             |
| RFQ SAST/SCA               | Licencias SAST/SCA         | Preventa/Compras        | Alta      | T-12 días      | Sí             |
| Deal registration Azure    | Cloud temporal             | Preventa/Compras        | Alta      | T-7 días       | No             |
| Validar SLA partner        | Guardias/soporte           | Preventa/Compras        | Alta      | T-7 días       | No             |

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿Se acepta solvencia por medios externos para el segundo DevOps/cloud senior?
- ¿Qué fabricantes de SAST/SCA son aceptados como equivalentes?
- ¿Se permite subcontratar el segundo DevOps/cloud senior si se declara en oferta?
- ¿El cloud temporal puede ser facturado por partner o debe ser directo?

16. Opinión final:
La licitación es BLOQUEANTE desde compras/partners por la ausencia de un segundo DevOps/cloud senior. El resto de necesidades (cloud, licencias, herramientas, soporte, guardias) pueden cubrirse con compras y partners existentes, especialmente Cloud Partner Ficticio S.A. y compras directas de software. Es imprescindible cerrar la contratación o alianza para el segundo DevOps/cloud senior antes de presentar oferta. Si no se resuelve, la oferta es inviable.

17. Documentos revisados:
1. Pliego administrativo OPP-SW-003 migración cloud
2. Pliego técnico OPP-SW-003 migración cloud
3. Anexo solvencia OPP-SW-003 migración cloud