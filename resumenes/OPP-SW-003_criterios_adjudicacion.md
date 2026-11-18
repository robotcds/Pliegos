1. Veredicto ejecutivo de estrategia de puntuacion: ALTA OPORTUNIDAD

La licitacion OPP-SW-003 presenta una estructura de puntuacion muy concentrada en criterios donde la empresa puede diferenciarse (plan de migracion, plan de reversibilidad, observabilidad/SLA, equipo y certificaciones), junto a un peso economico alto pero gestionable. La empresa dispone de referencias, perfiles y certificaciones relevantes, aunque hay gaps en solvencia formal y equipo DevOps. Si se cubren estos gaps (contratacion/partner), la oportunidad es alta.

2. Mapa completo de criterios de adjudicacion:

| Criterio                                 | Puntos | % Total | Tipo           | Formula/Tope/Umbral                  | Documento fuente |
|------------------------------------------|--------|---------|----------------|--------------------------------------|------------------|
| Precio                                  | 50     | 50%     | Formula        | P=50x(oferta_min/oferta_licitador)   | Adm. + Anexo     |
| Plan de migracion                       | 22     | 22%     | Juicio valor   | Subcriterios (ver abajo)             | Adm. + Tec.      |
| - Inventario y oleadas                  | 6      | 6%      | Juicio valor   |                                      | Adm. + Tec.      |
| - Automatizacion CI/CD                  | 5      | 5%      | Juicio valor   |                                      | Adm. + Tec.      |
| - Seguridad                             | 4      | 4%      | Juicio valor   |                                      | Adm. + Tec.      |
| - Gestion de riesgos                    | 4      | 4%      | Juicio valor   |                                      | Adm. + Tec.      |
| - Validacion postmigracion              | 3      | 3%      | Juicio valor   |                                      | Adm. + Tec.      |
| Plan de reversibilidad y continuidad     | 10     | 10%     | Juicio valor   |                                      | Adm. + Tec.      |
| Observabilidad y SLA operativo          | 8      | 8%      | Mixto/Autom.   | Tope: dashboards, alertas, SLA <2h   | Adm. + Tec.      |
| Certificaciones y equipo cloud          | 5      | 5%      | Automatico     | CKA 2, Azure Admin 2, ISO27001 1     | Adm. + Tec.      |
| Reduccion de plazo                      | 5      | 5%      | Automatico     | Tope: -10% sobre plazo base          | Adm. + Tec.      |

Umbral tecnico: 24/40 en migracion, reversibilidad y observabilidad (excluyente).

3. Concentracion de puntos:
- Precio: 50% del total.
- Plan de migracion: 22%.
- Plan de reversibilidad y continuidad: 10%.
- Observabilidad y SLA: 8%.
Acumulado: 90% en los 4 primeros bloques.

4. Lectura estrategica por criterio:

- Precio (50): Impacto maximo. Diferenciacion limitada, pero la empresa puede competir con descuentos de hasta 15% sin riesgo financiero grave. Riesgo: ofertas temerarias (>18% baja) exigen memoria de viabilidad y >22% se consideran de alto riesgo.
- Plan de migracion (22): Gran capacidad de diferenciacion. La empresa tiene proyectos y perfiles para destacar en inventario, automatizacion, seguridad y gestion de riesgos. Esfuerzo ALTO en memoria tecnica.
- Plan de reversibilidad (10): Diferenciacion media-alta. Experiencia en reversibilidad y continuidad en proyectos cloud y sector publico. Esfuerzo ALTO.
- Observabilidad y SLA (8): Criterio automatico con tope. Ofrecer dashboards, alertas y SLA <2h da el maximo. Esfuerzo MEDIO.
- Certificaciones/equipo (5): Criterio automatico. La empresa cubre ISO 27001 y Azure Admin, pero solo un DevOps con CKA. Gap a cubrir. Esfuerzo BAJO si se cubre el gap.
- Reduccion de plazo (5): Tope en -10%. La empresa puede asumirlo. Esfuerzo BAJO.

