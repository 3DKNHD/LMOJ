"""LIS estricta: decreciente, iguales (lis=1), bitónico."""

def _dump(a):
    return f"{len(a)}\n" + " ".join(map(str, a)) + "\n"

def generate():
    n = 200000
    yield "n1", _dump([0])
    yield "decreciente", _dump(list(range(n, 0, -1)))
    yield "iguales", _dump([7] * n)
    yield "creciente", _dump(list(range(n)))
    bit = list(range(1, n // 2 + 1)) + list(range(n // 2, 0, -1))
    yield "bitonico", _dump(bit)
    zig = []
    for i in range(n):
        zig.append(i // 2 if i % 2 == 0 else n - i // 2)
    yield "zigzag", _dump(zig)
