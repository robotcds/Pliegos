1. Veredicto ejecutivo de coherencia: INCOHERENCIAS CRITICAS

2. Resumen ejecutivo de coherencia:
La información procesada presenta incoherencias críticas y bloqueantes en solvencia de perfiles, solvencia de proyectos, clasificación empresarial y cobertura operativa. Existen contradicciones entre agentes sobre el cumplimiento de requisitos administrativos y técnicos, y la validación aritmética del área económica alerta de márgenes insuficientes para bajas competitivas. Hay duplicidad de riesgos en personal y cobertura geográfica, y la información sobre la fórmula económica y dimensionamiento de FTE es suficiente pero requiere validación. El paquete no está listo para Go/No-Go sin resolver los gaps de personal, clasificación y solvencia técnica, y sin aclarar la viabilidad operativa y de partners.

3. Tabla de veredictos consolidados por agente:
| Agente                        | Veredicto detectado         | Dato consolidado                | Confianza | Observaciones |
|-------------------------------|-----------------------------|-------------------------------|-----------|--------------|
| Resumen profesional           | RECOMENDABLE                | Referencia útil, no ofertable  | Alta      | Contrato ya adjudicado |
| Solvencia de perfiles         | NO CUMPLE                   | No cubre número ni experiencia | Alta      | Gap crítico en personal |
| Solvencia de proyectos        | NO CUMPLE                   | No cumple importe anual mínimo | Alta      | Gap crítico en experiencia |
| Requisitos administrativos    | CUMPLE PARCIALMENTE         | No cumple clasificación V3-5   | Alta      | Bloqueante |
| Criterios de adjudicación     | ALTA OPORTUNIDAD            | Criterios automáticos claros   | Alta      | No hay subjetividad |
| Económico-financiero          | RENTABLE CON GAPS           | Margen insuficiente para bajas | Alta      | Validación aritmética alerta de riesgo |
| Compras / Partners            | BLOQUEANTE                  | No hay personal ni partners    | Alta      | Gap crítico en cobertura |
| Delivery / Operación          | NO OPERABLE                 | No hay recursos ni backups     | Alta      | Gap crítico en operación |
| Service Design / ITIL         | APTO CON GAPS               | Gaps en 24x7 y herramientas    | Media     | Cubrible con acciones, pero depende de personal |
| Seguridad / DPO / ENS         | CUMPLE CON GAPS             | ENS básica cubierta, detalles pendientes | Alta      | No bloqueante, pero requiere adaptación |

4. Contradicciones detectadas:
| Contradicción | Agentes afectados | Evidencia | Dato consolidado propuesto | Confianza | Impacto en Go/No-Go |
|--------------|------------------|-----------|---------------------------|-----------|--------------------|
| Cumplimiento solvencia técnica (proyectos) | Solvencia de proyectos vs. Requisitos administrativos | Proyectos no cumplen importe anual, pero administrativo marca CUMPLE en solvencia técnica | NO CUMPLE (proyectos) | Alta | Bloqueante, riesgo de exclusión |
| Clasificación empresarial | Requisitos administrativos vs. corporativo | Pliego exige V3-5, empresa no la tiene, administrativo marca CUMPLE PARCIAL | NO CUMPLE | Alta | Bloqueante, riesgo de exclusión |
| Cobertura de personal y partners | Solvencia de perfiles, Compras, Delivery | No hay personal ni partners suficientes, todos marcan NO CUMPLE/BLOQUEANTE/NO OPERABLE | NO CUMPLE | Alta | Bloqueante |
| Margen económico y baja competitiva | Económico-financiero | Validación aritmética: margen insuficiente para bajas >3% | Margen máximo 2,8% para margen 10% | Alta | Riesgo económico alto |

5. Duplicidades consolidadas:
- Riesgo "Falta de personal suficiente y cobertura geográfica" aparece en Solvencia de perfiles, Compras, Delivery y Service Design. Consolidado como: "No se cubre el número mínimo de recursos ni la distribución geográfica exigida, ni con personal propio ni con partners."
- Riesgo "No disponer de clasificación empresarial V3-5" aparece en Administrativo y corporativo. Consolidado como: "No se dispone de la clasificación empresarial obligatoria, lo que implica exclusión."

6. Información incompleta o pendiente:
| Dato pendiente | Fuente | Por qué importa | Cómo validarlo | Prioridad |
|----------------|--------|----------------|---------------|----------|
| Capacidad de aportar solvencia de terceros (UTE/partners) | Solvencia de proyectos, Compras | Única vía para cumplir solvencia técnica y personal | Confirmar socios con experiencia y personal acreditable | Crítica |
| Plan de captación de personal y partners | Delivery, Compras | Sin plan, no es viable la operación | Presentar plan de contratación y acuerdos firmados | Crítica |
| Validación de margen real con estructura de costes definitiva | Económico-financiero | Margen insuficiente para bajas competitivas | Recalcular con costes reales y estructura de personal completa | Alta |
| Detalle de certificaciones valorables aportables | Solvencia de perfiles, Service Design | Afecta puntuación técnica | Recopilar certificados y asignar a perfiles | Media |

