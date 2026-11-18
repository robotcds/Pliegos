1. Veredicto ejecutivo Go/No-Go: NO-GO

2. Decisión ejecutiva:
La oportunidad OPP-SW-003 presenta bloqueos críticos de solvencia y cumplimiento que impiden presentar oferta en las condiciones actuales. Los gaps detectados en solvencia de perfiles (falta un segundo DevOps/cloud senior), solvencia de proyectos (solo dos referencias válidas de migración cloud en AAPP), clasificación empresarial (no disponible y exigida como obligatoria) y seguro de responsabilidad civil (1M EUR vs 1,5M EUR exigido) son todos excluyentes según pliego y no subsanables a corto plazo sin acciones urgentes y confirmadas. El resto de áreas (económica, técnica, partners, seguridad) son gestionables solo si se cierran estos bloqueos. No es viable ofertar sin resolverlos, ya que la exclusión es automática.

3. Resumen de semáforo por agente:
| Agente                        | Veredicto heredado         | Impacto en decisión | Riesgo | Comentario ejecutivo |
|-------------------------------|----------------------------|---------------------|--------|---------------------|
| Resumen profesional           | RECOMENDABLE CON GAPS      | Alto                | Alto   | Solo viable si se cierran gaps críticos |
| Solvencia de perfiles         | NO CUMPLE                  | Bloqueante          | Máximo | Falta 2º DevOps senior, excluyente |
| Solvencia de proyectos        | CUMPLE PARCIALMENTE        | Bloqueante          | Máximo | Solo 2 migraciones cloud, falta 3ª |
| Requisitos administrativos    | CUMPLE PARCIALMENTE        | Bloqueante          | Máximo | Sin clasificación y RC insuficiente |
| Criterios de adjudicación     | ALTA OPORTUNIDAD           | Condicionado        | Alto   | Solo si se cubren gaps de solvencia |
| Económico-financiero          | RENTABLE CON GAPS          | Condicionado        | Alto   | Viabilidad depende de solvencia |
| Compras / Partners            | BLOQUEANTE                 | Bloqueante          | Máximo | Gap DevOps bloqueante |
| Delivery / Operación          | NO OPERABLE                | Bloqueante          | Máximo | Gap DevOps bloqueante |
| Service Design / ITIL         | APTO CON GAPS              | Condicionado        | Alto   | Gap DevOps, RC, referencias |
| Seguridad / DPO / ENS         | CUMPLE CON GAPS            | Condicionado        | Alto   | Alcance ENS, logs, RC |
| Coherencia Documental         | INCOHERENCIAS CRITICAS     | Bloqueante          | Máximo | Consolidación de todos los bloqueos |

4. Riesgos bloqueantes:
| Riesgo                              | Fuente/agente         | Evidencia                                   | Impacto   | Probabilidad | Propietario | Acción de cierre                | Fecha límite | Decisión si no se cierra |
|-------------------------------------|-----------------------|---------------------------------------------|-----------|--------------|-------------|-------------------------------|--------------|-------------------------|
| Falta 2º DevOps/cloud senior        | Perfiles, compras     | Pliego, análisis perfiles                   | Exclusión | Muy alta     | RRHH/Compras | Contratar/partner firmado      | T-7 días     | NO-GO                  |
| Falta 3ª referencia migración cloud | Solvencia proyectos   | Pliego, análisis referencias                | Exclusión | Muy alta     | Dirección    | Aportar referencia válida      | T-7 días     | NO-GO                  |
| Falta clasificación empresarial     | Admin, corporativo    | Pliego, análisis admin                      | Exclusión | Muy alta     | Dirección    | Obtener clasificación          | T-7 días     | NO-GO                  |
| Seguro RC insuficiente              | Admin, seguridad      | Pliego, póliza 1M vs 1,5M EUR               | Exclusión | Muy alta     | Dirección    | Ampliar póliza RC              | T-7 días     | NO-GO                  |

