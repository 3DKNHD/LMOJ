from __future__ import annotations

import json
from datetime import datetime

from judge.paths import DATA, ensure_dirs

DB = DATA / "db.json"


def _empty() -> dict:
    return {"next_id": 1, "submissions": [], "best": {}}


def load_db() -> dict:
    ensure_dirs()
    if not DB.exists():
        return _empty()
    return json.loads(DB.read_text(encoding="utf-8"))


def save_db(db: dict) -> None:
    ensure_dirs()
    DB.write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def record_submission(problem: str, lang: str, source: str, result: dict) -> dict:
    db = load_db()
    sid = int(db.get("next_id", 1))
    row = {
        "id": sid,
        "problem": problem,
        "lang": lang,
        "when": datetime.now().isoformat(timespec="seconds"),
        "verdict": result["verdict"],
        "passed": result.get("passed", 0),
        "total": result.get("total", 0),
        "time": result.get("max_time", 0),
        "points_awarded": result.get("points_awarded", 0),
        "sample_only": result.get("sample_only", False),
        "source": source,
        "cases": result.get("cases", []),
        "compile_error": result.get("compile_error"),
    }
    db["submissions"].insert(0, row)
    db["next_id"] = sid + 1
    if result.get("verdict") == "AC" and not result.get("sample_only"):
        db.setdefault("best", {})[problem] = {
            "verdict": "AC",
            "submission": sid,
            "when": row["when"],
            "points": result.get("points", 0),
        }
    save_db(db)
    return row


def submissions(limit: int | None = None, problem: str | None = None) -> list[dict]:
    rows = load_db().get("submissions", [])
    if problem:
        rows = [r for r in rows if r.get("problem") == problem]
    if limit is not None:
        rows = rows[:limit]
    return rows


def get_submission(sid: int) -> dict | None:
    for row in load_db().get("submissions", []):
        if int(row["id"]) == sid:
            return row
    return None


def best_map() -> dict:
    return load_db().get("best", {})


def points_total(problems: list[dict]) -> tuple[int, int]:
    best = best_map()
    got = 0
    total = 0
    for p in problems:
        pts = int(p.get("points", 0))
        total += pts
        code = p.get("code") or p.get("slug")
        if best.get(code, {}).get("verdict") == "AC":
            got += pts
    return got, total
