from __future__ import annotations

import json
from pathlib import Path

from judge.paths import PROBLEMS, WORKSPACE, TEMPLATE_CPP, TEMPLATE_PY, ensure_dirs


class ProblemNotFound(Exception):
    pass


PUBLIC_META = (
    "code",
    "name",
    "points",
    "timeLimit",
    "memoryLimit",
    "tags",
    "partial",
    "author",
)


def _problem_dirs() -> list[Path]:
    if not PROBLEMS.exists():
        return []
    rows = []
    for p in PROBLEMS.iterdir():
        if p.is_dir() and (p / "meta.json").exists():
            rows.append(p)
    return sorted(rows, key=lambda d: (float(meta_of(d).get("points", 0)), d.name))


def meta_of(prob: Path) -> dict:
    raw = json.loads((prob / "meta.json").read_text(encoding="utf-8"))
    raw.setdefault("code", prob.name)
    raw.setdefault("name", prob.name)
    raw.setdefault("points", 1)
    raw.setdefault("timeLimit", 1.0)
    raw.setdefault("memoryLimit", 256)
    raw.setdefault("tags", [])
    raw.setdefault("partial", False)
    return raw


def public_meta(prob: Path) -> dict:
    meta = meta_of(prob)
    return {k: meta.get(k) for k in PUBLIC_META}


def find_problem(code: str) -> Path:
    direct = PROBLEMS / code
    if direct.is_dir() and (direct / "meta.json").exists():
        return direct
    for p in _problem_dirs():
        meta = meta_of(p)
        if meta.get("code") == code or p.name == code:
            return p
    raise ProblemNotFound(f"No existe el problema '{code}'")


def list_problems() -> list[dict]:
    rows = []
    for p in _problem_dirs():
        info = public_meta(p)
        info["slug"] = p.name
        info["has_samples"] = (p / "samples").is_dir()
        rows.append(info)
    return rows


def statement_md(prob: Path) -> str:
    sp = prob / "statement.md"
    if not sp.exists():
        return ""
    return sp.read_text(encoding="utf-8")


def sample_files(prob: Path) -> list[tuple[Path, Path]]:
    samples = prob / "samples"
    if not samples.is_dir():
        return []
    pairs = []
    for inp in sorted(samples.glob("*.in")):
        outp = inp.with_suffix(".out")
        if outp.exists():
            pairs.append((inp, outp))
    return pairs


def official_solution(prob: Path) -> Path:
    secret = prob / "secret"
    for name in ("sol.cpp", "sol.py"):
        cand = secret / name
        if cand.exists():
            return cand
    raise FileNotFoundError(f"Falta la solución oficial en {secret}")


def generator_path(prob: Path) -> Path:
    gen = prob / "secret" / "gen.py"
    if not gen.exists():
        raise FileNotFoundError(f"Falta el generador {gen}")
    return gen


def checker_path(prob: Path) -> Path | None:
    p = prob / "secret" / "checker.py"
    return p if p.exists() else None


def workspace_file(code: str, lang: str) -> Path:
    ensure_dirs()
    ext = "cpp" if lang == "cpp17" else "py"
    return WORKSPACE / f"{code}.{ext}"


def ensure_workspace(code: str, lang: str) -> Path:
    dest = workspace_file(code, lang)
    if not dest.exists():
        src = TEMPLATE_CPP if lang == "cpp17" else TEMPLATE_PY
        dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return dest
