### 0. Correccion local de estrategia economica
El script ha detectado que la formula economica depende de las ofertas competidoras y ha cruzado la recomendacion con el coste total estimado. Esta lectura prevalece sobre cualquier tabla generada por el agente que trate descuentos agresivos como objetivo sin validar margen.
- Margen estimado ofertando a PBL: 12,5%.
- El margen recomendado interno del 14,0% no se alcanza con el coste actual ni ofertando a PBL.
- Baja maxima aproximada para mantener margen minimo aprobable del 10,0%: 2,8%.
- Linea roja aproximada de margen 8,0%: 4,9%.
- Recomendacion corregida: zona prudente 0%-3%; 5%-8% solo con comite de riesgo y mejoras de coste; >=10% no recomendable con la estructura de costes actual.

---

### 1. Veredicto ejecutivo económico-financiero
**RENTABLE CON GAPS**

---

### 2. Resumen ejecutivo
- **Dinero disponible (PBL sin IVA):** 1.622.793,48 €
- **Coste total estimado de ejecución:** 1.420.000 € (estimación propia, ver detalle)
- **Margen bruto estimado (oferta a PBL):** 202.793 € (12,5%)
- **Puntuación económica esperada:** 48 puntos si somos oferta mínima; 43-47 puntos en escenarios competitivos
- **Recomendacion de precio corregida localmente:** con el coste total estimado detectado, la baja maxima aproximada para conservar margen minimo del 10,0% es 2,8% y la linea roja del 8,0% queda en 4,9%. Cualquier baja superior debe tratarse como opcion agresiva de comite, no como precio objetivo normal.

---

### 3. Estructura económica del contrato
| Concepto                | Importe (€)         |
|-------------------------|---------------------|
| PBL sin IVA             | 1.622.793,48        |
| IVA (21%)               | 340.786,63          |
| PBL con IVA             | 1.963.580,11        |
| Valor estimado          | 3.245.586,96        |
| Duración inicial        | 24 meses            |
| Prórrogas               | 24 meses (máx.)     |
| Lotes                   | No                  |
| Anualidades             | 2025: 490.895,03; 2026: 981.790,05; 2027: 490.895,03 |
| Modificaciones          | 0%                  |
| Bolsas                  | 47.611,20 € (horas extra) |
| Precios unitarios       | Horas extra: 21,94-25,60 €/h x1,75 |

**Oferta económica:** Se presenta sobre el importe sin IVA (1.622.793,48 € máx.).

---

### 4. Fórmula de puntuación económica
- **Literal:** Ci = 48 × (1 - (Oi - Omin) / Omax)
- **Puntos máximos:** 48
- **Variables:** Oi (nuestra oferta), Omin (mínima), Omax (máxima)
- **Comportamiento:** Oferta más baja obtiene 48 puntos. El resto, proporcional a la distancia entre Omin y Omax.
- **Dependencia de competidores:** Sí, la puntuación depende de la dispersión de ofertas.
- **Lectura práctica:** Si somos oferta mínima, 48 puntos. Si hay ofertas más bajas, la puntuación baja según la diferencia y el rango de ofertas.

---

### 4.b. Fórmulas de mejoras automáticas no económicas
- **Experiencia equipo:** Hasta 20 puntos (proporcional a meses de mejora sobre mínimo)
- **Certificaciones:** Hasta 12 puntos (por certificaciones valorables, ver tabla pliego)
- **Cobertura horaria:** 24x5 = 8 puntos; 24x7 = 20 puntos
- **Lectura:** Mejoras técnicas cuantificables, pero no afectan al precio ni al margen.

---

