# Prueba de Druid asíncrono

## Investigación sin GPT del 28 de octubre de 2026

La siguiente prueba debe usar una acción nueva `TEST_ASYNC_SIMPLE`, sin tareas
GPT ni REST. La configuración exacta y los comandos están en
[druid_async_simple_setup.md](druid_async_simple_setup.md).
El cliente nuevo `druid_async_diagnostics.py` no sustituye este probe antiguo:
el probe antiguo exige resultados DataSource/GPT y no acepta la respuesta fija
de la nueva acción. No ejecutar esa acción con el probe antiguo.

El cliente nuevo distingue acuse, 404 sin significado confirmado, formato
desconocido y resultado comprobado; permite comparar los dos modos y reanudar
solo los GET. La comparación real se ejecutó el 28/10/2026 con la acción creada
por el usuario, ID `a01aac92-01d1-40b9-8959-1937189f4d4c`. Síncrona: 200 con objeto
fijo; asíncrona: ID `bc9e5288-b855-4d44-92c6-b39dfbdcb15a` y 404 persistente en
recuperación. La auditoría aportada por el usuario muestra ResponseBody correcto
en ambos modos. El fallo se acota a entrega, persistencia, asociación o lectura
del resultado, sin atribuir todavía una causa interna concreta. No se cambió
el flujo principal.

La documentación oficial de Webhooks también admite tokens temporales del
endpoint ExternalAuthenticate para la cuenta de servicio indicada allí; no debe
interpretarse que todo token obtenido mediante ese endpoint sea inválido.
Se conserva el token de Webhooks configurado, sin renovar ni cambiar credenciales.

Estado: cliente experimental independiente. No cambia `oportunidades.py`, sus
credenciales, prompts ni las ejecuciones actuales. Estado de las pruebas reales:
GenericIntegration síncrono devuelve `PRUEBA_ASYNC_OK`; en modo asíncrono se recibe
un ID pero GetGenericIntegrationResponse devuelve 404 incluso después de esperar.
El recorrido asíncrono aún no está validado.

Copia confirmada mediante export del usuario: `AskGPT-agent-V4-Webhook-Test`,
ID `7a7e7161-2347-47d9-8134-b869a15c5210`. Conserva la entidad `GPT` y el orden
`misc` -> `gpt` -> `add response`, con ambos adaptadores de webhook guardados.
Las URLs y el token de Webhooks ya están en el `.env` local. No compartir el token.
La entidad necesitaba campos del webhook; tras crearlos, la llamada síncrona al
clon funciona. Se ha preparado un diagnóstico sin credenciales en la ejecución
`2026-10-23_12-58-12_PRUEBA-DRUID-ASYNC_8bb24c1b/diagnostico_para_druid.json`.

La exportación recibida identifica:

- Acción: `AskGPT-agent-V4`, ID `12cbe351-e90c-434d-b931-ea55d3f9c490`.
- Entidad: `GPT`, ID `42ebcd3f-8472-4e5d-8b75-768b87b33d6a`.
- Orden real: `misc` -> `gpt` -> `add response` (lo define `nextTasks`).
- El paso REST `gpt` utiliza el gateway de Druid, deployment `gpt-4.1`,
  `max_tokens: 15000`, herramientas y `tool_choice: required`.
- La exportación no muestra un timeout configurable del paso REST. No demuestra
  dónde está el corte de 100 s ni que el modo asíncrono lo elimine.
- No contiene lectura de `RequestBody` ni escritura de `ResponseBody`.

## Preparación en Druid

Trabajar sobre una **copia de la acción**, por ejemplo `AskGPT-agent-V4-Webhook-Test`.
Mantener la conexión REST existente y su autenticación configurada en Druid.
No cambiar todavía la acción que usa producción.

Verificar en la entidad `GPT` los campos requeridos por Webhooks:

| Campo | Tipo |
|---|---|
| RequestParams | String |
| RequestBody | JObject |
| RequestHeaders | String |
| ResponseBody | JObject |

Si no existen, un administrador deberá crearlos. Las siguientes expresiones son
propuestas para esa copia; deben guardarse y validarse en el editor de Druid.
No son un export listo para importar: los IDs de la copia los asigna la plataforma.

Sustituir la expresión del paso **misc** por:

```javascript
(function main() {
    let entity = Context.GetRequestEntity();
    if (entity == null || entity.RequestBody == null) {
        Context.RaiseError("MissingRequest", "Falta RequestBody");
        return;
    }
    let body = entity.RequestBody;
    if (typeof body === "string") body = JSON.parse(body);
    if (body.Messages == null || body.Messages.items == null || body.toolsJSON == null) {
        Context.RaiseError("InvalidRequest", "Se requieren Messages.items y toolsJSON");
        return;
    }
    entity.MessagesJSON = [];
    for (let i = 0; i < body.Messages.items.length; i++) {
        let message = body.Messages.items[i];
        entity.MessagesJSON.push({ role: message.Role, content: message.Content });
    }
    entity.toolsJSON = body.toolsJSON;
    entity.responseJSON = null;
    entity.finish_reason = null;
    entity.ResponseBody = null;
    Context.SetResponseEntity(entity);
})();
```

