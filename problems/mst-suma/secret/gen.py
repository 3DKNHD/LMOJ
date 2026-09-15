"""MST: n=1, estrella barata vs arista cara, y dos componentes."""

def _dump(n, edges):
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u} {v} {w}" for u,v,w in edges)
    return "\n".join(lines) + "\n"

def generate():
    yield "n1", _dump(1, [])
    n=100000
    star=[(1,i,1) for i in range(2,n+1)]
    star.append((2,3,10**9))
    yield "estrella", _dump(n, star)
    yield "camino", _dump(n, [(i,i+1,i) for i in range(1,n)])
    yield "dos-comp", _dump(n, [(i,i+1,1) for i in range(1,n//2)] + [(i,i+1,1) for i in range(n//2+1,n)])
    dense=[(i,i+1,10**9) for i in range(1,n)] + [(1,n,1)]
    yield "atajo-mst", _dump(n, dense)