### 5. Escenarios de puntuación económica
| Variación vs PBL | Oferta sin IVA | Oferta con IVA | Admisible | Puntos (mínima) | Puntos (comp. probable) | Puntos (comp. agresivo) | Margen EUR | Margen % | Riesgo | Lectura |
|------------------|---------------|---------------|-----------|-----------------|------------------------|-------------------------|------------|----------|--------|---------|
| +10%             | 1.785.073     | 2.159.940     | No        | -               | -                      | -                       | -          | -        | No admisible: supera PBL |
| +5%              | 1.703.933     | 2.061.760     | No        | -               | -                      | -                       | -          | -        | No admisible: supera PBL |
| +2%              | 1.655.249     | 2.003.851     | No        | -               | -                      | -                       | -          | -        | No admisible: supera PBL |
| 0%               | 1.622.793     | 1.963.580     | Sí        | 48              | 45,6                   | 43,2                    | 202.793    | 12,5%    | Bajo   | Máxima puntuación si mínima |
| -3%              | 1.574.110     | 1.905.673     | Sí        | 48              | 47                     | 44,6                    | 154.110    | 9,8%     | Medio  | Puntuación alta, margen ajustado |
| -5%              | 1.541.654     | 1.865.402     | Sí        | 48              | 48                     | 45,6                    | 121.654    | 7,9%     | Alto   | Margen bajo, riesgo económico |
| -8%              | 1.492.970     | 1.806.494     | Sí        | 48              | 48                     | 47                      | 72.970     | 4,9%     | Muy alto | Margen crítico, solo si imprescindible |
| -10%             | 1.460.514     | 1.766.223     | Sí        | 48              | 48                     | 47                      | 40.514     | 2,8%     | Muy alto | Solo con aprobación de riesgo |
| -12%             | 1.428.058     | 1.725.952     | Sí        | 48              | 48                     | 47                      | 8.058      | 0,6%     | No recomendable | Margen casi nulo |
| -15%             | 1.379.375     | 1.667.044     | Sí        | 48              | 48                     | 47                      | -40.625    | -2,9%    | No ofertar | Margen negativo |
| -18%             | 1.330.691     | 1.608.136     | Sí        | 48              | 48                     | 47                      | -89.309    | -6,7%    | No ofertar | Margen negativo |
| -20%             | 1.298.235     | 1.567.865     | Sí        | 48              | 48                     | 47                      | -121.765   | -9,4%    | No ofertar | Margen negativo |
| -22%             | 1.265.779     | 1.527.594     | Sí        | 48              | 48                     | 47                      | -154.221   | -12,2%   | No ofertar | Margen negativo |

**Nota:** Margen calculado sobre coste estimado 1.420.000 € (ver tabla maestra de costes).

---

### 6. Opciones de estrategia de precio y opinión
| Opción              | % sobre PBL | Precio sin IVA | Puntos esperados | Margen EUR | Margen % | Condiciones | Opinión |
|---------------------|-------------|---------------|------------------|------------|----------|-------------|---------|
| Conservadora        | 0%          | 1.622.793     | 48               | 202.793    | 12,5%    | Máxima seguridad, margen >10% | Recomendable si hay presión de costes |
| Objetivo            | -8%         | 1.492.970     | 48               | 72.970     | 4,9%     | Margen bajo, puntuación máxima | Solo si se asume riesgo, requiere comité |
| Agresiva            | -12%        | 1.428.058     | 48               | 8.058      | 0,6%     | Margen casi nulo | No recomendable |
| Límite/No ofertar   | -15%        | 1.379.375     | 48               | -40.625    | -2,9%    | Margen negativo | No ofertar |

---

### 7. Objetivos de puntuación
| % puntos económicos | Precio máx. estimado | Margen EUR | Advertencia |
|---------------------|---------------------|------------|-------------|
| 70%                 | 1.460.514           | 40.514     | Margen bajo, solo si imprescindible |
| 80%                 | 1.492.970           | 72.970     | Margen bajo, requiere comité |
| 90%                 | 1.541.654           | 121.654    | Margen ajustado |
| 95%                 | 1.574.110           | 154.110    | Margen aceptable |
| 100%                | 1.622.793           | 202.793    | Margen óptimo, máxima seguridad |

---

