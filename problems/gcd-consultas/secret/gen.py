"""GCD: todos iguales, coprimos consecutivos, potencias de 2."""

def _dump(a, qs):
    lines=[f"{len(a)} {len(qs)}", " ".join(map(str,a))]
    lines.extend(f"{l} {r}" for l,r in qs)
    return "\n".join(lines)+"\n"

def generate():
    n=100000
    qs=[(1,n),(1,1),(n,n)] + [(i, min(n,i+50)) for i in range(1,n,400)]
    yield "iguales", _dump([12]*n, qs)
    yield "coprimos", _dump(list(range(1,n+1)), qs[:200])
    p2=[1<<(i%30) for i in range(n)]
    yield "pot2", _dump(p2, qs[:300])
    yield "uno", _dump([1]*n, [(1,n)]*1000)
