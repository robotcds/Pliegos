1. Veredicto ejecutivo Go/No-Go: NO-GO

2. Decisión ejecutiva:
La oportunidad OPP-SW-004 presenta dos riesgos bloqueantes: la empresa no dispone del equipo mínimo de tres desarrolladores Java senior con experiencia específica en Spring, SQL y mantenimiento, y el coste económico corregido supera claramente el PBL. El gap de personal es causa directa de exclusión y hace inviable presentar oferta con el equipo actual. Además, corrigiendo la partida de desarrolladores Java, el coste estimado asciende a 540.880 EUR frente a 360.000 EUR de PBL sin IVA, por lo que tampoco hay viabilidad económica. No se recomienda avanzar salvo que se cierren los perfiles y se aclare/reformule el dimensionamiento económico.

3. Resumen de semáforo por agente:
| Agente                    | Veredicto heredado         | Impacto en decisión | Riesgo         | Comentario ejecutivo                                 |
|--------------------------|----------------------------|---------------------|----------------|------------------------------------------------------|
| Resumen profesional      | RECOMENDABLE CON GAPS      | Alto                | Alto           | Advierte gap de personal y penalizaciones            |
| Solvencia de perfiles    | NO CUMPLE                  | Crítico             | Máximo         | Gap literal, riesgo de exclusión                     |
| Solvencia de proyectos   | CUMPLE                     | Bajo                | Bajo           | Sin brechas, referencias válidas                     |
| Administrativo/legal     | CUMPLE PARCIALMENTE        | Alto                | Alto           | Gap en solvencia de personas                         |
| Criterios adjudicación   | ALTA OPORTUNIDAD           | Medio               | Medio          | Estrategia viable solo si se cubre el equipo         |
| Económico-financiero     | NO RENTABLE                | Crítico             | Máximo         | Coste corregido 540.880 EUR > PBL 360.000 EUR        |
| Compras / Partners       | BLOQUEANTE                 | Crítico             | Máximo         | No hay partner Java disponible                       |
| Delivery / Operación     | NO OPERABLE                | Crítico             | Máximo         | Gap de personal impide operar                        |
| Service Design / ITIL    | APTO CON GAPS              | Alto                | Alto           | Riesgo operativo por falta de personal               |
| Seguridad / DPO / ENS    | CUMPLE CON GAPS            | Bajo                | Bajo           | Cumple ENS básica, gaps menores                      |
| Coherencia Documental    | INCOHERENCIAS CRITICAS     | Crítico             | Máximo         | Gap de personal bloqueante, coherencia transversal   |

4. Riesgos bloqueantes:
| Riesgo                                         | Fuente/agente         | Evidencia                                    | Impacto     | Probabilidad | Propietario         | Acción de cierre                        | Fecha límite | Decisión si no se cierra         |
|------------------------------------------------|-----------------------|----------------------------------------------|-------------|--------------|---------------------|------------------------------------------|--------------|-------------------------------|
| No disponer de 3 desarrolladores Java senior   | Solvencia perfiles, Compras, Delivery, Coherencia | No hay perfiles internos ni partners disponibles | Exclusión   | 100%         | Dirección de RRHH    | Contratar y acreditar 2 perfiles externos| T-5 días     | NO-GO                        |
| Jefe de servicio sin experiencia específica/ITIL| Solvencia perfiles, Delivery | Ana Torres no acredita experiencia ni ITIL Foundation | Exclusión potencial | 80% | Dirección de RRHH | Sustituir o acreditar experiencia/certificado | T-5 días | NO-GO si no se acredita       |
| Coste corregido superior al PBL | Económico-financiero, Coherencia | Coste corregido 540.880 EUR frente a PBL 360.000 EUR | Pérdida económica | Alta | Dirección financiera | Validar dedicaciones o reformular modelo de servicio | T-5 días | NO-GO |

5. Riesgos altos no bloqueantes:
| Riesgo                                 | Impacto     | Mitigación                                  | Seguimiento           |
|----------------------------------------|-------------|---------------------------------------------|-----------------------|
| Penalizaciones por SLA                  | Alto        | Refuerzo de equipo, backup, formación       | Plan de contingencia  |
| Dependencia de proveedor saliente       | Alto        | Plan de transición detallado, acuerdos KT   | Comité de transición  |
| Saturación en picos de demanda          | Alto        | Refuerzo temporal, backup, métricas         | Seguimiento operativo |