### 8. Simulación con competidores
- **Conservador:** Competidor baja -5% (1.541.654 €). Si igualamos, margen 7,9% (bajo, requiere comité).
- **Probable:** Competidor baja -8% (1.492.970 €). Si igualamos, margen 4,9% (crítico, solo si imprescindible).
- **Favorable:** Somos oferta mínima (-10% o más). Margen <3%, solo recomendable si hay mejoras técnicas diferenciales.

---

### 9. Oferta anormalmente baja
- **Condición:** Según art. 85 RCAP y LCSP, se analizarán ofertas con baja excesiva respecto a la media.
- **Línea roja económica:** Margen bruto <8% (1.491.000 € aprox.)
- **Precio de riesgo:** Por debajo de 1.492.000 € sin IVA, justificación obligatoria y riesgo de exclusión.
- **Procedimiento:** Justificación técnica y económica detallada, desglose de costes, explicación de eficiencias y estructura de personal.

---

### 10. Tabla maestra de costes
| Concepto                | Cantidad | Coste pliego | Coste estimado | Total      | Tipo      | Fuente         | Confianza | Comentario |
|-------------------------|----------|--------------|---------------|------------|-----------|---------------|-----------|------------|
| Personal base           | 17       | 1.334.241    | 1.200.000     | 1.200.000  | Interno   | Estimación IA | Alta      | Incluye overhead y suplencias |
| Bolsa horas extra       | 600      | 47.611       | 47.611        | 47.611     | Pliego    | Pliego         | Alta      | 480 soporte, 120 sistemas |
| Hardware (portátiles)   | 17       | -            | 13.260        | 13.260     | Interno   | Coste empresa  | Media     | 780 €/ud. estándar |
| Smartphones             | 10       | -            | 3.200         | 3.200      | Interno   | Coste empresa  | Media     | 320 €/ud. |
| Licencias Office 365    | 17       | -            | 8.976         | 8.976      | Interno   | Coste empresa  | Alta      | 264 €/ud./año x 2 años |
| Licencias Visio/Planner | 2        | -            | 1.056         | 1.056      | Interno   | Coste empresa  | Media     | 264 €/ud./año x 2 años |
| Antivirus/seguridad     | 17       | -            | 2.448         | 2.448      | Interno   | Coste empresa  | Media     | 72 €/ud./año x 2 años |
| Formación continua      | 17       | -            | 10.200        | 10.200     | Interno   | Coste empresa  | Media     | 300 €/ud./año x 2 años |
| Desplazamientos         | 45       | -            | 17.100        | 17.100     | Interno   | Coste empresa  | Media     | 380 €/desplazamiento |
| Material oficina        | 17       | -            | 1.700         | 1.700      | Interno   | Estimación     | Media     | 50 €/ud. |
| Seguros/garantías       | 1        | -            | 19.473        | 19.473     | Interno   | 1,2% aval      | Alta      | 5% garantía definitiva |
| Contingencia técnica    | -        | -            | 85.000        | 85.000     | Interno   | 6% estándar    | Media     | Sobre total |
| **TOTAL**               | -        | 1.381.852    | 1.420.024     | 1.420.024  | -         | -             | -         | - |

---

### 11. Costes por categoría
- **Personal:** 1.200.000 €
- **Hardware:** 13.260 €
- **Software/licencias:** 10.032 €
- **Cloud:** No aplica (infraestructura cliente)
- **Seguridad/cumplimiento:** 2.448 €
- **Transición:** Incluida en personal (asunción 1 mes)
- **Reversibilidad:** Incluida en personal (devolución 1 mes)
- **Formación:** 10.200 €
- **Desplazamientos/presencialidad:** 17.100 €
- **Materiales/consumibles:** 1.700 €
- **Terceros/subcontratación:** No relevante
- **Garantías/seguros/financiación:** 19.473 €

---

### 12. Comparación coste pliego vs coste real
- **Coste pliego:** 1.381.852 € (personal + bolsa + GG + BI)
- **Coste real estimado:** 1.420.000 € (mayor por overhead, formación, desplazamientos, contingencia)
- **Desviaciones:** Pliego no incluye todos los costes indirectos, formación, desplazamientos ni contingencia realista.

---

