from __future__ import annotations

import hashlib
import importlib.util
import json
import threading
from pathlib import Path

from judge import core, pack
from judge.paths import CACHE

_LOCKS: dict[str, threading.Lock] = {}
_LOCKS_GUARD = threading.Lock()


def _lock(slug: str) -> threading.Lock:
    with _LOCKS_GUARD:
        if slug not in _LOCKS:
            _LOCKS[slug] = threading.Lock()
        return _LOCKS[slug]


def _digest(paths: list[Path]) -> str:
    h = hashlib.sha256()
    for p in sorted(paths, key=lambda x: str(x)):
        h.update(p.name.encode())
        h.update(p.read_bytes())
    return h.hexdigest()[:16]


def _load_generate(gen: Path):
    spec = importlib.util.spec_from_file_location(f"lmoj_gen_{gen.parent.parent.name}", gen)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No pude cargar {gen}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "generate"):
        raise RuntimeError(f"{gen} debe definir generate() que produzca (nombre, entrada)")
    return mod.generate


def _safe_name(name: str, used: set[str]) -> str:
    raw = "".join(ch if ch.isalnum() or ch in "-_" else "-" for ch in name.strip()) or "case"
    base = raw[:40]
    cand = base
    i = 2
    while cand in used:
        cand = f"{base}-{i}"
        i += 1
    used.add(cand)
    return cand


def generate_hidden(prob: Path) -> list[dict]:
    """Genera casos ocultos con el gen.py del problema y la solución oficial.

    No deja .in copiables en la carpeta del problema: todo vive en data/cache.
    """
    slug = prob.name
    with _lock(slug):
        return _generate_hidden_locked(prob)


def _generate_hidden_locked(prob: Path) -> list[dict]:
    gen = pack.generator_path(prob)
    official = pack.official_solution(prob)
    key = _digest([gen, official, prob / "meta.json"])
    dest = CACHE / prob.name / key
    manifest = dest / "manifest.json"
    if manifest.exists():
        data = json.loads(manifest.read_text(encoding="utf-8"))
        return data["cases"]

    dest.mkdir(parents=True, exist_ok=True)
    produce = _load_generate(gen)
    used: set[str] = set()
    raw_cases = []
    for item in produce():
        if not isinstance(item, (tuple, list)) or len(item) != 2:
            raise RuntimeError("generate() debe producir pares (nombre, texto_de_entrada)")
        name, text = item
        if not isinstance(text, str):
            raise RuntimeError(f"La entrada de '{name}' no es texto")
        raw_cases.append((_safe_name(str(name), used), text))

    if not raw_cases:
        raise RuntimeError(f"{gen} no produjo ningún caso")

    meta = pack.meta_of(prob)
    tl = float(meta.get("timeLimit", 1.0))
    mem = int(meta.get("memoryLimit", 256))
    lang = "cpp17" if official.suffix == ".cpp" else "py3"
    bin_path = dest / "official"
    argv = core.prepare_lang(lang, official, bin_path)
    run_mem = core.memory_for_lang(lang, mem)

    cases = []
    for name, text in raw_cases:
        stdout, stderr, code, dt = core.run_program(
            argv, text, tl=max(tl * 2, 2.0), memory_mb=run_mem
        )
        if code == -9:
            raise RuntimeError(f"La solución oficial TLE en caso oculto '{name}'")
        if code != 0:
            raise RuntimeError(
                f"La solución oficial falló en '{name}' (exit {code})\n{stderr[:400]}"
            )
        inp_path = dest / f"{name}.in"
        out_path = dest / f"{name}.out"
        inp_path.write_text(text, encoding="utf-8")
        out_path.write_text(stdout, encoding="utf-8")
        cases.append(
            {
                "name": name,
                "in": str(inp_path.relative_to(CACHE)),
                "out": str(out_path.relative_to(CACHE)),
                "official_time": round(dt, 4),
            }
        )

    payload = {"key": key, "cases": cases}
    manifest.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return cases


def hidden_payload(prob: Path) -> list[tuple[str, str, str]]:
    rows = []
    for case in generate_hidden(prob):
        inp = (CACHE / case["in"]).read_text(encoding="utf-8")
        out = (CACHE / case["out"]).read_text(encoding="utf-8")
        rows.append((case["name"], inp, out))
    return rows
