1. Veredicto ejecutivo Compras / Partners: BLOQUEANTE

2. Resumen ejecutivo:
El análisis de la licitación OPP-SW-004 desde Compras y Partners revela un bloqueo crítico: no se dispone internamente de los tres desarrolladores Java con experiencia específica en Spring, SQL y mantenimiento de aplicaciones corporativas exigidos por el pliego. Este gap es literal y no puede cubrirse con los perfiles actuales ni con la red de partners/autónomos disponible. El resto de necesidades (soporte L2, jefe de servicio, herramientas, entorno de pruebas, QA, DBA Oracle puntual) pueden cubrirse internamente o con partners/autónomos ya identificados. No hay productos hardware ni licencias software de compra obligatoria salvo herramientas de calidad de código y monitorización, que pueden adquirirse o subcontratarse. El límite de subcontratación (20-30%) permite cierta flexibilidad, pero la cobertura de los desarrolladores Java es ineludible y no hay partner ni autónomo en la red ficticia que lo cubra. Sin cerrar este gap, la oferta es inviable.

3. Mapa de necesidades externas:
| Necesidad                                 | Tipo         | Requisito literal/derivado | Cantidad | Especificación                                    | Quién lo aporta         | Acción                  |
|-------------------------------------------|--------------|---------------------------|----------|---------------------------------------------------|-------------------------|-------------------------|
| Desarrollador Java senior (Spring, SQL)   | Personal     | Literal                   | 2        | >=4 años exp. Spring, SQL, mantenimiento          | No disponible           | Buscar mercado externo  |
| Soporte L2 ITIL                           | Personal     | Literal                   | 1        | >=2 años exp. ITIL, SLA, incidencias              | Claudia Benitez         | Cubierto                |
| Jefe de servicio con ITIL Foundation      | Personal     | Literal/derivado          | 1        | >=5 años coord. mantenimiento, ITIL Foundation    | Gap parcial (Ana Torres)| Validar/Refuerzo        |
| QA/Testing                                | Personal     | Derivado                  | 0,2 FTE  | Pruebas regresión, automatización                 | Elena Garcia            | Cubierto                |
| DBA Oracle puntual                        | Servicio     | Derivado                  | Puntual  | Soporte incidencias críticas                      | Héctor Campos (autónomo)| Preacuerdo necesario    |
| Herramientas calidad código/monitorización| Software/SaaS| Derivado                  | 1        | SAST/SCA, monitorización aplicacional             | Adjudicatario           | Comprar/contratar       |

4. Productos, hardware y materiales:
No hay hardware obligatorio a aportar según pliego. Solo entorno de pruebas y herramientas software (ver punto 5).

5. Software, SaaS y licencias:
| Producto                  | Fabricante | Licencias/Métrica | Entornos | Duración | Aporta | Ambiguo | Acción                |
|---------------------------|------------|-------------------|----------|----------|--------|---------|-----------------------|
| Jira Service Management   | Atlassian  | 5 agentes         | PROD     | 24 meses | Cliente| No      | Validar si cliente aporta|
| Herramienta SAST/SCA      | Varios     | Por desarrollador | PRE/PRO  | 24 meses | Adjud. | No      | Comprar/contratar     |
| Monitorización aplicacional| Varios    | Por instancia     | PRE/PRO  | 24 meses | Adjud. | No      | Comprar/contratar     |

6. Fabricantes, canal y cartas:
| Fabricante | Obligatorio/Referencia | Partner/canal disponible | Carta requerida | Estado | Fecha objetivo | Riesgo |
|------------|-----------------------|--------------------------|-----------------|--------|---------------|--------|
| Atlassian  | Referencia            | Interno                  | No              | OK     | N/A           | Bajo   |
| SAST/SCA   | Equivalente permitido | Buscar mercado           | No              | N/A    | N/A           | Bajo   |

7. Subcontratación, UTE y medios externos:
- Límite subcontratación: 20% para DBA y pruebas de rendimiento, hasta 30% total.
- Actividades críticas: Soporte L2/L3 principal no subcontratable fuera UE.
- Subcontratistas a declarar si >10% del contrato.
- UTE permitida, pero no resuelve gap de desarrolladores Java si no hay partner adecuado.

