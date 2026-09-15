"""Pares: 0 y negativos. No confundir con prefijos pares."""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "un-cero", _dump([0])
    yield "todos-impares", _dump([1, -1, 3, -3, 10**9 - 1] * 40000)
    yield "todos-pares", _dump([0, 2, -2, 10**9, -(10**9)] * 40000)
    neg_even = [-(2 * i) for i in range(1, 200001)]
    yield "negativos-pares", _dump(neg_even)
    odd_then = [-1] * 199999 + [8]
    yield "un-par-al-final", _dump(odd_then)
    alt = [i for i in range(-100000, 100000)]
    yield "rango-corrido", _dump(alt)
