from __future__ import annotations

import os
import resource
import subprocess
import time
from pathlib import Path

CXX = os.environ.get("CXX", "g++")
CXXFLAGS = ["-std=c++17", "-O2", "-pipe", "-Wall", "-Wextra", "-Wshadow"]
PYTHON = os.environ.get("PYTHON", "python3")


class CompileError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


def compile_cpp(src: Path, bin_path: Path) -> None:
    bin_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [CXX, *CXXFLAGS, "-o", str(bin_path), str(src)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise CompileError((r.stderr or r.stdout).strip())


def _preexec(memory_bytes: int, cpu_sec: int):
    def inner() -> None:
        try:
            resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        except (ValueError, resource.error):
            pass
        try:
            resource.setrlimit(resource.RLIMIT_CPU, (cpu_sec, cpu_sec))
        except (ValueError, resource.error):
            pass
        if memory_bytes > 0:
            try:
                resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))
            except (ValueError, resource.error):
                pass

    return inner


def run_program(
    argv: list[str],
    stdin_data: str,
    *,
    tl: float,
    memory_mb: int,
) -> tuple[str, str, int, float]:
    cpu_sec = max(1, int(tl) + 1)
    mem = max(0, memory_mb) * 1024 * 1024
    t0 = time.perf_counter()
    try:
        r = subprocess.run(
            argv,
            input=stdin_data,
            capture_output=True,
            text=True,
            timeout=tl + 0.3,
            preexec_fn=_preexec(mem, cpu_sec),
        )
        dt = time.perf_counter() - t0
        return r.stdout, r.stderr, r.returncode, dt
    except subprocess.TimeoutExpired:
        dt = time.perf_counter() - t0
        return "", "", -9, dt
    except MemoryError:
        dt = time.perf_counter() - t0
        return "", "MLE", -11, dt


def lang_argv(lang: str, src: Path, bin_path: Path) -> list[str]:
    if lang == "cpp17":
        return [str(bin_path)]
    if lang == "py3":
        return [PYTHON, "-u", str(src)]
    raise ValueError(f"Lenguaje no soportado: {lang}")


def prepare_lang(lang: str, src: Path, bin_path: Path) -> list[str]:
    if lang == "cpp17":
        compile_cpp(src, bin_path)
        return [str(bin_path)]
    if lang == "py3":
        return [PYTHON, "-u", str(src)]
    raise ValueError(f"Lenguaje no soportado: {lang}")


def memory_for_lang(lang: str, memory_mb: int) -> int:
    if lang == "py3":
        return memory_mb + 128
    return memory_mb
