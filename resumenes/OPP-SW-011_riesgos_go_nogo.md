1. Veredicto ejecutivo Go/No-Go: NO-GO

2. Decisión ejecutiva:
La oportunidad OPP-SW-011 presenta múltiples riesgos bloqueantes de admisión y ejecución que impiden recomendar la presentación de oferta en las condiciones actuales. Existen brechas no subsanadas en solvencia económica (ventas IT mínimas no acreditadas), certificaciones obligatorias (ISO 20000-1, ISO 27001 y ENS MEDIA fuera de alcance requerido), partnership cloud (especialización Azure VMware Solution caducada y sin compromiso firmado), seguro RC (cobertura solo hasta 31/12/2026, sin compromiso de renovación para cubrir toda la ejecución), y referencias de proyectos (solo un CBE acreditado). La falta de evidencia documental y compromisos firmados en estos puntos supone riesgo cierto de exclusión y no admisión de la oferta.

3. Resumen de semáforo por agente:
| Agente              | Veredicto heredado         | Impacto en decisión | Riesgo         | Comentario ejecutivo                                 |
|---------------------|----------------------------|--------------------|----------------|------------------------------------------------------|
| A1 Resumen          | Extracción objetiva        | Nulo               | Bajo           | Informativo, sin contradicción                       |
| A2 Adm-Legal        | Extracción objetiva        | Alto               | Alto           | Brechas en evidencia y vigencia                      |
| A3 Solvencia        | Extracción objetiva        | Alto               | Alto           | Brechas en CBE y certificaciones                     |
| A4 Criterios Adj.   | Extracción objetiva        | Nulo               | Bajo           | Fórmula económica clara                              |
| A6 Servicio         | Extracción objetiva        | Medio              | Medio          | Faltan datos de herramientas y SLA                   |
| A8 Perfiles         | Extracción objetiva        | Alto               | Alto           | Dedicaciones y certificaciones incompletas           |
| A9 Seguridad        | Extracción objetiva        | Alto               | Alto           | ENS y ISO 27001 fuera de alcance                     |
| A10 Compras         | Extracción objetiva        | Alto               | Alto           | Partnership Azure incompleto                         |
| Económico-financiero| No evaluable               | Crítico            | Alto           | Brecha ventas IT, seguro RC, margen ajustado         |
| Delivery/Operación  | Operable con gaps          | Alto               | Alto           | Gaps en certificaciones, partners y SLA              |
| Coherencia Doc.     | Incoherencias críticas     | Crítico            | Muy alto       | Contradicciones y bloqueantes no resueltos           |

4. Riesgos bloqueantes:
| Riesgo                                 | Fuente/agente         | Evidencia                         | Impacto      | Probabilidad | Propietario         | Acción de cierre                        | Fecha límite   | Decisión si no se cierra |
|----------------------------------------|-----------------------|-----------------------------------|--------------|--------------|---------------------|------------------------------------------|---------------|-------------------------|
| Ventas IT mínimas no acreditadas       | Económico, A2, A3     | ERP, CA-2025                      | Exclusión    | Alta         | Dir. Financiera     | Clasificación alternativa o no ofertar   | 25/10/2026    | NO-GO                  |
| Certificación ISO 20000-1 no disponible| A2, A3, A9, Dossier   | No consta certificado             | Exclusión    | Alta         | Calidad             | Obtener certificado o no ofertar         | 25/10/2026    | NO-GO                  |
| Certificación ENS MEDIA fuera de alcance| A2, A3, A9, Dossier  | ENS-M-044 (no cubre producción)   | Exclusión    | Alta         | CISO                | Ampliar alcance o no ofertar             | 25/10/2026    | NO-GO                  |
| Certificación ISO 27001 fuera de alcance| A2, A3, A9, Dossier  | S-270-317 (excluye producción)    | Exclusión    | Alta         | CISO                | Ampliar alcance o no ofertar             | 25/10/2026    | NO-GO                  |
| Partnership Azure no vigente           | A2, A3, A10, Delivery | Especialización caducada, sin compromiso | Exclusión | Alta         | Compras/Alianzas     | Renovar y firmar compromiso              | 25/10/2026    | NO-GO                  |
| Seguro RC no cubre toda la ejecución   | Económico, A2, A3     | Póliza vence 31/12/2026           | Exclusión    | Alta         | Dir. Financiera     | Compromiso renovación firmado            | 25/10/2026    | NO-GO                  |
| Solo un CBE acreditado                 | A3, Dossier           | CBE-REF-001, falta segundo CBE    | Exclusión    | Alta         | Of. Proyectos        | Obtener segundo CBE firmado              | 25/10/2026    | NO-GO                  |
| Dedicaciones/certificados perfiles     | A6, A8, Delivery      | RRHH, CV, títulos incompletos     | Exclusión    | Alta         | RRHH                 | Reunir evidencia completa                | 25/10/2026    | NO-GO                  |

5. Riesgos altos no bloqueantes:
| Riesgo                        | Impacto         | Mitigación                        | Seguimiento           |
|-------------------------------|-----------------|-----------------------------------|-----------------------|
| Margen económico ajustado     | Rentabilidad    | Ajustar precio, comité de riesgo  | Dir. Financiera       |
| SLA y reporting incompletos   | Operativo       | Definir métricas y KPIs internos  | Dir. Operaciones      |
| Dependencia de partner cloud  | Operativo       | Contrato y penalización           | Compras/Alianzas      |

