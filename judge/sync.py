from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path

from judge.paths import DATA, PROBLEMS, ROOT


class SyncError(Exception):
    pass


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )


def _count_problems(root: Path) -> int:
    if not root.exists():
        return 0
    return sum(1 for p in root.iterdir() if p.is_dir() and (p / "meta.json").exists())


def _count_editorials(root: Path) -> int:
    if not root.exists():
        return 0
    return sum(1 for p in root.iterdir() if p.is_dir() and (p / "editorial.md").is_file())


def _remote_url() -> str:
    r = _git("remote", "get-url", "origin")
    if r.returncode != 0:
        return ""
    return r.stdout.strip()


def _current_branch() -> str:
    r = _git("rev-parse", "--abbrev-ref", "HEAD")
    if r.returncode != 0:
        return ""
    return r.stdout.strip()


def _tracking() -> tuple[str, str]:
    up = _git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}")
    if up.returncode == 0:
        ref = up.stdout.strip()
        if "/" in ref:
            remote, branch = ref.split("/", 1)
            return remote, branch
    branch = _current_branch()
    if not branch or branch == "HEAD":
        raise SyncError(
            "No hay rama con tracking. Cambia a main (u otra rama) y vuelve a sync."
        )
    return "origin", branch


def last_sync_info() -> dict:
    stamp = DATA / ".sync-stamp"
    info = {
        "remote": _remote_url(),
        "branch": _current_branch(),
        "is_git": (ROOT / ".git").is_dir(),
        "last": None,
        "head": None,
        "message": None,
        "problems": _count_problems(PROBLEMS),
        "editorials": _count_editorials(PROBLEMS),
    }
    if stamp.exists():
        info["last"] = stamp.read_text(encoding="utf-8").strip()
    if info["is_git"]:
        r = _git("rev-parse", "--short", "HEAD")
        if r.returncode == 0:
            info["head"] = r.stdout.strip()
        m = _git("log", "-1", "--pretty=%s")
        if m.returncode == 0:
            info["message"] = m.stdout.strip()
    return info


def _stamp() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / ".sync-stamp").write_text(
        datetime.now().isoformat(timespec="seconds") + "\n", encoding="utf-8"
    )


def sync_repo() -> dict:
    """Trae lo último del remote origin: problemas, editoriales y el resto del juez."""
    if not (ROOT / ".git").is_dir():
        raise SyncError("Este directorio no es un clone git.")
    url = _remote_url()
    if not url:
        raise SyncError(
            "No hay remote origin. Configúralo con: git remote add origin <url>"
        )

    before_p = _count_problems(PROBLEMS)
    before_e = _count_editorials(PROBLEMS)

    remote, branch = _tracking()
    fetch = _git("fetch", remote, branch)
    if fetch.returncode != 0:
        raise SyncError(fetch.stderr.strip() or fetch.stdout.strip())
    pull = _git("merge", "--ff-only", f"{remote}/{branch}")
    if pull.returncode != 0:
        raise SyncError(pull.stderr.strip() or pull.stdout.strip())

    _stamp()
    info = last_sync_info()
    info["updated"] = True
    info["mode"] = "pull"
    info["new_problems"] = info["problems"] - before_p
    info["new_editorials"] = info["editorials"] - before_e
    return info
