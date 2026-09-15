"""Multi-source: todas estaciones, solo un extremo, y dos puntas de un camino."""

def _dump(n, stations, edges):
    lines=[f"{n} {len(edges)} {len(stations)}", " ".join(map(str,stations))]
    lines.extend(f"{u} {v}" for u,v in edges)
    return "\n".join(lines)+"\n"

def generate():
    n=100000
    path=[(i,i+1) for i in range(1,n)]
    yield "todas", _dump(n, list(range(1,n+1)), path)
    yield "un-extremo", _dump(n, [1], path)
    yield "dos-puntas", _dump(n, [1,n], path)
    yield "descon", _dump(n, [1], [(i,i+1) for i in range(1, n//2)])
    star=[(1,i) for i in range(2,n+1)]
    yield "hub", _dump(n, [2,3], star)
