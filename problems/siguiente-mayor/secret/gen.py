"""NGE: creciente (todo el siguiente), decreciente (todo -1), meseta."""

def _dump(a):
    return f"{len(a)}\n" + " ".join(map(str,a)) + "\n"

def generate():
    n=200000
    yield "creciente", _dump(list(range(n)))
    yield "decreciente", _dump(list(range(n,0,-1)))
    yield "iguales", _dump([0]*n)
    yield "pico-final", _dump(list(range(n-1)) + [n+5])
    zig=[i if i%2==0 else n-i for i in range(n)]
    yield "zigzag", _dump(zig)
