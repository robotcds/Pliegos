1. Veredicto ejecutivo de coherencia: INCOHERENCIAS CRITICAS

2. Resumen ejecutivo de coherencia:
La información procesada presenta incoherencias críticas en solvencia económica, certificaciones, partnership cloud, cobertura de seguros y referencias de proyectos. Hay contradicciones entre agentes sobre el cumplimiento de ventas IT mínimas, vigencia y alcance de certificaciones ISO/ENS, partnership Azure, y cobertura de seguro RC durante toda la ejecución. Faltan evidencias documentales para varios requisitos clave, y existen brechas en la acreditación de CBE, dedicaciones de perfiles y compromiso de partners. La base no está lista para Go/No-Go sin resolver estos puntos.

3. Tabla de veredictos consolidados por agente:
| Agente | Veredicto detectado | Dato consolidado | Confianza | Observaciones |
|--------|---------------------|------------------|-----------|--------------|
| A1     | Extracción objetiva | Datos generales  | Alta      | Informativo, sin contradicción |
| A2     | Extracción objetiva | Solvencia, certificados, RC, ROLECE | Media | Contradicciones en evidencia y vigencia |
| A3     | Extracción objetiva | Solvencia, CBE, certificados | Media | Brechas en CBE y certificaciones |
| A4     | Extracción objetiva | Criterios adjudicación | Alta | Fórmula económica clara, sin contradicción |
| A6     | Extracción objetiva | Requisitos servicio | Media | Faltan datos de herramientas y SLA |
| A8     | Extracción objetiva | Perfiles y equipo | Media | Dedicaciones y certificaciones incompletas |
| A9     | Extracción objetiva | Seguridad y datos | Media | ENS y ISO 27001 fuera de alcance |
| A10    | Extracción objetiva | Compras y partners | Media | Partnership Azure incompleto |
| Económico-financiero | No evaluable | Costes, margen, ventas IT | Baja | Brecha ventas IT, seguro RC, margen ajustado |
| Delivery/Operación | Operable con gaps | Cobertura parcial | Media | Gaps en certificaciones, partners y SLA |

4. Contradicciones detectadas:
| Contradicción | Agentes afectados | Evidencia | Dato consolidado propuesto | Confianza | Impacto en Go/No-Go |
|---------------|------------------|----------|--------------------------|-----------|---------------------|
| Ventas IT mínimas | A2, A3, Económico | ERP, CA-2025, PCAP | NO ACREDITADO (brecha 20.000 EUR) | Alta | Bloqueante, requiere alternativa por clasificación |
| Certificaciones ISO/ENS | A2, A3, A9, Dossier | Certificados, PCAP, PPT | NO ACREDITADO (alcance y vigencia insuficiente) | Alta | Bloqueante, requiere actualización y ampliación |
| Partnership Azure | A2, A3, A10, Delivery | Carta partner, PCAP, PPT | NO ACREDITADO (especialización caducada, sin compromiso) | Alta | Bloqueante, requiere renovación y compromiso firmado |
| Seguro RC | A2, A3, Económico | Póliza, PCAP | CUMPLE al cierre, NO ACREDITADO ejecución | Alta | Bloqueante, requiere compromiso de renovación |
| CBE proyectos | A3, Dossier | CBE-REF-001, PCAP | 1 CBE acreditado, 1 pendiente | Media | Bloqueante, requiere CBE adicional |
| Certificación ISO 20000-1 | A2, A3, A9, Dossier | NO CONSTA | NO ACREDITADO | Alta | Bloqueante, no disponible |
| Certificación ENS MEDIA | A2, A3, A9, Dossier | ENS-M-044 | NO ACREDITADO (no cubre producción) | Alta | Bloqueante, requiere certificación para producción |
| Certificación ISO 27001 | A2, A3, A9, Dossier | S-270-317 | NO ACREDITADO (excluye producción) | Alta | Bloqueante, requiere ampliación de alcance |
| ROLECE/clasificación | A2, A3, Dossier | ROLECE ROL-2026-0915 | NO ACREDITADO (sin clasificación alternativa) | Alta | Bloqueante, requiere clasificación o alternativa válida |
| Dedicaciones perfiles | A6, A8, Delivery | RRHH, PPT | NO ACREDITADO (QA, desarrolladores, soporte N2) | Media | Bloqueante, requiere evidencia documental |

