1. Veredicto ejecutivo de coherencia: INCOHERENCIAS CRITICAS

2. Resumen ejecutivo de coherencia:
La información procesada presenta incoherencias críticas y transversales. La primera es de personal: no se dispone del equipo mínimo de tres desarrolladores Java senior exigido por el pliego, ni internamente ni vía partners, lo que bloquea la viabilidad de la oferta. La segunda es económica: el agente económico calculó inicialmente la partida de tres desarrolladores Java al 70% como 1,05 FTE durante 2 años, cuando debe ser 2,1 FTE durante 2 años. Corrigiendo esta partida, el coste estimado sube a 540.880 EUR frente a un PBL sin IVA de 360.000 EUR. La información está lista para Go/No-Go solo si ambos puntos se tratan como bloqueantes: solvencia de perfiles y no rentabilidad.

3. Tabla de veredictos consolidados por agente:
| Agente                        | Veredicto detectado         | Dato consolidado                        | Confianza | Observaciones                                                      |
|-------------------------------|-----------------------------|-----------------------------------------|-----------|--------------------------------------------------------------------|
| Resumen profesional           | RECOMENDABLE CON GAPS       | Gap de perfiles Java bloqueante         | Alta      | Advierte riesgo por equipo mínimo y penalizaciones                 |
| Solvencia de perfiles         | NO CUMPLE                   | No hay 3 desarrolladores Java           | Alta      | Gap literal, riesgo de exclusión                                   |
| Solvencia de proyectos        | CUMPLE                      | Solvencia de proyectos OK               | Alta      | Dos referencias válidas                                             |
| Requisitos administrativos    | CUMPLE PARCIALMENTE         | Gap en solvencia de personas            | Alta      | Advierte riesgo en perfiles Java                                   |
| Criterios de adjudicación     | ALTA OPORTUNIDAD            | Gap de perfiles puede invalidar oferta   | Media     | Estrategia viable solo si se cubre el equipo                       |
| Económico-financiero          | NO RENTABLE                 | Coste corregido 540.880 EUR > PBL 360.000 EUR | Alta | Incoherencia aritmética corregida; no hay zona rentable             |
| Compras / Partners            | BLOQUEANTE                  | No hay partner Java disponible           | Alta      | Gap literal, no cubierto ni interna ni externamente                |
| Delivery / Operacion          | NO OPERABLE                 | Gap de personal impide operar           | Alta      | No se puede arrancar el servicio                                    |
| Service Design / ITIL         | APTO CON GAPS               | Gap de dimensionamiento Java            | Alta      | Riesgo operativo por falta de personal                             |
| Seguridad / DPO / ENS         | CUMPLE CON GAPS             | Cumple ENS básica, gaps menores         | Alta      | Falta detalle en acuerdos de encargado y subcontratistas           |

4. Contradicciones detectadas:
| Contradicción                                               | Agentes afectados                | Evidencia                                                                 | Dato consolidado propuesto                | Confianza | Impacto en Go/No-Go                |
|-------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------|-------------------------------------------|-----------|-------------------------------------|
| Cumplimiento de equipo mínimo de desarrolladores Java       | Todos excepto Solvencia proyectos| Solvencia de perfiles, Compras, Delivery: NO CUMPLE; Resumen: GAPS        | NO CUMPLE (gap bloqueante)                | Muy alta  | Bloquea la viabilidad de la oferta  |
| Jefe de servicio con ITIL Foundation y experiencia específica| Solvencia de perfiles, Delivery  | Ana Torres: experiencia en dirección, no en mantenimiento ni ITIL         | Gap parcial, requiere refuerzo/validación | Alta      | Riesgo de exclusión, pero menor     |
| Estrategia de adjudicación viable vs. gap de personal       | Criterios adjudicación vs. resto | Criterios: ALTA OPORTUNIDAD; resto: NO CUMPLE por personal                | NO CUMPLE si no se cubre el gap           | Alta      | Oferta inviable sin cubrir el gap   |
| Rentabilidad económica del contrato                         | Económico-financiero             | Coste inicial 312.800 EUR contenía error en desarrolladores Java          | NO RENTABLE: coste corregido 540.880 EUR  | Alta      | Bloquea la viabilidad económica     |

5. Duplicidades consolidadas:
- Riesgo de exclusión por falta de desarrolladores Java senior aparece en Resumen, Solvencia de perfiles, Compras, Delivery y Service Design. Se consolida en un único riesgo bloqueante.
- Gap en experiencia/certificación del jefe de servicio aparece en Solvencia de perfiles y Delivery. Se consolida como gap parcial, no bloqueante inmediato.
- Riesgo económico aparece en Económico-financiero y en la validación automática. Se consolida como bloqueante de rentabilidad tras corregir la partida de desarrolladores Java.

