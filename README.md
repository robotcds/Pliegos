# Pliegos

## Precisión y cobertura documental de capa 1

Los extractores y el redactor comparten reglas ampliadas de fases/documentación,
economía contractual, baremos, anormalidad, garantías, equipo/continuidad, medios,
SLA, seguridad y cierre. Distinguen exenciones documentales de obligaciones,
clasificaciones contractuales y errores del resumen de contradicciones del pliego.
El formato AGE se conserva. El reparto por agente, límites de capa 1 y validación
están en [cobertura de capa 1](docs/cobertura_capa1.md).

Los nuevos JSON incluyen `registro_procesamiento` por extractor con el índice
preparado, compactación y avisos locales. Los informes previos no se actualizan
automáticamente; `--desde-json` no recupera información ausente de la extracción.

## Recomendaciones por agente (solo JSON)

Solo al ejecutar `--capa todas`, los doce agentes generan una lista adicional `recomendaciones`, separada de
`contenido` y `puntos_revision`. Cada propuesta incluye `titulo`, `recomendacion`,
`fundamento`, `evidencias`, `candidatos` (si corresponde) y `pendientes`.
Incluye además identificador y estado de propuesta pendiente de validación.
Se generan hasta cinco recomendaciones concretas de la especialidad, o una lista
vacía cuando no hay base útil. Se guardan en el JSON individual y en el consolidado.

Esta pasada usa el informe del agente, avisos y contexto empresarial pertinente.
El agente de perfiles recibe `INVENTED_PROFILES` y puede proponer candidatos con
encaje y carencias; todo el contexto empresarial ficticio se identifica como no
acreditativo. La extracción factual de capa 1 se conserva separada. Las propuestas
no se envían al redactor ni se añaden al PDF.

`estado_recomendaciones` distingue `no_generadas`, `generadas`, `sin_propuestas`
y `error`. La extracción se guarda antes de solicitar recomendaciones. Un fallo
de esta pasada no interrumpe los demás agentes; el JSON conserva aviso y diagnóstico.
Añade una llamada a Druid por agente, con hasta un reintento de recomendaciones
(además de los reintentos técnicos de Druid). Los informes anteriores y
`--desde-json` no generan recomendaciones retrospectivamente.

## Puntos de revisión por agente (solo JSON)

Cada agente de ambas capas incorpora `puntos_revision` en su JSON individual.
En el consolidado se conserva en `agentes[]` para capa 1 y en `analisis_capa2[]`
para capa 2. Hay un máximo de **cinco bloques por agente**, agrupados por materia
y ordenados mediante reglas de impacto contractual: documentos ausentes,
contradicciones, admisión/solvencia, condiciones económicas y ejecución.
Es una prioridad orientativa, no una evaluación jurídica generativa.
Cada bloque contiene `id`, `tipo`, `estado`, `titulo`, `prioridad`, `detalle`,
`origen` y `subpuntos`. Los subpuntos conservan `seccion`, `detalle` y `evidencia`
de cada cuestión original; no se eliminan asuntos para cumplir el límite.
No se rellenan cinco bloques cuando hay menos materias pendientes.
Se recogen ausencias y ambigüedades explícitas de
la respuesta, incluidos valores pendientes en tablas, conservando su contexto.
Una exención expresa no se marca como pendiente; la mezcla «NO EXIGIDO/NO CONSTA»
sí requiere revisión. Una lista vacía no acredita exhaustividad ni detecta por sí
sola omisiones que el agente no haya señalado.

La obtención es local y no añade llamadas a Druid. Estos nuevos metadatos se
excluyen de la entrada editorial y no se añaden a los PDF ni al Markdown.
La extracción original y sus avisos mantienen su tratamiento anterior.

