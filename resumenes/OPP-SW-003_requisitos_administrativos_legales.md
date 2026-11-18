1. Veredicto ejecutivo administrativo/legal: CUMPLE PARCIALMENTE

2. Tabla de extraccion administrativa:

| Campo                        | Extraccion                                                                                                                        |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Fecha limite                 | 30/09/2026 a las 13:00                                                                                                             |
| Forma de presentacion        | Plataforma electronica, dos sobres electronicos (1: admin/tecnica, 2: economica)                                                  |
| Condiciones de participacion | Capacidad de obrar, no prohibicion contratar, certificados Hacienda y SS, clasificacion Grupo V, Subgrupo 2, Cat. 3, ISO 27001     |
| Solvencia economica          | Volumen anual >= 900.000 EUR, seguro RC profesional >= 1.500.000 EUR                                                              |
| Solvencia tecnica administrativa | Tres migraciones cloud en AAPP, ultimos 5 años, >=250.000 EUR, >=6 meses, una con Kubernetes/AKS; equipo mínimo específico      |
| Clasificacion                | Grupo V, Subgrupo 2, Categoria 3 (obligatoria, no admite alternativa para empresas españolas)                                      |
| Documentacion administrativa | DEUC, certificados Hacienda/SS, poderes, CVs, memoria migracion, plan reversibilidad, plan seguridad, oferta económica, anexos     |
| Garantias                    | Definitiva: 5% del precio de adjudicación. No hay provisional. Seguro RC 1.500.000 EUR                                            |
| Lotes                        | No hay lotes                                                                                                                      |
| Subcontratacion              | Máx. 25% (excepto dirección proyecto y arquitectura cloud, no subcontratable)                                                     |
| Formato de oferta            | Dos sobres electrónicos, sobre 1 (admin/técnica), sobre 2 (económica), máx. 50 páginas memoria, PDF, firma electrónica            |
| Exclusiones                  | No variantes, info económica en sobre 1, superar 50 páginas, no plan reversibilidad, superar presupuesto, no cumplir solvencia     |
| Condiciones legales          | Duración 10 meses, sin prórroga, penalizaciones, RGPD, confidencialidad, propiedad intelectual, ENS media, no cesión total IP     |
| Obligaciones del adjudicatario| Herramientas, cloud temporal, soporte partner, cartas compromiso, cumplimiento ENS, reporting, facturación por hitos              |

3. Comparacion requisito vs empresa:

