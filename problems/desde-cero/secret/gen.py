"""Reloj 24h: wrap en 86400, ceros a la izquierda y t de 64 bits."""

DAY = 86400


def _dump(times):
    lines = [str(len(times))]
    lines.extend(str(t) for t in times)
    return "\n".join(lines) + "\n"


def generate():
    yield "medianoche", _dump([0, DAY, 2 * DAY, 10**18 // DAY * DAY])
    yield "un-segundo-antes", _dump([DAY - 1, 2 * DAY - 1, 10**18])
    yield "hitos", _dump([1, 59, 60, 61, 3599, 3600, 3601, 3661, 43200])
    seq = []
    t = 0
    for i in range(100000):
        seq.append(t)
        t += 37
        if i % 1000 == 0:
            t += 10**12
    yield "pasos-37", _dump(seq)
    yield "solo-grande", _dump([10**18 - i for i in range(50)])
