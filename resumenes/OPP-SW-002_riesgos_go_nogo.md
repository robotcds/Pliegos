1. Veredicto ejecutivo Go/No-Go: GO CONDICIONADO

2. Decision ejecutiva:
La oportunidad es viable y recomendable, pero existen riesgos bloqueantes que requieren cierre previo a la presentación de oferta. Los principales focos son: validación de la facturación mínima auditada (2024/2025), certificación ENS categoría media con alcance explícito IA/RAG, y compromisos firmados de partners críticos (cloud UE, anonimización, pentest). El margen económico es adecuado solo en escenarios conservadores (>10%), y la operativa depende de la integración de subencargados y equivalencia SaaS UE. Si se cierran estas condiciones, la empresa puede ofertar con riesgos gestionables; de lo contrario, la oferta sería excluible o no rentable.

3. Resumen de semaforo por agente:
| Agente                  | Veredicto heredado      | Impacto en decision | Riesgo         | Comentario ejecutivo                  |
|------------------------|-------------------------|---------------------|---------------|--------------------------------------|
| Resumen profesional    | RECOMENDABLE            | Positivo            | Bajo          | Cumple requisitos, riesgos controlables|
| Solvencia de perfiles  | CUMPLE                  | Positivo            | Bajo          | Equipo cubre mínimos                  |
| Solvencia de proyectos | CUMPLE                  | Positivo            | Bajo          | Referencias válidas                   |
| Administrativo/Legal   | CUMPLE PARCIALMENTE     | Condicionado        | Medio-Alto    | Facturación y ENS requieren validación |
| Criterios adjudicación | ALTA OPORTUNIDAD        | Positivo            | Bajo          | Estrategia sólida                     |
| Económico-financiero   | RENTABLE CON GAPS       | Condicionado        | Medio-Alto    | Margen bajo en bajas agresivas        |
| Compras/Partners       | CUBIERTO CON PARTNERS   | Condicionado        | Medio         | Depende de compromisos                |
| Delivery/Operación     | OPERABLE CON GAPS       | Condicionado        | Medio         | Depende de partners y accesos cliente |
| Service Design/ITIL    | APTO CON GAPS           | Condicionado        | Medio         | Gaps en SLA, CMDB, ServiceNow         |
| Seguridad/DPO/ENS      | CUMPLE CON GAPS         | Condicionado        | Alto          | Alcance ENS, logs, subencargados IA   |
| Coherencia Documental  | COHERENTE CON OBSERVACIONES | Condicionado   | Medio         | Observaciones relevantes              |

4. Riesgos bloqueantes:
| Riesgo                        | Fuente/agente      | Evidencia                  | Impacto | Probabilidad | Propietario | Accion de cierre           | Fecha limite | Decision si no se cierra |
|-------------------------------|--------------------|---------------------------|---------|-------------|-------------|----------------------------|--------------|-------------------------|
| Facturación mínima auditada    | Administrativo     | Duda sobre cierre 2024/25 | Alto    | Media       | D. Financiero| Certificado auditoría      | T-10         | NO-GO                   |
| Alcance ENS IA/RAG            | Seguridad          | Gap en alcance ENS        | Alto    | Media       | D. Seguridad | Certificado ENS actualizado| T-10         | NO-GO                   |
| Compromiso cloud/anonimización| Compras/Delivery   | Carta partner/contrato    | Alto    | Media       | D. Compras   | Carta partner firmada      | T-10         | NO-GO                   |
| Margen <10%                   | Económico          | Margen negativo en bajas  | Alto    | Media       | D. Comercial | Validar precio/margen      | T-10         | NO-GO                   |

5. Riesgos altos no bloqueantes:
| Riesgo                        | Impacto | Mitigación                  | Seguimiento |
|-------------------------------|---------|----------------------------|-------------|
| Incremento costes cloud/IA    | Alto    | Control consumo, revisión   | Mensual     |
| Logs 24 meses, retención      | Alto    | Validar capacidad, ajuste   | Mensual     |
| SLA críticos, penalizaciones  | Alto    | Refuerzo equipo, runbooks   | Mensual     |
| Dependencia partners          | Alto    | Contratos, backup partners  | Mensual     |
| Equivalencia SaaS UE         | Medio   | Validación técnica/legal    | Pre-oferta  |

6. Condiciones para GO:
1. Certificado auditoría de facturación 2024/2025 (D. Financiero, T-10).
2. Certificado ENS actualizado con alcance IA/RAG (D. Seguridad, T-10).
3. Carta de compromiso de cloud partner y anonimización (D. Compras, T-10).
4. Validación de precio/margen mínimo 10% (D. Comercial, T-10).
5. Validación técnica/legal de equivalencia SaaS UE (D. Seguridad, T-10).

7. Motivos de NO-GO o de GO condicionado:
Los riesgos de exclusión por solvencia económica, alcance ENS y dependencias de partners impiden un GO limpio. El margen económico solo es aceptable en escenarios conservadores. Si no se cierran las condiciones, la oferta sería excluible o no rentable.

8. Riesgos aceptables:
- Gaps en SLA, CMDB, ServiceNow, logs y penalizaciones pueden aceptarse si se refuerza el equipo y se planifica la transición.
- Incremento de costes cloud/IA es aceptable si se controla el consumo y se revisa mensualmente.

9. Plan de mitigación previo a oferta:
- T-15: Solicitar certificados y cartas a partners.
- T-10: Validar facturación, ENS, compromisos cloud/anonimización.
- T-5: Revisar precio/margen, validar equivalencia SaaS UE.
- T-1: Confirmar documentación, preparar memoria técnica.

10. Plan de mitigación post-adjudicación:
- Antes de formalización: Validar contratos partners, actualizar ENS.
- Transición: Planificar accesos, dimensionar equipo, refuerzo SLA.
- Go-live: Validar logs, monitorización, runbooks.
- Primer mes: Revisión consumo cloud, penalizaciones, backup partners.

11. Escenarios de decisión:
- Conservador: Oferta con margen >10%, todos certificados y compromisos cerrados. GO.
- Probable: Margen 10-12%, certificados y compromisos en curso. GO CONDICIONADO.
- Agresivo: Margen <10%, certificados o compromisos pendientes. NO-GO.

12. Preguntas críticas pendientes:
- ¿La facturación 2024/2025 está auditada y aceptada por el órgano?
- ¿El certificado ENS incluye explícitamente el servicio IA/RAG?
- ¿Los partners cloud y anonimización firman compromiso antes de oferta?
- ¿La equivalencia SaaS UE cumple requisitos legales y técnicos?
- ¿Volumetría tickets/incidencias confirmada por cliente?

13. Recomendación final al comité:
Se recomienda GO CONDICIONADO, sujeto al cierre de facturación auditada, alcance ENS IA/RAG, compromisos cloud/anonimización y margen mínimo 10%. Si no se cierran, NO-GO.

14. Fuentes utilizadas:
- Agentes: Resumen profesional, Solvencia de perfiles, Solvencia de proyectos, Administrativo/Legal, Criterios adjudicación, Económico-financiero, Compras/Partners, Delivery/Operación, Service Design/ITIL, Seguridad/DPO/ENS, Coherencia Documental.
- Documentos: Pliego administrativo, Pliego técnico, Anexo solvencia.