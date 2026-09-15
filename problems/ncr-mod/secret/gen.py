"""nCr: k>n, bordes 0 y 1e6, y volumen."""

def _dump(pairs):
    lines=[str(len(pairs))]
    lines.extend(f"{n} {k}" for n,k in pairs)
    return "\n".join(lines)+"\n"

def generate():
    yield "bordes", _dump([(0,0),(1,0),(1,1),(10**6,0),(10**6,10**6),(3,4)])
    vol=[]
    n,k=0,0
    for i in range(100000):
        vol.append((n,k))
        n = (n*5+3) % (10**6+1)
        k = (k*7+i) % (10**6+1)
    yield "volumen", _dump(vol)
    yield "mitad", _dump([(i, i//2) for i in range(0, 2000)])
