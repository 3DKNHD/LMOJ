"""Triángulo: degenerados, 1e9+1e9 y permutaciones de lados."""


def _dump(triples):
    lines = [str(len(triples))]
    lines.extend(f"{a} {b} {c}" for a, b, c in triples)
    return "\n".join(lines) + "\n"


def generate():
    yield "equilateros", _dump([(1, 1, 1), (10**9, 10**9, 10**9)])
    yield "degenerados", _dump([(1, 2, 3), (1, 1, 2), (1, 10**9 - 1, 10**9), (2, 3, 5)])
    # 1e9, 1e9, 1 — sí; 1e9, 1, 1 — no. Si sumas en int, 1e9+1e9 revienta.
    yield "anti-int", _dump([(10**9, 10**9, 1), (10**9, 1, 1), (10**9, 10**9, 10**9)])
    pit = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
    perms = []
    for a, b, c in pit:
        perms.extend([(a, b, c), (c, a, b), (b, c, a)])
    yield "pitagoricos-perm", _dump(perms)
    big = []
    for i in range(100000):
        if i % 4 == 0:
            big.append((i + 1, i + 1, i + 1))
        elif i % 4 == 1:
            big.append((i + 1, i + 2, 2 * i + 3))  # degenerado a+b=c
        elif i % 4 == 2:
            big.append((10**9, 10**9, 2))
        else:
            big.append((1, 2, 10**9))
    yield "volumen", _dump(big)
