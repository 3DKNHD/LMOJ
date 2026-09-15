"""Prefijos: consultas de un punto, todo el arreglo, y signos que cancelan."""


def _dump(a, qs):
    lines = [f"{len(a)} {len(qs)}", " ".join(map(str, a))]
    lines.extend(f"{L} {R}" for L, R in qs)
    return "\n".join(lines) + "\n"


def generate():
    n = 200000
    yield "n1", _dump([-(10**9)], [(1, 1)] * 10)

    ones = [1] * n
    qs = [(1, n), (1, 1), (n, n), (n // 2, n // 2 + 1)]
    step = n // 300
    for i in range(1, n + 1, step):
        qs.append((i, min(n, i + step)))
        qs.append((1, i))
    yield "unos-barrido", _dump(ones, qs[:n])

    alt = [10**9 if i % 2 else -(10**9) for i in range(n)]
    qs2 = [(1, n)] * 1000 + [(i, i) for i in range(1, 2000)]
    qs2 += [(1, i) for i in range(1, 5000)]
    yield "cancelan-signo", _dump(alt, qs2[:n])

    # prefijo creciente: a[i]=i, consultas [i,n]
    inc = list(range(1, n + 1))
    qs3 = [(i, n) for i in range(1, n + 1, 50)]
    yield "triangulo", _dump(inc, qs3)
