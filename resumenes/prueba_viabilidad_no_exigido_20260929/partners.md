1. Veredicto ejecutivo Compras / Partners: CUBIERTO CON GAPS

---

Extracción de viabilidad

Tabla de requisitos (Compras/Partners):
| Parámetro                        | Literal y apartado del pliego                  | Umbral y fecha exigidos         | Estado         | Brecha, acción y responsable           |
|----------------------------------|-----------------------------------------------|-------------------------------|---------------|----------------------------------------|
| Partner Microsoft                | Pliego técnico, ANEXO COMPRAS / PARTNERS      | No exigido, pero valorable     | NO EXIGIDO    | No obligatorio, mejora técnica         |
| Licencias Power BI Pro           | Pliego administrativo, ANEXO COMPRAS / PARTNERS| 5 licencias durante proyecto  | NO ACREDITADO | Comprar/licenciar antes de inicio      |
| Gateway de datos                 | Pliego administrativo, ANEXO COMPRAS / PARTNERS| 1 gateway, antes de inicio    | NO ACREDITADO | Confirmar compra/instalación           |
| Herramienta calidad de datos     | Pliego administrativo, ANEXO COMPRAS / PARTNERS| 1 herramienta, antes de inicio| NO ACREDITADO | Seleccionar y comprar                  |
| Repositorio Git                  | Pliego administrativo, ANEXO COMPRAS / PARTNERS| 1 repositorio, antes de inicio| NO ACREDITADO | Confirmar compra/uso                   |
| Subcontratación                  | Pliego administrativo, Condiciones de participación| UTE NO PERMITIDA, subcontratación permitida| CUMPLE        | Declarar subcontratistas si aportan solvencia|
| Certificación Microsoft          | Pliego técnico, ANEXO COMPRAS / PARTNERS      | Valoración, no obligación      | NO EXIGIDO    | Mejora técnica, no bloqueante          |
| SLA soporte Power BI             | Pliego técnico, Service Design / ITIL         | 8x5, respuesta 2h, resolución 1d| PENDIENTE VALIDACIÓN | Confirmar SLA back-to-back con partner/fabricante|


Fichas de evidencia (PARTNERSHIP):
| Campo                  | Valor exacto aportado / NO CONSTA         | Documento interno / identificador         |
|-----------------------|------------------------------------------|------------------------------------------|
| Fabricante            | Microsoft                                | Portal alianzas / CRM                    |
| Titular               | Sermicro Software Ficticio S.L.           | Portal alianzas / CRM                    |
| Nivel actual          | Indirect reseller via Cloud Partner Ficticio S.A. | Portal alianzas / CRM            |
| Especialización       | NO CONSTA (no hay especialización propia) | Portal alianzas / CRM                    |
| Caducidad nivel       | NO CONSTA                                 | Portal alianzas / CRM                    |
| Caducidad especialización | NO CONSTA                             | Portal alianzas / CRM                    |
| Compromiso            | NO CONSTA (no hay carta propia)           | Portal alianzas / CRM                    |

| Fabricante            | Microsoft                                | Portal alianzas / CRM                    |
| Titular               | Cloud Partner Ficticio S.A.               | Portal alianzas / CRM                    |
| Nivel actual          | Microsoft Solutions Partner                | Portal alianzas / CRM                    |
| Especialización       | Digital & App Innovation                  | Portal alianzas / CRM                    |
| Caducidad nivel       | NO CONSTA                                 | Portal alianzas / CRM                    |
| Caducidad especialización | NO CONSTA                             | Portal alianzas / CRM                    |
| Compromiso            | Carta disponible en 7 días si oportunidad registrada | Portal alianzas / CRM          |

---

2. Resumen ejecutivo:

Hay que comprar/licenciar:
- 5 licencias Power BI Pro para el equipo del proyecto (no aportadas por el cliente).
- Gateway de datos (hardware/software, según arquitectura; confirmar si se instala en cliente o adjudicatario).
- Herramienta de calidad de datos (selección y compra, no especificada; puede ser SaaS o software).
- Repositorio Git (puede ser cloud, SaaS o propio; confirmar si requiere compra/licencia).

Dependencias críticas:
- Licencias Power BI Pro: compra obligatoria, sin alternativa interna.
- Gateway de datos: dependencia de fabricante Microsoft; confirmar canal y compatibilidad.
- Herramienta calidad de datos: elegir producto compatible con Power BI y SQL Server.
- Experiencia Microsoft: mejora técnica, no bloqueante.
- Subcontratación permitida, UTE prohibida.

