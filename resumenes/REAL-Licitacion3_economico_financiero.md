### 0. Correccion local de estrategia economica
El script ha detectado que la formula economica depende de las ofertas competidoras y ha cruzado la recomendacion con el coste total estimado. Esta lectura prevalece sobre cualquier tabla generada por el agente que trate descuentos agresivos como objetivo sin validar margen.
- Margen estimado ofertando a PBL: 13,8%.
- El margen recomendado interno del 14,0% no se alcanza con el coste actual ni ofertando a PBL.
- Baja maxima aproximada para mantener margen minimo aprobable del 10,0%: 4,2%.
- Linea roja aproximada de margen 8,0%: 6,3%.
- Recomendacion corregida: zona prudente 0%-3%; 5%-8% solo con comite de riesgo y mejoras de coste; >=10% no recomendable con la estructura de costes actual.

---

### 1. Veredicto ejecutivo económico-financiero
**MARGEN AJUSTADO** (con riesgo de erosión de margen si la oferta baja por debajo del 12% sobre PBL; zona de rentabilidad solo asegurada en precios objetivo y conservadores).

---

### 2. Resumen ejecutivo
- **Dinero disponible (PBL sin IVA):** 4.257.280 €
- **Coste total estimado de ejecución:** 3.670.000 € (estimación propia, ver tabla de costes)
- **Margen estimado (oferta a PBL):** 587.280 € (13,8%)
- **Puntuación económica esperada:** 55/55 si somos oferta mínima; 49-53/55 en escenarios con competencia agresiva.
- **Recomendacion de precio corregida localmente:** con el coste total estimado detectado, la baja maxima aproximada para conservar margen minimo del 10,0% es 4,2% y la linea roja del 8,0% queda en 6,3%. Cualquier baja superior debe tratarse como opcion agresiva de comite, no como precio objetivo normal.

---

### 3. Estructura económica del contrato
| Concepto                | Importe (€)         |
|-------------------------|---------------------|
| PBL sin IVA             | 4.257.280           |
| IVA (21%)               | 894.028,80          |
| PBL con IVA             | 5.151.308,80        |
| Valor estimado total    | 10.217.472          |
| Duración inicial        | 25 meses (1 mes transición no facturable) |
| Prórrogas               | Hasta 24 meses adicionales |
| Lotes                   | 2 (Lote 1: 1.527.680 €, Lote 2: 2.729.600 €) |
| Anualidades             | 2024: 532.160 €, 2025: 2.128.640 €, 2026: 1.596.480 € |
| Modificaciones          | Hasta 20% del precio inicial (por necesidades de la Adm.) |
| Bolsas de horas         | Lote 1: 2.640 h/año, Lote 2: 7.040 h/año |
| Precios unitarios       | Por perfil/hora (ver desglose pliego) |

**La oferta se presenta sobre el PBL sin IVA de cada lote.**

---

### 4. Fórmula de puntuación económica
- **Literal:**
  - Si σ < 5: P = 55 × (oferta mínima / oferta licitador)
  - Si σ ≥ 5: P = 55 × (PBL - oferta licitador) / (PBL - oferta mínima)
- **Puntos máximos:** 55
- **Variables:** Oferta licitador, oferta mínima, PBL
- **Comportamiento:**
  - Si somos oferta mínima, 55/55 puntos.
  - Si hay dispersión alta (σ ≥ 5), la penalización por no ser la mínima es mayor.
- **Dependencia de competidores:** Sí, puntos dependen de la oferta más baja.
- **Lectura práctica:** Zona de máxima puntuación entre -10% y -15% si la competencia no baja más; bajadas adicionales pueden no aportar puntos y erosionan margen.

---

### 4.b. Fórmulas de mejoras automáticas no económicas
- **No hay mejoras automáticas cuantificables por fórmula en el pliego.**
- **SLA/ANS:** Penalizaciones y cumplimiento, pero no suman puntos económicos.

---

