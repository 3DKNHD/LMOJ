from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
DATA = ROOT / "data"
WORKSPACE = ROOT / "workspace"
CACHE = DATA / "cache"
CONFIG_PATH = ROOT / "config.json"
TEMPLATE_CPP = ROOT / "template.cpp"
TEMPLATE_PY = ROOT / "template.py"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {
            "site_name": "LMOJ",
            "host": "127.0.0.1",
            "port": 5050,
        }
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def save_config(cfg: dict) -> None:
    CONFIG_PATH.write_text(
        json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def ensure_dirs() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)