Partners propuestos:
- Cloud Partner Ficticio S.A. para licencias Microsoft, gateway y soporte cloud.

Bloqueos:
- Confirmar arquitectura de gateway (cliente vs adjudicatario).
- Validar SLA back-to-back para soporte Power BI y gateway.

Opinión de viabilidad:
- El proyecto es viable con compras y partnership, pero requiere cerrar la compra de licencias, gateway y herramienta de calidad de datos antes de inicio. No hay bloqueo por canal, pero sí por falta de evidencia de compra/licencia.

---

3. Mapa de necesidades externas:
| Necesidad                | Tipo         | Requisito literal o derivado | Cantidad/volumen | Especificación                  | Quien lo aporta           | Acción                |
|-------------------------|--------------|------------------------------|------------------|-------------------------------|---------------------------|-----------------------|
| Power BI Pro licencias  | Software     | Literal                      | 5                | Power BI Pro, anual/temporal  | Adjudicatario             | Comprar/licenciar     |
| Gateway de datos        | Hardware/SW  | Literal                      | 1                | Microsoft, compatible         | Adjudicatario/partner     | Confirmar compra      |
| Herramienta calidad datos| Software    | Literal                      | 1                | Compatible Power BI/SQL       | Adjudicatario             | Seleccionar/comprar   |
| Repositorio Git         | Software     | Literal                      | 1                | Cloud/SaaS/propio             | Adjudicatario             | Confirmar compra/uso  |
| SLA soporte Power BI    | Servicio     | Derivado                     | N/A              | 8x5, respuesta 2h, resolución 1d| Partner/fabricante        | Validar SLA           |

---

4. Productos, hardware y materiales:
| Producto         | Cantidad | Características         | Fabricante obligatorio/referencia | Equivalente permitido | Garantía/soporte | Stock | Lead time | Responsable |
|------------------|----------|------------------------|-----------------------------------|-----------------------|------------------|-------|-----------|-------------|
| Gateway de datos | 1        | Microsoft, Power BI    | Microsoft                         | No                   | NBD estándar     | No    | 7-10 días | Partner      |

---

5. Software, SaaS y licencias:
| Producto             | Fabricante | Licencias/metrica | Entornos | Duración | Aporta cliente/adjudicatario/tercero | Ambiguo | Acción |
|----------------------|------------|-------------------|----------|----------|--------------------------------------|---------|--------|
| Power BI Pro         | Microsoft  | 5 usuarios        | DEV/PRO  | 8 meses  | Adjudicatario                        | No      | Comprar|
| Herramienta calidad datos| Variable| 1 licencia        | DEV/PRO  | 8 meses  | Adjudicatario                        | Sí      | Seleccionar/comprar|
| Repositorio Git      | Variable   | 1 cuenta          | DEV/PRO  | 8 meses  | Adjudicatario                        | Sí      | Confirmar compra/uso|

---

6. Fabricantes, canal y cartas:
| Fabricante | Obligatorio/Referencia | Partner/canal disponible | Carta requerida | Estado | Fecha objetivo | Riesgo |
|------------|-----------------------|--------------------------|-----------------|--------|---------------|--------|
| Microsoft  | Sí (gateway, Power BI)| Cloud Partner Ficticio S.A.| Sí (mejora técnica) | Disponible en 7 días | T-7 | Bajo |

---

7. Subcontratación, UTE y medios externos:
- UTE NO PERMITIDA (pliego administrativo).
- Subcontratación permitida, pero solo para ejecución, no para solvencia.
- No hay actividades críticas no subcontratables.
- Declarar subcontratistas si aportan solvencia o ejecutan parte relevante.

---

8. Make / Buy / Partner:
| Capacidad                | Interno | Comprar | Partner | Autonomo | Recomendación | Justificación |
|-------------------------|---------|---------|---------|----------|---------------|---------------|
| Power BI Pro licencias  | No      | Sí      | Sí      | No       | Comprar/partner| No aportadas internamente|
| Gateway de datos        | No      | Sí      | Sí      | No       | Comprar/partner| Requiere canal Microsoft|
| Herramienta calidad datos| No     | Sí      | No      | No       | Comprar        | No aportada internamente|
| Repositorio Git         | No      | Sí      | No      | No       | Comprar        | No aportada internamente|
| SLA soporte Power BI    | No      | No      | Sí      | No       | Partner        | Requiere canal/fabricante|

---

