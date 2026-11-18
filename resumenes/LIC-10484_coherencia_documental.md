1. Veredicto ejecutivo de coherencia: COHERENTE CON OBSERVACIONES

2. Resumen ejecutivo de coherencia:
La información consolidada está mayoritariamente lista para Go/No-Go, pero existen brechas críticas en la acreditación de solvencia sectorial, experiencia de perfiles clave y evidencia documental interna. No se detectan incoherencias matemáticas graves ni contradicciones entre fórmulas económicas, pero la ausencia de datos sectoriales, CBE y CV firmados impide declarar cumplimiento pleno. Los riesgos y duplicidades han sido consolidados, y las contradicciones entre agentes se han resuelto o marcadas como pendientes de validación. La base es utilizable para decisión preliminar, pero requiere validación documental antes de ofertar.

3. Tabla de veredictos consolidados por agente:
| Agente                  | Veredicto detectado         | Dato consolidado                  | Confianza | Observaciones |
|------------------------|-----------------------------|-----------------------------------|-----------|--------------|
| Resumen profesional    | RECOMENDABLE CON GAPS       | Viable condicionado               | Alta      | Brecha documental sectorial |
| Solvencia de perfiles  | Extracción objetiva         | NO ACREDITADO perfiles clave      | Media     | Falta CV/títulos firmados |
| Solvencia de proyectos | Extracción objetiva         | NO ACREDITADO solvencia técnica   | Media     | Falta CBE/relación sectorial |
| Requisitos admin/legales| Extracción objetiva        | CUMPLE requisitos formales        | Alta      | Cumple formal, brecha sectorial |
| Criterios adjudicación | Extracción objetiva         | Criterios claros, fórmula correcta| Alta      | Fórmula económica coherente |
| Económico-financiero   | RENTABLE CON GAPS           | NO ACREDITADO solvencia sectorial | Alta      | Falta ventas sectoriales |
| Compras/Partners       | Extracción objetiva         | NO EXIGIDO partners/certificados  | Alta      | No hay dependencias externas |
| Delivery/Operación     | OPERABLE                    | Cubierto operativo, brecha documental| Alta  | Software propio, falta evidencia |
| Service Design/ITIL    | Extracción objetiva         | CUMPLE modelo operativo           | Alta      | No hay requisitos ITIL/CMDB |
| Seguridad/DPO/ENS      | Extracción objetiva         | NO EXIGIDO ENS/ISO, CUMPLE RGPD   | Alta      | No hay requisitos técnicos |

4. Contradicciones detectadas:
| Contradicción                                    | Agentes afectados         | Evidencia                  | Dato consolidado propuesto | Confianza | Impacto en Go/No-Go |
|--------------------------------------------------|--------------------------|----------------------------|---------------------------|-----------|---------------------|
| Solvencia sectorial NO ACREDITADA vs. cobertura declarada | Resumen, Económico, Proyectos | Lista ficticia interna, pliego | NO ACREDITADO            | Alta      | Bloqueante, requiere validación |
| Perfiles clave declarados vs. falta de CV/títulos | Perfiles, Delivery        | Lista ficticia interna     | NO ACREDITADO             | Alta      | Bloqueante, requiere validación |
| Software propio declarado vs. falta de evidencia  | Delivery, Compras         | Lista ficticia interna     | PENDIENTE VALIDACION      | Media     | Medio, requiere validación |

5. Duplicidades consolidadas:
- Riesgo de falta de solvencia sectorial y experiencia de perfiles clave aparece en Resumen, Económico, Proyectos y Perfiles. Consolidado como "Riesgo de exclusión por falta de acreditación sectorial y perfiles clave".
- Riesgo de falta de evidencia documental interna aparece en Económico, Delivery y Perfiles. Consolidado como "Riesgo de exclusión por falta de evidencia documental interna".

6. Información incompleta o pendiente:
| Dato pendiente                  | Fuente                | Por qué importa           | Cómo validarlo           | Prioridad |
|-------------------------------|-----------------------|--------------------------|--------------------------|-----------|
| Desglose ventas sector energía/gas | Económico, Resumen   | Solvencia sectorial      | Aportar ventas auditadas | Alta      |
| CBE y relación de servicios sectoriales | Proyectos, Económico | Solvencia técnica        | Aportar CBE y relación firmada | Alta      |
| CV y títulos firmados perfiles clave | Perfiles, Delivery   | Solvencia de perfiles    | Aportar CV/títulos firmados | Alta      |
| Evidencia software propio conexión remota | Delivery, Compras  | Requisito operativo      | Aportar evidencia software | Media     |