El paso REST **gpt** y sus mapeos de `MessagesJSON`, `toolsJSON`, `responseJSON`
y `finish_reason` se conservan. Este contrato solo necesita los mensajes iniciales
system/user del programa, no conversaciones de herramientas de varios turnos.

Sustituir la expresión del último paso **add response** por:

```javascript
(function main() {
    let entity = Context.GetResponseEntity();
    if (entity == null || entity.responseJSON == null) {
        Context.RaiseError("MissingGPTResponse", "El paso GPT no devolvió responseJSON");
        return;
    }
    entity.ResponseBody = {
        DataSource: {
            finish_reason: entity.finish_reason,
            responseJSON: entity.responseJSON
        }
    };
    entity.MessagesJSON = null;
    Context.SetResponseEntity(entity);
})();
```

Esto devuelve solo el resultado; no se devuelve toda la entidad ni `RequestHeaders`.
Se conserva `finish_reason`, incluido `length`, para que Python rechace truncamientos.
El ID que debe ir en la URL es el de **la copia**, no el de la acción original.

## Configuración local

Añadir a `.env` (sin compartir el token):

```dotenv
DRUID_ASYNC_START_URL=https://druidendpoints.druidplatform.com/api/Druid/8805a55b-9947-47b5-d511-08de9ea71a4f/GPT/ID_REAL_DE_LA_COPIA/GenericIntegration
DRUID_ASYNC_POLL_URL=https://druidendpoints.druidplatform.com/api/Druid/8805a55b-9947-47b5-d511-08de9ea71a4f/GetGenericIntegrationResponse
DRUID_WEBHOOK_TOKEN=
```

El token se obtiene de **Webhooks > Authentication**. No se asume que sirva el
token de `ExternalAuthenticate`. La URL debe copiarse del bot correcto: la de
la captura es una base conocida, no una comprobación de permisos o publicación.

## Prueba

Desde la carpeta del proyecto:

```powershell
python druid_async_probe.py --preparar
python druid_async_probe.py
```

El primer comando guarda un mensaje mínimo sin red. El segundo hace **una llamada
real a GPT a través de Druid**, con respuesta esperada `PRUEBA_ASYNC_OK`.
Guarda entrada, acuse, consultas y resultado bajo `resumenes/..._PRUEBA-DRUID-ASYNC_...`.
No genera un PDF ni una extracción de licitación validada.

Para una petición completa después de validar el transporte:

```powershell
python druid_async_probe.py --entrada "RUTA_AL_JSON_DE_ENTRADA_GPT" --espera 900
```

El JSON contiene la entidad GPT (`Messages.items`, `toolsJSON`), no el sobre
`TenantId/Operations/Payload` de PerformOperations ni respuestas de ejecuciones pasadas.
No se fragmentan los documentos. El modelo y límite de salida se configuran en Druid.

Para continuar consultando una invocación existente sin repetir el POST:

```powershell
python druid_async_probe.py --reanudar "RUTA_A_LA_CARPETA_DE_PRUEBA" --espera 900
```

No se reintenta automáticamente el inicio: si se pierde el acuse, puede haber un
trabajo en marcha. Revisar el log de Druid antes de lanzar otro. Los GET transitorios
se repiten sobre el mismo ID. Un timeout local no cancela la integración remota.

## Contrato por confirmar

La documentación especifica `invocationId`, estados pendientes y `ResponseBody`,
pero no fija el JSON exacto de los sobres de todos los tenants. El cliente admite
el acuse `{ "invocationId": "..." }` o un GUID en texto plano (formato observado
en este tenant), pendientes HTTP 202 o estados textuales habituales y el resultado
anterior directo o dentro de `ResponseBody`.
Estos estados son compatibilidad provisional, **no una afirmación sobre este tenant**.
Ante otro formato, archiva y se detiene. Necesitamos las respuestas reales para
ajustarlo; nunca trata un acuse o estado desconocido como resultado del agente.

Después de una prueba corta, probar A9 con la misma entrada completa y verificar
si supera 100 segundos sin cancelación. No dar por resuelto el timeout del gateway
ni las repeticiones del modelo solo porque se reciba un invocationId.

Fuente: https://docs.druidai.com/1385954/Content/Webhooks/Exchanging%20Data%20with%20External%20Systems.htm#ExecuteAsynchronousIntegrationsLongRunningRequests
