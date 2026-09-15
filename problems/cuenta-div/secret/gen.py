"""Divisores: 1, primos, 10^6 y altamente compuestos."""


def _dump(nums):
    lines = [str(len(nums))]
    lines.extend(str(x) for x in nums)
    return "\n".join(lines) + "\n"


def generate():
    yield "bordes", _dump([1, 2, 4, 10**6, 999983])  # 999983 es primo
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 99991, 999983]
    yield "primos", _dump(primos)
    # 720720 = 16*9*5*7*11*13 tiene muchos divisores
    hc = [6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 55440, 720720]
    yield "altamente-compuestos", _dump(hc)
    vol = []
    x = 1
    for i in range(100000):
        vol.append(x)
        x = x * 3 + 1
        if x > 10**6:
            x = (i % 10**6) + 1
    yield "volumen", _dump(vol)
    yield "todos-cuadrados", _dump([i * i for i in range(1, 1001)])
