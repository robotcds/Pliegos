# Extracción de viabilidad

Ampliación basada en `IA - Fuentes para proyecto VIABILIDAD.docx`, aportado por el usuario.
Se conservan las tareas y los datos corporativos anteriores. Los requisitos nuevos se
definen en `viabilidad.py` y se incorporan a los prompts de sistema y de usuario.
La arquitectura vigente está descrita en [capas.md](capas.md). A1 es una referencia
factual breve; A2, A3, A4, A6, A8, A9 y A10 extraen únicamente requisitos del pliego,
con fuentes y estados de lectura. Las tablas de contraste empresarial, estados de
cumplimiento, estimaciones y acciones corresponden a la capa 2. Los resultados
esperados más abajo describen el contraste de viabilidad, no la salida de los extractores.

## Reparto de responsabilidades

| Información del documento | Responsable principal | Campos que debe extraer | Fuente interna prevista |
|---|---|---|---|
| Volumen anual de negocio | A3 extrae; Económico-financiero contrasta | Ventas globales y de la línea IT por ejercicio, tres ejercicios de referencia, mejor ejercicio, umbral | ERP SAP/Dynamics/Navision y cuentas auditadas |
| Patrimonio y ratios | A3 extrae; Económico-financiero contrasta | Patrimonio, ejercicio, activo/pasivo, fórmula, componentes y resultado comparable | ERP y balance auditado |
| RC / riesgos profesionales | A3 extrae; A2 recoge admisibilidad; Económico-financiero contrasta | Cobertura, límite, actividad, titular, asegurador, póliza, vigencia y renovación | Póliza, recibo y Finanzas |
| CBE | Solvencia de proyectos | Objeto/tecnologías, neto ejecutado, inicio/fin, adjudicador, CPV, emisor y buena ejecución | SharePoint/OneDrive/gestor documental o CRM |
| Perfiles | Solvencia de perfiles | Titulación, experiencia en empresa/sector/relevante por separado, certificación personal, emisor y vigencia | RRHH Workday/SuccessFactors/Meta4 y títulos/CV/certificados |
| ISO 9001 / ISO 14001 | Administrativo y Legal | Titular, alcance/áreas, identificador, emisor y caducidad | Calidad / Compliance |
| ISO 20000 | Service Design / ITIL | Alcance del servicio, titular, emisor, caducidad y equivalencias admitidas | Calidad / Compliance |
| ISO 27001 / ENS | Seguridad / DPO / ENS | Alcance de sistemas y entornos, nivel ENS, titular, emisor, caducidad | Calidad / Compliance |
| Fabricantes y alianzas | Compras / Partners | Nivel propio/externo, titular, especialización, vencimiento y compromiso | Portal de alianzas / CRM Salesforce o Dynamics |
| ROLECE y clasificación | Administrativo y Legal | Inscripción y actualización; grupo, subgrupo, categoría; qué solvencia puede sustituir | Certificado del registro ROLECE |

Resumen sintetiza; Criterios distingue mínimos y elementos puntuables; Delivery
transforma caducidades y dependencias en acciones; Coherencia y Go/No-Go consolidan
sin dar por resueltas las carencias de evidencia.

La columna «Acceso a la Fuente» del documento original está vacía. Esta modificación
no instala conectores ni afirma haber accedido a sistemas externos. Tampoco convierte
las afirmaciones jurídicas generales del documento en reglas universales: se extrae
lo exigido en cada pliego y las dudas de admisibilidad se remiten a revisión jurídica.

## Caso de prueba OPP-SW-011

Caso íntegramente ficticio y realista: portal ciudadano y operación IT del Ayuntamiento
Ficticio de Valleverde. Se selecciona como **opción 12** en el menú actual; LIC-10484
conserva la opción 11 y Examples pasa a la 13.

Pliegos locales: `opp-sw-011-administrativo.txt` y `opp-sw-011-tecnico.txt` en
`data/ficticios/`. El dossier `opp-sw-011-evidencias.txt` es evidencia interna del
licitador, separada del pliego. Se carga únicamente para el identificador OPP-SW-011
y no modifica los perfiles ni los datos de ninguna otra licitación. No es prueba de
que se hayan consultado ERP, SharePoint, RRHH, fabricantes o ROLECE.

## Resultados esperados antes de ejecutar la IA

