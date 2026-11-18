1. Veredicto ejecutivo Compras / Partners: CUBIERTO

2. Resumen ejecutivo:
La licitación OPP-SW-005 requiere la aportación de licencias Power BI Pro temporales, un gateway de datos, repositorio Git y herramienta de calidad de datos, además del equipo técnico. No hay hardware físico ni materiales a suministrar. El cliente aporta las licencias Power BI Service para usuarios finales. No se exige partner de fabricante ni UTE, y la subcontratación no es crítica. Todos los perfiles mínimos están cubiertos internamente. Las dependencias externas se limitan a la compra de licencias Power BI Pro y, si se opta por cloud propio para desarrollo, a la contratación de workspace y posible uso de Cloud Partner Ficticio S.A. No hay bloqueos ni riesgos críticos no gestionables. Viabilidad alta.

3. Mapa de necesidades externas:
| Necesidad                        | Tipo         | Requisito literal/derivado | Cantidad/volumen | Especificación                        | Quien lo aporta         | Acción                       |
|----------------------------------|--------------|---------------------------|------------------|---------------------------------------|-------------------------|------------------------------|
| Licencias Power BI Pro           | Software     | Literal                   | 5                | Power BI Pro temporales para equipo   | Adjudicatario           | Comprar antes de inicio      |
| Gateway de datos                 | Software     | Literal/derivado          | 1                | Gateway Power BI compatible           | Adjudicatario           | Validar con cliente/fabricar |
| Workspace Power BI desarrollo    | SaaS         | Derivado                  | 1                | Workspace cloud si no es on-prem      | Adjudicatario/Partner   | Validar, contratar si aplica |
| Repositorio Git                  | Software     | Literal/derivado          | 1                | GitHub, Azure DevOps o equivalente    | Adjudicatario           | Usar propio o contratar      |
| Herramienta calidad de datos     | Software     | Literal/derivado          | 1                | Data quality tool (open source/prop.) | Adjudicatario           | Seleccionar y provisionar    |

4. Productos, hardware y materiales:
| Producto | Cantidad | Características | Fabricante obligatorio/referencia | Equivalente permitido | Garantía/soporte | Stock | Lead time | Responsable |
|----------|----------|----------------|-----------------------------------|----------------------|------------------|-------|-----------|-------------|
| N/A      | N/A      | N/A            | N/A                               | N/A                  | N/A              | N/A   | N/A       | N/A         |
No hay hardware físico a suministrar.

5. Software, SaaS y licencias:
| Producto                | Fabricante | Licencias/metrica | Entornos | Duración | Aporta | Ambiguo | Acción |
|-------------------------|-----------|-------------------|----------|----------|--------|---------|--------|
| Power BI Pro            | Microsoft | 5 usuarios        | DEV/PRO  | 8 meses  | Adjudicatario | No      | Comprar |
| Power BI Service        | Microsoft | 300 usuarios      | PRO      | Cliente  | Cliente | No      | Validar |
| Gateway Power BI        | Microsoft | 1                 | DEV/PRO  | 8 meses  | Adjudicatario | Sí*     | Validar |
| Workspace Power BI      | Microsoft | 1                 | DEV      | 8 meses  | Adjudicatario/Partner | Sí* | Validar |
| Repositorio Git         | GitHub/Azure | 1               | DEV      | 8 meses  | Adjudicatario | No      | Usar/contratar |
| Herramienta calidad datos| Varios   | 1                 | DEV      | 8 meses  | Adjudicatario | No      | Seleccionar |
*Ambiguo: Confirmar si gateway y workspace se instalan en infra cliente o adjudicatario.

6. Fabricantes, canal y cartas:
| Fabricante | Obligatorio/Referencia | Partner/canal disponible | Carta requerida | Estado | Fecha objetivo | Riesgo |
|------------|-----------------------|--------------------------|----------------|--------|---------------|--------|
| Microsoft  | Referencia            | Cloud Partner Ficticio S.A. | No (no exigida) | Disponible | N/A           | Bajo   |

7. Subcontratación, UTE y medios externos:
- Límite: No se permite UTE. Subcontratación no crítica, no hay actividades excluidas ni subcontratistas a declarar obligatoriamente.
- Solvencia: No se requiere integración de solvencia externa.

