1. Veredicto ejecutivo de coherencia: INCOHERENCIAS CRITICAS

2. Resumen ejecutivo de coherencia:
La información procesada presenta contradicciones graves entre agentes en solvencia de perfiles, solvencia de proyectos, cobertura de partners, operatividad y cumplimiento de certificaciones obligatorias. Existen gaps críticos en la cobertura de perfiles técnicos clave, dependencia de partners no cerrados, y carencias en certificaciones (ISO 20000). Hay incoherencias entre los veredictos de cumplimiento y la realidad de los recursos disponibles, así como riesgos duplicados y datos incompletos sobre licencias, dimensionamiento y acceso a herramientas. La base documental no está lista para un Go/No-Go sin resolver estos bloqueos y validar datos clave.

3. Tabla de veredictos consolidados por agente:
| Agente                        | Veredicto detectado         | Dato consolidado                | Confianza | Observaciones |
|-------------------------------|-----------------------------|-------------------------------|-----------|--------------|
| Resumen profesional           | RECOMENDABLE                | Oportunidad atractiva pero de alto riesgo | Media     | No detecta gaps críticos de perfiles ni partners |
| Solvencia de perfiles         | NO CUMPLE                   | NO CUMPLE                      | Alta      | Gaps críticos en todos los perfiles clave |
| Solvencia de proyectos        | CUMPLE PARCIALMENTE         | NO CUMPLE (importe anual insuficiente) | Alta      | No se alcanza el importe anual mínimo exigido |
| Requisitos administrativos    | CUMPLE PARCIALMENTE         | CUMPLE PARCIALMENTE            | Alta      | Falta ISO 20000, riesgo de exclusión |
| Criterios de adjudicación     | ALTA OPORTUNIDAD            | ALTA OPORTUNIDAD (si se cumplen mínimos) | Media     | Riesgo de exclusión por gaps técnicos |
| Económico-financiero          | MARGEN AJUSTADO             | MARGEN AJUSTADO                | Alta      | Margen bajo, riesgo si se baja precio |
| Compras / Partners            | ALTO RIESGO                 | ALTO RIESGO                    | Alta      | Sin partners ni acuerdos cerrados |
| Delivery / Operación          | NO OPERABLE                 | NO OPERABLE                    | Alta      | Sin equipo ni partners, no viable |
| Service Design / ITIL         | APTO CON GAPS               | APTO CON GAPS                  | Alta      | Gaps en herramientas y cobertura 24x7 |
| Seguridad / DPO / ENS         | CUMPLE CON GAPS             | CUMPLE CON GAPS                | Alta      | Gap ENS alta, reversibilidad, SOC 24x7 |

4. Contradicciones detectadas:
| Contradicción | Agentes afectados | Evidencia | Dato consolidado propuesto | Confianza | Impacto en Go/No-Go |
|--------------|------------------|-----------|---------------------------|-----------|---------------------|
| Cumplimiento de solvencia de perfiles | Resumen profesional vs Solvencia de perfiles, Compras, Delivery | Resumen profesional dice RECOMENDABLE, pero perfiles y delivery dicen NO CUMPLE/NO OPERABLE | NO CUMPLE | Alta | Bloqueante, riesgo de exclusión |
| Solvencia de proyectos (importe anual) | Solvencia de proyectos vs Requisitos administrativos | Proyectos no suman el importe anual mínimo, pero administrativo dice CUMPLE | NO CUMPLE | Alta | Bloqueante, riesgo de exclusión |
| Certificaciones obligatorias (ISO 20000) | Requisitos administrativos vs Seguridad | Falta ISO 20000, sólo ISO 27001 disponible | NO CUMPLE | Alta | Bloqueante, riesgo de exclusión |
| Operatividad real | Delivery vs Compras, Service Design | Delivery dice NO OPERABLE, Compras y Service Design reconocen gaps críticos | NO OPERABLE | Alta | Bloqueante, no viable sin partners |
| Estrategia económica | Económico-financiero vs Criterios de adjudicación | Margen ajustado, riesgo de margen negativo si se baja precio para puntuar | MARGEN AJUSTADO | Alta | Riesgo alto, requiere comité de riesgo |

5. Duplicidades consolidadas:
- Riesgo de exclusión por falta de perfiles clave y partners: aparece en Solvencia de perfiles, Compras, Delivery, Service Design.
- Riesgo por falta de certificación ISO 20000: aparece en Administrativo y Seguridad.
- Riesgo de margen insuficiente: aparece en Económico-financiero y Criterios de adjudicación.

