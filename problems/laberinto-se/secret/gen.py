"""S-E: muro total, pasillo, y serpiente que obliga el largo."""

def _dump(rows):
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join(rows) + "\n"

def generate():
    n = m = 1000
    open_ = ["." * m for _ in range(n)]
    open_[0] = "S" + "." * (m - 1)
    open_[-1] = "." * (m - 1) + "E"
    yield "abierto", _dump(open_)
    wall = ["#" * m for _ in range(n)]
    wall[0] = "S" + "#" * (m - 1)
    wall[-1] = "#" * (m - 1) + "E"
    yield "separados", _dump(wall)
    hall = ["." * m]
    hall[0] = "S" + "." * (m - 2) + "E"
    yield "pasillo", _dump(hall)
    snake = []
    for i in range(n):
        if i % 2 == 0:
            snake.append("." * m)
        else:
            snake.append("#" * (m - 1) + ".")
    snake[0] = "S" + snake[0][1:]
    snake[-1] = snake[-1][:-1] + "E"
    yield "serpiente", _dump(snake)
    tiny = ["SE"]
    yield "adyacentes", _dump(tiny)
