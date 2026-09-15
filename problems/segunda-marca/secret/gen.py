"""Segunda distinta: no basta con el segundo del arreglo ordenado con repetidos."""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "n1", _dump([0])
    yield "todos-iguales", _dump([-(10**9)] * 200000)
    yield "dos-valores", _dump([1, 0] * 100000)
    # máximo repetido al inicio, segundo único al final
    arr = [10**9] * 199999 + [10**9 - 1]
    yield "segundo-al-final", _dump(arr)
    desc = list(range(200000, 0, -1))
    yield "todos-distintos-desc", _dump(desc)
    # segundo máximo negativo (todos ≤ 0)
    neg = [-(i % 50) for i in range(200000)]
    yield "todo-no-positivo", _dump(neg)
