"""0/1: un ítem enorme, todos caben, y W saturado."""

def _dump(W, items):
    lines = [f"{len(items)} {W}"]
    lines.extend(f"{w} {v}" for w, v in items)
    return "\n".join(lines) + "\n"

def generate():
    yield "no-cabe", _dump(5, [(6, 10)] * 10)
    yield "todos-caben", _dump(100000, [(1, 10**9)] * 100)
    items = [(i + 1, (i + 1) * 1000) for i in range(100)]
    yield "w-igual-indice", _dump(5050, items)
    heavy = [(1000, 1)] * 50 + [(1, 10**9)] * 50
    yield "mezcla-pesado-liviano", _dump(100000, heavy)
    yield "un-optimo", _dump(10, [(10, 5), (9, 100), (1, 1)])