### 13. Penalizaciones y riesgo económico
- **SLA/ANS:** Penalizaciones de hasta 1-5% del contrato por incumplimiento grave, hasta 10% por reiteración.
- **Retrasos:** 0,6 €/1.000 € día de retraso.
- **Incumplimiento criterios adjudicación:** Hasta 5% del contrato.
- **Exposición máxima:** Hasta 50% del contrato en penalizaciones acumuladas.

---

### 14. Cash flow y calendario de facturación
- **Pagos:** Trimestrales, abonos a cuenta.
- **Cobros:** 60 días estimados tras factura.
- **Compras iniciales:** Hardware y licencias al inicio (aprox. 30.000 €).
- **Avales:** 5% del importe de adjudicación (81.140 € aprox. a PBL).
- **Seguros:** Incluidos en costes.
- **Circulante:** Riesgo bajo-medio, salvo retrasos de cobro.

---

### 15. Revisión de precios
- **No existe revisión de precios.**
- **Impacto:** Riesgo de inflación en personal y licencias si el contrato se prorroga.
- **Acción recomendada:** Incluir contingencia y revisar precios internos antes de prórroga.

---

### 16. Margen del proyecto
- **Coste total estimado:** 1.420.000 €
- **Contingencia incluida:** 85.000 € (6%)
- **Margen bruto para precios de oferta:**
    - A PBL: 202.793 € (12,5%)
    - -5%: 121.654 € (7,9%)
    - -8%: 72.970 € (4,9%)
    - -10%: 40.514 € (2,8%)
    - -12%: 8.058 € (0,6%)
    - -15%: -40.625 € (-2,9%)

---

### 17. Zona óptima de oferta
- **Precio objetivo:** 1.541.654 € (-5% sobre PBL), margen 7,9%, puntuación máxima si somos mínimos.
- **Precio agresivo:** 1.492.970 € (-8% sobre PBL), margen 4,9%, solo si imprescindible y con comité de riesgo.
- **Precio límite:** 1.491.000 € (margen 4,8%), por debajo, riesgo de anormalidad y margen crítico.

---

### 18. Recomendaciones de decisión
- **Presentarse:** Sí, si se puede asegurar margen >5% y se justifica competitividad técnica.
- **Condiciones para ofertar:** Validar costes reales de personal, overhead y desplazamientos. No bajar de -8% sin comité.
- **Cotizaciones necesarias:** Hardware, licencias, desplazamientos, seguros.
- **Aprobaciones internas:** Comité de riesgo si margen <10%.
- **Riesgos a cerrar:** Inflación salarial, penalizaciones por SLA, retrasos de cobro.

---

### 19. Preguntas al órgano de contratación
- ¿Se aceptan revisiones de precios en prórrogas?
- ¿Se puede facturar mensualmente en vez de trimestral?
- ¿Se pueden ajustar precios unitarios de bolsa de horas en prórroga?
- ¿Hay penalizaciones específicas por rotación de personal?
- ¿Se pueden repercutir costes de formación obligatoria?

---

### 20. Documentos revisados
1. Anuncio.pdf
2. PCAP.pdf
3. PPT.pdf
4. poc (detalle licitación)
5. poc (perfil contratante)
6. poc (perfil contratante ampliado)

---

**Conclusión:**
- El contrato es **rentable con gaps** si se oferta a PBL o con baja moderada (-5%).
- El margen cae rápidamente con bajas agresivas; no ofertar por debajo de -8% sin comité de riesgo.
- La zona óptima es entre 0% y -5% sobre PBL, asegurando margen y puntuación alta.
- Requiere control estricto de costes y justificación si se opta por estrategia agresiva.

---

### Simulacion local de formulas economicas detectadas
Bloque calculado por Python a partir de formulas localizadas en los documentos. Sirve para validar la respuesta del agente y para ver claramente el efecto de cada rango de descuento.
- Presupuesto de referencia usado: 1.622.793 EUR sin IVA.
- Coste total estimado usado para margenes: 1.420.024 EUR.

