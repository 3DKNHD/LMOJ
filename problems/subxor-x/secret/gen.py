"""XOR subarray: todos 0 (C(n+1,2)), X=0, y prefijos que se repiten."""

def _dump(X, a):
    return f"{len(a)} {X}\n" + " ".join(map(str,a)) + "\n"

def generate():
    n=200000
    yield "ceros-x0", _dump(0, [0]*n)
    yield "ceros-x1", _dump(1, [0]*n)
    yield "unos", _dump(1, [1]*n)
    yield "ninguno", _dump((1<<29), [1]*n)
    alt=[1,3,1,3]* (n//4)
    yield "periodo-2", _dump(2, alt)