### 5. Escenarios de puntuación económica
| Variación vs PBL | Oferta sin IVA | Oferta con IVA | Admisible | Puntos (mínima) | Puntos (comp. probable) | Puntos (comp. agresivo) | Margen EUR | Margen % | Riesgo | Lectura |
|------------------|---------------|---------------|-----------|-----------------|------------------------|------------------------|-----------|----------|--------|---------|
| +10%             | 4.682.998     | 5.664.427     | No        | 0               | 0                      | 0                      | 1.012.998 | 21,6%    | No admisible | Sobre PBL, no permitido |
| +5%              | 4.470.144     | 5.408.874     | No        | 0               | 0                      | 0                      | 800.144   | 17,9%    | No admisible | Sobre PBL, no permitido |
| +2%              | 4.342.426     | 5.251.335     | No        | 0               | 0                      | 0                      | 672.426   | 15,5%    | No admisible | Sobre PBL, no permitido |
| 0%               | 4.257.280     | 5.151.309     | Sí        | 55              | 52-53                  | 49-51                  | 587.280   | 13,8%    | Bajo   | Máximo precio admisible |
| -3%              | 4.129.562     | 4.995.771     | Sí        | 55              | 53-54                  | 51-52                  | 459.562   | 11,1%    | Bajo   | Zona conservadora |
| -5%              | 4.044.416     | 4.893.745     | Sí        | 55              | 55                     | 52-53                  | 374.416   | 9,3%     | Medio  | Zona objetivo mínimo |
| -8%              | 3.916.698     | 4.739.205     | Sí        | 55              | 55                     | 53-54                  | 246.698   | 6,3%     | Alto   | Margen bajo, riesgo |
| -10%             | 3.831.552     | 4.637.177     | Sí        | 55              | 55                     | 54-55                  | 161.552   | 4,2%     | Muy alto | Margen crítico |
| -12%             | 3.746.406     | 4.535.150     | Sí        | 55              | 55                     | 55                     | 76.406    | 2,0%     | Muy alto | Margen crítico, solo si imprescindible |
| -15%             | 3.618.688     | 4.378.613     | Sí        | 55              | 55                     | 55                     | -51.312   | -1,4%    | No admisible | Bajo coste, margen negativo |
| -18%             | 3.490.970     | 4.222.076     | Sí        | 55              | 55                     | 55                     | -179.030  | -5,1%    | No admisible | Margen negativo |
| -20%             | 3.405.824     | 4.120.048     | Sí        | 55              | 55                     | 55                     | -264.176  | -7,8%    | No admisible | Margen negativo |
| -22%             | 3.320.678     | 4.018.021     | Sí        | 55              | 55                     | 55                     | -349.322  | -10,5%   | No admisible | Margen negativo |

---

### 6. Opciones de estrategia de precio y opinión
| Opción              | % sobre PBL | Precio sin IVA | Puntos esperados | Margen EUR | Margen % | Condiciones | Opinión |
|---------------------|-------------|---------------|------------------|------------|----------|-------------|---------|
| Conservadora        | -3%         | 4.129.562     | 55               | 459.562    | 11,1%    | Margen >10% | Recomendable si hay presión de costes |
| Objetivo            | -8%         | 3.916.698     | 55               | 246.698    | 6,3%     | Margen bajo | Solo si se justifica por competencia |
| Agresiva            | -12%        | 3.746.406     | 55               | 76.406     | 2,0%     | Margen crítico | Solo si imprescindible para ganar |
| Límite/No ofertar   | -15%        | 3.618.688     | 55               | -51.312    | -1,4%    | Margen negativo | No ofertar, no cubre costes |

---

### 7. Objetivos de puntuación
| % Puntos | Precio máx. estimado | Margen EUR | Advertencia |
|----------|----------------------|------------|-------------|
| 70%      | 4.257.280            | 587.280    | Máximo precio admisible, margen justo |
| 80%      | 4.129.562            | 459.562    | Zona conservadora, margen >10% |
| 90%      | 4.044.416            | 374.416    | Zona objetivo, margen 9% |
| 95%      | 3.916.698            | 246.698    | Zona agresiva, margen bajo |
| 100%     | 3.746.406            | 76.406     | Solo si imprescindible, margen crítico |

---

### 8. Simulación con competidores
- **Conservador:** Competidor baja -5% → 52-53/55 puntos si ofertamos a PBL.
- **Probable:** Competidor baja -8% → 51-53/55 puntos si ofertamos a -5%.
- **Favorable:** Somos oferta mínima → 55/55 puntos.

---

### 9. Oferta anormalmente baja
- **Condición:** Si la puntuación es inferior en más de 10 puntos a la media de las ofertas (3 o más licitadores).
- **Línea roja económica:** Margen bruto <0% (precio <3.670.000 € sin IVA).
- **Precio de riesgo:** Por debajo de -12% sobre PBL (3.746.406 € sin IVA).
- **Procedimiento:** Justificación detallada de estructura de costes, eficiencia, subcontratación y condiciones especiales.

---