5. Duplicidades consolidadas:
- Riesgo de partnership Azure: aparece en Delivery, Compras y Económico; se consolida como "Falta especialización vigente y compromiso firmado".
- Riesgo de certificaciones ISO/ENS: aparece en Seguridad, Solvencia y Delivery; se consolida como "Certificados fuera de alcance y vigencia insuficiente".
- Riesgo de seguro RC: aparece en Solvencia, Económico y Delivery; se consolida como "Cobertura solo al cierre, falta compromiso de renovación".

6. Información incompleta o pendiente:
| Dato pendiente | Fuente | Por qué importa | Cómo validarlo | Prioridad |
|----------------|--------|----------------|---------------|----------|
| CBE segundo proyecto | Dossier, A3 | Requisito de solvencia técnica | Obtener CBE firmado y neto ejecutado | Alta |
| Compromiso renovación seguro RC | Dossier, Económico | Cobertura durante ejecución | Solicitar compromiso firmado | Alta |
| Renovación especialización Azure VMware | Dossier, Compras, Delivery | Partnership cloud exigido | Solicitar certificado actualizado y compromiso | Alta |
| Certificación ENS MEDIA para producción | Dossier, Seguridad | Requisito de seguridad | Solicitar auditoría y certificado para entorno producción | Alta |
| Certificación ISO 27001 para producción | Dossier, Seguridad | Requisito de seguridad | Solicitar ampliación de alcance | Alta |
| Certificación ISO 20000-1 | Dossier, Seguridad | Requisito de gestión de servicio | Solicitar auditoría y certificado | Alta |
| Dedicaciones y certificaciones QA, desarrolladores, soporte N2 | RRHH, A8, Delivery | Requisito de perfiles | Reunir evidencia documental | Alta |
| Declaración de ausencia de variaciones ROLECE | Dossier, A2 | Requisito administrativo | Solicitar declaración firmada | Media |

7. Riesgos consolidados limpios:
| Riesgo | Categoria | Fuente principal | Fuentes secundarias | Impacto | Probabilidad | Estado | Acción recomendada |
|--------|----------|------------------|---------------------|--------|-------------|-------|-------------------|
| Brecha ventas IT | Solvencia | Económico, A2, A3 | Dossier | Alto | Alta | Abierto | Buscar alternativa por clasificación |
| Certificaciones fuera de alcance | Solvencia/Seguridad | Dossier, A9 | A2, A3, Delivery | Alto | Alta | Abierto | Actualizar y ampliar certificaciones |
| Partnership Azure incompleto | Compras/Delivery | Dossier, A10 | Delivery, Económico | Alto | Alta | Abierto | Renovar especialización y compromiso |
| Seguro RC solo al cierre | Solvencia | Dossier, Económico | A2, A3, Delivery | Alto | Alta | Abierto | Obtener compromiso de renovación |
| CBE insuficiente | Solvencia técnica | Dossier, A3 | Delivery | Alto | Media | Abierto | Obtener CBE adicional |
| Dedicaciones y certificaciones perfiles | Operación | RRHH, A8, Delivery | A6 | Medio | Alta | Abierto | Reunir evidencia documental |

8. Hechos consolidados para Go/No-Go:
- Ventas IT 2025: 1.180.000 EUR (brecha 20.000 EUR vs umbral)
- Patrimonio neto 2025: 410.000 EUR (cumple)
- Ratio liquidez corriente: 1,50 (cumple)
- Seguro RC: 1.000.000 EUR, vigente al cierre, falta compromiso de renovación
- Certificaciones ISO 9001, 14001, 27001: vigentes, pero ISO 27001 excluye producción
- ENS MEDIA: vigente para desarrollo, no para producción
- Partnership Azure: especialización caducada, falta compromiso
- CBE: 1 acreditado, 1 pendiente
- ROLECE: inscripción vigente, sin clasificación alternativa
- Dedicaciones y certificaciones QA, desarrolladores, soporte N2: no acreditadas

