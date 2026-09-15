"""DAG: cadena 1, diamante 2, y capas que multiplican."""

def _dump(n, edges):
    lines=[f"{n} {len(edges)}"]
    lines.extend(f"{u} {v}" for u,v in edges)
    return "\n".join(lines)+"\n"

def generate():
    n=100000
    yield "n1", _dump(1, [])
    yield "cadena", _dump(n, [(i,i+1) for i in range(1,n)])
    yield "nada-a-n", _dump(n, [(i,i+1) for i in range(1, n-1)])
    # capas: 1 -> bloque -> n
    edges=[]
    mid=min(n-2, 300)
    for i in range(2, mid+2):
        edges.append((1,i)); edges.append((i,n))
    yield "diamante", _dump(n, edges)
    # topo  i -> i+1 y i -> i+2
    e2=[(i,i+1) for i in range(1,n)] + [(i,i+2) for i in range(1,n-1)]
    yield "fibonacci-dag", _dump(n, e2)
