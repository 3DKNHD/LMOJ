"""Suma acotada: ceros (n), todo >S (0), y un bloque justo."""

def _dump(S, a):
    return f"{len(a)} {S}\n" + " ".join(map(str,a)) + "\n"

def generate():
    n=200000
    yield "ceros", _dump(0, [0]*n)
    yield "todo-grande", _dump(1, [2]*n)
    yield "unos", _dump(n//2, [1]*n)
    yield "un-gigante", _dump(10**9, [10**9]+[0]*(n-1))
    a=[10**9]*n
    yield "ll-sum", _dump(10**18, a)
