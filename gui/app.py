from __future__ import annotations

import sys
from pathlib import Path

GUI = Path(__file__).resolve().parent
ROOT = GUI.parent
sys.path.insert(0, str(ROOT))

import markdown  # noqa: E402
from flask import Flask, abort, redirect, render_template, request, url_for  # noqa: E402

from judge import pack as P  # noqa: E402
from judge import store  # noqa: E402
from judge import submit as S  # noqa: E402
from judge import sync as Y  # noqa: E402
from judge.paths import load_config, ensure_dirs  # noqa: E402

app = Flask(
    __name__,
    template_folder=str(GUI / "templates"),
    static_folder=str(GUI / "static"),
)
MD = markdown.Markdown(extensions=["fenced_code", "tables", "nl2br"])
LANGS = [("cpp17", "C++17"), ("py3", "Python 3")]


def md(text: str) -> str:
    MD.reset()
    return MD.convert(text or "")


@app.context_processor
def inject_shell():
    cfg = load_config()
    problems = P.list_problems()
    best = store.best_map()
    got, total = store.points_total(problems)
    ac = sum(1 for p in problems if best.get(p["code"], {}).get("verdict") == "AC")
    return {
        "site_name": cfg.get("site_name", "LMOJ"),
        "points_got": got,
        "points_total": total,
        "ac_count": ac,
        "problem_count": len(problems),
        "langs": LANGS,
    }


def _samples_html(prob: Path) -> list[dict]:
    rows = []
    for inp, outp in P.sample_files(prob):
        rows.append(
            {
                "name": inp.stem,
                "input": inp.read_text(encoding="utf-8"),
                "output": outp.read_text(encoding="utf-8"),
            }
        )
    return rows


@app.route("/")
def home():
    problems = P.list_problems()
    best = store.best_map()
    recent = store.submissions(limit=8)
    info = Y.last_sync_info()
    return render_template(
        "home.html",
        problems=problems,
        best=best,
        recent=recent,
        sync=info,
    )


@app.route("/problems")
def problems():
    rows = P.list_problems()
    best = store.best_map()
    return render_template("problems.html", problems=rows, best=best)


@app.route("/problem/<code>", methods=["GET", "POST"])
def problem(code: str):
    try:
        prob = P.find_problem(code)
    except P.ProblemNotFound:
        abort(404)
    meta = P.public_meta(prob)
    lang = request.values.get("lang", "cpp17")
    if lang not in ("cpp17", "py3"):
        lang = "cpp17"
    src_path = P.ensure_workspace(meta["code"], lang)
    code_text = src_path.read_text(encoding="utf-8")
    result = None
    if request.method == "POST":
        code_text = request.form.get("code", code_text)
        lang = request.form.get("lang", lang)
        sample_only = request.form.get("mode") == "sample"
        result = S.run_submission(prob, code_text, lang, sample_only=sample_only)
        store.record_submission(meta["code"], lang, code_text, result)
        code_text = src_path.read_text(encoding="utf-8")
    best = store.best_map().get(meta["code"], {})
    return render_template(
        "problem.html",
        meta=meta,
        statement_html=md(P.statement_md(prob)),
        samples=_samples_html(prob),
        code=code_text,
        lang=lang,
        result=result,
        best=best,
        recent=store.submissions(limit=6, problem=meta["code"]),
    )


@app.route("/submissions")
def submissions():
    code = request.args.get("problem") or None
    rows = store.submissions(limit=80, problem=code)
    return render_template("submissions.html", rows=rows, filter_problem=code)


@app.route("/submission/<int:sid>")
def submission(sid: int):
    row = store.get_submission(sid)
    if row is None:
        abort(404)
    return render_template("submission.html", row=row)


@app.route("/sync", methods=["GET", "POST"])
def sync_page():
    cfg = load_config()
    error = None
    info = Y.last_sync_info()
    if request.method == "POST":
        url = (request.form.get("pack_url") or "").strip()
        branch = (request.form.get("pack_branch") or "main").strip()
        try:
            info = Y.sync_pack(url or None, branch or None)
        except Y.SyncError as e:
            error = str(e)
            info = Y.last_sync_info()
        cfg = load_config()
    return render_template(
        "sync.html",
        cfg=cfg,
        info=info,
        error=error,
    )


def main() -> None:
    ensure_dirs()
    cfg = load_config()
    host = cfg.get("host", "127.0.0.1")
    port = int(cfg.get("port", 5050))
    print(f"LMOJ — http://{host}:{port}")
    print("Solo en esta máquina. Ctrl+C para salir.")
    app.run(host=host, port=port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
