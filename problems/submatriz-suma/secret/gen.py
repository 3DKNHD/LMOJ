"""2D: celda única, matriz total, signos."""

def _dump(mat, qs):
    n,m=len(mat),len(mat[0])
    lines=[f"{n} {m} {len(qs)}"]
    lines.extend(" ".join(map(str,row)) for row in mat)
    lines.extend(f"{a} {b} {c} {d}" for a,b,c,d in qs)
    return "\n".join(lines)+"\n"

def generate():
    n=m=1000
    ones=[[1]*m for _ in range(n)]
    qs=[(1,1,n,m),(1,1,1,1),(n,m,n,m),(2,2,n-1,m-1)]
    yield "unos", _dump(ones, qs*200)
    alt=[[10**9 if (i+j)%2==0 else -10**9 for j in range(m)] for i in range(n)]
    yield "ajedrez-val", _dump(alt, [(1,1,n,m),(1,1,n,1),(1,1,1,m)]*100)
    qs2=[(i,i,i,i) for i in range(1, min(n,m)+1, 3)]
    yield "diagonal", _dump(ones, qs2)