8. Make / Buy / Partner:
| Capacidad                  | Interno | Comprar | Partner | Autónomo | Recomendación | Justificación |
|----------------------------|---------|---------|---------|----------|---------------|---------------|
| BI/ETL/Power BI            | Sí      | No      | No      | No       | Interno       | Perfil Paula  |
| Analista funcional         | Sí      | No      | No      | No       | Interno       | Perfil Luis   |
| Backend integraciones      | Sí      | No      | No      | No       | Interno       | Perfil Sofia  |
| Licencias Power BI Pro     | No      | Sí      | No      | No       | Comprar       | Requisito     |
| Gateway/Workspace Power BI | No      | Sí      | Posible | No       | Validar/Comprar| Derivado     |
| Herramienta calidad datos  | No      | Sí      | No      | No       | Comprar       | Derivado     |

9. Mapa de partners propuestos:
| Necesidad         | Partner/autónomo candidato | Encaje | Documentación disponible | Gap | Criticidad | Acción |
|-------------------|---------------------------|--------|-------------------------|-----|------------|--------|
| Licencias Power BI| Cloud Partner Ficticio S.A.| Sí     | Carta, referencias      | No  | Baja       | Usar si cloud |

10. Cadena de suministro y dependencias:
Cadena: Cliente (Power BI Service) → Adjudicatario (desarrollo, licencias Pro, gateway, calidad datos) → Microsoft (fabricante) → Cloud Partner Ficticio S.A. (si cloud propio)
| Dependencia                | Criticidad | Single point of failure | Alternativas | Riesgo |
|----------------------------|------------|------------------------|--------------|--------|
| Licencias Power BI Pro     | Media      | No                     | Sí           | Bajo   |
| Gateway/Workspace Power BI | Media      | No                     | Sí           | Bajo   |
| Cloud Partner Ficticio S.A.| Baja       | No                     | Sí           | Bajo   |

11. SLA back-to-back:
| SLA cliente (8x5, 2h/1d) | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|--------------------------|----------------------------|-------------------------|-----|-----------------------|
| 8x5 soporte BI           | Microsoft/Cloud Partner    | 8x5 estándar            | No  | N/A                   |

12. Logística, staging, stock, garantía y retirada:
No aplica: no hay hardware ni materiales físicos a suministrar.

13. Riesgos de compras y partners:
| Dependencia           | Riesgo         | Impacto | Probabilidad | Mitigación         | Responsable |
|----------------------|----------------|---------|--------------|--------------------|-------------|
| Licencias Power BI   | Retraso compra | Bajo    | Baja         | Compra anticipada  | Compras     |
| Gateway/Workspace    | Ambigüedad     | Bajo    | Media        | Validar con cliente| Preventa    |

14. Matriz de acciones de Compras/Preventa:
| Acción                        | Necesidad                | Responsable | Prioridad | Fecha objetivo | Bloquea oferta |
|-------------------------------|--------------------------|-------------|-----------|----------------|----------------|
| Validar gateway/workspace     | Gateway/Workspace        | Preventa    | Alta      | T-10 días      | Sí             |
| Comprar licencias Power BI Pro| Licencias Power BI Pro   | Compras     | Alta      | T-7 días       | No             |
| Seleccionar calidad datos     | Herramienta calidad datos| Preventa    | Media     | T-12 días      | No             |

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿El gateway de datos debe instalarse en infraestructura del cliente o del adjudicatario?
- ¿El workspace de desarrollo Power BI debe estar en cloud propio o se habilita en el entorno del cliente?
- ¿Se permite el uso de herramientas open source para calidad de datos?

16. Opinión final:
La licitación está cubierta internamente salvo la compra de licencias Power BI Pro y posibles servicios cloud para desarrollo. No hay dependencias críticas no resueltas. Se recomienda validar con el cliente la ubicación del gateway y workspace antes de la oferta. Estrategia: compra directa de licencias y uso de Cloud Partner Ficticio S.A. solo si se requiere cloud propio.

17. Documentos revisados:
1. Pliego administrativo OPP-SW-005 BI expedientes
2. Pliego técnico OPP-SW-005 BI expedientes
3. Anexo solvencia OPP-SW-005 BI expedientes