5. Criterios automaticos y formulas:
- Precio: Formula lineal. Mejor oferta = 50 puntos. Resto: P=50x(oferta_min/oferta_licitador). Bajadas >18% requieren memoria de viabilidad. Bajadas >22% = alto riesgo.
- Observabilidad/SLA: Tope en SLA <2h. No suma mas por bajar mas.
- Reduccion de plazo: Tope en -10%. No suma mas por reducir mas.
- Certificaciones: Tope por CKA, Azure Admin y ISO 27001. No suma mas.

6. Baremo de presupuestos y puntuacion economica:

| Presupuesto sin IVA | DtoN vs PL | Formula aplicada         | Puntos | % max | Lectura estrategica                  |
|---------------------|------------|-------------------------|--------|-------|--------------------------------------|
| 540.000 (PL)        | 0%         | 50x(540/540)=50         | 50     | 100%  | Maxima puntuacion, sin baja          |
| 500.000             | -7,4%      | 50x(500/540)=46,3       | 46,3   | 92,6% | Descuento habitual, seguro           |
| 480.000             | -11,1%     | 50x(480/540)=44,4       | 44,4   | 88,8% | Descuento competitivo, sin riesgo    |
| 450.000             | -16,7%     | 50x(450/540)=41,7       | 41,7   | 83,3% | Descuento max. sin memoria viabilidad|
| 440.000             | -18,5%     | 50x(440/540)=40,7       | 40,7   | 81,4% | Requiere memoria viabilidad          |
| 420.000             | -22,2%     | 50x(420/540)=38,9       | 38,9   | 77,8% | Alto riesgo, posible exclusion       |
| 600.000             | +11,1%     | 50x(540/600)=45         | 45     | 90%   | Penalizacion por sobreprecio         |

No hay zona donde bajar mas reste puntos, pero bajadas excesivas pueden ser temerarias.

7. Mejoras automaticas cuantificables:

| Mejora                | Unidad ofertada | Puntos | Tope | Recomendacion                  |
|-----------------------|-----------------|--------|------|-------------------------------|
| SLA respuesta critica | <2h             | 8      | 8    | Ofertar 2h, no menos           |
| Reduccion de plazo    | -10%            | 5      | 5    | Ofertar -10%, no menos         |
| Certificaciones CKA   | 1               | 2      | 2    | Aportar CKA, cubrir gap        |
| Certificaciones Azure | 1               | 2      | 2    | Aportar Azure Admin            |
| ISO 27001             | 1               | 1      | 1    | Ya disponible                  |

8. Criterios subjetivos:
- Plan de migracion: Reforzar inventario, automatizacion, seguridad, gestion de riesgos y validacion postmigracion. Usar proyectos cloud y sector publico como evidencia.
- Plan de reversibilidad: Detallar procedimientos, exportacion, rollback, continuidad y evidencias de proyectos similares.
- Observabilidad: Describir dashboards, alertas, monitorizacion y SLA operativo.

9. Elementos diferenciadores de la empresa:
- Experiencia en migraciones cloud y AKS en sector publico (REF-005, REF-006).
- Perfiles senior en DevOps, backend y gestion de proyectos.
- Certificaciones ISO 27001, Azure Admin.
- Capacidad de documentar planes de migracion y reversibilidad detallados.

10. Debilidades y riesgos competitivos:
- Solo un DevOps con CKA: gap a cubrir para puntuar maximo en equipo.
- Solvencia formal: falta clasificacion empresarial, solo alternativa para empresas no espanolas.
- Riesgo de empate en criterios automaticos (SLA, plazo, certificaciones).
- Bajadas de precio temerarias pueden excluir la oferta.

11. Plan desarrollado de focos para ganar:

