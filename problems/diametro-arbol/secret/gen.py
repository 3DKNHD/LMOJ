"""Diámetro: bambú n-1, estrella 2, oruga."""

def _dump(n, edges):
    lines=[str(n)]
    lines.extend(f"{u} {v}" for u,v in edges)
    return "\n".join(lines)+"\n"

def generate():
    yield "n1", _dump(1, [])
    n=200000
    yield "bambu", _dump(n, [(i,i+1) for i in range(1,n)])
    yield "estrella", _dump(n, [(1,i) for i in range(2,n+1)])
    k=n//2
    cat=[(i,i+1) for i in range(1,k)]
    p=k+1
    i=1
    while p<=n:
        cat.append((i,p)); p+=1; i = i+1 if i<k else 1
    yield "oruga", _dump(n, cat)
    bin_e=[]
    for i in range(1,n+1):
        if 2*i<=n: bin_e.append((i,2*i))
        if 2*i+1<=n: bin_e.append((i,2*i+1))
    yield "heap", _dump(n, bin_e)
