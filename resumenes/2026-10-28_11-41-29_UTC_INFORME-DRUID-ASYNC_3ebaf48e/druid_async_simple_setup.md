# Prueba independiente TEST_ASYNC_SIMPLE

Esta acción todavía debe crearse y publicarse manualmente. Los archivos de este
repositorio no prueban que exista en DRUID. No se ha asignado ningún ID ficticio.

## Configuración exacta

En el tenant **sermicro-dev**, agente **API COIIM**:

1. Crear una acción nueva `TEST_ASYNC_SIMPLE`, activa. Descripción: diagnóstico
   de GenericIntegration sin GPT ni servicios externos. Categoría: diagnóstico.
2. Request Entity y Response Entity: `GPT`, la entidad existente de este agente.
   No activar `Is Response Collection`.
3. Comprobar estos campos, con tipos exactos:

   | Campo | Tipo |
   |---|---|
   | RequestParams | String |
   | RequestHeaders | String |
   | RequestBody | JObject |
   | ResponseBody | JObject |

4. Añadir **una única tarea Custom Code**, petición y respuesta `GPT`:
   `START -> Custom Code -> END`. No debe haber tarea REST, GPT, SQL ni flujo
   de licitaciones. Pegar el contenido completo de
   `docs/druid_async_simple_custom_code.js`.
5. Para esta acción de diagnóstico, revisar las opciones `Reduce Connector Audit
   Logging` y `Disable Connector Audit Full Database Logging`: no activar la
   reducción si se necesitan las entidades de entrada/salida para la inspección.
   No exportar `RequestHeaders` con credenciales al compartir los logs.
6. Guardar y **publicar**. Copiar el ID real de la **acción**, no el ID de la tarea.
7. En Webhooks > Druid del mismo agente, confirmar las URLs que muestra la
   plataforma. El Bot ID debe ser `8805a55b-9947-47b5-d511-08de9ea71a4f`.

La respuesta exacta de `ResponseBody` debe ser:

```json
{"status":"success","message":"PRUEBA_ASYNC_OK","test":"TEST_ASYNC_SIMPLE"}
```

El código usa el patrón oficial GetRequestEntity/SetResponseEntity y asigna un
objeto a ResponseBody. **No** asignar JSON.stringify(...) a un campo JObject.
RequestBody recibe un objeto JSON de prueba; no requiere Messages/toolsJSON.
No leer RequestHeaders en este código ni devolver toda la entidad GPT.

## Ejecución local

La autenticación reutiliza `DRUID_WEBHOOK_TOKEN` y el lector `.env` del proyecto.
No se cambian las credenciales ni se hace login adicional. Los errores de
autenticación se registran, no se resuelven sustituyendo tokens automáticamente.

Sin red:

```powershell
python druid_async_diagnostics.py audit
python druid_async_diagnostics.py prepare
```

Cuando exista la nueva acción, sustituir ID_REAL_PUBLICADO por su ID:

```powershell
python druid_async_diagnostics.py compare --integration-id ID_REAL_PUBLICADO --timeout 120 --interval 10 --observe-404
```

Este comando usa el host y Bot ID de las URLs existentes, cambiando únicamente
el ID de acción y, si se indica, `--entity`. Rechaza los IDs conocidos de las
acciones GPT. Primero ejecuta un POST síncrono. **Solo si coincide la respuesta
fija**, hace un POST asíncrono con el mismo cuerpo. Después solo hace GET.
El UUID diagnosticCorrelationId del cuerpo permite buscar la prueba en las
entidades del audit log; no se presume que sea una correlación interna de DRUID.

El parámetro `--observe-404` autoriza una observación controlada: el 404 no se
clasifica como pendiente, sino HTTP_404_MEANING_UNCONFIRMED. Sin ese parámetro
se conserva la evidencia y se detiene al primer 404. Un timeout local no
confirma que el trabajo siga activo, no lo cancela y no relanza el POST.

Reanudar exclusivamente GET de la nueva prueba:

```powershell
python druid_async_diagnostics.py resume --directory "RUTA_DE_LA_PRUEBA_NUEVA" --timeout 120 --interval 10 --observe-404
```

Se guarda estado.json, sync.json, async_start.json y poll_0001.json... con horas
UTC, URL efectiva, método, parámetros, tiempo, código, cabeceras de respuesta
y cuerpo completo, salvo secretos redactados. Nunca se registran Authorization
de petición, contraseñas ni cookies de respuesta. No se redirige automáticamente.
Si el acuse se pierde, no hay reintento: SUBMISSION_OUTCOME_UNKNOWN.

