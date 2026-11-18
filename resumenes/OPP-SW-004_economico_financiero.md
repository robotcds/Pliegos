### 1. Veredicto ejecutivo económico-financiero
**NO RENTABLE**

La salida inicial de Druid indicaba `RENTABLE CON GAPS`, pero contenía una incoherencia aritmética relevante: el coste de los tres desarrolladores Java estaba calculado como `62.000 EUR/año x 1,05 FTE x 2 años`, cuando el pliego exige tres desarrolladores al 70%, es decir, `2,1 FTE/año x 2 años`. Corrigiendo solo esa partida, el coste mínimo estimado pasa a `540.880 EUR`, por encima del PBL sin IVA de `360.000 EUR`.

---

### 2. Resumen ejecutivo
- **Dinero disponible (PBL sin IVA):** 360.000 EUR
- **PBL con IVA:** 435.600 EUR
- **Coste total estimado corregido:** 540.880 EUR
- **Margen a PBL:** -180.880 EUR (-50,2%)
- **Fórmula económica:** P = 55 x oferta mínima / oferta licitador
- **Oferta anormal:** inferior al 85% del PBL, es decir, por debajo de 306.000 EUR.
- **Recomendación:** no ofertar con el modelo de equipo mínimo exigido, salvo que se demuestre que las dedicaciones del pliego son orientativas y no obligatorias.

---

### 3. Estructura económica del contrato
| Concepto | Importe/Estructura |
|---|---:|
| PBL sin IVA | 360.000 EUR |
| IVA 21% | 75.600 EUR |
| PBL con IVA | 435.600 EUR |
| Valor estimado | 360.000 EUR |
| Duración | 24 meses |
| Anualidades | 180.000 EUR/año |
| Facturación | Mensual tras certificación |
| Revisión de precios | No prevista |
| Bolsa mínima incluida | 900 h/año |
| Bolsa adicional puntuable | Máximo 100 h/año |

---

### 4. Fórmula de puntuación económica
- **Literal:** P = 55 x oferta mínima / oferta licitador.
- **Puntos máximos:** 55.
- **Lectura:** bajar precio puede mejorar puntuación, pero el contrato ya queda en pérdida incluso ofertando al precio máximo.

---

### 5. Tabla de bajadas/subidas, presupuesto, puntos y margen
Hipótesis de puntuación: competidor mínimo con baja del -10% (324.000 EUR). Si nuestra oferta es igual o inferior a esa referencia, se simula 55/55.

| % sobre PBL | Precio sin IVA | Margen EUR | Margen % | Puntos esc. comp. -10% | Lectura |
|---:|---:|---:|---:|---:|---|
| +10% | 396.000 EUR | -144.880 EUR | -36,6% | No admisible | Supera PBL |
| +5% | 378.000 EUR | -162.880 EUR | -43,1% | No admisible | Supera PBL |
| +2% | 367.200 EUR | -173.680 EUR | -47,3% | No admisible | Supera PBL |
| 0% | 360.000 EUR | -180.880 EUR | -50,2% | 49,5/55 | No rentable |
| -3% | 349.200 EUR | -191.680 EUR | -54,9% | 51/55 | No rentable |
| -5% | 342.000 EUR | -198.880 EUR | -58,2% | 52,1/55 | No rentable |
| -8% | 331.200 EUR | -209.680 EUR | -63,3% | 53,8/55 | No rentable |
| -10% | 324.000 EUR | -216.880 EUR | -66,9% | 55/55 | No rentable |
| -12% | 316.800 EUR | -224.080 EUR | -70,7% | 55/55 | No rentable |
| -15% | 306.000 EUR | -234.880 EUR | -76,8% | 55/55 | No rentable y umbral anormal |
| -18% | 295.200 EUR | -245.680 EUR | -83,2% | 55/55 | No rentable |
| -20% | 288.000 EUR | -252.880 EUR | -87,8% | 55/55 | No rentable |
| -22% | 280.800 EUR | -260.080 EUR | -92,6% | 55/55 | No rentable |

---

### 6. Tabla maestra de costes corregida
| Concepto | Cálculo corregido | Total estimado | Tipo | Confianza |
|---|---:|---:|---|---|
| Jefe de servicio 25% | 72.000 x 0,25 x 2 años | 36.000 EUR | Personal | Alta |
| 3 desarrolladores Java 70% | 62.000 x 3 x 0,70 x 2 años | 260.400 EUR | Personal | Alta |
| Soporte L2 100% | 42.000 x 1 x 2 años | 84.000 EUR | Personal | Alta |
| QA 20% | 43.000 x 0,20 x 2 años | 17.200 EUR | Personal | Alta |
| Guardias despliegue | 650 x 2 noches/mes x 12 meses | 15.600 EUR | Personal | Media |
| Sustituciones/vacaciones | Estimación Druid mantenida | 15.000 EUR | Personal | Media |
| Overhead gestión/estructura | Estimación Druid mantenida | 36.000 EUR | Personal | Media |
| Contingencia técnica | Estimación Druid mantenida | 18.000 EUR | Contingencia | Media |
| Herramientas calidad/monitorización | SonarQube/Grafana equivalentes | 6.000 EUR | Software | Media |
| Licencias Jira agentes | 900 x 5 x 2 años | 9.000 EUR | Software | Media |
| Entorno de pruebas | Estimación Druid | 3.000 EUR | Hardware | Media |
| DBA Oracle/PostgreSQL | 24 h x 150 EUR/h | 3.600 EUR | Terceros | Media |
| Transición | 4% PBL | 14.400 EUR | Transición | Media |
| Reversibilidad | 2% PBL | 7.200 EUR | Reversibilidad | Media |
| Formación | 24 h x 95 EUR/h | 2.280 EUR | Formación | Alta |
| Desplazamientos | 12 visitas x 380 EUR | 4.560 EUR | Viajes | Media |
| Seguros/aval | Estimación Druid | 8.640 EUR | Financiación | Media |
| **TOTAL CORREGIDO** |  | **540.880 EUR** |  |  |

---

### 7. Conclusión económica
No existe zona de oferta rentable con los datos actuales. Incluso ofertando al PBL máximo, el contrato queda aproximadamente `180.880 EUR` por debajo del coste estimado corregido. La oportunidad debe tratarse como **NO RENTABLE** salvo que el órgano de contratación aclare que las dedicaciones son meramente referenciales o que parte del equipo/servicio no debe incluirse en el precio.

---

### 8. Preguntas críticas
- ¿Las dedicaciones de jefe de servicio, desarrolladores, soporte L2 y QA son mínimas obligatorias o referencias estimativas?
- ¿Las 900 horas/año sustituyen parte de la dedicación recurrente o son adicionales?
- ¿Existe una partida separada para transición, reversibilidad, guardias o herramientas?
- ¿Puede revisarse el precio por subida salarial durante los 24 meses?
- ¿Se admite un modelo bajo demanda que reduzca la dedicación fija?

---

### 9. Documentos revisados
1. Pliego administrativo OPP-SW-004 mantenimiento Java
2. Pliego técnico OPP-SW-004 mantenimiento Java
3. Anexo solvencia OPP-SW-004 mantenimiento Java

---

### Validación automática de coherencia económica
La respuesta original de Druid fue corregida localmente. La incoherencia principal estaba en la partida de desarrolladores Java: `3 desarrolladores x 70% x 24 meses` equivale a `2,1 FTE/año durante 2 años`, no a `1,05 FTE`. El coste total corregido usado para la decisión es `540.880 EUR`.
