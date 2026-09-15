"""Suma: el borde es el desborde de int, no el máximo aislado."""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "uno-neg", _dump([-(10**9)])
    yield "ceros", _dump([0] * 200000)
    yield "lleno-positivo", _dump([10**9] * 200000)
    yield "lleno-negativo", _dump([-(10**9)] * 200000)
    mix = []
    for i in range(200000):
        mix.append(10**9 if i % 3 == 0 else -(10**9) if i % 3 == 1 else 0)
    yield "bloques-3", _dump(mix)
    cancel = [10**9, -(10**9)] * 100000
    yield "cancelan", _dump(cancel)
