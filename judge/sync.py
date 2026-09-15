from __future__ import annotations

import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from judge.paths import PROBLEMS, ROOT, load_config, save_config


class SyncError(Exception):
    pass


def _git(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd or ROOT),
        capture_output=True,
        text=True,
    )


def last_sync_info() -> dict:
    stamp = PROBLEMS / ".sync-stamp"
    cfg = load_config()
    info = {
        "pack_url": cfg.get("pack_url") or "",
        "pack_branch": cfg.get("pack_branch") or "main",
        "is_clone": (PROBLEMS / ".git").is_dir(),
        "last": None,
        "head": None,
        "message": None,
    }
    if stamp.exists():
        info["last"] = stamp.read_text(encoding="utf-8").strip()
    if info["is_clone"]:
        r = _git("rev-parse", "--short", "HEAD", cwd=PROBLEMS)
        if r.returncode == 0:
            info["head"] = r.stdout.strip()
        m = _git("log", "-1", "--pretty=%s", cwd=PROBLEMS)
        if m.returncode == 0:
            info["message"] = m.stdout.strip()
    return info


def set_pack_url(url: str, branch: str = "main") -> None:
    cfg = load_config()
    cfg["pack_url"] = url.strip()
    cfg["pack_branch"] = branch.strip() or "main"
    save_config(cfg)


def _stamp() -> None:
    PROBLEMS.mkdir(parents=True, exist_ok=True)
    (PROBLEMS / ".sync-stamp").write_text(
        datetime.now().isoformat(timespec="seconds") + "\n", encoding="utf-8"
    )


def _count_problems(root: Path) -> int:
    if not root.exists():
        return 0
    return sum(1 for p in root.iterdir() if p.is_dir() and (p / "meta.json").exists())


def _pull(branch: str) -> None:
    fetch = _git("fetch", "origin", branch, cwd=PROBLEMS)
    if fetch.returncode != 0:
        raise SyncError(fetch.stderr.strip() or fetch.stdout.strip())
    pull = _git("merge", "--ff-only", f"origin/{branch}", cwd=PROBLEMS)
    if pull.returncode != 0:
        raise SyncError(pull.stderr.strip() or pull.stdout.strip())


def _clone_into_problems(url: str, branch: str) -> None:
    parent = PROBLEMS.parent
    backup = parent / ".problems-bundled"
    if backup.exists():
        shutil.rmtree(backup)
    had_local = PROBLEMS.exists()
    if had_local:
        PROBLEMS.rename(backup)
    clone = _git("clone", "--branch", branch, url, str(PROBLEMS))
    if clone.returncode != 0:
        if had_local and backup.exists():
            backup.rename(PROBLEMS)
        raise SyncError(clone.stderr.strip() or clone.stdout.strip())
    if backup.exists():
        for child in backup.iterdir():
            if child.name.startswith("."):
                continue
            dest = PROBLEMS / child.name
            if dest.exists():
                continue
            if child.is_dir():
                shutil.copytree(child, dest)
            else:
                shutil.copy2(child, dest)
        shutil.rmtree(backup, ignore_errors=True)


def sync_pack(url: str | None = None, branch: str | None = None) -> dict:
    """Baja o actualiza el pack de problemas desde GitHub."""
    cfg = load_config()
    url = (url or cfg.get("pack_url") or "").strip()
    branch = (branch or cfg.get("pack_branch") or "main").strip()
    if not url:
        raise SyncError(
            "No hay URL de pack. Pon pack_url en config.json o usa: ./lmoj sync <url>"
        )
    set_pack_url(url, branch)

    git_dir = PROBLEMS / ".git"
    if git_dir.is_dir():
        remote = _git("remote", "get-url", "origin", cwd=PROBLEMS)
        if remote.returncode == 0 and remote.stdout.strip() != url:
            _git("remote", "set-url", "origin", url, cwd=PROBLEMS)
        _pull(branch)
        mode = "pull"
    else:
        _clone_into_problems(url, branch)
        mode = "clone"

    _stamp()
    info = last_sync_info()
    info["updated"] = True
    info["mode"] = mode
    info["problems"] = _count_problems(PROBLEMS)
    return info
