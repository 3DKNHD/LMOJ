"""Binpow: 0^0, múltiplos del MOD y exponentes 1e18."""

MOD = 10**9 + 7


def _dump(pairs):
    lines = [str(len(pairs))]
    lines.extend(f"{a} {b}" for a, b in pairs)
    return "\n".join(lines) + "\n"


def generate():
    yield "ceros", _dump([(0, 0), (0, 1), (0, 10**18), (1, 0), (MOD, 0)])
    yield "multiplos-mod", _dump([(MOD, 1), (2 * MOD, 3), (10**18, 1), (10**18, 2)])
    base2 = [(2, e) for e in range(0, 60)]
    yield "potencias-2", _dump(base2)
    vol = []
    a, b = 3, 0
    for i in range(100000):
        vol.append((a, b))
        a = (a * 5 + 1) % (10**18)
        b = (b * 7 + i) % (10**18)
    yield "volumen", _dump(vol)
    yield "uno", _dump([(1, 10**18), (MOD + 1, 10**18)])
