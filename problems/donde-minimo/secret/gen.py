"""Primera ocurrencia del mínimo: empatar no debe mover el índice."""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "n1", _dump([10**9])
    yield "min-al-inicio", _dump([-(10**9)] + [10**9] * 199999)
    yield "min-al-final", _dump([0] * 199999 + [-(10**9)])
    empate = [5] * 100000 + [1] * 50000 + [1] * 50000
    yield "empate-en-bloque", _dump(empate)
    desc = list(range(200000, 0, -1))
    yield "estrictamente-desc", _dump(desc)
    # mínimo único en el medio, copias mayores a los lados
    mid = [3] * 99999 + [-4] + [3] * 100000
    yield "unico-en-medio", _dump(mid)
