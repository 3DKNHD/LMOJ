"""Pares X: todo igual (C(n,2)), ningún par, y X=2v con un solo valor."""


def _dump(X, arr):
    return f"{len(arr)} {X}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    n = 200000
    yield "sin-pares", _dump(10**9, list(range(n)))
    yield "todos-iguales", _dump(2, [1] * n)
    yield "x-cero", _dump(0, [i - n // 2 for i in range(n)])
    # muchos 3 y el complemento 10, X=13
    arr = [3] * (n // 2) + [10] * (n - n // 2)
    yield "dos-valores", _dump(13, arr)
    # un único 5 y el resto 1, X=6
    arr2 = [1] * (n - 1) + [5]
    yield "uno-especial", _dump(6, arr2)
    neg = [-(10**9)] * (n // 2) + [10**9] * (n - n // 2)
    yield "extremos", _dump(0, neg)