| Prueba | Resultado esperado |
|---|---|
| Ventas 2023–2025 | Globales 920.000 / 1.350.000 / 1.680.000 EUR; IT 610.000 / 980.000 / 1.180.000 EUR. Mejor IT: 2025; déficit 20.000 frente a 1.200.000. NO CUMPLE por esta vía |
| Patrimonio y liquidez | 410.000 ≥ 350.000 EUR; 720.000 / 480.000 = 1,50 ≥ 1,20. Ambos cumplen |
| RC | RC-IT-2026-031, un millón por siniestro y dos millones agregado, 01/01–31/12/2026. Cumple al cierre; falta compromiso de renovación para 2027 |
| CBE REF-001 | Emisor/adjudicador Ayuntamiento Ficticio de Sierra Capital; 465.000 EUR netos ejecutados, no los 480.000 adjudicados; CPV 72262000; 01/02/2024–30/04/2025; buena ejecución acreditada |
| CBE REF-002 | 390.000 EUR es importe comercial. Falta CBE y neto ejecutado certificado. Segundo CBE NO ACREDITADO |
| ISO 9001 | Q-901-114, Certificadora Ficticia Iberia, desarrollo/operación IT, hasta 31/12/2027: cumple |
| ISO 14001 | M-140-208, Certificadora Ficticia Ambiental, instalaciones Madrid, hasta 30/06/2026: caducada al cierre |
| ISO 20000-1 | No disponible ni equivalente aportado; no convertir ITIL personal en certificado de empresa |
| ISO 27001 | S-270-317, Certificadora Ficticia Seguridad, hasta 31/12/2027; oficina de desarrollo únicamente, excluye producción: fuera de alcance |
| ENS MEDIA | ENS-M-044, Auditora Ficticia ENS, hasta 31/12/2026; entorno de desarrollo Madrid, no producción Azure: fuera de alcance |
| Partnership | Sermicro es indirect reseller; Cloud Partner Ficticio S.A. tiene nivel Infrastructure (Azure) hasta 31/03/2027, pero especialización Azure VMware Solution caducada 31/08/2026 y sin compromiso firmado |
| Ana Torres | Ingeniera informática, 6 años empresa, 10 sector, 8 dirigiendo; PMP PMI PMP-AT-0921 hasta 30/09/2026: no cumple al cierre de 30/10/2026 |
| Sofia Martin | Ingeniera informática, 4 años empresa, 7 sector, 6 backend; AWS Developer Associate sin fecha ni certificado verificable: NO ACREDITADO |
| ROLECE | ROL-2026-0915 emitido 15/09/2026: inscripción aportada; sin grupos/subgrupos/categorías ni declaración al cierre. V/2/3 es alternativa solo a ventas y CBE, no obligación independiente |
| Consolidación | No GO incondicional: faltan solvencia y acreditaciones obligatorias; distinguir carencias documentales e incumplimientos demostrados |

## Repetir la comprobación

```powershell
python -m unittest discover -s tests -v
python comprobar_viabilidad.py
python comprobar_viabilidad.py --live
python verificar_campos_viabilidad.py resumenes/prueba_viabilidad_revision_20260929
```

La prueba local valida carga y aislamiento; **no demuestra extracción por IA**.
La opción `--live` realiza nueve llamadas a Druid con los prompts de la aplicación:
siete especialistas, Coherencia y Go/No-Go. Guarda prompts y respuestas por separado
en una carpeta nueva dentro de `resumenes/`. Las dos consolidaciones se prueban con
esas siete salidas, no con una ejecución completa de los doce agentes.
Los resultados esperados de esta página no se envían al modelo. Debe contrastarse
el contenido de las respuestas, no solo la presencia de una tabla o de palabras clave.
`verificar_campos_viabilidad.py` comprueba presencia textual de los datos esperados y
guarda `cobertura_campos.json`; su éxito no acredita por sí solo la corrección de
fuentes, relaciones entre filas, estados o cálculos. El informe de revisión de la
ejecución se guarda por separado como `revision.md`.
Para evitar repetir llamadas sin cambios se puede añadir
`--reuse-from ruta/a/ejecucion/anterior`: solo reutiliza una respuesta si coincide
exactamente el prompt completo, incluidas las salidas previas consumidas por el agente.
El dossier es sintético; la prueba no acredita integraciones externas ni garantiza
que otras licitaciones o futuras ejecuciones tengan el mismo resultado.

## Resultado de la ejecución revisada

Véase [revisión y limitaciones](../resumenes/prueba_viabilidad_revision_20260929/revision.md): 58 de 59 comprobaciones de cobertura textual, con observaciones semánticas. La extracción no está validada sin reservas.
# Corrección de carga y evidencia — 29/09/2026

Se incluyen las referencias `AdditionalDocumentReference` del XML. LIC-10484
contiene diez documentos, incluidos CDC y anexos. El extractor lee XLSX con
openpyxl, conserva hoja/celda y muestra fórmulas como no calculadas. Los PDF
incluyen número de página en el texto. Instalar dependencias con
`python -m pip install -r requirements.txt`.

Los documentos fallidos, sin URL, bloqueados o pendientes por límite de caracteres
permanecen en el índice. Los formatos sin extractor producen un error explícito.
Una remisión a un documento ausente no autoriza a declarar NO EXIGIDO. Las listas
ficticias no acreditan cuentas, pólizas ni vigencias; una próxima auditoría tampoco
acredita caducidad. La solvencia sectorial y el importe anual acumulado de servicios
deben interpretarse según el pliego.

Pruebas locales: `python -m unittest discover -s tests -v`.
Prueba IA sin sobrescribir informes previos:
`python comprobar_viabilidad.py --contract LIC-10484 --live`.
Se puede limitar con `--agents economic projects security`.
La presencia textual de campos no equivale a validación semántica.
