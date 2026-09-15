"""Islas 4-conectadas: tablero lleno, vacío, ajedrez y franjas."""


def _dump(rows):
    n, m = len(rows), len(rows[0])
    return f"{n} {m}\n" + "\n".join(rows) + "\n"


def generate():
    n = m = 1000
    yield "todo-tierra", _dump(["." * m] * n)
    yield "todo-agua", _dump(["#" * m] * n)
    chess = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append("." if (i + j) % 2 == 0 else "#")
        chess.append("".join(row))
    yield "ajedrez", _dump(chess)
    # franjas horizontales .#.#
    stripes = []
    for i in range(n):
        stripes.append(("." if i % 2 == 0 else "#") * m)
    yield "franjas", _dump(stripes)
    # un punto cada 3 celdas: islas 1x1
    dots = []
    for i in range(n):
        s = []
        for j in range(m):
            s.append("." if i % 3 == 0 and j % 3 == 0 else "#")
        dots.append("".join(s))
    yield "puntos-aislados", _dump(dots)
    yield "una-fila", _dump([".#" * 500])