### 10. Tabla maestra de costes (estimación)
| Concepto                | Cantidad | Coste pliego | Coste estimado | Total      | Tipo         | Fuente         | Confianza | Comentario |
|-------------------------|----------|--------------|---------------|------------|--------------|---------------|-----------|------------|
| Personal (todas áreas)  | 1        | 3.547.733    | 3.200.000     | 3.200.000  | Directo      | Estimación IA | Alta      | Incluye salarios, overhead y guardias |
| Hardware reposición     | 1        | 0            | 80.000        | 80.000     | Directo      | Estimación     | Media     | Stock y reposición |
| Licencias software      | 1        | 0            | 60.000        | 60.000     | Directo      | Estimación     | Media     | Herramientas ITSM, monitorización |
| Cloud y backup          | 1        | 0            | 60.000        | 60.000     | Directo      | Estimación     | Media     | Azure, backup, VPN |
| Seguridad/cumplimiento  | 1        | 0            | 40.000        | 40.000     | Directo      | Estimación     | Media     | Formación, pentest, auditoría |
| Transición/reversibilidad| 1        | 0            | 50.000        | 50.000     | Directo      | Estimación     | Media     | 4% transición, 2% reversibilidad |
| Formación               | 1        | 0            | 20.000        | 20.000     | Directo      | Estimación     | Media     | Formación usuarios y técnicos |
| Desplazamientos         | 1        | 0            | 30.000        | 30.000     | Directo      | Estimación     | Media     | Sedes periféricas |
| Materiales/consumibles  | 1        | 0            | 10.000        | 10.000     | Directo      | Estimación     | Media     | Fungibles, almacén |
| Subcontratación/terceros| 1        | 0            | 20.000        | 20.000     | Directo      | Estimación     | Media     | Soporte cloud, seguridad |
| Garantías/seguros/financ| 1        | 0            | 20.000        | 20.000     | Indirecto    | Estimación     | Media     | Avales, RC, circulante |
| Contingencia técnica    | 1        | 0            | 80.000        | 80.000     | Indirecto    | Estimación     | Media     | 6% sobre personal |
| **TOTAL**               |          | 3.547.733    | **3.670.000** | **3.670.000** |              |               |           |            |

---

### 11. Costes por categoría
- **Personal:** 3.200.000 €
- **Hardware:** 80.000 €
- **Software/licencias:** 60.000 €
- **Cloud:** 60.000 €
- **Seguridad/cumplimiento:** 40.000 €
- **Transición/reversibilidad:** 50.000 €
- **Formación:** 20.000 €
- **Desplazamientos/presencialidad:** 30.000 €
- **Materiales/consumibles:** 10.000 €
- **Terceros/subcontratación:** 20.000 €
- **Garantías/seguros/financiación:** 20.000 €
- **Contingencia:** 80.000 €

---

### 12. Comparación coste pliego vs coste real
- **Coste pliego:** 3.547.733 € (directo + indirecto, según desglose pliego)
- **Coste real estimado:** 3.670.000 € (incluye overhead, contingencia, costes no explicitados en pliego)
- **Desviaciones relevantes:**
  - Pliego no incluye costes de transición, reversibilidad, formación, desplazamientos, materiales, subcontratación ni contingencia técnica realista.
  - Coste real superior en ~122.000 € (3,4%) respecto a pliego.

---

### 13. Penalizaciones y riesgo económico
- **Penalizaciones por SLA/ANS:** Hasta 10% del presupuesto del contrato por acumulación.
- **Penalizaciones por falta de recursos:** Proporcional a horas no cubiertas, con factores de corrección.
- **Penalizaciones por rotación:** Horas no solapadas descontadas de bolsa.
- **Exposición máxima:** 10% del PBL (425.728 €).

---

### 14. Cash flow y calendario de facturación
- **Facturación:** Trimestral vencida, solo por horas efectivamente trabajadas y certificadas.
- **Primer mes:** No facturable (transición).
- **Pagos:** 60 días estimados tras factura.
- **Compras iniciales:** Hardware, licencias y circulante a analizar si superan 20% PBL.
- **Avales:** 5% garantía definitiva + 5% complementaria si oferta anormal.
- **Riesgo financiero:** Moderado, por volumen y pagos diferidos.

---

### 15. Revisión de precios
- **No existe revisión de precios.**
- **Riesgo:** Alto en contratos >24 meses por inflación salarial, licencias y cloud.
- **Acción recomendada:** Incluir contingencia y negociar revisiones en prórrogas.

---

