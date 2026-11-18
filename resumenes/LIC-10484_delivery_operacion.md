1. Veredicto ejecutivo Delivery / Operacion: OPERABLE

2. Operational Readiness Score:
| Área                | Score | Semáforo                        | Razón                                                                                 |
|---------------------|-------|----------------------------------|---------------------------------------------------------------------------------------|
| Personal            | 90    | Cubierto                         | Perfiles esenciales identificados, backup previsto, dedicación flexible, sin turnos críticos. |
| Turnos              | 100   | Cubierto                         | Horario definido por adjudicatario, solo requiere disponibilidad L-V 9:00-14:00.           |
| Herramientas        | 85    | Cubrible con acciones            | Único requisito: software propio para conexión remota, disponible internamente.           |
| Infraestructura     | 100   | Cubierto                         | Oficinas propias, remoto, reuniones presenciales puntuales.                              |
| Partners            | 100   | Cubierto                         | No se exigen partners ni subcontratistas críticos.                                       |
| Cobertura geográfica| 95    | Cubierto                         | Servicio remoto, reuniones presenciales solo en Madrid máximo 2/año.                      |
| Transición          | 90    | Cubierto                         | Arranque simple, sin dependencias críticas, plan de transición estándar.                  |
| SLA                 | 100   | Cubierto                         | No hay SLA críticos ni penalizaciones complejas, solo plazos de entrega de informes.      |
| Continuidad         | 90    | Cubierto                         | Backup previsto, personal de apoyo/sustitución exigido, bus factor ≥2.                    |
| Dependencias cliente| 90    | Cubierto                         | Solo requiere información de acceso a puntos de suministro y coordinación inicial.         |

Puntuación global: 94/100

3. Alcance operativo real:
| Parámetro           | Valor/Descripción                                                                 | Fuente                         |
|---------------------|-------------------------------------------------------------------------------|---------------------------------|
| Usuarios            | División de Mantenimiento y responsables de 15 sucursales                       | PPT p.3-4                      |
| Sedes               | Todos los edificios del Banco de España (ver Anexos 1 y 2)                      | PPT p.3, Anexos 1 y 2           |
| Sistemas/aplicaciones| Programa informático propio para conexión remota a puntos de suministro         | PPT p.4                        |
| Dispositivos/activos| No aplica (servicio de consultoría, no gestión de activos físicos)              | PPT, PCP CDC                   |
| Horario             | L-V 9:00-14:00 comunicación, resto flexible                                     | PCP CDC p.14                   |
| Modalidad           | Remoto, presencial solo 2 reuniones/año en Madrid                               | PPT p.10-11                    |
| Tickets/mes         | No aplica (servicio por informes y consultas, no tickets)                       | PPT, PCP CDC                   |
| Cambios             | No aplica                                                                       | PPT, PCP CDC                   |
| Incidencias críticas| No aplica                                                                       | PPT, PCP CDC                   |
| Cobertura geográfica| Nacional (remoto), presencial solo Madrid                                       | PPT, PCP CDC                   |
| Duración            | 2 años iniciales, prorrogable hasta 5 años                                      | PCP CDC p.4                    |
| Fecha/go-live       | 10/01/2027 (estimada)                                                           | Documento de aprobación         |

4. Recursos humanos y dimensionamiento:
| Perfil                                 | Necesidad nominal | Necesidad operativa real | Disponible | Gap | Turnos/guardias | Bus factor | Acción                |
|----------------------------------------|-------------------|-------------------------|------------|-----|------------------|-----------|----------------------|
| Responsable Técnico (ingeniería)       | 1                 | 1                       | 1+backup   | 0   | N/A              | 2         | Asignar titular+backup|
| Responsable Jurídico-económico         | 1                 | 1                       | 1+backup   | 0   | N/A              | 2         | Asignar titular+backup|
| Coordinador de Proyecto                | 1                 | 1 (puede ser uno de los anteriores) | 1+backup | 0 | N/A | 2 | Asignar rol         |
| Personal de apoyo/sustitución          | 1 (mínimo)        | 1 (mínimo)              | 2+         | 0   | N/A              | 2+        | Pool de apoyo         |

5. Cobertura de turnos y ubicaciones:
- Turnos: No se exige cobertura fuera de L-V 9:00-14:00. No hay turnos extendidos, fines de semana ni festivos.
- Guardias: No exigidas.
- Ubicaciones: Servicio desde oficinas del adjudicatario (Madrid, Barcelona, Valencia, remoto). Presencialidad solo para reuniones puntuales en Madrid.
- Cobertura geográfica: Nacional, pero presencial solo Madrid.