6. Información incompleta o pendiente:
| Dato pendiente | Fuente | Por qué importa | Cómo validarlo | Prioridad |
|---------------|--------|----------------|---------------|----------|
| Cierre de acuerdos con partners para perfiles clave | Compras, Delivery | Sin partners no se puede operar ni cumplir mínimos | Solicitar cartas de compromiso y CVs acreditados | Crítica |
| Certificación ISO 20000 o equivalentes admitidos | Administrativo, Seguridad | Es obligatoria, sin ella hay riesgo de exclusión | Consultar pliego y aclarar con órgano de contratación | Crítica |
| Importe anual acumulado de proyectos de referencia | Solvencia de proyectos | No se alcanza el mínimo exigido | Revisar importes y ventana temporal, buscar proyectos adicionales | Crítica |
| Detalle de licencias y acceso a herramientas cliente | Delivery, Service Design | Sin acceso no se puede operar | Solicitar inventario y acuerdos de acceso | Alta |
| Volumetría real de tickets/incidencias | Delivery, Service Design | Impacta en dimensionamiento y costes | Solicitar datos al cliente | Alta |

7. Riesgos consolidados limpios:
| Riesgo | Categoría | Fuente principal | Fuentes secundarias | Impacto | Probabilidad | Estado | Acción recomendada |
|--------|----------|------------------|---------------------|---------|-------------|--------|-------------------|
| Exclusión por falta de perfiles clave | Técnico/operativo | Solvencia de perfiles | Delivery, Compras | Muy alto | Muy alta | Abierto | Cerrar acuerdos con partners y acreditar perfiles |
| Exclusión por falta de ISO 20000 | Legal/administrativo | Administrativo | Seguridad | Muy alto | Alta | Abierto | Aportar equivalencia o negociar con cliente |
| Margen insuficiente para competir | Económico | Económico-financiero | Criterios de adjudicación | Alto | Alta | Abierto | Revisar costes y estrategia de precio |
| No operatividad por falta de equipo | Operativo | Delivery | Compras, Service Design | Muy alto | Muy alta | Abierto | Cerrar equipo y partners antes de ofertar |
| Dependencia de licencias y herramientas cliente | Operativo | Delivery | Service Design | Alto | Alta | Abierto | Validar acceso y acuerdos con cliente |

8. Hechos consolidados para Go/No-Go:
- No se cumplen los requisitos de perfiles clave ni se dispone de partners acreditados.
- No se alcanza el importe anual acumulado mínimo en proyectos de referencia.
- Falta la certificación ISO 20000, obligatoria según pliego.
- El margen económico es muy ajustado y puede ser negativo si se baja precio para puntuar.
- La operatividad real es inviable sin cerrar equipo y partners.
- Hay riesgos críticos de exclusión y no operatividad.

9. Datos que el A13 no debe usar sin validar:
- Cualquier afirmación de cumplimiento de solvencia de perfiles o proyectos.
- Cualquier afirmación de cumplimiento de certificaciones obligatorias.
- Cualquier simulación de margen que no contemple el coste real de partners externos.
- Cualquier dato de operatividad que no contemple la falta de equipo y partners.

10. Correcciones aplicadas:
- Se ha consolidado el veredicto de solvencia de proyectos como NO CUMPLE, ya que la suma de importes anuales no alcanza el mínimo exigido.
- Se ha consolidado el veredicto de solvencia de perfiles como NO CUMPLE, por ausencia de perfiles clave y partners.
- Se ha marcado la falta de ISO 20000 como bloqueante, aunque algunos agentes la consideraban subsanable.
- Se ha recalculado el margen económico considerando la necesidad de partners externos, lo que reduce el margen real.

11. Paquete limpio para A13:
- Decisión preliminar sugerida: NO-GO PROBABLE
- Bloqueantes: Falta de perfiles clave y partners, falta de ISO 20000, importe anual de proyectos insuficiente.
- Condiciones pendientes: Cierre de acuerdos con partners, validación de equivalencias de certificaciones, revisión de importes de proyectos, validación de acceso a herramientas y licencias.
- Riesgos altos: Exclusión por solvencia técnica y administrativa, no operatividad, margen insuficiente.
- Evidencias positivas: Experiencia en proyectos similares (aunque de menor importe), certificación ISO 27001, ENS media, capacidad de subcontratación, política de precios competitiva.
- Preguntas críticas: ¿Se puede cerrar acuerdos con partners y acreditar perfiles antes de la oferta? ¿El órgano de contratación admite equivalencias a ISO 20000? ¿Se puede aportar proyectos adicionales para cumplir el importe anual? ¿El cliente aporta licencias y acceso a herramientas?

12. Fuentes utilizadas:
- Agentes revisados: Resumen profesional, Solvencia de perfiles, Solvencia de proyectos, Requisitos administrativos, Criterios de adjudicación, Económico-financiero, Compras / Partners, Delivery / Operación, Service Design / ITIL, Seguridad / DPO / ENS.
- Documentos procesados: ANEXO I.pdf, Anuncio.pdf, DOC20240806095753Pliegodefinitivofirmado.pdf, DOC_CD2024-000901195.pdf, perfil-contratante, PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf, y referencias a enlaces no accesibles.