| Foco/Frente                | Criterios impactados         | Objetivo puntuacion | Acciones concretas                                  | Evidencias internas           | Responsable         | Riesgo si no se trabaja | Esfuerzo |
|----------------------------|------------------------------|---------------------|-----------------------------------------------------|-------------------------------|---------------------|------------------------|----------|
| Plan migracion detallado   | Migracion (22), Observab.    | >20/22              | Redactar memoria con inventario, CI/CD, riesgos      | REF-005, Ana Torres, Ivan     | Jefe proyecto       | No superar umbral      | ALTO     |
| Plan reversibilidad        | Reversibilidad (10)          | 10/10               | Documentar rollback, exportacion, continuidad        | REF-005, REF-006             | Jefe proyecto       | Penalizacion/exclusion | ALTO     |
| Equipo y certificaciones   | Equipo (5)                   | 5/5                 | Aportar CKA, Azure Admin, ISO 27001                  | Ivan Lopez, Javier Prieto     | RRHH/Partner        | Perder puntos          | MEDIO    |
| Oferta economica           | Precio (50)                  | >44/50              | Definir descuento competitivo sin riesgo             | Politica precio               | Direccion financiera| Exclusion/temeridad    | ALTO     |
| Observabilidad/SLA         | Observab. (8)                | 8/8                 | Ofertar dashboards, alertas, SLA 2h                  | Ivan Lopez, herramientas      | DevOps              | Perder puntos          | MEDIO    |
| Reduccion de plazo         | Plazo (5)                    | 5/5                 | Ofertar -10% plazo                                  | Politica mejora               | Jefe proyecto       | Perder puntos          | BAJO     |

12. DAFO de estrategia de adjudicacion:

FORTALEZAS
- Experiencia en migraciones cloud publicas: La empresa ha ejecutado proyectos similares (REF-005, REF-006), lo que refuerza la memoria tecnica y la credibilidad ante el cliente. Impacta en plan de migracion y reversibilidad.
- Certificaciones relevantes: Dispone de ISO 27001 y Azure Admin, cubriendo requisitos de seguridad y cloud. Impacta en equipo/certificaciones.
- Capacidad de documentar planes detallados: El equipo senior puede preparar memorias tecnicas de alto nivel, diferenciandose en criterios subjetivos.

DEBILIDADES
- Gap en CKA/DevOps: Solo un DevOps con CKA, lo que impide puntuar maximo en equipo. Impacta en certificaciones/equipo.
- Solvencia formal: No dispone de clasificacion empresarial, lo que puede excluir la oferta si no se permite alternativa. Impacta en admision.
- Riesgo de empate en criterios automaticos: En SLA, plazo y certificaciones, muchos licitadores pueden empatar. Impacta en observabilidad, plazo, equipo.

OPORTUNIDADES
- Concentracion de puntos en memoria tecnica: 40 puntos en migracion, reversibilidad y observabilidad permiten diferenciarse si la memoria es excelente.
- Capacidad de descuento competitivo: La empresa puede ofertar hasta -15% sin riesgo, compitiendo bien en precio.
- Uso de referencias recientes: Proyectos ejecutados en los ultimos 2 anos en cloud y AKS son muy valorables.

AMENAZAS
- Competidores con clasificacion formal: Empresas con clasificacion pueden excluir a la empresa si no se permite alternativa.
- Ofertas temerarias: Bajadas de precio excesivas pueden llevar a exclusion o penalizacion.
- Empate en criterios automaticos: Si todos ofertan SLA/plazo maximos, la diferenciacion se reduce a memoria tecnica y precio.

13. Prioridad de preparacion de oferta:
- ALTO: Plan de migracion, plan de reversibilidad, oferta economica, cubrir gap CKA/DevOps.
- MEDIO: Observabilidad/SLA, documentacion de equipo, referencias de proyectos.
- BAJO: Reduccion de plazo, certificaciones ya disponibles, evidencias de cumplimiento binario.

14. Documentos revisados:
1. Pliego administrativo OPP-SW-003 migracion cloud
2. Pliego tecnico OPP-SW-003 migracion cloud
3. Anexo solvencia OPP-SW-003 migracion cloud