6. Información incompleta o pendiente:
| Dato pendiente                                 | Fuente                | Por qué importa                        | Cómo validarlo                  | Prioridad |
|------------------------------------------------|-----------------------|----------------------------------------|----------------------------------|-----------|
| Incorporación de 2 desarrolladores Java senior  | Solvencia de perfiles | Es requisito literal de exclusión      | Contratar y acreditar perfiles   | Crítica   |
| Certificación ITIL Foundation jefe de servicio  | Solvencia de perfiles | Puede ser causa de exclusión formal    | Aportar certificado o sustituir  | Alta      |
| Preacuerdo con DBA Oracle autónomo              | Compras, Delivery     | Soporte puntual crítico                | Firmar preacuerdo                | Media     |
| Detalle de acuerdo de encargado RGPD            | Seguridad             | Cumplimiento legal y contractual       | Redactar y firmar acuerdo        | Media     |

7. Riesgos consolidados limpios:
| Riesgo                                         | Categoría         | Fuente principal         | Fuentes secundarias         | Impacto   | Probabilidad | Estado   | Acción recomendada                |
|------------------------------------------------|-------------------|-------------------------|-----------------------------|-----------|--------------|----------|-----------------------------------|
| Falta de 2 desarrolladores Java senior         | Operativo/legal   | Solvencia de perfiles   | Compras, Delivery, Resumen  | Crítico   | Muy alta     | Abierto  | Contratar antes de ofertar        |
| Jefe de servicio sin ITIL Foundation           | Legal/operativo   | Solvencia de perfiles   | Delivery                    | Alto      | Alta         | Abierto  | Certificar o sustituir            |
| Coste corregido superior al PBL                | Económico         | Económico-financiero    | Validación local            | Crítico   | Alta         | Abierto  | No ofertar salvo aclaración de dedicaciones |
| Penalizaciones por incumplimiento de SLA       | Operativo         | Resumen, Económico      | Service Design              | Alto      | Media        | Abierto  | Plan de contingencia              |
| Dependencia de DBA Oracle puntual              | Operativo         | Compras, Delivery       | Service Design              | Medio     | Media        | Abierto  | Preacuerdo urgente                |
| Falta de acuerdo de encargado RGPD             | Legal             | Seguridad               | -                           | Medio     | Media        | Abierto  | Redactar y firmar                 |

8. Hechos consolidados para Go/No-Go:
- El pliego exige tres desarrolladores Java senior (Spring, SQL, mantenimiento).
- Solo hay uno disponible; faltan dos, ni internos ni en red de partners.
- Jefe de servicio propuesto no acredita ITIL Foundation ni experiencia específica en mantenimiento.
- Solvencia de proyectos, económica y legal: CUMPLE.
- Subcontratación permitida hasta 30%, pero no resuelve el gap de personal.
- Margen económico no viable con coste corregido: 540.880 EUR frente a 360.000 EUR de PBL sin IVA.
- Resto de requisitos técnicos, legales y de seguridad: cubiertos con observaciones.

9. Datos que el A13 no debe usar sin validar:
- Cualquier afirmación de que se cumple el equipo mínimo de desarrolladores Java.
- Que Ana Torres cumple inequívocamente como jefe de servicio (falta ITIL Foundation y experiencia específica).
- Que la oferta es viable sin incorporar los perfiles faltantes.

10. Correcciones aplicadas:
- No se han recalculado costes ni márgenes, ya que el gap de personal bloquea la viabilidad antes de llegar a la fase económica.
- Se ha consolidado el riesgo de personal como único y bloqueante, eliminando duplicidades.

11. Paquete limpio para A13:
- Decisión preliminar sugerida: NO-GO PROBABLE
- Bloqueantes: Falta de 2 desarrolladores Java senior, coste corregido superior al PBL, jefe de servicio sin ITIL Foundation ni experiencia específica.
- Condiciones pendientes: Incorporar y acreditar los perfiles faltantes, certificar jefe de servicio, preacuerdo DBA Oracle, acuerdo de encargado RGPD.
- Riesgos altos: Penalizaciones por SLA, dependencia de DBA puntual, ausencia de revisión de precios.
- Evidencias positivas: Solvencia de proyectos, económica y legal cubiertas; experiencia en sector público; herramientas y procesos ITIL disponibles.
- Preguntas críticas: ¿Se pueden contratar y acreditar los desarrolladores Java antes de la presentación? ¿Se puede certificar o sustituir al jefe de servicio? ¿Se puede firmar el preacuerdo con el DBA y el acuerdo de encargado RGPD a tiempo?

12. Fuentes utilizadas:
- Agentes: Resumen profesional, Solvencia de perfiles, Solvencia de proyectos, Requisitos administrativos, Criterios de adjudicación, Económico-financiero, Compras/Partners, Delivery/Operación, Service Design/ITIL, Seguridad/DPO/ENS.
- Documentos: Pliego administrativo, Pliego técnico, Anexo solvencia OPP-SW-004 mantenimiento Java.
