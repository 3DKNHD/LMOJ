"""Casos para A+B: desbordes de 32 bits, signos y volumen, no un RNG genérico."""

LIM = 10**18


def _dump(pairs):
    lines = [str(len(pairs))]
    lines.extend(f"{a} {b}" for a, b in pairs)
    return "\n".join(lines) + "\n"


def generate():
    corners = []
    for a in (0, 1, -1, LIM, -LIM, LIM - 1, -LIM + 1):
        for b in (0, 1, -1, LIM, -LIM):
            corners.append((a, b))
    yield "esquinas-32bit", _dump(corners)

    yield "ceros", _dump([(0, 0)] * 50)

    yield "mismo-signo-max", _dump([(LIM, LIM), (-LIM, -LIM), (LIM, LIM - 1), (-LIM, -LIM + 1)])

    yield "anti-int", _dump([(LIM, LIM), (-LIM, -LIM)] * 1000)

    volume = []
    a, b = -LIM, LIM
    for i in range(100000):
        volume.append((a, b))
        a = -a if i % 3 == 0 else a + (1 if a < LIM else -1)
        b = -b if i % 5 == 0 else b - (1 if b > -LIM else -1)
        a = max(-LIM, min(LIM, a))
        b = max(-LIM, min(LIM, b))
    yield "volumen-t-max", _dump(volume)
