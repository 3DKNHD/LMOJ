"""Cobertura: todos el mismo rango, puntos aislados y nido completo."""

M = 10**6


def _dump(M, segs):
    lines = [f"{len(segs)} {M}"]
    lines.extend(f"{L} {R}" for L, R in segs)
    return "\n".join(lines) + "\n"


def generate():
    n = 200000
    yield "todo-el-eje", _dump(M, [(1, M)] * n)
    yield "puntos", _dump(M, [(i % M + 1, i % M + 1) for i in range(n)])
    nested = [(1, M - i % 100) for i in range(n)]
    yield "casi-nido", _dump(M, nested)
    # oleadas que se solapan 3
    waves = []
    for i in range(n):
        L = 1 + (i * 3) % (M - 10)
        waves.append((L, L + 9))
    yield "ventanas-10", _dump(M, waves)
    yield "un-pico", _dump(M, [(500000, 500000)] * n)
    yield "extremos", _dump(M, [(1, 1)] * (n // 2) + [(M, M)] * (n - n // 2))