5. Riesgos altos no bloqueantes:
| Riesgo                        | Impacto   | Mitigación                        | Seguimiento           |
|-------------------------------|-----------|-----------------------------------|-----------------------|
| Alcance ENS/logs              | Alto      | Validar alcance/logs con cliente  | Seguridad/DPO         |
| Volumetría/usuarios indefinida| Alto      | Solicitar detalle al cliente      | Dirección técnica     |
| Penalizaciones por SLA        | Alto      | Plan de contingencia y reporting  | Dirección de proyecto |

6. Condiciones para GO:
1. Contratar o firmar acuerdo con un segundo DevOps/cloud senior con experiencia demostrable en Azure/K8s/CI/CD (RRHH/Compras, evidencia: CV y contrato, T-7 días).
2. Aportar una tercera referencia válida de migración cloud en AAPP (Dirección, evidencia: certificado cliente, T-7 días).
3. Obtener la clasificación empresarial Grupo V, Subgrupo 2, Cat. 3 (Dirección, evidencia: certificado, T-7 días).
4. Ampliar el seguro de RC a 1,5M EUR (Dirección, evidencia: póliza, T-7 días).

7. Motivos de NO-GO o de GO condicionado:
El NO-GO se fundamenta en la imposibilidad de cumplir requisitos obligatorios de pliego: solvencia de perfiles, solvencia de proyectos, clasificación empresarial y seguro de RC. Todos son excluyentes y no subsanables tras la presentación de oferta. Si se resolvieran antes de la fecha límite, podría considerarse un GO condicionado.

8. Riesgos aceptables:
- Alcance ENS/logs, volumetría y penalizaciones por SLA son riesgos altos pero gestionables si se cierran los bloqueos principales. No impiden la oferta si se mitigan con acciones previas y planes de contingencia.

9. Plan de mitigación previo a oferta:
- T-15: Lanzar búsqueda y proceso de contratación/partner para DevOps senior, iniciar ampliación seguro RC, solicitar clasificación empresarial, buscar tercera referencia.
- T-10: Validar avances en contratación, seguro y clasificación; preparar documentación de referencia.
- T-5: Confirmar cierre de todos los bloqueos, obtener evidencias documentales.
- T-1: Validar checklist de cumplimiento, preparar oferta solo si todo está cerrado.

10. Plan de mitigación post-adjudicación:
- Antes de formalización: Validar documentación de solvencia, clasificación y póliza RC.
- Transición: Confirmar onboarding de personal clave y partners.
- Go-live: Validar cobertura operativa y de seguridad.
- Primer mes: Seguimiento reforzado de SLA, reporting y cumplimiento ENS.

11. Escenarios de decisión:
- Escenario conservador: NO-GO. No se cierran bloqueos, no se oferta.
- Escenario probable: NO-GO. No se cierran todos los bloqueos a tiempo.
- Escenario agresivo: GO CONDICIONADO solo si se cierran los 4 bloqueos críticos antes de T-7 días.

12. Preguntas críticas pendientes:
- ¿Permitiría el órgano de contratación acreditar solvencia por medios alternativos si no se dispone de clasificación empresarial?
- ¿Se aceptaría una referencia de migración cloud en consorcio o UTE?
- ¿Es posible ampliar el seguro RC en plazo?
- ¿Se puede subcontratar el segundo DevOps senior cumpliendo el límite del 25%?

13. Recomendación final al comité:
Se recomienda NO-GO salvo cierre documentado de los 4 bloqueos críticos antes de T-7 días. Si se cierran, pasar a GO condicionado con validación documental previa a oferta.

14. Fuentes utilizadas:
- Agentes: Resumen profesional, Solvencia de perfiles, Solvencia de proyectos, Requisitos administrativos y legales, Criterios de adjudicación, Económico-financiero, Compras/Partners, Delivery/Operación, Service Design/ITIL, Seguridad/DPO/ENS, Coherencia Documental.
- Documentos: Pliego administrativo, Pliego técnico, Anexo solvencia OPP-SW-003 migración cloud.