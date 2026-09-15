"""Máximo: el borde es dónde está el mayor y si todo es negativo."""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "uno", _dump([-(10**9)])
    yield "todos-iguales", _dump([7] * 200000)
    yield "todo-negativo", _dump(list(range(-200000, 0)))
    head = [10**9] + [-10**9] * 199999
    yield "max-al-inicio", _dump(head)
    tail = [0] * 199999 + [10**9]
    yield "max-al-final", _dump(tail)
    saw = [i if i % 2 == 0 else -i for i in range(200000)]
    yield "sierra", _dump(saw)