7. Riesgos consolidados limpios:
| Riesgo                                         | Categoria         | Fuente principal         | Fuentes secundarias | Impacto | Probabilidad | Estado | Acción recomendada |
|-----------------------------------------------|-------------------|-------------------------|---------------------|--------|-------------|--------|-------------------|
| Exclusión por falta de solvencia sectorial    | Solvencia         | Económico, Proyectos     | Resumen, Perfiles   | Alto   | Alta        | Abierto | Validar ventas sectoriales |
| Exclusión por falta de experiencia perfiles   | Solvencia         | Perfiles, Delivery       | Económico, Resumen  | Alto   | Alta        | Abierto | Validar CV/títulos |
| Exclusión por falta de evidencia software     | Operación         | Delivery, Compras        | Resumen             | Medio  | Media       | Abierto | Validar software propio |
| Penalidades por retraso en informes           | Operación         | Service Design, Seguridad| Económico           | Medio  | Media       | Abierto | Vigilar plazos y calidad |

8. Hechos consolidados para Go/No-Go:
- El pliego exige solvencia sectorial y técnica específica, no acreditada en evidencia interna.
- Se exige experiencia mínima de 3 años en perfiles clave, no acreditada en evidencia interna.
- No se exige póliza RC, clasificación, ENS, ISO ni partnership.
- El modelo operativo es viable, pero requiere evidencia de software propio.
- La fórmula económica es coherente y dependiente de la oferta mínima.
- No hay dependencias externas ni requisitos de subrogación, hardware, licencias o partners.
- Penalidades por retraso y conciliación laboral pueden impactar en gestión.

9. Datos que el A13 no debe usar sin validar:
- Ventas globales como sustituto de ventas sectoriales.
- Declaración de cobertura de perfiles sin CV/títulos firmados.
- Declaración de software propio sin evidencia documental.
- CBE o relación de servicios sin acreditación documental.

10. Correcciones aplicadas:
- No se han recalculado costes, márgenes ni número de perfiles; se ha consolidado el estado de NO ACREDITADO para solvencia sectorial y perfiles clave, diferenciando evidencia interna de acreditación documental.

11. Paquete limpio para A13:
- Decision preliminar sugerida: GO CONDICIONADO PROBABLE
- Bloqueantes: Falta de acreditación de solvencia sectorial y experiencia de perfiles clave.
- Condiciones pendientes: Aportar ventas sectoriales, CBE, CV/títulos firmados, evidencia software propio.
- Riesgos altos: Exclusión por falta de solvencia sectorial y perfiles clave.
- Evidencias positivas: Cumplimiento de requisitos administrativos, modelo operativo viable, fórmula económica coherente.
- Preguntas críticas: ¿Se puede acreditar ventas sectoriales y experiencia de perfiles clave antes del cierre de oferta?

12. Fuentes utilizadas:
- Agentes revisados: Resumen profesional, Solvencia de perfiles, Solvencia de proyectos, Requisitos administrativos y legales, Criterios de adjudicación, Económico-financiero, Compras/Partners, Delivery/Operación, Service Design/ITIL, Seguridad/DPO/ENS.
- Documentos procesados: LIC10484 PCP CLAUS.pdf, LIC10484 PPT.pdf, LIC10484 PPT Anexo 2.pdf, LIC10484 PCP CDC Anexo 2.pdf, LIC10484 PPT Anexo 1.pdf, LIC10484 PCP CDC Anexo 1.xlsx, LIC10484 PCP ANEXOS.pdf, LIC10484 PCP CDC.pdf, LIC10484 PPT Anexo 3.pdf, Documento de aprobación del expediente.

Extracción de viabilidad (matriz breve):
| Parámetro                        | Estado         | Dato decisivo / umbral                | Fuente pliego / doc. | Acción interna / evidencia |
|----------------------------------|---------------|--------------------------------------|----------------------|---------------------------|
| Volumen anual sector energía/gas | NO ACREDITADO | ≥34.440 EUR, 1 de 3 últimos ejercicios| PCP CDC.pdf, 10.C    | Aportar ventas sectoriales |
| Relación servicios sectoriales    | NO ACREDITADO | ≥16.072 EUR/año, 1 de 3 últimos años  | PCP CDC.pdf, 10.D    | Aportar CBE/relación firmada|
| Perfiles clave                   | NO ACREDITADO | 2 perfiles, ≥3 años experiencia       | PPT.pdf, 10-11; PCP CDC.pdf, 10.E | Aportar CV/títulos firmados |
| Software propio conexión remota   | PENDIENTE VALIDACION | 1 sistema propio, funcional         | PPT.pdf, 4           | Aportar evidencia software |
| Garantía definitiva              | PENDIENTE     | 5% sobre oferta sin IVA               | PCP CDC.pdf, 12.A/B  | Preparar aval/seguro caución |
| Requisitos admin/legales         | CUMPLE        | Capacidad obrar, no prohibición, DEUC | PCP CLAUS.pdf, 9, 17 | Cumple formal              |
| Criterios adjudicación           | CUMPLE        | Fórmula económica, experiencia perfiles| PCP CDC.pdf, 15.B    | Fórmula coherente          |
| Partners/certificados            | NO EXIGIDO    | No se exige partnership, ISO, ENS     | PCP CDC.pdf, 10.B    | N/A                       |
| Subcontratación                  | CUMPLE        | Permitida, no tareas críticas         | PCP CLAUS.pdf, 36-38 | Declarar subcontratistas   |