### 16. Margen del proyecto
- **Coste total estimado:** 3.670.000 €
- **Contingencia incluida:** 80.000 €
- **Margen bruto (oferta a PBL):** 587.280 € (13,8%)
- **Margen bruto (oferta -8%):** 246.698 € (6,3%)
- **Margen bruto (oferta -12%):** 76.406 € (2,0%)
- **Sensibilidad:** Cada punto de baja adicional reduce margen en ~42.500 €.

---

### 17. Zona óptima de oferta
- **Precio objetivo:** -3% a -8% sobre PBL (4.129.562 € a 3.916.698 € sin IVA), margen 6-11%.
- **Precio agresivo:** -12% (3.746.406 € sin IVA), margen 2%.
- **Precio límite:** -15% (3.618.688 € sin IVA), margen negativo, no ofertar.

---

### 18. Recomendaciones de decisión
- **Presentarse:** Sí, si se puede ofertar con margen >8% (precio mínimo recomendado: 3.916.698 € sin IVA).
- **Condiciones para ofertar:** Validar costes de personal, subcontratación y cloud; asegurar cobertura de penalizaciones y contingencias.
- **Cotizaciones necesarias:** Hardware, licencias, cloud, subcontratistas.
- **Aprobaciones internas:** Comité de riesgo si margen <10%.
- **Riesgos a cerrar:** Inflación salarial, subidas de licencias, penalizaciones por ANS, pagos diferidos.

---

### 19. Preguntas al órgano de contratación
- ¿Se aceptan revisiones de precios en prórrogas?
- ¿Se pueden ajustar precios unitarios en bolsas de horas en función de perfiles?
- ¿Qué criterios se aplican para la justificación de oferta anormalmente baja?
- ¿Se permite facturación parcial en transición o solo tras aceptación total?
- ¿Qué costes de licencias y cloud son asumidos por la Adm. y cuáles por el adjudicatario?
- ¿Hay penalizaciones adicionales no explicitadas en el pliego?

---

### 20. Documentos revisados
1. DOC2024020214010801+PPT+2023+VI.pdf
2. DOC20240202141404130-24_PLIEGO.pdf
3. DOC20240202144445012+Anexo+II+Lista+final+de+sedes+del+MITMA+7+nov+2023.pdf
4. DOC20240202144504013+Anexo+III+Resumen+Infraestructura.pdf
5. DOC20240202144519014+Anexo+IV+Resumen+de+activos.pdf
6. DOC20240202144535015+Anexo+V+Conocimientos+equipo+de+trabajo.pdf
7. DOC20240202144619016+Anexo+VI+Datos+de+peticiones+de+servicio+e+incidencias.pdf
8. DOC_CD2024-000159639.pdf
9. DOC_CN2024-000157989.pdf
10. poc (detalle licitación)
11. poc (perfil contratante)
12. poc (perfil contratante duplicado)

---

### Simulacion local de formulas economicas detectadas
Bloque calculado por Python a partir de formulas localizadas en los documentos. Sirve para validar la respuesta del agente y para ver claramente el efecto de cada rango de descuento.
- Presupuesto de referencia usado: 4.257.280 EUR sin IVA.
- Coste total estimado usado para margenes: 3.670.000 EUR.

#### Formula dependiente de competidores #1: DOC20240202141404130-24_PLIEGO.pdf
Detectado: 55 puntos maximos. Si sigma >= 5, puntuacion lineal por baja frente a la oferta mas economica. Si sigma < 5, proporcional inversa por importe.
Importante: no se puede saber la puntuacion exacta antes de conocer las ofertas competidoras; por eso se simulan mejores ofertas competidoras.
Tabla escenario sigma < 5