6. Condiciones para GO:
No aplicable: los bloqueantes impiden un GO condicionado salvo que se acrediten todos los requisitos de admisión y ejecución antes del cierre de oferta.

7. Motivos de NO-GO o de GO condicionado:
La suma de bloqueantes de admisión (ventas IT, certificaciones, partnership, seguro RC, CBE, perfiles) impide un GO limpio. No es posible ofertar sin riesgo cierto de exclusión. Solo sería viable un GO condicionado si se acreditan todos los requisitos documentales y compromisos antes del cierre.

8. Riesgos aceptables:
Riesgos de margen ajustado, SLA internos y dependencia de partner cloud pueden aceptarse si se gestiona el precio y se firman los compromisos, pero no son admisibles mientras persistan los bloqueantes de admisión.

9. Plan de mitigación previo a oferta:
- T-15: Solicitar certificados y compromisos a partners y aseguradoras; requerir CBE y documentación de perfiles.
- T-10: Revisar evidencias recibidas; validar alcance y vigencia de certificaciones.
- T-5: Simular presentación documental completa; checklist de admisión.
- T-1: Confirmar recepción de todos los documentos y compromisos firmados.

10. Plan de mitigación post-adjudicación:
- Antes de formalización: Validar vigencia de todos los certificados y compromisos.
- Transición: Plan de onboarding y backup de perfiles críticos.
- Go-live: Validar entorno cloud y cumplimiento ENS/ISO.
- Primer mes: Auditoría interna de cumplimiento contractual y documental.

11. Escenarios de decisión:
- Escenario conservador: NO-GO. No se acreditan los requisitos de admisión.
- Escenario probable: NO-GO. No se prevé obtener todos los documentos a tiempo.
- Escenario agresivo: GO condicionado solo si se acreditan todos los bloqueantes antes del cierre. Riesgo muy alto.

12. Preguntas críticas pendientes:
- ¿Admitiría el órgano de contratación una prórroga para aportar certificados o compromisos pendientes?
- ¿Se aceptan medios externos para cubrir partnership y certificaciones?
- ¿Puede el partner cloud firmar compromiso de adscripción nominativa?
- ¿Se admite compromiso de renovación de seguro RC como suficiente?

13. Recomendación final al comité:
Se recomienda NO-GO salvo acreditación documental completa de todos los requisitos de admisión y ejecución antes del cierre de oferta. Si se obtienen, reevaluar para posible GO condicionado.

14. Fuentes utilizadas:
Agentes: A1, A2, A3, A4, A6, A8, A9, A10, Económico-financiero, Delivery/Operación, Coherencia Documental. Documentos: PCAP OPP-SW-011, PPT OPP-SW-011, Dossier interno OPP-SW-011, ERP Dynamics FIN-2025-042, CA-2025, RC-IT-2026-031, CBE-REF-001, CAL-2026-09, S-270-317, ENS-M-044, ALI-027, FAB-2026-09, RH-2026-09, ROL-2026-0915.

---

Extracción de viabilidad:
| Parámetro                        | Estado         | Dato decisivo                        | Fuente           | Acción                       |
|----------------------------------|---------------|--------------------------------------|------------------|------------------------------|
| Ventas IT mínimas                | NO ACREDITADO | 1.180.000 EUR vs 1.200.000 EUR       | ERP, CA-2025     | Buscar clasificación         |
| Patrimonio neto                  | CUMPLE        | 410.000 EUR                          | CA-2025          | Ninguna                      |
| Ratio liquidez corriente         | CUMPLE        | 1,50                                 | CA-2025          | Ninguna                      |
| Seguro RC                        | NO ACREDITADO | Vence 31/12/2026, sin renovación     | RC-IT-2026-031   | Solicitar compromiso         |
| CBE proyectos                    | NO ACREDITADO | Solo 1 CBE acreditado                | CBE-REF-001      | Obtener segundo CBE          |
| ISO 9001                         | CUMPLE        | Vigente, alcance correcto            | CAL-2026-09      | Ninguna                      |
| ISO 14001                        | NO ACREDITADO | Vence 30/06/2026, sin renovación     | CAL-2026-09      | Solicitar renovación         |
| ISO 20000-1                      | NO ACREDITADO | No disponible                        | Dossier          | Obtener certificado          |
| ISO 27001                        | NO ACREDITADO | Excluye producción                   | S-270-317        | Ampliar alcance              |
| ENS MEDIA                        | NO ACREDITADO | No cubre producción                  | ENS-M-044        | Ampliar alcance              |
| Partnership Azure                | NO ACREDITADO | Especialización caducada, sin compromiso | ALI-027, FAB-2026-09 | Renovar y firmar compromiso |
| ROLECE/clasificación             | NO ACREDITADO | Sin clasificación alternativa        | ROL-2026-0915    | Obtener clasificación        |
| Perfiles y dedicaciones          | NO ACREDITADO | QA, desarrolladores, soporte N2      | RH-2026-09       | Reunir evidencia             |