6. Herramientas, activos e infraestructuras para operar:
| Herramienta/activo                    | Aporta           | Estado     | Necesario antes de | Impacto si falta         | Acción                  |
|---------------------------------------|------------------|------------|--------------------|--------------------------|------------------------|
| Software conexión remota a suministros| Proveedor        | Disponible | Go-live            | No se puede revisar consumo | Validar compatibilidad |
| Oficinas y medios de comunicación     | Proveedor        | Disponible | Go-live            | No se puede operar        | N/A                    |

7. Dependencias de Compras / Partners:
| Capacidad/Producto/Partner            | Estado A10 | Impacto operativo | SLA tercero vs SLA cliente | Riesgo | Acción |
|---------------------------------------|-----------|-------------------|---------------------------|--------|--------|
| Software conexión remota              | Disponible| Nulo               | N/A                       | Bajo   | Validar compatibilidad |
| Partners/subcontratistas              | No requerido | Nulo             | N/A                       | Nulo   | N/A    |

8. Modelo de soporte y escalados:
- L0/L1: No aplica (no hay soporte técnico ni tickets).
- L2/L3: Responsables técnico y jurídico-económico resuelven todas las consultas.
- Escalados: No hay escalados a fabricante ni partner.
- Horario: L-V 9:00-14:00 comunicación, resto flexible.

9. Plan de transición y go-live:
- Fase 1 (T-30 a T-15): Asignación de responsables, validación de software, acceso a datos de suministro.
- Fase 2 (T-15 a T-7): Revisión de documentación, prueba de conexión remota, simulacro de informe.
- Fase 3 (T-7 a T0): Confirmación de backups, comunicación a cliente, arranque operativo.
- Go-live: War room virtual, seguimiento intensivo primera semana.

10. Curva de incorporación:
| Hito      | Recursos           | Herramientas         | Partners | Bloqueos |
|-----------|--------------------|----------------------|---------|----------|
| T-30      | Asignar responsables| Validar software     | N/A     | N/A      |
| T-15      | Pool de apoyo      | Prueba conexión      | N/A     | Acceso datos|
| T-7       | Confirmar backups  | Simulacro informe    | N/A     | N/A      |
| T0        | Todos operativos   | Operación estable    | N/A     | N/A      |
| T+30      | Revisión           | Ajustes menores      | N/A     | N/A      |

11. Dependencias de transición:
| Dependencia                | Necesaria antes de | Responsable | Estado   | Riesgo | Mitigación           |
|----------------------------|--------------------|-------------|----------|--------|----------------------|
| Acceso a datos de suministro| T-15               | Cliente     | Pendiente| Bajo   | Solicitar con antelación|
| Validación software         | T-15               | Proveedor   | Listo    | Bajo   | Prueba previa        |

12. Continuidad, capacidad y picos:
- Crecimiento/picos: No se prevén picos críticos, volumen bajo y estable.
- Rotación: Backup previsto, pool de apoyo.
- Caída de herramienta: Software propio, bajo riesgo.
- Caída VPN/sede: Operación remota, contingencia por teletrabajo.
- Ausencia personas clave: Bus factor ≥2, sustitución prevista.
- Contingencias: Reuniones presenciales pueden reprogramarse.

13. Procedimientos operativos requeridos:
- Revisión de facturación
- Elaboración de informes técnicos y jurídicos
- Asistencia a contratación pública
- Asesoramiento regulatorio
- Gestión de consultas puntuales
- Sustitución de personal
- Reporting periódico

14. Automatización y shift-left:
- Automatización de descarga y análisis de datos de consumo.
- Plantillas de informes periódicos.
- Checklists para revisión de facturas.
- Base de conocimiento para consultas frecuentes.

15. Gap analysis operacional:
| Capacidad                        | Necesidad | Disponible | Gap | Probabilidad | Impacto | Riesgo | Acción | Fecha límite |
|-----------------------------------|-----------|------------|-----|--------------|---------|--------|--------|-------------|
| Responsable Técnico               | 1         | 1+backup   | 0   | N/A          | N/A     | N/A    | Asignar| T-30        |
| Responsable Jurídico-económico    | 1         | 1+backup   | 0   | N/A          | N/A     | N/A    | Asignar| T-30        |
| Software conexión remota          | 1         | 1          | 0   | N/A          | N/A     | N/A    | Validar | T-15        |
| Personal de apoyo/sustitución     | 1+        | 2+         | 0   | N/A          | N/A     | N/A    | Pool   | T-15        |

16. Riesgos operativos principales:
| Riesgo                        | Causa                        | Consecuencia                | Propietario | Mitigación           |
|-------------------------------|------------------------------|-----------------------------|-------------|----------------------|
| Ausencia simultánea de titulares| Bajas/vacaciones             | Retraso en informes         | Delivery    | Pool de apoyo        |
| Acceso tardío a datos cliente   | Retraso en entrega           | Demora en informes          | Cliente     | Solicitar anticipado |
| Fallo software conexión         | Incompatibilidad técnica     | Imposibilidad de revisión   | Delivery    | Prueba previa        |