#### Formula lineal Omin/Omax #1: PCAP.pdf
Detectado: 48 puntos maximos. La oferta minima obtiene el maximo; el resto se calcula frente a Omin y Omax, por lo que hay que simular competidores.
| Variacion vs PL | Oferta sin IVA | Puntos si somos minima | Puntos comp. -5% | Puntos comp. -10% | Puntos comp. -15% | Margen EUR | Margen % | Lectura |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 10,0% | 1.785.073 EUR | No admisible | No admisible | No admisible | No admisible | 365.049 EUR | 20,5% | No admisible: supera el PL salvo permiso expreso. |
| 5,0% | 1.703.933 EUR | No admisible | No admisible | No admisible | No admisible | 283.909 EUR | 16,7% | No admisible: supera el PL salvo permiso expreso. |
| 2,0% | 1.655.249 EUR | No admisible | No admisible | No admisible | No admisible | 235.225 EUR | 14,2% | No admisible: supera el PL salvo permiso expreso. |
| 0,0% | 1.622.793 EUR | 48 | 45,6 | 43,2 | 40,8 | 202.769 EUR | 12,5% | Tensionado: defendible solo si la mejora de puntos compensa. |
| -3,0% | 1.574.110 EUR | 48 | 47 | 44,6 | 42,2 | 154.086 EUR | 9,8% | Solo con aprobacion de comite de riesgo. |
| -5,0% | 1.541.654 EUR | 48 | 48 | 45,6 | 43,2 | 121.630 EUR | 7,9% | Alto riesgo: por debajo de linea roja de margen. |
| -8,0% | 1.492.970 EUR | 48 | 48 | 47 | 44,6 | 72.946 EUR | 4,9% | Alto riesgo: por debajo de linea roja de margen. |
| -10,0% | 1.460.514 EUR | 48 | 48 | 48 | 45,6 | 40.490 EUR | 2,8% | Alto riesgo: por debajo de linea roja de margen. |
| -12,0% | 1.428.058 EUR | 48 | 48 | 48 | 46,6 | 8.034 EUR | 0,6% | Alto riesgo: por debajo de linea roja de margen. |
| -15,0% | 1.379.374 EUR | 48 | 48 | 48 | 48 | -40.650 EUR | -2,9% | No rentable con coste actual. |
| -18,0% | 1.330.691 EUR | 48 | 48 | 48 | 48 | -89.333 EUR | -6,7% | No rentable con coste actual. |
| -20,0% | 1.298.235 EUR | 48 | 48 | 48 | 48 | -121.789 EUR | -9,4% | No rentable con coste actual. |
| -22,0% | 1.265.779 EUR | 48 | 48 | 48 | 48 | -154.245 EUR | -12,2% | No rentable con coste actual. |
Lectura estrategica local:
- La formula reparte 48 puntos con Omin/Omax; si somos la oferta minima obtenemos el maximo, pero si otro baja mas perdemos puntos de forma gradual.
- Para evitar conclusiones falsas, la tabla simula Omax=PBL y competidores minimos al -5%, -10% y -15%.
- Margen a PBL: 12,5%.
- Baja maxima aproximada para mantener margen minimo aprobable del 10,0%: 2,8%.
- Linea roja aproximada de margen 8,0%: 4,9%.
- Recomendacion local: no llamar 'objetivo' a una baja que quede por debajo del 10% de margen; debe pasar a agresiva o no recomendable.

---

### Validacion automatica de coherencia economica
El script ha revisado aritmeticamente la respuesta anterior y ha detectado posibles incoherencias:
- Fila 'Conservadora': aparece como objetivo/recomendable, pero su margen estimado es 12,5%, por debajo del margen recomendado (14,0%). Debe tratarse como opcion tensionada.
- Fila 'Objetivo': aparece como objetivo/recomendable, pero su margen estimado es 4,9%, por debajo del minimo aprobable (10,0%).
- Esta validacion se calcula localmente con las cifras escritas en la salida. Si Druid corrige la tabla en una nueva ejecucion, este bloque desaparecera.