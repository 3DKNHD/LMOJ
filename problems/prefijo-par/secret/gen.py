"""Prefijos pares: ataca paridad, no magnitud. Alternancias y bloqueos de impares."""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "un-impar", _dump([7])
    yield "un-par", _dump([8])
    yield "todos-pares", _dump([0, 2, -4, 10**9, -(10**9)] * 4000)
    yield "todos-impares", _dump([1, -1, 3, -3, 10**9 - 1] * 4000)

    alt = []
    for i in range(200000):
        alt.append(1 if i % 2 == 0 else 2)
    yield "alterna-impar-par", _dump(alt)

    # dos impares seguidos vuelven a paridad anterior; bloques crecientes
    blocks = []
    odd = 1
    for k in range(1, 600):
        blocks.extend([odd] * k)
        odd = -odd if k % 2 else odd + 2
    yield "bloques-impares", _dump(blocks[:200000])

    zeros = [0] * 200000
    zeros[0] = 1
    zeros[-1] = 1
    yield "ceros-con-puntas", _dump(zeros)
