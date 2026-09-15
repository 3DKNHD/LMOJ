"""Intervalos: toque en un punto, anidados y cadena justa L=R+1."""


def _dump(segs):
    lines = [str(len(segs))]
    lines.extend(f"{L} {R}" for L, R in segs)
    return "\n".join(lines) + "\n"


def generate():
    yield "uno", _dump([(1, 10**9)])
    n = 200000
    # todos el mismo punto: solo 1
    yield "mismo-punto", _dump([(7, 7)] * n)
    # cadena que SÍ encaja: [1,1][2,2]...
    yield "puntos-consecutivos", _dump([(i, i) for i in range(1, n + 1)])
    # cadena que choca: [1,2][2,3][3,4]...
    chocan = [(i, i + 1) for i in range(1, n + 1)]
    yield "toque-en-extremo", _dump(chocan)
    # anidados: [1,n], [2,n-1], ...
    nested = []
    L, R = 1, n
    while L <= R and len(nested) < n:
        nested.append((L, R))
        L += 1
        R -= 1
    while len(nested) < n:
        nested.append((1, 1))
    yield "anidados", _dump(nested)
    # greedy clásico: corto al final gana
    mix = [(1, 10**9)] + [(2 * i, 2 * i) for i in range(1, n)]
    yield "uno-largo-y-puntos", _dump(mix)