Con `--capa todas` se guardan doce JSON `*_respuesta.json`, uno por agente,
y `<expediente>_consolidado.json`, también con `--formato ejecutivo` o
`--formato completo`. Los individuales se llaman
`<expediente>_capa1_<nombre_agente>_respuesta.json` o
`<expediente>_capa2_<nombre_agente>_respuesta.json`, independientemente del modo
de ejecución. El nombre del agente se normaliza sin tildes y con guiones bajos;
por ejemplo `capa1_resumen_breve` o `capa2_economico_financiero`.
Incluyen también el campo `capa`. Se guardan al finalizar cada agente, antes del PDF.

## Salida predeterminada: resumen AGE

```powershell
python .\oportunidades.py --capa 1
```

Ejecuta los ocho agentes de extracción, guarda `<expediente>_capa1.json` y añade
un último agente redactor con revisión del borrador contra el JSON íntegro.
Genera **un único PDF**, `<expediente>_resumen_legible.pdf`, dentro de la carpeta de esta ejecución en `resumenes/`.
Empieza con RESPUESTA, sin PREGUNTA, y termina con Conclusión operativa.
Usa Letter, márgenes laterales de 3 cm, tipografía serif, tablas de hasta cuatro columnas,
listas de obligaciones, subapartados explicativos y una conclusión por puntos.
El prompt editable está en [docs/prompt_resumen_age.md](docs/prompt_resumen_age.md).
El contenido editorial validado se conserva en `<expediente>_resumen_legible.redaccion.json`.

Cada extractor guarda también su respuesta completa en `*_respuesta.json` al terminar.
El redactor recibe todas las respuestas del expediente dentro del JSON consolidado
`<expediente>_capa1.json`, incluidos sus estados, fuentes y avisos; no selecciona archivos
por comodines ni mezcla ejecuciones anteriores. En cada ejecución editorial se conserva
una carpeta independiente bajo `<expediente>_resumen_legible_ejecuciones/` con
`entrada_completa.json`, un JSON por agente y las respuestas de borrador/revisión.
Las respuestas mal formadas también se guardan, como texto original dentro de un JSON
de diagnóstico. Estos diagnósticos no se utilizan como hechos de la licitación.

La revisión editorial contrasta el informe con el JSON completo y destaca estados de
exigencia, plazos abreviados, reglas de experiencia y alternativas documentales.
Antes de publicar se comprueban además regresiones concretas: garantía provisional
expresamente no exigida, plazos de confirmación/acuse, periodos coincidentes y efectos
documentales de ROLECE. Si persisten, se reintenta solo la revisión (hasta tres veces);
si no se resuelven, no se publica el nuevo PDF y se conserva la extracción.
Estos controles son alarmas de cobertura, no una garantía de exactitud jurídica ni una
verificación semántica exhaustiva. Los importes y requisitos siguen procediendo del JSON.
Los Markdown de los extractores se conservan como diagnóstico. Los PDF anteriores
ya existentes no se borran, pero no vuelven a generarse en el modo predeterminado.

Para regenerar solamente el resumen a partir de una extracción existente:

```powershell
python .\oportunidades.py --desde-json .\resumenes\LIC-10484_capa1.json
```

El lector editorial recupera llaves de cierre duplicadas inequívocas sin cambiar
valores ni completar texto truncado. Los borradores recuperados deben superar las
mismas validaciones y revisión editorial. Los reintentos reciben el error y la
respuesta anterior junto a la fuente completa; no basta una introducción o un
JSON sin conclusión. Las respuestas originales y los borradores estructuralmente
válidos se conservan en la carpeta de ejecución para diagnóstico.

Este modo necesita Druid configurado y realiza la redacción y su revisión, sin
descargar de nuevo los pliegos ni repetir los agentes extractores. El formato
se valida antes de publicar el PDF; un fallo conserva el JSON de extracción.
La comprobación editorial es generativa, no una garantía automática de fidelidad
de cada afirmación: revisa los requisitos críticos frente a las fuentes.

