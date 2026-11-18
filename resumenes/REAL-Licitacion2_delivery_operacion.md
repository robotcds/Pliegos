1. Veredicto ejecutivo Delivery / Operacion: NO OPERABLE (en condiciones actuales, sin cierre de gaps críticos de perfiles y partners).

2. Operational Readiness Score:
| Area                | Score | Semáforo                | Razon                                                                 |
|---------------------|-------|-------------------------|-----------------------------------------------------------------------|
| Personal            | 20    | Gap crítico             | No hay perfiles clave ni expertos acreditados en tecnologías core.     |
| Turnos              | 30    | Gap crítico             | No hay FTE ni backups para cubrir 8x5 real, menos 12x5/24x7.           |
| Herramientas        | 60    | Cubrible con acciones   | ITSM y reporting cubribles, pero falta validación Remedy y acceso.     |
| Infraestructura     | 60    | Cubrible con acciones   | Hardware propio cubierto, dependencias en licencias cliente.           |
| Partners            | 10    | Gap crítico             | No hay partners para Citrix, NetApp, Cisco, SCCM, UEM, SQL.            |
| Cobertura geográfica| 50    | Cubrible con acciones   | Madrid/Barcelona/Valencia cubierto, resto depende de partners.         |
| Transición          | 30    | Gap crítico             | Sin equipo ni partners, no se puede planificar transición realista.    |
| SLA                 | 20    | Gap crítico             | No hay SLA back-to-back ni recursos para cumplir ANS críticos.         |
| Continuidad         | 30    | Gap crítico             | Bus factor 1 en todo, sin backups ni plan de contingencia real.        |
| Dependencias cliente| 40    | Info insuficiente       | Faltan detalles de accesos, inventario, licencias, soporte saliente.   |

Puntuación global: 35/100 (NO OPERABLE)

3. Alcance operativo real:
| Elemento         | Valor estimado (pliego)         | Fuente                |
|------------------|---------------------------------|-----------------------|
| Usuarios         | 16.000+ puestos físicos, 15.000 VDIs, 34.000+ móviles | Anexo I, Pliego |
| Sedes            | Nacional, oficinas Correos/CEX   | Anexo I, Pliego       |
| Sistemas         | Citrix, Hyper-V, NetApp, SQL, SCCM, UEM, Remedy | Anexo I, Pliego |
| Dispositivos     | ThinClient, portátiles, impresoras, PDA, tablets | Anexo I, Pliego |
| Horario          | 8x5 ampliado, guardias, 24x7 para incidencias críticas | Anexo I, Pliego |
| Modalidad        | Remoto/presencial mixto         | Anexo I, Pliego       |
| Tickets/mes      | No especificado, requiere aclaración | -                 |
| Cambios          | No especificado, requiere aclaración | -                 |
| Incidencias P1   | SLA <4h resolución, 24x7        | Anexo XVII, Pliego    |
| Cobertura geográfica | Nacional, Baleares, Canarias (gap) | Anexo I, Pliego |
| Duración         | 24 meses (+prórrogas)           | Pliego, Anuncio       |
| Go-live          | 1 mes transición, luego operación plena | Anexo I, Pliego |

4. Recursos humanos y dimensionamiento:
| Perfil                        | Necesidad nominal | Necesidad operativa real | Disponible | Gap | Turnos/guardias | Bus factor | Acción |
|-------------------------------|-------------------|-------------------------|------------|-----|-----------------|-----------|--------|
| Responsable gestión/seguimiento| 1                 | 1+backup                | 0          | 1   | 8x5             | 1         | Contratar externo |
| Admin. sistemas virtualizados | 4                 | 4+backup                | 0          | 4   | 8x5+guardias     | 1         | Contratar/partner |
| Admin. NetApp                 | 1                 | 1+backup                | 0          | 1   | 8x5+guardias     | 1         | Contratar/partner |
| Admin. SQL Server             | 1                 | 1+backup                | 0          | 1   | 8x5+guardias     | 1         | Contratar/partner |
| Admin. Cisco                  | 1                 | 1+backup                | 0          | 1   | 8x5+guardias     | 1         | Contratar/partner |
| Admin. Workplace (SCCM/UEM)   | 3                 | 3+backup                | 0          | 3   | 8x5+guardias     | 1         | Contratar/partner |
| Admin. movilidad              | 2                 | 2+backup                | 0          | 2   | 8x5+guardias     | 1         | Contratar/partner |
| Bolsa expertos                | Variable          | Variable                | 0          | Sí  | Bajo demanda     | 1         | Contratar/partner |

5. Cobertura de turnos y ubicaciones:
- 8x5: No cubierto (sin FTE ni backups en perfiles clave).
- 12x5/16x5: No cubierto.
- 24x7: No cubierto, ni siquiera con guardias (no hay equipo ni partner).
- Guardias: No cubierto.
- Sedes: Madrid/Barcelona/Valencia cubrible, resto depende de partners no identificados.
- Remoto/presencial: Cubrible si se contrata equipo externo.
- Geográfica: Gap crítico fuera de sedes principales.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo | Aporta | Estado | Necesario antes de | Impacto si falta | Acción |
|--------------------|--------|--------|-------------------|------------------|--------|
| Remedy ITSM        | Cliente| Acceso pendiente | Go-live | No se puede operar ni medir SLA | Validar acceso y formación |
| SCCM, UEM, Citrix, NetApp | Cliente| Licencias y acceso pendiente | Go-live | No se puede operar | Validar con cliente |
| Portátiles, móviles| Proveedor| Comprable | Go-live | Bajo | Comprar |
| Office/Teams       | Proveedor| Comprable | Go-live | Bajo | Comprar |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner | Estado A10 | Impacto operativo | SLA tercero vs SLA cliente | Riesgo | Acción |
|---------------------------|------------|-------------------|--------------------------|--------|--------|
| Citrix/NetApp/Cisco/SCCM/UEM/SQL | No hay partner | No se puede operar | No hay SLA back-to-back | Crítico | Buscar y cerrar partner antes de oferta |

