"""Unbounded: gcd no divide S, un 1 que lo hace trivial, y S máximo."""

def _dump(S, c):
    return f"{len(c)} {S}\n" + " ".join(map(str,c)) + "\n"

def generate():
    yield "imposible", _dump(3, [2,4,6])
    yield "hay-uno", _dump(100000, [1] + list(range(2,101)))
    yield "solo-grandes", _dump(100000, [99991, 99989, 100000])
    yield "canonicos", _dump(99999, [1,5,10,25,50,100])
    yield "repetidos", _dump(50000, [7]*100)