La capa 1 es ahora el modo por defecto. `--capa todas` añade los procesadores de
capa 2 y guarda un JSON consolidado que también recibe el redactor.
`--formato ejecutivo` y `--formato completo` son alias de compatibilidad: también
generan el único resumen legible con el formato de referencia.

Script de consola para cargar un XML de licitaciones, contar los pliegos, elegir uno por numero y generar informes a traves de la API de Druid usando la informacion del XML y los documentos enlazados.

El flujo está separado en dos capas y mantiene la selección de licitación, lectura de
XML o carpetas `Examples`, descarga de documentos, enlaces internos, Druid, reintentos
y generación de Markdown y PDF.

- **A1 · Referencia inicial:** resumen factual de máximo 100 palabras y 5 viñetas.
- **Capa 1 · Extracción:** A2 Administrativo-legal, A3 Requisitos de solvencia de la
  empresa, A4 Criterios de adjudicación, A6 Requisitos del servicio, A8 Perfiles y
  equipo, A9 Seguridad y protección de datos y A10 Compras, proveedores y colaboradores.
  Recogen datos y reglas del expediente con fuentes; no comparan con la empresa,
  recomiendan, estiman ni generan escenarios.
- **Capa 2 · Procesamiento:** Económico-financiero, Delivery / Operación, Coherencia
  Documental y Riesgos / Go-No-Go. Reciben los siete informes de extracción y los
  metadatos del expediente; distinguen esa información de los datos internos y ficticios.

Consulta la [separación, revisión de prompts y cobertura](docs/capas.md).

## Instalacion