7. Riesgos consolidados limpios:
| Riesgo | Categoría | Fuente principal | Fuentes secundarias | Impacto | Probabilidad | Estado | Acción recomendada |
|--------|-----------|------------------|---------------------|--------|-------------|--------|-------------------|
| No cubrir número mínimo de personal ni distribución geográfica | Operativo/Exclusión | Solvencia de perfiles | Delivery, Compras | Muy alto | Muy alta | Abierto | Buscar socios/contratar |
| No disponer de clasificación empresarial V3-5 | Legal/Exclusión | Administrativo | Corporativo | Muy alto | Muy alta | Abierto | No ofertar salvo cambio |
| No cumplir solvencia técnica de proyectos | Legal/Exclusión | Solvencia de proyectos | Administrativo | Muy alto | Muy alta | Abierto | Buscar socios/UTE |
| Margen insuficiente para baja competitiva | Económico | Económico-financiero | Interno | Alto | Alta | Abierto | Recalcular costes, ajustar oferta |
| Gaps en certificaciones valorables | Técnico | Solvencia de perfiles | Service Design | Medio | Alta | Abierto | Buscar perfiles certificados |

8. Hechos consolidados para Go/No-Go:
- El pliego exige clasificación empresarial V3-5, que la empresa no tiene.
- No se cubre el número mínimo de personal ni la distribución geográfica exigida.
- No se cumple el requisito de solvencia técnica de proyectos (importe anual mínimo).
- El margen bruto estimado solo permite bajas del 2,8% para mantener margen mínimo aprobable.
- La subcontratación y UTE son posibles, pero no resuelven los gaps si los socios no aportan solvencia y personal.
- Los criterios de adjudicación son 100% automáticos y claros.
- ENS básica y requisitos de seguridad se cumplen, pero hay detalles operativos a adaptar.

9. Datos que el A13 no debe usar sin validar:
- Cualquier afirmación de cumplimiento de solvencia técnica de proyectos sin aportar contratos adicionales o socios.
- Cualquier afirmación de viabilidad operativa sin plan de captación de personal y partners firmado.
- Cualquier cálculo de margen que no incluya la estructura de personal completa y costes reales.
- Cualquier afirmación de cumplimiento de clasificación empresarial sin acreditación formal.

10. Correcciones aplicadas:
- Se ha consolidado el margen máximo de baja competitiva en 2,8% para mantener margen mínimo aprobable (fuente: validación aritmética del agente económico-financiero).
- Se ha corregido el dato de solvencia técnica de proyectos a NO CUMPLE, prevaleciendo la evidencia de proyectos ejecutados sobre la tabla administrativa.
- Se ha consolidado el riesgo de personal y cobertura geográfica en un único riesgo operativo crítico.

11. Paquete limpio para A13:
- Decisión preliminar sugerida: NO-GO PROBABLE
- Bloqueantes: Falta de clasificación empresarial V3-5, no cubrir número mínimo de personal ni solvencia técnica de proyectos.
- Condiciones pendientes: Confirmar socios/UTE con solvencia y personal, plan de captación de personal, validación de margen real.
- Riesgos altos: Exclusión automática por clasificación y solvencia, inviabilidad operativa, margen insuficiente para competir.
- Evidencias positivas: Criterios de adjudicación automáticos y claros, ENS básica cubierta, experiencia en sector público.
- Preguntas críticas: ¿Se puede acreditar solvencia de terceros? ¿Se puede captar el personal necesario a tiempo? ¿Se puede ajustar el margen sin comprometer la viabilidad?

12. Fuentes utilizadas:
- Agentes: Resumen profesional, Solvencia de perfiles, Solvencia de proyectos, Requisitos administrativos, Criterios de adjudicación, Económico-financiero, Compras/Partners, Delivery/Operación, Service Design/ITIL, Seguridad/DPO/ENS.
- Documentos: Anuncio.pdf, PCAP.pdf, PPT.pdf, enlaces POC (detalle licitación, perfil contratante).

---

### Validacion local de formulas y margen para consolidacion
El script ha detectado una formula economica lineal Omin/Omax en los documentos y no ha detectado una formula por rangos DtoN/Dto1/PE1. Por tanto, cualquier referencia a DtoN como requisito pendiente de esta licitacion debe tratarse como no aplicable salvo validacion manual contraria.
- Formula detectada: 48 puntos con Omin/Omax en PCAP.pdf.
- PBL sin IVA usado: 1.622.793 EUR.
- Coste total estimado usado: 1.420.024 EUR.
- Margen ofertando a PBL: 12,5%.
- Baja maxima aproximada para mantener margen minimo 10,0%: 2,8%.
- Linea roja aproximada de margen 8,0%: 4,9%.