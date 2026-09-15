from __future__ import annotations

import importlib.util
from pathlib import Path

from judge import core, generate, pack
from judge.paths import CACHE, ensure_dirs


def norm_out(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def default_equal(got: str, expected: str) -> bool:
    return norm_out(got) == norm_out(expected)


def _load_checker(path: Path):
    spec = importlib.util.spec_from_file_location(f"lmoj_checker_{path.parent.parent.name}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No pude cargar {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "check"):
        raise RuntimeError(f"{path} debe definir check(entrada, esperado, obtenido)")
    return mod.check


def compare(prob: Path, inp: str, expected: str, got: str) -> tuple[bool, str]:
    checker = pack.checker_path(prob)
    if checker is None:
        ok = default_equal(got, expected)
        return ok, "" if ok else "WA"
    fn = _load_checker(checker)
    result = fn(inp, expected, got)
    if isinstance(result, bool):
        return result, "" if result else "WA"
    ok, msg = result
    return bool(ok), str(msg)


def run_submission(
    prob: Path,
    source: str,
    lang: str,
    *,
    sample_only: bool = False,
) -> dict:
    ensure_dirs()
    meta = pack.meta_of(prob)
    tl = float(meta.get("timeLimit", 1.0))
    mem = int(meta.get("memoryLimit", 256))
    src = pack.ensure_workspace(meta.get("code", prob.name), lang)
    src.write_text(source, encoding="utf-8")

    work = CACHE / "_run" / prob.name
    work.mkdir(parents=True, exist_ok=True)
    bin_path = work / "user"
    try:
        argv = core.prepare_lang(lang, src, bin_path)
    except core.CompileError as e:
        return {
            "verdict": "CE",
            "compile_error": e.message,
            "cases": [],
            "passed": 0,
            "total": 0,
            "time_limit": tl,
            "memory_limit": mem,
            "lang": lang,
            "max_time": 0.0,
            "points_awarded": 0,
            "sample_only": sample_only,
        }

    tests: list[tuple[str, str, str, bool]] = []
    for inp, outp in pack.sample_files(prob):
        tests.append(
            (
                inp.stem,
                inp.read_text(encoding="utf-8"),
                outp.read_text(encoding="utf-8"),
                True,
            )
        )
    if not sample_only:
        try:
            for name, inp, out in generate.hidden_payload(prob):
                tests.append((name, inp, out, False))
        except Exception as e:
            return {
                "verdict": "SE",
                "compile_error": f"Error del pack (generador/oficial): {e}",
                "cases": [],
                "passed": 0,
                "total": 0,
                "time_limit": tl,
                "memory_limit": mem,
                "lang": lang,
                "max_time": 0.0,
                "points_awarded": 0,
                "sample_only": sample_only,
            }

    if not tests:
        return {
            "verdict": "SE",
            "compile_error": "El problema no tiene samples ni generador.",
            "cases": [],
            "passed": 0,
            "total": 0,
            "time_limit": tl,
            "memory_limit": mem,
            "lang": lang,
            "max_time": 0.0,
            "points_awarded": 0,
            "sample_only": sample_only,
        }

    run_mem = core.memory_for_lang(lang, mem)
    cases = []
    passed = 0
    fail = None
    max_time = 0.0
    for name, inp, expected, is_sample in tests:
        stdout, stderr, code, dt = core.run_program(
            argv, inp, tl=tl, memory_mb=run_mem
        )
        max_time = max(max_time, dt)
        row = {
            "name": name,
            "sample": is_sample,
            "time": round(dt, 3),
            "verdict": "AC",
            "expected": "",
            "got": "",
            "stderr": "",
            "input_preview": "",
            "checker": "",
        }
        if code == -9:
            row["verdict"] = "TLE"
            fail = fail or "TLE"
        elif code == -11 or "MLE" in (stderr or "") or code in (-6, 137):
            row["verdict"] = "MLE"
            fail = fail or "MLE"
        elif code != 0:
            row["verdict"] = "RE"
            row["stderr"] = (stderr or "")[:800]
            fail = fail or "RE"
        else:
            ok, msg = compare(prob, inp, expected, stdout)
            if ok:
                row["verdict"] = "AC"
                passed += 1
            else:
                row["verdict"] = "WA"
                row["checker"] = msg
                fail = fail or "WA"
                if is_sample:
                    row["input_preview"] = inp[:2000]
                    row["expected"] = norm_out(expected)[:4000]
                    row["got"] = norm_out(stdout)[:4000]
                else:
                    row["got"] = ""
                    row["expected"] = ""

        if is_sample and row["verdict"] != "AC" and not row["input_preview"]:
            row["input_preview"] = inp[:2000]
            row["expected"] = norm_out(expected)[:4000]
            row["got"] = norm_out(stdout)[:4000]
            if stderr:
                row["stderr"] = stderr[:800]

        cases.append(row)

    total = len(tests)
    if fail is None and passed == total:
        verdict = "AC"
    else:
        verdict = fail or "WA"

    points = int(meta.get("points", 1))
    if sample_only:
        awarded = 0
    elif verdict == "AC":
        awarded = points
    elif meta.get("partial") and total:
        awarded = int(points * passed / total)
    else:
        awarded = 0

    return {
        "verdict": verdict,
        "compile_error": None,
        "cases": cases,
        "passed": passed,
        "total": total,
        "time_limit": tl,
        "memory_limit": mem,
        "lang": lang,
        "max_time": round(max_time, 3),
        "points_awarded": awarded,
        "sample_only": sample_only,
        "problem": meta.get("code", prob.name),
        "points": points,
    }
