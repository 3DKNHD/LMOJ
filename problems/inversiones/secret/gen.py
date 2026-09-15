"""Inversiones: permutaciones con forma, no shuffle uniforme.

Construye arreglos cuya cantidad de inversiones es conocida o extrema:
identidad, reverso, bitónico, un swap, meseta de repetidos, y n máximo.
"""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    n = 200000
    yield "ordenado", _dump(list(range(1, n + 1)))
    yield "reverso", _dump(list(range(n, 0, -1)))

    bitonic = list(range(1, n // 2 + 1)) + list(range(n, n // 2, -1))
    yield "bitonico", _dump(bitonic)

    one_swap = list(range(1, n + 1))
    one_swap[0], one_swap[-1] = one_swap[-1], one_swap[0]
    yield "un-swap-extremos", _dump(one_swap)

    plateau = [i // 7 + 1 for i in range(n)]
    yield "meseta-repetidos", _dump(plateau)

    # intercalado par/impar descendente: muchas inversiones locales
    inter = []
    hi, lo = n, 1
    while lo <= hi:
        inter.append(hi)
        hi -= 1
        if lo <= hi:
            inter.append(lo)
            lo += 1
    yield "zigzag-extremos", _dump(inter)
