"""DSU: sin aristas, estrella, camino, y consultas al mismo nodo."""


def _dump(n, edges, qs):
    lines = [f"{n} {len(edges)} {len(qs)}"]
    lines.extend(f"{u} {v}" for u, v in edges)
    lines.extend(f"{u} {v}" for u, v in qs)
    return "\n".join(lines) + "\n"


def generate():
    n = 200000
    qs_self = [(i, i) for i in range(1, 1001)]
    yield "sin-cables", _dump(n, [], qs_self + [(1, 2), (1, n), (2, 3)])

    star = [(1, i) for i in range(2, n + 1)]
    qs_star = [(2, 3), (2, n), (1, n), (n, n)]
    step = n // 400
    for i in range(2, n + 1, step):
        qs_star.append((i, min(n, i + 1)))
        qs_star.append((1, i))
    yield "estrella", _dump(n, star, qs_star[:n])

    path = [(i, i + 1) for i in range(1, n)]
    qs_path = [(1, n), (1, 2), (n - 1, n), (n // 3, 2 * n // 3)]
    yield "camino", _dump(n, path, qs_path * 100)

    # dos bloques
    two = [(i, i + 1) for i in range(1, n // 2)] + [(i, i + 1) for i in range(n // 2 + 1, n)]
    qs_two = [(1, n // 2), (n // 2 + 1, n), (1, n), (n // 2, n // 2 + 1)]
    yield "dos-bloques", _dump(n, two, qs_two * 200)

    loops = [(i, i) for i in range(1, min(n, 5000) + 1)]
    yield "solo-bucles", _dump(n, loops, [(1, 2), (5, 5), (n, 1)])
