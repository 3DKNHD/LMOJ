"""Máquinas: k=1, una lenta, y n grande con t distintos para no sumar de más en ll."""


def _dump(k, t):
    return f"{len(t)} {k}\n" + " ".join(map(str, t)) + "\n"


def generate():
    yield "una", _dump(10**9, [10**9])
    yield "k1-rapida", _dump(1, [10**9] * 199999 + [1])
    n = 200000
    yield "todas-iguales", _dump(n, [2] * n)  # T=2
    # una rapidísima y el resto inútiles
    yield "una-domina", _dump(10**9, [1] + [10**9] * (n - 1))
    t = [i + 1 for i in range(n)]
    yield "tiempos-1-a-n", _dump(10**9, t)
    yield "k-pequena", _dump(3, [5, 5, 5, 5])
