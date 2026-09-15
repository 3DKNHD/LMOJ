"""BIT: solo queries, updates que anulan, y rango de un punto."""

def _dump(a, ops):
    lines=[f"{len(a)} {len(ops)}", " ".join(map(str,a))]
    lines.extend(ops)
    return "\n".join(lines)+"\n"

def generate():
    n=200000
    a=[1]*n
    qs=[f"2 1 {n}", f"2 1 1", f"2 {n} {n}"]
    yield "solo-query", _dump(a, qs)
    ops=[]
    for i in range(1, n+1, 2):
        ops.append(f"1 {i} -1")
    ops.append(f"2 1 {n}")
    yield "anula-impares", _dump(a, ops)
    ops2=[f"1 1 {10**9}"]*1000 + [f"2 1 {n}"]*1000
    yield "un-punto-caliente", _dump([0]*n, ops2)
    ops3=[]
    for i in range(1, 50001):
        ops3.append(f"2 {i} {n-i+1}")
        ops3.append(f"1 {i} 1")
    yield "mix-barrido", _dump(list(range(n)), ops3)
