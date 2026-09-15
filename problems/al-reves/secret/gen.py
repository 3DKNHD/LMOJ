"""Reverso: palíndromos y n=1 no disfrazan un reverse a medias."""


def _dump(arr):
    return f"{len(arr)}\n" + " ".join(map(str, arr)) + "\n"


def generate():
    yield "n1", _dump([0])
    pal = list(range(1, 100001)) + list(range(100000, 0, -1))
    yield "palindromo", _dump(pal)
    yield "creciente", _dump(list(range(1, 200001)))
    yield "signos", _dump([10**9 if i % 2 == 0 else -(10**9) for i in range(200000)])
    yield "ceros-y-punta", _dump([0] * 199999 + [-1])
    # no simétrico: bloques de tamaño creciente
    blocks = []
    v = 1
    while len(blocks) < 200000:
        blocks.extend([v] * v)
        v += 1
    yield "bloques-crecientes", _dump(blocks[:200000])