8. Make / Buy / Partner:
| Capacidad                        | Interno | Comprar | Partner | Autónomo | Recomendación         | Justificación                  |
|----------------------------------|---------|---------|---------|----------|-----------------------|-------------------------------|
| Desarrollador Java senior        | No      | No      | No      | No       | Buscar mercado externo| Gap literal, no cubierto      |
| Soporte L2 ITIL                  | Sí      | No      | No      | No       | Interno               | Claudia Benitez disponible     |
| Jefe de servicio ITIL Foundation | Parcial | No      | No      | No       | Validar/reforzar      | Ana Torres, falta ITIL         |
| QA/Testing                       | Sí      | No      | No      | No       | Interno               | Elena Garcia disponible        |
| DBA Oracle puntual               | No      | No      | No      | Sí       | Autónomo (Héctor Campos)| Preacuerdo necesario         |
| Herramientas SAST/monitorización | No      | Sí      | No      | No       | Comprar/contratar     | Necesidad derivada             |

9. Mapa de partners propuestos:
| Necesidad         | Partner/autónomo candidato | Encaje | Documentación disponible | Gap | Criticidad | Acción              |
|-------------------|---------------------------|--------|-------------------------|-----|------------|---------------------|
| DBA Oracle puntual| Héctor Campos             | Parcial| CV, NDA, compromiso     | No  | Media      | Preacuerdo urgente  |
| SAST/monitorización| N/A                      | N/A    | N/A                     | Sí  | Baja       | Buscar proveedor    |

10. Cadena de suministro y dependencias:
Cadena: Cliente > Adjudicatario > (Autónomo DBA, proveedores SAST/monitorización)
| Dependencia           | Criticidad | Single point of failure | Alternativas | Riesgo |
|-----------------------|------------|------------------------|--------------|--------|
| Desarrolladores Java  | Crítica    | Sí                     | No           | Bloqueo|
| DBA Oracle puntual    | Media      | Sí (Héctor Campos)     | Buscar otro  | Medio  |
| SAST/monitorización   | Baja       | No                     | Sí           | Bajo   |

11. SLA back-to-back:
| SLA cliente                | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|----------------------------|----------------------------|-------------------------|-----|-----------------------|
| Respuesta P1 <= 1h (8x5)   | DBA autónomo               | Puntual, planificado    | Sí  | Preacuerdo, refuerzo  |
| Resolución crítica <= 8h   | DBA autónomo               | Puntual, planificado    | Sí  | Preacuerdo, refuerzo  |

12. Logística, staging, stock, garantía y retirada:
No aplica: no hay hardware ni materiales a suministrar.

13. Riesgos de compras y partners:
| Dependencia           | Riesgo         | Impacto | Probabilidad | Mitigación           | Responsable |
|-----------------------|----------------|---------|--------------|----------------------|-------------|
| Desarrolladores Java  | No cubrir gap  | Máximo  | Alta         | Buscar mercado externo| Compras     |
| DBA Oracle puntual    | No disponibilidad| Medio  | Media        | Preacuerdo urgente   | Compras     |
| SAST/monitorización   | Retraso compra | Bajo    | Baja         | RFQ rápido           | Compras     |

14. Matriz de acciones de Compras/Preventa:
| Acción                  | Necesidad                | Responsable | Prioridad | Fecha objetivo | Bloquea oferta |
|-------------------------|--------------------------|-------------|-----------|---------------|----------------|
| Buscar desarrolladores  | Gap Java                 | Compras     | Alta      | T-15 días     | Sí             |
| Preacuerdo DBA          | Soporte Oracle           | Compras     | Media     | T-10 días     | No             |
| RFQ SAST/monitorización | Herramientas calidad     | Compras     | Media     | T-12 días     | No             |

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿Se aceptan desarrolladores Java subcontratados o solo personal propio?
- ¿El entorno de pruebas puede ser cloud o debe ser on-premise?
- ¿Qué herramienta ITSM exacta usará el cliente y cuántos usuarios debe aportar el adjudicatario?

16. Opinión final:
La estrategia de compras/partners debe centrarse en cerrar urgentemente el gap de desarrolladores Java senior, ya sea mediante contratación directa, búsqueda de partner externo o UTE con empresa especializada. Sin resolver este punto, la oferta es inviable. El resto de necesidades son gestionables con la red actual y compras menores. Se recomienda activar búsqueda de mercado y preacuerdos antes de presentar oferta.

17. Documentos revisados:
1. Pliego administrativo OPP-SW-004 mantenimiento Java
2. Pliego técnico OPP-SW-004 mantenimiento Java
3. Anexo solvencia OPP-SW-004 mantenimiento Java