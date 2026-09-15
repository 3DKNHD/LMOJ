"""Árboles con forma: bambú, estrella, binario, oruga. Consultas en extremos."""

N = 20000


def _values(n):
    mask = (1 << 30) - 1
    return [((i * 107 + 13) ^ (i << 3)) & mask for i in range(1, n + 1)]


def _dump(n, edges, queries, vals=None):
    vals = vals or _values(n)
    q = len(queries)
    lines = [f"{n} {q}", " ".join(map(str, vals))]
    lines.extend(f"{u} {v}" for u, v in edges)
    lines.extend(f"{u} {v}" for u, v in queries)
    return "\n".join(lines) + "\n"


def _queries_on(n, extra):
    qs = [(1, 1), (1, n), (n, n), (n // 2 or 1, n)]
    # barrido de hojas hacia la raíz
    step = max(1, n // 400)
    for i in range(1, n + 1, step):
        qs.append((i, min(n, i + step)))
        qs.append((1, i))
        qs.append((n, i))
    qs.extend(extra)
    return qs[:20000]


def generate():
    bamboo = [(i, i + 1) for i in range(1, N)]
    yield "bambu", _dump(N, bamboo, _queries_on(N, [(N, 1), (2, N - 1)]))

    star = [(1, i) for i in range(2, N + 1)]
    yield "estrella", _dump(N, star, _queries_on(N, [(2, 3), (2, N), (N - 1, N)]))

    binary = []
    for i in range(1, N + 1):
        L, R = 2 * i, 2 * i + 1
        if L <= N:
            binary.append((i, L))
        if R <= N:
            binary.append((i, R))
    yield "binario-completo", _dump(N, binary, _queries_on(N, [(N, N // 2), (3, 8)]))

    # oruga: espalda 1-2-...-k y patas colgando
    k = N // 2
    caterpillar = [(i, i + 1) for i in range(1, k)]
    pata = k + 1
    i = 1
    while pata <= N:
        caterpillar.append((i, pata))
        pata += 1
        i = i + 1 if i < k else 1
    yield "oruga", _dump(N, caterpillar, _queries_on(N, [(k, N), (1, k)]))

    # dos estrellas unidas por un puente
    mid = N // 2
    twin = [(1, i) for i in range(2, mid + 1)]
    twin.append((1, mid + 1))
    twin.extend((mid + 1, j) for j in range(mid + 2, N + 1))
    yield "dos-estrellas", _dump(N, twin, _queries_on(N, [(2, N), (mid, mid + 2), (3, 4)]))
