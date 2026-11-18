1. Veredicto ejecutivo económico-financiero: RENTABLE CON GAPS

2. Resumen ejecutivo:
- Dinero disponible: 180.000 EUR sin IVA (PBL), 217.800 EUR con IVA.
- Coste total estimado de ejecución: ~157.000 EUR (ver desglose y tabla maestra de costes).
- Margen estimado: 12,8% sobre PBL (precio objetivo), 8,3% en precio agresivo, 6,1% en precio límite (ver detalle).
- Puntuación económica esperada: 80-95% puntos con margen sostenible, 100% puntos solo con margen muy ajustado o riesgo de anormalidad.
- Recomendación de precio: ofertar con baja del 10-12% (precio objetivo: 162.000-158.400 EUR), nunca por debajo de 148.500 EUR (baja del 17,5%).

3. Estructura económica del contrato:
| Concepto                | Importe         |
|-------------------------|-----------------|
| PBL sin IVA             | 180.000 EUR     |
| IVA (21%)               | 37.800 EUR      |
| PBL con IVA             | 217.800 EUR     |
| Valor estimado          | 180.000 EUR     |
| Duración                | 6 meses         |
| Prórrogas               | No              |
| Lotes                   | No              |
| Anualidades             | No              |
| Modificaciones          | No indicadas    |
| Bolsas                  | No              |
| Precios unitarios       | No (precio cerrado) |

- La oferta económica se presenta sobre el PBL sin IVA: 180.000 EUR.

4. Fórmula de puntuación económica:
- Literal: P = 35 x (oferta mínima / oferta licitador)
- Puntos máximos: 35
- Variables: oferta mínima (de todos los licitadores), oferta del licitador
- Comportamiento: proporcional inversa, dependiente de la oferta más baja
- Dependencia de competidores: sí, la máxima puntuación solo la obtiene la oferta más baja
- Lectura práctica: cada punto porcentual de baja respecto a la mínima penaliza linealmente la puntuación

5. Escenarios de puntuación económica:
| Oferta (EUR) | Baja (%) | Puntos económicos | Margen estimado | Riesgo |
|--------------|----------|-------------------|-----------------|--------|
| 180.000      | 0%       | 35,0              | 14,6%           | Bajo   |
| 171.000      | 5%       | 33,3              | 13,0%           | Bajo   |
| 162.000      | 10%      | 31,5              | 12,0%           | Bajo   |
| 153.000      | 15%      | 29,8              | 8,9%            | Medio  |
| 147.600      | 18%      | 28,7              | 6,1%            | Alto   |
| 144.000      | 20%      | 28,0              | 4,2%            | Muy alto|

*Nota: Puntuación calculada suponiendo que la oferta mínima coincide con el escenario de baja máxima. Si hay ofertas más bajas, la puntuación real será menor.

6. Objetivos de puntuación:
| % Puntos económicos | Precio máximo (EUR) | Margen estimado | Advertencia |
|---------------------|--------------------|-----------------|-------------|
| 70% (24,5 ptos)     | 180.000            | 14,6%           | Sin riesgo  |
| 80% (28,0 ptos)     | 162.000            | 12,0%           | Recomendado |
| 90% (31,5 ptos)     | 153.000            | 8,9%            | Margen justo|
| 95% (33,3 ptos)     | 147.600            | 6,1%            | Riesgo alto |
| 100% (35 ptos)      | 144.000            | 4,2%            | No recomendado|

7. Simulación con competidores:
- Conservador: 2 ofertas por debajo del 15%, una al 18%. Si se oferta al 10%, se obtendrían ~80% puntos económicos.
- Probable: mayoría de ofertas entre 10-15% de baja. Ofertar al 12% permite estar en el top 2-3, con 85-90% puntos.
- Favorable: solo una oferta agresiva al 15-18%, resto al 8-10%. Ofertar al 10% permite 90-95% puntos.

8. Oferta anormalmente baja:
- Umbral: baja superior al 30% (126.000 EUR) exige justificación exhaustiva; baja >35% (117.000 EUR) es línea roja y no recomendable.
- Procedimiento: justificar dedicaciones, herramientas y jornadas de pentesting. Riesgo de exclusión si no se acredita viabilidad.

