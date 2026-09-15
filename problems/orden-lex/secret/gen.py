"""Topo lex: sin aristas (1..n), cadena inversa, y un ciclo al final."""

def _dump(n, edges):
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u} {v}" for u, v in edges)
    return "\n".join(lines) + "\n"

def generate():
    n = 100000
    yield "sin-deps", _dump(n, [])
    yield "cadena", _dump(n, [(i, i + 1) for i in range(1, n)])
    #  n -> n-1 -> ... fuerza el orden n, n-1, ...
    yield "cadena-inversa", _dump(n, [(i + 1, i) for i in range(1, n)])
    yield "ciclo", _dump(n, [(1, 2), (2, 3), (3, 1)] + [(4, 5)])
    # 1 antes que todos los pares: lex 1,2,3,...
    star = [(1, i) for i in range(2, n + 1)]
    yield "estrella-out", _dump(n, star)
