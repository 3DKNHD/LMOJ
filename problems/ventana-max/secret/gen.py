"""Ventana: k=1, k=n, máximo al inicio que caduca."""

def _dump(k, a):
    return f"{len(a)} {k}\n" + " ".join(map(str,a)) + "\n"

def generate():
    n=200000
    yield "k1", _dump(1, list(range(n)))
    yield "k-n", _dump(n, list(range(n,0,-1)))
    yield "caduca", _dump(3, [10**9]+[0]*(n-1))
    yield "crece", _dump(100, list(range(n)))
    yield "sierra", _dump(2, [i%2 for i in range(n)])