6. Condiciones para GO:
1. Incorporar y acreditar documentalmente dos desarrolladores Java senior (Spring, SQL, mantenimiento) antes de T-5 días. Responsable: RRHH. Evidencia: CV, contratos, declaración responsable.
2. Acreditar experiencia específica y certificación ITIL Foundation del jefe de servicio antes de T-5 días. Responsable: RRHH. Evidencia: CV, certificado ITIL.
3. Preacuerdo firmado con DBA Oracle autónomo antes de T-5 días. Responsable: Compras. Evidencia: preacuerdo firmado.
4. Validar que las dedicaciones del pliego no son mínimas obligatorias o reformular el modelo económico para que el coste total quede por debajo del PBL con margen mínimo aprobable. Responsable: Dirección financiera/Delivery. Evidencia: aclaración del órgano de contratación y nuevo modelo de costes.

7. Motivos de NO-GO o de GO condicionado:
El NO-GO se fundamenta en la imposibilidad de cumplir el requisito excluyente de personal técnico principal y en la falta de rentabilidad económica del contrato con el dimensionamiento actual. Sin cerrar el gap de desarrolladores Java, la oferta será excluida. Aunque se cerrase ese gap, el contrato seguiría siendo no rentable si el coste corregido de 540.880 EUR se mantiene frente a un PBL de 360.000 EUR.

8. Riesgos aceptables:
- Gaps menores en seguridad, ENS, acuerdos de encargado y subcontratistas pueden gestionarse y no bloquean la oferta.
- Los gaps menores de seguridad, ENS, acuerdos de encargado y subcontratistas pueden gestionarse y no bloquean la oferta.

9. Plan de mitigación previo a oferta:
- T-15: Lanzar búsqueda urgente de perfiles Java senior y validar disponibilidad de jefe de servicio con ITIL.
- T-10: Preacuerdo con DBA Oracle, aclaración económica de dedicaciones, simulación económica corregida, revisión de memoria técnica.
- T-5: Validar documentación de solvencia de personal, firmar acuerdos, checklist de requisitos excluyentes.
- T-1: Revisión final de oferta, simulación de puntuación, validación de anexos y formatos.

10. Plan de mitigación post-adjudicación:
- Antes de formalización: Validar disponibilidad real de equipo, firmar contratos, onboarding.
- Transición: Plan detallado de transferencia de conocimiento, acuerdos con proveedor saliente.
- Go-live: Refuerzo de equipo en arranque, seguimiento diario de SLA.
- Primer mes: Revisión de cumplimiento, plan de mejora, comité de seguimiento.

11. Escenarios de decisión:
- Escenario conservador: NO-GO. No se cubre el gap de personal ni la brecha económica.
- Escenario probable: NO-GO. Aunque se busquen perfiles, el coste corregido supera el PBL si no cambia el dimensionamiento.
- Escenario agresivo: NO-GO. No se recomienda ofertar sin cubrir perfiles ni rentabilidad.

12. Preguntas críticas pendientes:
- ¿Se permite acreditar los perfiles mediante compromiso de contratación en vez de contrato firmado?
- ¿El cliente aceptaría experiencia en dirección de proyectos como equivalente a coordinación de servicios de mantenimiento?
- ¿Se puede ampliar el plazo de presentación para cerrar la cobertura de personal?

13. Recomendación final al comité:
Se recomienda NO-GO. Solo podría convertirse en GO CONDICIONADO si se incorporan y acreditan dos desarrolladores Java senior, se acredita la jefatura de servicio y se valida un modelo económico corregido que no supere el PBL y mantenga margen mínimo aprobable.

14. Fuentes utilizadas:
- Agentes: Resumen profesional, Solvencia de perfiles, Solvencia de proyectos, Requisitos administrativos y legales, Criterios de adjudicación, Económico-financiero, Compras/Partners, Delivery/Operación, Service Design/ITIL, Seguridad/DPO/ENS, Coherencia Documental.
- Documentos: Pliego administrativo, Pliego técnico, Anexo solvencia OPP-SW-004 mantenimiento Java.