17. Supuestos operativos:
- El volumen de facturas y consultas es estable y bajo.
- El acceso a los sistemas de medición remota será facilitado por el cliente antes de go-live.
- No se requiere presencialidad salvo reuniones puntuales en Madrid.
- No se exige software/fabricante concreto ni licencias especiales.
- Validar estos supuestos antes de la oferta.

18. Preguntas al cliente:
- ¿Puede confirmar el volumen medio mensual de facturas a revisar y consultas esperadas?
- ¿Qué sistema de medición remota utiliza actualmente el Banco de España?
- ¿Habrá acceso directo a los portales de las comercializadoras?
- ¿Se requiere algún formato específico para los informes?
- ¿Hay algún periodo de cierre crítico o ventana de entrega inamovible?

19. Decision operativa:
OPERAR INTERNAMENTE. El servicio es plenamente operable con recursos propios y pool de apoyo, sin dependencias críticas de partners ni compras. Condiciones mínimas para pasar a oferta: confirmar disponibilidad de responsables y backup, validar compatibilidad del software de conexión remota, confirmar acceso a datos de suministro antes de go-live. Condiciones mínimas para go-live: acceso a datos, validación de software, comunicación de responsables al cliente.

20. Documentos revisados:
1. LIC10484 PCP CLAUS.pdf
2. LIC10484 PPT.pdf
3. LIC10484 PPT Anexo 2.pdf
4. LIC10484 PCP CDC Anexo 2.pdf
5. LIC10484 PPT Anexo 1.pdf
6. LIC10484 PCP CDC Anexo 1.xlsx
7. LIC10484 PCP ANEXOS.pdf
8. LIC10484 PCP CDC.pdf
9. LIC10484 PPT Anexo 3.pdf
10. Documento de aprobación del expediente

---

Extracción de viabilidad (matriz breve):
| Parámetro                        | Estado     | Dato decisivo                                    | Fuente                  | Acción                |
|-----------------------------------|------------|--------------------------------------------------|-------------------------|-----------------------|
| Responsable Técnico               | CUMPLE     | 1+backup disponible, experiencia exigida          | Salida perfiles         | Asignar titular+backup|
| Responsable Jurídico-económico    | CUMPLE     | 1+backup disponible, experiencia exigida          | Salida perfiles         | Asignar titular+backup|
| Personal de apoyo/sustitución     | CUMPLE     | Pool disponible                                  | Salida perfiles         | Asignar pool          |
| Software conexión remota          | CUMPLE     | Disponible, configurable                         | Salida compras/partners | Validar compatibilidad |
| Subcontratistas/partners críticos | NO EXIGIDO | No requeridos                                    | Pliego, compras         | N/A                   |
| Cobertura presencial Madrid       | CUMPLE     | Oficinas propias, desplazamiento puntual posible  | Capacidades internas    | Planificar reuniones   |
| SLA críticos                      | NO EXIGIDO | No hay SLA críticos ni penalizaciones complejas   | Pliego                  | N/A                   |
| Herramientas adicionales          | NO EXIGIDO | No requeridas                                    | Pliego                  | N/A                   |
| Solvencia sectorial               | NO ACREDITADO| No consta desglose sectorial en facturación      | Inventario interna      | Aportar CBE si exige   |
| Certificados específicos           | NO EXIGIDO | No exigidos                                      | Pliego                  | N/A                   |
| Póliza RC                         | NO EXIGIDO | No exigida                                       | Pliego                  | N/A                   |
| Formación externa/idiomas         | NO EXIGIDO | No exigidos                                      | Pliego                  | N/A                   |
| Subrogación personal              | NO EXIGIDO | No exigida                                       | Pliego                  | N/A                   |
| Garantía provisional              | NO EXIGIDO | No exigida                                       | Pliego                  | N/A                   |
| Garantía definitiva               | CUMPLE     | Capacidad de aval suficiente                     | Inventario interna      | Preparar aval          |
| Comité de seguimiento             | NO EXIGIDO | No exigido                                       | Pliego                  | N/A                   |
| Acuerdo de nivel de servicio      | NO EXIGIDO | No exigido                                       | Pliego                  | N/A                   |
| Formación interna                 | CUMPLE     | Capacidad de formación interna                   | Capacidades internas    | Planificar si necesario|
| Plan de transición                | CUMPLE     | Arranque simple, sin dependencias críticas        | Capacidades internas    | Ejecutar plan estándar |
| Continuidad acreditaciones        | CUMPLE     | Backup previsto, bus factor ≥2                   | Capacidades internas    | Mantener pool          |