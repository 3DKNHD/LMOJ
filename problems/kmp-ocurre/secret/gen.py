"""KMP: P=T, sin match, y overlap aaaa / aa."""

def generate():
    yield "iguales", "a\n" + "a\n"
    yield "sin", "z\n" + ("a"*1000000) + "\n"
    yield "overlap", "aa\n" + ("a"*1000000) + "\n"
    p = "ab"*500
    t = ("ab"*2000 + "c") * 200
    yield "periodico", p + "\n" + t[:1000000] + "\n"
    yield "un-char-final", "b\n" + ("a"*999999+"b") + "\n"