| Requisito exacto                                                                 | Documento fuente y evidencia breve                                                                 | Cumplimiento           | Info interna usada                                   | Brecha/accion necesaria                                                                                 |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Capacidad de obrar, no prohibición contratar, Hacienda/SS al corriente           | Pliego adm.: "capacidad de obrar, no prohibición... certificados positivos Hacienda y SS"           | CUMPLE                 | Dato corporativo                                      | Ninguna                                                                                                 |
| Clasificación Grupo V, Subgrupo 2, Cat. 3 (obligatoria)                          | Pliego adm.: "se exige clasificación empresarial equivalente..."                                    | NO CUMPLE              | No tiene clasificación empresarial                    | No puede acreditar clasificación exigida, salvo cambio de criterio en pliego                            |
| Solvencia económica: volumen >=900.000 EUR, seguro RC >=1.500.000 EUR            | Pliego adm.: "volumen anual mínimo 900.000 EUR y seguro RC 1.500.000 EUR"                         | CUMPLE PARCIALMENTE    | Facturación sí, seguro RC solo 1.000.000 EUR          | Necesita ampliar seguro RC a 1.500.000 EUR antes de presentar oferta                                    |
| ISO 27001                                                                        | Pliego adm.: "se exige ISO 27001"                                                                 | CUMPLE                 | Certificaciones empresa                               | Ninguna                                                                                                 |
| Solvencia técnica: 3 migraciones cloud AAPP, >=250k EUR, >=6 meses, 1 con AKS    | Anexo solvencia: "tres referencias... importe mínimo 250.000 EUR... una con Kubernetes/AKS"        | CUMPLE PARCIALMENTE    | Proyectos REF-005, REF-006, REF-003                   | Solo dos cumplen todos los requisitos (REF-005, REF-006); REF-003 no tiene 6 meses. Faltaría una más.   |
| Equipo mínimo: 2 DevOps cloud senior, backend senior, jefe proyecto              | Anexo solvencia: "dos DevOps/cloud senior... backend senior... jefe de proyecto..."                | CUMPLE PARCIALMENTE    | Perfiles internos                                     | Solo un DevOps cloud senior claro (Ivan Lopez). Falta un segundo DevOps cloud senior.                   |
| Subcontratación máx. 25%, no dirección ni arquitectura cloud                     | Pliego adm.: "subcontratación máxima 25%... no dirección ni arquitectura cloud"                    | CUMPLE                 | Política empresa, subcontratistas homologados         | Ninguna                                                                                                 |
| No variantes, no info económica en sobre 1, máx. 50 páginas memoria              | Pliego adm.: "no se admiten variantes... propuesta no podrá superar 50 páginas..."                 | CUMPLE                 | Procedimientos internos de oferta                     | Controlar formato y estructura de oferta                                                                |
| Garantía definitiva 5% del precio                                                | Pliego adm.: "garantía definitiva 5% del precio de adjudicación"                                   | CUMPLE                 | Capacidad aval/garantía 120.000 EUR                   | Ninguna                                                                                                 |
| RGPD, confidencialidad, ENS media                                                | Pliego técnico: "cumpla ENS categoría MEDIA... ISO 27001..."                                       | CUMPLE                 | Certificaciones, cumplimiento RGPD                    | Ninguna                                                                                                 |
| Propiedad intelectual: no cesión total del producto base                         | Pliego adm.: "no cesión total de propiedad intelectual..."                                         | CUMPLE                 | Política empresa                                      | Ninguna                                                                                                 |

4. Riesgos de exclusion (priorizados):
1. No disponer de la clasificación empresarial obligatoria (Grupo V, Subgrupo 2, Cat. 3) para empresas españolas.
2. No alcanzar el seguro de responsabilidad civil profesional mínimo exigido (1.500.000 EUR).
3. No poder acreditar tres migraciones cloud en AAPP con los requisitos de importe, duración y tecnología (solo dos cumplen).
4. No disponer de dos DevOps/cloud senior con experiencia mínima requerida.

5. Checklist de documentacion a preparar:
- DEUC firmado electrónicamente.
- Certificados positivos de Hacienda y Seguridad Social.
- Escrituras y poderes del representante.
- CVs del equipo mínimo (2 DevOps/cloud senior, backend senior, jefe de proyecto).
- Memoria de migración (máx. 50 páginas).
- Plan de continuidad y reversibilidad.
- Plan de seguridad y gestión de cambios.
- Oferta económica (sobre 2).
- Anexos oficiales del pliego.
- Carta de compromiso del partner cloud para soporte AKS.
- Certificado ISO 27001.
- Póliza de seguro RC profesional ampliada a 1.500.000 EUR.
- Referencias de tres migraciones cloud en AAPP (con importes, duración, tecnología).

6. Decision operativa:
NO RECOMENDADO PRESENTARSE salvo que se resuelvan las siguientes brechas antes de la oferta:
- Obtener la clasificación empresarial exigida (Grupo V, Subgrupo 2, Cat. 3) o que el órgano acepte medios alternativos para empresas españolas.
- Ampliar el seguro de responsabilidad civil profesional a 1.500.000 EUR.
- Incorporar un segundo perfil DevOps/cloud senior con experiencia acreditada.
- Identificar y documentar una tercera referencia de migración cloud en AAPP que cumpla importe, duración y tecnología.
Si no se resuelven estos puntos, la oferta será excluida por incumplimiento de requisitos esenciales.

7. Documentos revisados:
- Pliego administrativo OPP-SW-003 migracion cloud
- Pliego tecnico OPP-SW-003 migracion cloud
- Anexo solvencia OPP-SW-003 migracion cloud