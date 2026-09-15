"""Dijkstra: camino de 1e9, estrella, desconectado. Fuerza ll."""

def _dump(n, s, t, edges):
    lines = [f"{n} {len(edges)} {s} {t}"]
    lines.extend(f"{u} {v} {w}" for u, v, w in edges)
    return "\n".join(lines) + "\n"

def generate():
    n = 100000
    yield "st-igual", _dump(n, 7, 7, [(1, 2, 1)])
    path = [(i, i + 1, 10**9) for i in range(1, n)]
    yield "camino-pesado", _dump(n, 1, n, path)
    star = [(1, i, i) for i in range(2, n + 1)]
    yield "estrella", _dump(n, 2, n, star)
    yield "desconectado", _dump(n, 1, n, [(i, i + 1, 1) for i in range(1, n // 2)])
    mix = [(1, 2, 1), (2, n, 10**9), (1, n, 3)]
    mix += [(i, min(n, i + 3), 5) for i in range(1, 5000)]
    yield "atajo-barato", _dump(n, 1, n, mix)
