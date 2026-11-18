(function main() {
    let entity = Context.GetRequestEntity();
    if (entity == null) {
        Context.RaiseError("MissingEntity", "TEST_ASYNC_SIMPLE requires a request entity");
        return;
    }
    entity.ResponseBody = {
        "status": "success",
        "message": "PRUEBA_ASYNC_OK",
        "test": "TEST_ASYNC_SIMPLE"
    };
    Context.SetResponseEntity(entity);
})();