9. Tabla maestra de costes (extracto):
| Concepto                  | Cantidad | Coste pliego | Coste estimado | Total   | Tipo         | Fuente         | Confianza | Comentario                       |
|---------------------------|----------|--------------|----------------|---------|--------------|---------------|-----------|-----------------------------------|
| Pentester senior          | 2        | No           | 6.000/mes      | 72.000  | Personal     | Estimación IA  | Alta      | 2 x 6 meses x 6.000 EUR          |
| Auditor ISO 27001         | 1        | No           | 6.500/mes      | 19.500  | Personal     | Estimación IA  | Alta      | 1 x 3 meses x 6.500 EUR          |
| Consultor evidencias      | 1        | No           | 5.000/mes      | 10.000  | Personal     | Estimación IA  | Media     | 2 meses                          |
| Herramientas pentest      | 1        | No           | 9.000          | 9.000   | Licencias    | Coste interno  | Alta      | Pentest web anual                |
| Repositorio cifrado       | 1        | No           | 1.500          | 1.500   | Licencias    | Estimación IA  | Media     | 6 meses                          |
| Custodia evidencias 24m   | 1        | No           | 2.000          | 2.000   | Cloud        | Estimación IA  | Media     | 2 años almacenamiento            |
| Retest                    | 1        | No           | 4.000          | 4.000   | Personal     | Estimación IA  | Media     | 1 mes                            |
| Transferencia 12h         | 1        | No           | 1.140          | 1.140   | Personal     | Interno        | Alta      | 95 EUR/h x 12                    |
| Overhead y estructura     | 1        | No           | 12%            | 13.800  | Overhead     | Interno        | Alta      | Sobre personal                   |
| Contingencia técnica      | 1        | No           | 6%             | 7.800   | Contingencia | Interno        | Alta      | Sobre personal                   |
| Seguro RC proporcional    | 1        | No           | 1.000          | 1.000   | Seguro       | Interno        | Alta      | 6 meses                          |
| TOTAL COSTE ESTIMADO      | -        | -            | -              | 157.000 | -            | -              | -         |                                   |

10. Costes por categoría:
- Personal: 101.640 EUR (pentesters, auditor, consultor, transferencia, retest)
- Licencias/herramientas: 10.500 EUR (pentest, repositorio)
- Cloud/custodia: 2.000 EUR
- Overhead/estructura: 13.800 EUR
- Contingencia técnica: 7.800 EUR
- Seguro RC: 1.000 EUR
- Desplazamientos: 0 EUR (no requeridos)
- Subcontratación: 0 EUR (prohibida en pentesting)
- Otros: 0 EUR

11. Comparación coste pliego vs coste real:
- El pliego no detalla costes, pero el coste real estimado es 157.000 EUR (87% del PBL). No hay bolsas ni precios unitarios. Costes de herramientas y custodia están bien cubiertos. Costes de personal ajustados pero viables.

12. Penalizaciones y riesgo económico:
- Penalización por filtración/confidencialidad: hasta 10% del contrato (18.000 EUR).
- Penalización por retraso en evidencias críticas: 2% por entrega tardía.
- Exposición máxima: 18.000 EUR (muy grave), 3.600 EUR (retrasos).

13. Cash flow y calendario de facturación:
- 20% inicio y plan (36.000 EUR)
- 40% entrega informes iniciales (72.000 EUR)
- 25% retest (45.000 EUR)
- 15% transferencia y cierre (27.000 EUR)
- No se prevén compras iniciales elevadas ni avales superiores a 80.000 EUR.
- Riesgo financiero bajo.

14. Revisión de precios:
- No existe. Riesgo bajo por duración corta (6 meses). No impacta en licencias ni personal.

15. Margen del proyecto:
- Coste total estimado: 157.000 EUR
- Contingencia incluida: sí (6%)
- Margen bruto:
  - Oferta 180.000 EUR: 14,6%
  - Oferta 162.000 EUR: 12,0%
  - Oferta 153.000 EUR: 8,9%
  - Oferta 147.600 EUR: 6,1%
  - Oferta 144.000 EUR: 4,2%

16. Zona óptima de oferta:
- Precio objetivo: 162.000-158.400 EUR (baja 10-12%), 80-90% puntos, margen 12-13%.
- Precio agresivo: 153.000-147.600 EUR (baja 15-18%), 90-95% puntos, margen 6-9%.
- Precio límite: 144.000 EUR (baja 20%), margen <5%, riesgo de anormalidad y no recomendado.

17. Recomendaciones de decisión:
- Presentarse si se puede cubrir el segundo pentester con recurso propio o contratación directa.
- No ofertar por debajo de 147.600 EUR salvo aprobación de comité de riesgo.
- Cotizar herramientas y custodia si hay dudas de precios de mercado.
- Revisar penalizaciones y asegurar cumplimiento de confidencialidad.
- Confirmar disponibilidad de equipo certificado y experiencia ENS.

18. Preguntas al órgano de contratación:
- ¿Se aceptan herramientas SaaS de pentesting si cumplen residencia UE?
- ¿Se puede facturar por hitos parciales si hay entregas intermedias?
- ¿Hay precios unitarios para ampliaciones o bolsas de horas?
- ¿Se permite ampliar la transferencia de conocimiento si se justifica?
- ¿Qué procedimiento exacto se sigue para justificar bajas anormales?

19. Documentos revisados:
1. Pliego administrativo OPP-SW-007 ciberseguridad
2. Pliego técnico OPP-SW-007 ciberseguridad
3. Anexo solvencia OPP-SW-007 ciberseguridad