8. Modelo de soporte y escalados:
- L0/L1: No cubierto (no hay equipo N1/N2 en workplace ni movilidad).
- L2/L3: No cubierto (no hay expertos en virtualización, NetApp, SQL, Cisco, UEM).
- Escalado a fabricante: No viable sin partner/certificados.
- Horarios: No cubierto.

9. Plan de transición y go-live:
- No viable: sin equipo ni partners no se puede planificar discovery, KT, shadowing ni war room.
- Plazo mínimo realista: 8-12 semanas tras cierre de equipo y partners.

10. Curva de incorporación:
| Hito      | Recursos | Herramientas | Partners | Bloqueos |
|-----------|----------|--------------|----------|----------|
| T-60/T-45 | Buscar y contratar todos los perfiles clave y partners | Validar acceso Remedy, SCCM, UEM, Citrix, NetApp | Cerrar acuerdos | Todo bloqueado |
| T-30      | Onboarding, formación, shadowing | Configuración ITSM | Validar licencias | Todo bloqueado |
| T-15      | Pruebas, simulacros | Runbooks | Validar backups | Todo bloqueado |
| T-7       | Go/no-go | Validar acceso | Validar escalados | Todo bloqueado |
| T0        | No viable | - | - | - |

11. Dependencias de transición:
| Dependencia | Necesaria antes de | Responsable | Estado | Riesgo | Mitigación |
|-------------|-------------------|-------------|--------|--------|------------|
| Equipo completo | T-45 | RRHH/Compras | No | Crítico | Contratar antes de oferta |
| Partners clave | T-45 | Compras | No | Crítico | Cerrar acuerdos antes de oferta |
| Accesos/licencias | T-30 | Cliente | No | Alto | Validar con cliente |
| Inventario/documentación | T-30 | Cliente | No | Alto | Solicitar antes de transición |

12. Continuidad, capacidad y picos:
- No hay capacidad de cubrir bajas, vacaciones, picos ni contingencias.
- Bus factor 1 en todo.
- Sin equipo ni partners, no hay continuidad operativa.

13. Procedimientos operativos requeridos:
- Incidencias, peticiones, cambios, problemas, crisis, seguridad, accesos, backup, monitorización, inventario, escalados, reporting, reversibilidad: todos a crear/adaptar tras cierre de equipo y partners.

14. Automatización y shift-left:
- No aplicable hasta tener equipo y herramientas. Oportunidad futura en scripts, autoservicio y reporting.

15. Gap analysis operacional:
| Capacidad | Necesidad | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción | Fecha límite |
|-----------|-----------|------------|-----|-------------|---------|--------|--------|-------------|
| Perfiles clave | 100% | 0% | 100% | 100% | Crítico | No operar | Contratar antes de oferta |
| Partners | 100% | 0% | 100% | 100% | Crítico | No operar | Contratar antes de oferta |
| Licencias/accesos | 100% | 0% | 100% | 100% | Crítico | Validar antes de go-live |

16. Riesgos operativos principales:
1. No disponer de perfiles clave: No se puede operar, exclusión directa.
2. No disponer de partners: No se puede operar, exclusión directa.
3. No disponer de licencias/accesos: No se puede operar, exclusión directa.
4. No poder cumplir SLA: Penalizaciones y resolución de contrato.

17. Supuestos operativos:
- Se asume que el cliente aporta licencias y accesos a Remedy, SCCM, UEM, Citrix, NetApp, SQL.
- Se asume que se puede subcontratar perfiles clave y partners.
- Se asume que la transición mínima realista es de 8 semanas tras cierre de equipo.
- Todos estos supuestos deben validarse antes de presentar oferta.

18. Preguntas al cliente:
- ¿Aporta el cliente licencias y accesos a Citrix, NetApp, SCCM, UEM, SQL, Remedy?
- ¿Se aceptan partners/freelance como recursos adscritos si acreditan experiencia y certificaciones?
- ¿Se aceptan cartas de compromiso de partners/freelance para cubrir solvencia técnica?
- ¿Qué nivel de detalle se exige en la acreditación de experiencia y certificaciones?
- ¿Se aceptan equivalentes a Citrix, NetApp, SCCM, UEM si cumplen requisitos funcionales?
- ¿Se puede ampliar el plazo de transición si no se cierra equipo antes de la firma?
- ¿Se puede presentar oferta condicionada a cierre de equipo y partners?

19. Decision operativa:
NO OFERTAR SIN REDISEÑO RADICAL DEL MODELO DE RECURSOS Y PARTNERS. No es operable ni arrancable en condiciones actuales. Condiciones mínimas para pasar a oferta: cierre de todos los perfiles clave y partners críticos, validación de licencias y accesos, plan de transición realista de al menos 8 semanas. Condiciones mínimas para go-live: equipo completo, partners firmados, accesos y licencias validados, procedimientos y runbooks preparados, simulacro de P1 y validación de SLA.

20. Documentos revisados:
1. ANEXO I.pdf
2. Anuncio.pdf
3. DOC20240806095753Pliegodefinitivofirmado.pdf
4. DOC_CD2024-000901195.pdf
5. poc (Anuncio.pdf)
6. poc (Anuncio.pdf)
7. CORREOS-Codigo-General-de-Conducta.pdf
8. perfil-contratante
9. PoliticaProteccionDatosCanalEticoClientesyProveedores--ES.pdf