```powershell
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Rellena en `.env` las URLs, el tenant y los identificadores de Druid. Por elección
expresa, el usuario y la contraseña se leen directamente de
`DRUID_USERNAME` y `DRUID_PASSWORD` en `.env` o en el entorno.
Las credenciales locales no se incluyen en Git.

Tambien puedes usar variables permanentes de Windows con `setx`:

```powershell
setx DRUID_AUTH_URL "https://sermicro-dev.druidapcback.druidplatform.com/api/services/app/WebAPIService/ExternalAuthenticate"
setx DRUID_GPT_URL "https://sermicro-dev.druidapcback.druidplatform.com/druidwebview/api/DataSource/PerformOperations"
setx DRUID_TENANT "tu_tenant"
setx DRUID_TENANT_ID "668"
setx DRUID_BOT_ID "8805a55b-9947-47b5-d511-08de9ea71a4f"
setx DRUID_OPERATION_ID "12cbe351-e90c-434d-b931-ea55d3f9c490"
setx DRUID_TIMEOUT_SECONDS "180"
setx DRUID_MAX_RETRIES "3"
setx DRUID_RETRY_BASE_SECONDS "12"
```

Cierra y vuelve a abrir PowerShell despues de usar `setx`.

## Uso

```powershell
python oportunidades.py
```

Por defecto carga `data/sample.xml`, que contiene las 10 licitaciones ficticias originales de software para probar el flujo completo: desarrollo web, IA, cloud, mantenimiento, BI, mobile, ciberseguridad, e-learning, IoT y data lake. Cada licitacion incluye varios documentos, como una licitacion real: pliego administrativo, pliego tecnico y anexo de solvencia. Los anexos mezclan requisitos de equipo y requisitos de experiencia previa de empresa, como numero de proyectos similares, importes, duraciones y ventanas temporales. Los pliegos administrativos incluyen condiciones de participacion, documentacion, sobres, garantias, subcontratacion, lotes, RGPD, confidencialidad, propiedad intelectual, causas de exclusion, criterios de adjudicacion con pesos, formulas, umbrales, topes y mejoras, anexos economico-financieros con presupuesto, formula economica, costes obligatorios, facturacion, anormalidad, penalizaciones, licencias, cloud, personal, hardware, transicion y reversibilidad, y anexos de compras/partners con fabricantes, licencias, cartas, subcontratistas, partners, stock, garantias, logistica, BOM/RFQ y riesgos de suministro. Los pliegos tecnicos incluyen requisitos de Delivery / Operacion como go-live, turnos, cobertura geografica, volumen de tickets, dependencias de cliente, curva de incorporacion, herramientas criticas, stock operativo y readiness, requisitos Service Design / ITIL como SLA, KPI, N1/N2/N3, ITSM, CMDB, transicion, gobierno, reporting, continuidad, seguridad operativa, automatizacion y reversibilidad, ademas de requisitos Seguridad / DPO / ENS como ENS BASICA/MEDIA/ALTA, RGPD, subencargados, cloud, transferencias, logging, incidentes, brechas, SOC/SIEM, desarrollo seguro, auditorias y borrado. Esos documentos estan en `data/ficticios/` y se leen como ficheros locales.

El grupo de ficticios incluye tambien el expediente `LIC-10484` del Banco de España, incorporado desde el XML aportado para pruebas. El XML normalizado se conserva en `data/ficticios/lic-10484.xml`.

Ademas del listado del XML, el menu muestra la opcion `13. Licitaciones reales desde Examples` (su numero se ajusta al total de entradas). Al elegirla, el script lista las carpetas dentro de `Examples/` (por ejemplo `Examples/Licitacion1`) y construye una licitacion real a partir de los PDF/documentos que encuentre en esa carpeta. Primero informa del numero de documentos encontrados en la carpeta elegida y, despues de procesarlos, informa de cuantos documentos adicionales ha leido desde enlaces internos detectados en los documentos.

Para usar otro XML:

```powershell
python oportunidades.py --xml C:\ruta\archivo.xml
```

### Ejecutar únicamente A1 y la capa 1

Desde la carpeta que contiene `oportunidades.py`:

```powershell
python oportunidades.py --capa 1
```

Con un XML distinto:

```powershell
python oportunidades.py --capa 1 --xml C:\ruta\archivo.xml
```

Se conserva el mismo menú, incluida la opción de carpetas reales `Examples`. Ejecuta
A1, A2, A3, A4, A6, A8, A9 y A10, en ese orden. No ejecuta agentes de procesamiento.
Son ocho agentes; los reintentos técnicos de Druid
se conservan para errores de transporte; Compras usa una sola llamada de extracción.

Guarda los ocho Markdown en `extracciones/` dentro de la carpeta de la ejecución,
los JSON individuales en `agentes/` y el único PDF `<expediente>_resumen_legible.pdf`
en la raíz de esa carpeta. El informe conserva fuentes, estados de lectura y avisos.

También genera `<expediente>_capa1.json`, pensado para integrarlo directamente en una
API web. El JSON usa el contrato `oportunidades.capa1.v1` y mantiene este orden fijo:
metadatos del expediente, `documentos_fuente`, `avisos_procesamiento` y `agentes` en
el orden A1, A2, A3, A4, A6, A8, A9 y A10. Cada agente contiene `id`, `nombre`, `orden`,
`tipo`, `estado` y `contenido`. Dentro de `contenido` se incluyen `resumen`,
`secciones`, `pendientes_y_no_localizados`, `trazabilidad` y `salida_original`.
Las tablas se convierten en objetos con `columnas` y `filas`, conservando la secuencia
del informe y los nombres de las columnas. `salida_original` permite recuperar el
texto completo si la web necesita mostrarlo o reprocesarlo.

### Ejecutar las dos capas

```powershell
python oportunidades.py --capa todas
```

Primero se completan los ocho agentes anteriores; después se ejecutan
Económico-financiero, Delivery / Operación, Coherencia Documental y Riesgos / Go-No-Go.
La segunda capa recibe las siete extracciones completas como informes derivados,
con sus fuentes, además de los metadatos y avisos. A1 no sustituye a los especialistas.
Los límites de contexto configurados siguen aplicándose; una extracción parcial
no demuestra que no exista un requisito.

El modo completo añade el JSON consolidado y las respuestas de los agentes de
capa 2 en la misma ejecución. Usa el mismo formato de resumen legible.

## Configuracion

Puedes ajustar estos valores en `.env`:

- `DRUID_AUTH_URL`: endpoint de autenticacion que devuelve `result.accessToken`.
- `DRUID_GPT_URL`: endpoint de la segunda API que ejecuta la consulta GPT en Druid.
- `DRUID_TENANT`: tenant de la primera llamada. Usuario y contraseña se configuran en las constantes del código indicadas arriba.
- `DRUID_TENANT_ID`, `DRUID_BOT_ID`, `DRUID_OPERATION_ID`: identificadores usados en el payload de la segunda llamada.
- `DRUID_TIMEOUT_SECONDS`: timeout enviado a Druid. Por defecto son 180 segundos.
- `DRUID_MAX_RETRIES`: numero maximo de intentos por agente cuando Druid devuelve errores temporales como 504/GatewayTimeout, 502, 503, 429 o timeout de conexion. Por defecto son 3 intentos.
- `DRUID_RETRY_BASE_SECONDS`: espera base entre reintentos. Por defecto son 12 segundos y se aplica espera incremental.
- `MAX_DOCUMENT_CHARS`: limite aproximado de caracteres recopilados al leer documentos antes de preparar los prompts.
- `MAX_PROMPT_DOCUMENT_CHARS`: opcional. Si no se define, no se compacta el texto antes de enviarlo a cada agente.
- `MAX_SUMMARY_PROMPT_DOCUMENT_CHARS`, `MAX_PROFILES_PROMPT_DOCUMENT_CHARS`, `MAX_PROJECTS_PROMPT_DOCUMENT_CHARS`, `MAX_ADMIN_LEGAL_PROMPT_DOCUMENT_CHARS`, `MAX_AWARD_CRITERIA_PROMPT_DOCUMENT_CHARS`, `MAX_ECONOMIC_FINANCIAL_PROMPT_DOCUMENT_CHARS`, `MAX_PURCHASES_PARTNERS_PROMPT_DOCUMENT_CHARS`, `MAX_DELIVERY_OPERATIONS_PROMPT_DOCUMENT_CHARS`, `MAX_SERVICE_DESIGN_ITIL_PROMPT_DOCUMENT_CHARS`, `MAX_SECURITY_DPO_ENS_PROMPT_DOCUMENT_CHARS`: limites opcionales por agente. Usalos solo si Druid devuelve HTTP 500 por tamano de prompt.
- `MAX_COHERENCE_AGENT_OUTPUT_CHARS`: limite de caracteres por salida de agente anterior enviados al A11 Coherencia Documental. Por defecto son 6500 por agente.
- `MAX_GO_NO_GO_AGENT_OUTPUT_CHARS`: limite de caracteres por salida de agente anterior enviados al A13 Go/No-Go. Por defecto son 6000 por agente.
- `MAX_LINK_DEPTH`: profundidad maxima para seguir enlaces encontrados dentro de documentos.
- `ALLOWED_DOCUMENT_HOSTS`: dominios permitidos separados por coma.

Los documentos remotos descargados se cachean en `data/docs/`. Los documentos locales referenciados por el XML, por ejemplo `data/ficticios/opp-sw-001.txt`, se leen directamente desde la carpeta del proyecto.
En licitaciones reales cargadas desde `Examples/`, el script tambien intenta seguir URLs visibles en el texto de los documentos y enlaces embebidos en anotaciones PDF, pero solo procesa enlaces que parezcan documentos descargables, PDF, Word, Excel, ZIP o enlaces oficiales de detalle/perfil de licitacion. Los enlaces institucionales genericos se omiten para reducir ruido, errores 403/404 y carga en Druid.
Cada agente mantiene el indice completo de documentos procesados y, por defecto, envia a Druid todo el texto leido de esos documentos. En capa 1 no compacta el texto. Para agentes de capa 2 puede compactarlo si defines `MAX_PROMPT_DOCUMENT_CHARS` o algun limite especifico por agente. Si Druid devuelve un error temporal, el script reintenta automaticamente el mismo agente. Si aun asi falla, guarda diagnostico en `ultima_respuesta_druid_error.json` dentro de la carpeta de la ejecución.




## Ampliación de viabilidad documental

Los prompts incorporan los campos del documento IA - Fuentes para proyecto VIABILIDAD, repartidos por especialidad. La capa 1 extrae requisitos; la capa 2 los contrasta y procesa. El caso sintético `OPP-SW-011` está disponible en la opción 12 e incluye evidencia interna aislada para comprobar la extracción y las carencias. Consulta [reparto, caso esperado y prueba con Druid](docs/viabilidad.md).

Prueba local: `python comprobar_viabilidad.py`. Prueba real de nueve agentes mediante Druid: `python comprobar_viabilidad.py --live`. Los resultados se guardan en una carpeta nueva, sin sustituir los informes existentes.

Pruebas de separación, prompts, PDF y regresión: `python -m unittest discover -s tests -v`.

La capa 1 usa un prompt por agente con todos los textos extraídos, sin revisión
adicional por materias ni selección de fragmentos. Conserva las reglas ampliadas
dentro de cada prompt. No genera recomendaciones separadas en `--capa 1`.
Son ocho llamadas de extracción, más el redactor y su revisión editorial; pueden
existir reintentos técnicos o editoriales. Los nuevos JSON no incluyen una revisión
documental por fragmentos ni garantizan exhaustividad por superar validaciones formales.

El redactor conserva los detalles extraídos y puede añadir apartados omitidos. Si no
supera los controles, se conserva el diagnóstico y no se publica el nuevo PDF. Para
recuperar omisiones de una extracción antigua hay que repetir `python oportunidades.py
--capa 1`; `--desde-json` solo vuelve a redactar lo que ya contiene ese JSON. Consulta
[cobertura, responsabilidades y controles](docs/cobertura_capa1.md).


## Salidas por ejecución

`python .\oportunidades.py --capa 1` genera el resumen legible con el formato
 de `docs/referencia_resumen_legible.pdf`. Las opciones históricas de formato
 se aceptan por compatibilidad, pero el comando principal produce un único PDF legible.

Cada ejecución crea `resumenes/AAAA-MM-DD_HH-MM-SS_expediente_id/`:

- `*_resumen_legible.pdf`: informe para lectura.
- `*_capa1.json`: extracción completa; también JSON consolidado al ejecutar ambas capas.
- `agentes/`: respuestas JSON individuales.
- `extracciones/`: textos Markdown de los agentes.
- `diagnosticos/`: entrada y respuestas de redacción, incluido `redaccion.json`.
- `ejecucion.json`: identificador, fechas, estado y listado de archivos.

La consola imprime la carpeta de la ejecución. Repetir expediente no sobrescribe salidas.
Una ejecución fallida conserva lo obtenido y queda marcada como fallida.
`--desde-json ruta` copia la entrada en la nueva carpeta y vuelve a redactar;
no repite ni corrige por sí mismo la extracción documental.
Los diagnósticos no son renders temporales: permiten investigar fallos y comprobar
qué información recibió el redactor. No se crean carpetas `temp_render` durante la ejecución normal.

### Requisitos documentales y revisiones contrastadas

Los siete especialistas de capa 1 reciben los documentos completos en una única
llamada cada uno. El registro Markdown con columnas `Materia`, `Requisito completo`
y `Fuente` se conserva como `contenido.requisitos_documentales` en los JSON
individuales y consolidado. El redactor integra esos detalles completos en el cuerpo,
con sus fuentes: una mención en un título o en la conclusión no acredita cobertura.
Esto impide perder requisitos registrados, pero no prueba que el extractor haya
encontrado todos los requisitos del pliego ni valida automáticamente su interpretación.

Para corregir una extracción con una revisión documental explícita:

```powershell
python .\oportunidades.py --desde-json RUTA_JSON --revision-documental RUTA_REVISION_JSON
```

La revisión declara el identificador interno, los PDF revisados y sus SHA-256,
los requisitos, agente responsable, materia, texto profesional y páginas. Se rechaza
si los documentos originales o el expediente no coinciden. La aplicación guarda
el JSON corregido y los individuales, conservando el original sin revisar en
`diagnosticos/extraccion_automatica_sin_revisar.json`; identifica el contenido
corregido como revisión local, sin atribuirlo a la respuesta automática original.
No aplica revisiones por coincidencia de nombre ni las inyecta en otras licitaciones.
En el flujo normal `--capa 1`, tras conservar la extracción automática, se busca una
revisión en `docs/auditorias/` para el identificador y las mismas huellas de los PDF.
Si coincide, la consola lo indica y aplica los JSON corregidos antes de componer el
informe. Cambiar el contenido de los PDF invalida esa reutilización: un nombre o
identificador idéntico no basta. Las extracciones Markdown conservan la respuesta
automática; los JSON publicados identifican expresamente la revisión contrastada.

`docs/auditorias/licitacion1_revision.json` contiene la revisión local de las
15 observaciones de errores y 44 de omisiones de Licitación 1, más ocho
correcciones recibidas el 22/10/2026. Sus 69 registros cubren las 67 observaciones,
con páginas y huellas de los PDF. Las adiciones individualizan ayuda al usuario,
plazo ordinario de transparencia, duración/supervivencia de confidencialidad y
características opcionales valorables en juicio técnico sin puntuación propia,
modalidad SaaS y reparto de operación, propiedad municipal de desarrollos e IA,
obligatoriedad de prórrogas acordadas y plazos completos de cobro. También concreta
el plazo de acreditación de declaraciones sociales a requerimiento. Mantiene expresamente
las discrepancias pendientes, sin resolverlas mediante supuestos. La composición
`registro_contrastado`, con apertura y cierre revisados, conserva ese texto y sus
tablas directamente en el formato profesional del PDF, sin nueva reescritura del
modelo. Puede regenerarse sin autenticación Druid. Esta cobertura se limita a las
observaciones revisadas; no certifica exhaustividad de los pliegos completos.

Si los tres intentos del redactor final devuelven texto que no puede leerse como
JSON, una ejecución con al menos seis agentes puede recuperarse mediante
maquetación local de las extracciones completas. El PDF se identifica desde la
apertura como **dossier de extracción con revisión editorial pendiente** y guarda
el modo de recuperación y el error en `diagnosticos/redaccion/*/composicion.json`.
No se completan fragmentos cortados, no se repiten los agentes ni se realizan
llamadas a otro proveedor de IA. Se conservan todas las celdas de tablas anchas
como fichas y las referencias se imprimen a ancho completo. La recuperación no
se activa para eludir errores semánticos, informes JSON con estructura inválida
o fallos de revisión. La validación de requisitos en el PDF sigue siendo obligatoria.

Los enlaces TED de detalle se descargan por su exportación PDF oficial, conservando
URL de origen y URL de descarga en caché. Una respuesta web vacía no se etiqueta
como documento escaneado o necesidad de OCR sin comprobarlo.

La extracción general utiliza un registro documental común para las siete
especialidades, sin índices de salida contradictorios. Los prompts separan fases,
obligaciones, criterios, unidades, bases de penalización y discrepancias pendientes.
Las páginas numéricas se refuerzan dentro de la misma solicitud completa; las
tablas PDF incorporan además las filas que pueden alinearse por sus coordenadas,
conservando también el texto original. No se fragmenta el trabajo de un agente.

El control de cobertura conserva los registros y también los hechos que un agente
haya dejado en otras tablas o párrafos. Se aplica a los JSON individuales, al
consolidado y al PDF, con procedencia explícita cuando falta una cita individual.
Los sobres JSON completos `Response` se desenvuelven antes de interpretar Markdown.
Estos controles evitan pérdidas entre formatos; no prueban por sí solos que el
modelo haya extraído todo el pliego o interpretado correctamente cada cláusula.

El índice auxiliar de cifras no repite páginas completas: señala su ubicación y
conserva líneas numéricas, mientras los documentos originales siguen íntegros en
la misma solicitud. Ante un HTTP 504, los reintentos aumentan el tiempo interno
de Druid y el tiempo de espera HTTP (hasta 900 segundos, o el valor configurado si
es mayor). Esto no modifica los posibles límites del gateway del servicio.
Los prompts se envían una sola vez mediante `Payload.Messages`. Se comprobó con
la operación configurada que también acepta la petición sin `MessagesJSON`;
enviar ambos duplicaba el tamaño del cuerpo HTTP. Los diagnósticos de error
registran la duración y los tiempos solicitados de cada intento para distinguir
el límite del cliente, el de la operación y un posible límite externo del gateway.
Si `ChatResponse` es inválido, se buscan resultados completos en los mensajes y
argumentos estructurados de esa misma respuesta antes de repetir la llamada.
Si no existe ninguno válido, se archiva la respuesta API íntegra en
`diagnosticos/druid/respuesta_rechazada_*.json`. No se completan textos cortados.
Si Druid indica `finish_reason: length`, se identifica expresamente el límite de
salida, se conserva la respuesta rechazada y el siguiente intento regenera la
extracción completa con control de alcance y de repeticiones. No continúa un
fragmento ni reduce los documentos. A8 se centra en equipo, perfiles, continuidad
y su acreditación; el inventario transversal de solvencia se asigna a A3.
A8 entrega fichas Markdown por perfil y materia con viñetas citadas, evitando la
tabla larga repetitiva. La normalización conserva el nombre del perfil en cada
hecho para no confundir ni deduplicar condiciones iguales de personas distintas.

La revisión editorial identifica las celdas afectadas por las alarmas mediante
IDs, para no confundir la representación de una fila con un texto del JSON.
Como compatibilidad, admite sustituir una fila completa solo si coincide de
forma exacta, es única y conserva el número de celdas. El lector editorial puede
recuperar una conclusión JSON íntegra situada tras una llave de cierre prematura;
no completa valores ni acepta texto truncado. Después siguen siendo obligatorios
los controles de estructura, cobertura documental y fidelidad antes de publicar.

El registro Markdown admite filas abreviadas requisito/fuente únicamente cuando
hay una materia explícita anterior en la misma tabla y una referencia reconocible.
Los separadores vacíos no son requisitos. No se heredan fuentes ni se recortan
columnas adicionales: una fila ambigua se archiva y solicita hasta tres intentos
de extracción completa al mismo agente, conservando todos los documentos. Si no
se resuelve, se detiene con un error controlado y diagnóstico por agente bajo
`diagnosticos/extraccion/`, sin publicar una extracción parcial como válida.

La comprobación del PDF reconoce URLs partidas por la maquetación, permitiendo
solo espacios dentro de la URL y conservando todos sus caracteres. Se registra
un aviso de formato. Si el requisito y su fuente están en el cuerpo pero no se
confirma su coincidencia en el texto extraído del PDF, se permite publicar con
aviso explícito de revisión manual. No se relajan las omisiones del cuerpo, los
rechazos semánticos, la lectura de PDF ni los errores de JSON. Los avisos quedan
en `comprobacion_cobertura.json`, en `validacion_resumen_pdf` del JSON consolidado,
en la redacción y al final del PDF; los recuentos distinguen registros localizados
y pendientes, sin declarar completa una comprobación que no lo sea.