9. Datos que el A13 no debe usar sin validar:
- Ventas IT como cumplidas (brecha)
- Certificaciones ISO/ENS como cubriendo producción
- Partnership Azure como vigente y comprometido
- Seguro RC como cubriendo toda la ejecución
- CBE como cubiertos (solo 1 acreditado)
- Dedicaciones y certificaciones de perfiles como cubiertas
- Clasificación alternativa por ROLECE (no acreditada)

10. Correcciones aplicadas:
- Recalculada brecha ventas IT: 1.180.000 EUR vs 1.200.000 EUR (brecha 20.000 EUR)
- Certificaciones ISO/ENS ajustadas a alcance y vigencia real según dossier
- Partnership Azure ajustado a vigencia y compromiso real
- Seguro RC ajustado a vigencia al cierre, no ejecución
- CBE ajustado a evidencia documental

11. Paquete limpio para A13:
- Decision preliminar sugerida: NO-GO PROBABLE
- Bloqueantes: ventas IT, certificaciones ISO/ENS, partnership Azure, seguro RC, CBE, dedicaciones perfiles
- Condiciones pendientes: compromiso renovación seguro RC, CBE segundo proyecto, renovación especialización Azure VMware, certificación ENS MEDIA y ISO 27001 para producción, certificación ISO 20000-1, declaración ROLECE, evidencia perfiles
- Riesgos altos: brecha ventas IT, certificaciones fuera de alcance, partnership Azure, seguro RC, CBE insuficiente
- Evidencias positivas: patrimonio neto, ratio liquidez, inscripción ROLECE, certificaciones ISO 9001/14001 vigentes
- Preguntas críticas: ¿Se puede acreditar clasificación alternativa? ¿Se puede renovar partnership Azure? ¿Se puede ampliar certificaciones? ¿Se puede obtener CBE y compromiso seguro RC?

12. Fuentes utilizadas:
- Agentes: A1, A2, A3, A4, A6, A8, A9, A10, Económico-financiero, Delivery/Operación
- Documentos: PCAP OPP-SW-011, PPT OPP-SW-011, ERP Dynamics FIN-2025-042, CA-2025, RC-IT-2026-031, CBE-REF-001, Compliance CAL-2026-09, ENS-M-044, S-270-317, ROL-2026-0915, ALI-027, FAB-2026-09, RH-2026-09

Extracción de viabilidad:
| Parámetro | Estado | Dato decisivo | Fuente | Acción |
|-----------|--------|--------------|--------|--------|
| Ventas IT | NO ACREDITADO | 1.180.000 EUR vs 1.200.000 EUR | ERP, CA-2025 | Buscar alternativa por clasificación |
| Patrimonio neto | CUMPLE | 410.000 EUR | CA-2025 | Ninguna |
| Ratio liquidez | CUMPLE | 1,50 | CA-2025 | Ninguna |
| Seguro RC | CUMPLE al cierre, NO ACREDITADO ejecución | Vigencia 31/12/2026, fin contrato 30/10/2027 | RC-IT-2026-031 | Obtener compromiso renovación |
| Certificaciones ISO/ENS | NO ACREDITADO | Alcance y vigencia insuficiente | Compliance CAL-2026-09, ENS-M-044, S-270-317 | Actualizar y ampliar |
| Partnership Azure | NO ACREDITADO | Especialización caducada, sin compromiso | ALI-027, FAB-2026-09 | Renovar y firmar compromiso |
| CBE | 1 acreditado, 1 pendiente | CBE-REF-001 | CBE-REF-001 | Obtener CBE adicional |
| ROLECE/clasificación | NO ACREDITADO | Inscripción vigente, sin clasificación | ROL-2026-0915 | Solicitar clasificación o alternativa |
| Dedicaciones perfiles | NO ACREDITADO | QA, desarrolladores, soporte N2 | RH-2026-09, PPT | Reunir evidencia documental |