## Cómo leer el resultado

| Resultado | Evidencia y siguiente paso |
|---|---|
| SYNC_CONTROL_FAILED_ASYNC_NOT_SENT | Resolver creación/publicación/mapeo/entidad/autorización. Todavía no se probó el modo asíncrono. |
| ACKNOWLEDGED_NOT_VERIFIED | Hay un ID; no demuestra creación de trabajo, ejecución ni almacenamiento. |
| RESULT_RETRIEVED | Coincide exactamente la respuesta esperada. Recorrido completo observado para esta acción sin GPT. |
| HTTP_404_MEANING_UNCONFIRMED | Recuperación no encuentra resultado. No se conoce el estado interno del trabajo. |
| HTTP_202_ACCEPTED_RESULT_NOT_PROVEN | HTTP aceptado, sin resultado comprobado. No se traduce a un esquema DRUID inventado. |
| SUCCESS_HTTP_UNKNOWN_BODY | Detener e inspeccionar formato; no tratar cualquier 200 como éxito. |
| FINAL_HTTP_ERROR | Revisar código/cuerpo; incluye 401/403 y redirects no seguidos. |
| RETRYABLE_HTTP_ERROR | Fallo HTTP observado; solo se repiten GET dentro del límite. |
| POLLING_TIMEOUT | Final de la observación local; no equivale a timeout del servidor. |

La documentación dice que existe un estado de ejecución incompleta, pero no
publica su JSON/código exactos. `--verified-pending-status VALOR` solo se usa si
soporte confirma ese valor real del campo status; no tiene valores por defecto.

## ResponseBody y variante opcional

Primero validar la respuesta literal plana. Si la acción simple síncrona falla,
revisar que ResponseBody sea JObject y que request/response usen la misma entidad.
Si la síncrona pasa, eso demuestra la construcción/devolución síncrona del objeto,
**no** su persistencia en el mecanismo asíncrono.

Solo si aporta una variable nueva, crear otra acción independiente, por ejemplo
TEST_ASYNC_SIMPLE_NESTED, con el código de
`docs/druid_async_simple_nested_custom_code.js`. Sigue devolviendo un JObject,
esta vez con el objeto fijo bajo `result`; no es una prueba de tipos String.
Ejecutarla con su propio ID y `--response-shape nested`. No cambiar la acción
primaria ni utilizar las acciones GPT. No es necesario hacerlo si la prueba
plana ya demuestra un fallo antes de ejecutar el Custom Code en el servidor.

## Evidencias que necesita soporte

Pedir búsqueda del invocationId, UTC, Bot ID, action ID, host y correlaciones de
respuesta. Si falta resultado y no hay rastro de tarea, solo DRUID puede comprobar
aceptación, encolado, worker, errores internos y almacenamiento/lectura asociados.
La falta de audit log también puede deberse a filtros, publicación o reducción
de logging; por sí sola no prueba que no existiera ejecución.

No se prueba otro host por deducir el subdominio desde el tenant. Si la plataforma
o soporte facilitan una URL de tenant distinta, registrar esa evidencia y pasar
**ambas URLs exactas** con `--start-url` y `--poll-url`, en otra carpeta. No mezclar
inicio global con recuperación en otro host. La llamada síncrona y la asíncrona
deben conservar el mismo Bot ID y la misma acción.

## Referencias oficiales

- [Contrato GenericIntegration y modo asíncrono](https://docs.druidai.com/1385954/Content/Webhooks/Exchanging%20Data%20with%20External%20Systems.htm#ExecuteAsynchronousIntegrationsLongRunningRequests)
- [Autenticación Webhooks](https://docs.druidai.com/1385954/Content/Webhooks.htm)
- [Acciones, publicación y opciones de auditoría](https://docs.druidai.com/docs/Content/7_Integrations/Defining%20the%20Integration%20Actions.htm)

El mecanismo asíncrono está documentado desde 9.10. Los límites del paso REST y
del LLM deben confirmarse por separado: no se demuestra que asyncResponse=true
elimine el corte del conector GPT. La página general de acciones menciona además
un límite agregado de timeouts de tareas de 250 segundos, mientras la de webhooks
describe trabajos de más de cinco minutos. Confirmar con soporte el alcance por
versión y ruta; no deducir un límite efectivo del tenant a partir de esas frases.
