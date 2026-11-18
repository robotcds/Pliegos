// Optional independent action for a controlled serialization comparison.
// Keep the primary TEST_ASYNC_SIMPLE action unchanged.
(function main() {
    let entity = Context.GetRequestEntity();
    if (entity == null) {
        Context.RaiseError("MissingEntity", "A request entity is required");
        return;
    }
    entity.ResponseBody = {
        "result": {
            "status": "success",
            "message": "PRUEBA_ASYNC_OK",
            "test": "TEST_ASYNC_SIMPLE"
        }
    };
    Context.SetResponseEntity(entity);
})();
