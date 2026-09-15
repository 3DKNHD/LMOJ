"""Bipartito: bosque (sí), ciclo impar, ciclo par."""

def _dump(n, edges):
    lines=[f"{n} {len(edges)}"]
    lines.extend(f"{u} {v}" for u,v in edges)
    return "\n".join(lines)+"\n"

def generate():
    n=100000
    yield "sin", _dump(n, [])
    yield "estrella", _dump(n, [(1,i) for i in range(2,n+1)])
    yield "ciclo-impar", _dump(n, [(1,2),(2,3),(3,1)] + [(i,i+1) for i in range(4,n)])
    even=[(i,i+1) for i in range(1,n)] + [(n,1)]  # n par → ciclo par
    yield "ciclo-hamilton", _dump(n, even)
    yield "completo-k2", _dump(n, [(1,2)]*1 + [(3,i) for i in range(4, min(n,100)+1)])