9. Mapa de partners propuestos:
| Necesidad           | Partner/autonomo candidato | Encaje | Documentación disponible | Gap | Criticidad | Acción |
|---------------------|----------------------------|--------|-------------------------|-----|-----------|--------|
| Power BI, gateway   | Cloud Partner Ficticio S.A.| Sí     | Carta, compromiso       | No  | Alta      | Solicitar carta, deal registration|

---

10. Cadena de suministro y dependencias:
Texto: Cliente aporta Power BI Service corporativo; adjudicatario compra licencias Pro, gateway y herramienta calidad de datos vía partner Microsoft. Cloud Partner Ficticio S.A. es canal para Microsoft. No hay UTE. Subcontratación permitida para ejecución.

Tabla:
| Dependencia         | Criticidad | Single point of failure | Alternativas | Riesgo |
|---------------------|------------|------------------------|-------------|--------|
| Licencias Power BI  | Alta       | Sí (partner Microsoft) | No          | Medio  |
| Gateway de datos    | Alta       | Sí (partner Microsoft) | No          | Medio  |
| Herramienta calidad datos| Media | No                     | Sí          | Bajo   |

---

11. SLA back-to-back:
| SLA cliente         | Proveedor/partner necesario | SLA proveedor disponible | Gap | Mitigación contractual |
|---------------------|----------------------------|-------------------------|-----|-----------------------|
| 8x5, respuesta 2h   | Cloud Partner Ficticio S.A.| 12x5, guardias planificadas| Sí  | Acuerdo específico, penalización|

---

12. Logística, staging, stock, garantía y retirada:
- No hay hardware físico relevante salvo gateway de datos.
- Stock y lead time del gateway: 7-10 días vía partner.
- No se requiere staging, asset tagging ni retirada RAEE.
- Garantía NBD estándar Microsoft.

---

13. Riesgos de compras y partners:
| Dependencia         | Riesgo     | Impacto | Probabilidad | Mitigación | Responsable |
|---------------------|------------|---------|-------------|------------|-------------|
| Licencias Power BI  | Medio      | Alta    | Media       | Compra anticipada, reserva stock| Compras/partner|
| Gateway de datos    | Medio      | Alta    | Media       | Confirmar canal, carta fabricante| Compras/partner|
| SLA soporte Power BI| Alto       | Media   | Alta        | Acuerdo back-to-back, penalización| Preventa/partner|

---

14. Matriz de acciones de Compras/Preventa:
| Acción                  | Necesidad           | Responsable sugerido | Prioridad | Fecha objetivo relativa | Bloquea oferta si no se cierra |
|------------------------|---------------------|----------------------|----------|------------------------|-------------------------------|
| BOM y RFQ              | Licencias, gateway  | Compras/partner      | Alta     | T-12 días              | Sí                            |
| Solicitar carta fabricante| Power BI, gateway| Preventa/partner     | Alta     | T-7 días               | Sí                            |
| Validar SLA back-to-back| Soporte Power BI   | Preventa/partner     | Alta     | T-6 días               | Sí                            |
| Seleccionar herramienta calidad datos| Calidad datos| Preventa/Compras| Media    | T-10 días              | Sí                            |
| Confirmar arquitectura gateway| Gateway       | Preventa/partner     | Alta     | T-10 días              | Sí                            |

---

15. Preguntas al órgano de contratación/fabricantes/partners:
- ¿El gateway de datos debe instalarse en infraestructura del cliente o del adjudicatario?
- ¿Qué herramienta de calidad de datos se considera compatible y aceptable?
- ¿Se permite usar repositorio Git cloud/SaaS o debe ser on-premise?
- ¿Qué SLA mínimo se exige para soporte Power BI y gateway?
- ¿Se requiere carta de fabricante Microsoft para licencias y gateway?

---

16. Opinión final:
La estrategia recomendada es comprar licencias Power BI Pro, gateway de datos y herramienta de calidad de datos vía Cloud Partner Ficticio S.A., asegurando carta de fabricante y SLA back-to-back. No hay bloqueo por canal, pero sí por falta de evidencia de compra/licencia. Cerrar BOM, RFQ y acuerdos antes de presentar oferta. Subcontratación permitida, UTE prohibida. Viabilidad alta si se cierran compras y partnership antes de oferta.

---

17. Documentos revisados:
1. Pliego administrativo OPP-SW-005 BI expedientes
2. Pliego técnico OPP-SW-005 BI expedientes
3. Anexo solvencia OPP-SW-005 BI expedientes