"""Rango cerrado: puntos en L, en R, y fuera por 1."""


def _dump(n, L, R, arr):
    return f"{n} {L} {R}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "todo-adentro", _dump(200000, -10**9, 10**9, list(range(-100000, 100000)))
    yield "nada", _dump(200000, 10, 20, [9] * 100000 + [21] * 100000)
    yield "punto", _dump(200000, 5, 5, [5] * 100000 + [4] * 50000 + [6] * 50000)
    # todos exactamente en los bordes
    bordes = [-(10**9), 10**9] * 100000
    yield "solo-extremos-del-intervalo", _dump(200000, -(10**9), 10**9, bordes)
    L, R = -3, 10
    arr = []
    for i in range(200000):
        arr.append(L - 1 + (i % (R - L + 3)))
    yield "ventana-deslizante", _dump(200000, L, R, arr)
    yield "n1-fuera", _dump(1, 0, 1, [-1])
