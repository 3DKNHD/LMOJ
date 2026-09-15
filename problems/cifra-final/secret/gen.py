"""Última cifra: negativos (C++ % trampa) y ±10^18."""


def _dump(nums):
    lines = [str(len(nums))]
    lines.extend(str(x) for x in nums)
    return "\n".join(lines) + "\n"


def generate():
    yield "ceros", _dump([0, 10, -10, 100, -100, 10**18, -(10**18)])
    digits = []
    for d in range(10):
        digits.extend([d, -d, 10 + d, -(10 + d), 10**15 + d, -(10**15 + d)])
    yield "cada-digito", _dump(digits)
    # -922337... no, 1e18 cabe en ll. El único lío es -n cuando n = -2^63; aquí el min es -1e18.
    yield "ll-minimo-pack", _dump([-(10**18) + k for k in range(10)] + [10**18 - k for k in range(10)])
    vol = []
    x = -(10**18)
    for i in range(100000):
        vol.append(x)
        x += 99991
        if x > 10**18:
            x -= 2 * 10**18
    yield "volumen-paso", _dump(vol)
