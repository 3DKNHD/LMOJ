"""BFS 1→n: camino, estrella (dist 2), desconectado y n=1."""


def _dump(n, edges):
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u} {v}" for u, v in edges)
    return "\n".join(lines) + "\n"


def generate():
    n = 100000
    yield "n1", _dump(1, [])
    yield "sin-aristas", _dump(n, [])
    path = [(i, i + 1) for i in range(1, n)]
    yield "camino", _dump(n, path)
    star = [(1, i) for i in range(2, n + 1)]
    yield "estrella", _dump(n, star)
    # 1 no llega a n: componente 1..n/2
    half = [(i, i + 1) for i in range(1, n // 2)]
    yield "cortado", _dump(n, half)
    # atajo 1-n más un camino largo
    mix = [(1, n)] + [(i, i + 1) for i in range(1, min(n, 5000))]
    yield "atajo", _dump(n, mix)
    loops = [(1, 1), (n, n), (2, 2)] + [(1, 2), (2, n)]
    yield "bucles-y-puente", _dump(n, loops)