| Nuestra baja | Oferta sin IVA | Margen EUR | Margen % | Mejor oferta -5% | Mejor oferta -10% | Mejor oferta -15% | Mejor oferta -20% | Lectura |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0,0% | 4.257.280 EUR | 587.280 EUR | 13,8% | 52,2/55 | 49,5/55 | 46,8/55 | - | Tensionado pero defendible. |
| 3,0% | 4.129.562 EUR | 459.562 EUR | 11,1% | 53,9/55 | 51/55 | 48,2/55 | - | Tensionado pero defendible. |
| 5,0% | 4.044.416 EUR | 374.416 EUR | 9,3% | 55/55 | 52,1/55 | 49,2/55 | - | Solo con aprobacion de riesgo. |
| 8,0% | 3.916.698 EUR | 246.698 EUR | 6,3% | 55/55 | 53,8/55 | 50,8/55 | - | Alto riesgo: por debajo de linea roja de margen. |
| 10,0% | 3.831.552 EUR | 161.552 EUR | 4,2% | 55/55 | 55/55 | 51,9/55 | - | Alto riesgo: por debajo de linea roja de margen. |
| 12,0% | 3.746.406 EUR | 76.406 EUR | 2,0% | 55/55 | 55/55 | 53,1/55 | - | Alto riesgo: por debajo de linea roja de margen. |
| 15,0% | 3.618.688 EUR | -51.312 EUR | -1,4% | 55/55 | 55/55 | 55/55 | - | No rentable con coste actual. |
| 18,0% | 3.490.970 EUR | -179.030 EUR | -5,1% | 55/55 | 55/55 | 55/55 | - | No rentable con coste actual. |
| 20,0% | 3.405.824 EUR | -264.176 EUR | -7,8% | 55/55 | 55/55 | 55/55 | - | No rentable con coste actual. |
Tabla escenario sigma >= 5

| Nuestra baja | Oferta sin IVA | Margen EUR | Margen % | Mejor oferta -5% | Mejor oferta -10% | Mejor oferta -15% | Mejor oferta -20% | Lectura |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0,0% | 4.257.280 EUR | 587.280 EUR | 13,8% | - | 0/55 | 0/55 | 0/55 | Tensionado pero defendible. |
| 3,0% | 4.129.562 EUR | 459.562 EUR | 11,1% | - | 16,5/55 | 11/55 | 8,2/55 | Tensionado pero defendible. |
| 5,0% | 4.044.416 EUR | 374.416 EUR | 9,3% | - | 27,5/55 | 18,3/55 | 13,8/55 | Solo con aprobacion de riesgo. |
| 8,0% | 3.916.698 EUR | 246.698 EUR | 6,3% | - | 44/55 | 29,3/55 | 22/55 | Alto riesgo: por debajo de linea roja de margen. |
| 10,0% | 3.831.552 EUR | 161.552 EUR | 4,2% | - | 55/55 | 36,7/55 | 27,5/55 | Alto riesgo: por debajo de linea roja de margen. |
| 12,0% | 3.746.406 EUR | 76.406 EUR | 2,0% | - | 55/55 | 44/55 | 33/55 | Alto riesgo: por debajo de linea roja de margen. |
| 15,0% | 3.618.688 EUR | -51.312 EUR | -1,4% | - | 55/55 | 55/55 | 41,2/55 | No rentable con coste actual. |
| 18,0% | 3.490.970 EUR | -179.030 EUR | -5,1% | - | 55/55 | 55/55 | 49,5/55 | No rentable con coste actual. |
| 20,0% | 3.405.824 EUR | -264.176 EUR | -7,8% | - | 55/55 | 55/55 | 55/55 | No rentable con coste actual. |
Lectura estrategica local:
- Esta formula no permite fijar una puntuacion unica antes de conocer la competencia; hay que decidir precio por equilibrio entre puntos esperados y margen.
- Si nuestra oferta es la mas economica, obtenemos la maxima puntuacion economica, pero bajar mas solo mejora la posicion relativa si evita que otro licitador quede por debajo.
- Margen a PBL: 13,8%.
- El margen recomendado interno del 14,0% no se alcanza ni ofertando a PBL; antes de bajar precio conviene reducir coste, alcance o riesgo.
- Baja maxima para mantener margen minimo aprobable 10,0%: 4,2%.
- Linea roja operativa con margen 8,0%: 6,3%.
- Recomendacion local: tratar 0%-3% como zona prudente/tensionada, 5%-8% como decision de comite y >=10% como alto riesgo con el coste actual.

---

### Validacion automatica de coherencia economica
El script ha revisado aritmeticamente la respuesta anterior y ha detectado posibles incoherencias:
- Fila '-5%': aparece como objetivo/recomendable, pero su margen estimado es 9,3%, por debajo del minimo aprobable (10,0%).
- Fila 'Conservadora': aparece como objetivo/recomendable, pero su margen estimado es 11,1%, por debajo del margen recomendado (14,0%). Debe tratarse como opcion tensionada.
- Fila 'Objetivo': aparece como objetivo/recomendable, pero su margen estimado es 6,3%, por debajo del minimo aprobable (10,0%).
- Esta validacion se calcula localmente con las cifras escritas en la salida. Si Druid corrige la tabla en una nueva ejecucion, este bloque desaparecera.