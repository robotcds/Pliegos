"""Per-invocation output isolation and durable execution status."""
from contextvars import ContextVar
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from uuid import uuid4
import json
import re

_current = ContextVar("output_run", default=None)

def output_directory(root, category=None):
    run = _current.get()
    directory = run[0] if run else Path(root) / "resumenes"
    if category and run:
        directory /= category
    directory.mkdir(parents=True, exist_ok=True)
    return directory

def execution_id():
    run = _current.get()
    return run[1]["id"] if run else uuid4().hex


def has_active_run():
    return _current.get() is not None

def begin_run(root, expediente, mode):
    identifier = uuid4().hex
    name = re.sub(r"[^\w.-]+", "_", str(expediente)).strip("._")[:100] or "sin_expediente"
    directory = Path(root) / "resumenes" / (datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "_" + name + "_" + identifier[:8])
    directory.mkdir(parents=True, exist_ok=False)
    record = {"id": identifier, "expediente": expediente, "modo": mode,
              "inicio": datetime.now().astimezone().isoformat(), "estado": "en_curso"}
    _current.set((directory, record))
    _save(directory, record)
    print(f"Carpeta de esta ejecución: {directory}")
    return directory


def resume_run(directory, expediente, mode):
    directory = Path(directory).expanduser().resolve()
    record = json.loads((directory / 'ejecucion.json').read_text(encoding='utf-8'))
    if record['expediente'] != expediente or record['modo'] != mode:
        raise ValueError('La ejecución a reanudar pertenece a otro expediente o capa')
    record['estado'] = 'en_curso'
    record.pop('fin', None)
    record.pop('error_tipo', None)
    record['reanudaciones'] = record.get('reanudaciones', 0) + 1
    _current.set((directory, record))
    _save(directory, record)
    print(f'Reanudando ejecución: {directory}')
    return directory

def _save(directory, record):
    target = directory / "ejecucion.json"
    temporary = target.with_suffix(".tmp")
    temporary.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(target)

@contextmanager
def output_session():
    token = _current.set(None)
    try:
        yield
    except BaseException as exc:
        run = _current.get()
        if run:
            run[1]["estado"] = "fallida"
            run[1]["error_tipo"] = type(exc).__name__
        raise
    finally:
        run = _current.get()
        try:
            if run:
                directory, record = run
                if record["estado"] == "en_curso":
                    record["estado"] = "completada"
                record["fin"] = datetime.now().astimezone().isoformat()
                record["archivos"] = sorted(str(p.relative_to(directory)) for p in directory.rglob("*") if p.is_file() and p.name != "ejecucion.json")
                _save(directory, record)
        finally:
            _current.reset(token)
