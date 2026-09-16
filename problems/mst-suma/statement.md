# Cablear el campus

Hay $n$ edificios y $m$ posibles cables. El cable $i$ uniría los edificios $u$ y $v$ (en los dos sentidos) y costaría $w$. Puedes usar un subconjunto de esos cables.

Quieres que **todos** los edificios queden en una sola red, pagando lo **mínimo** posible. No hace falta usar cables de más: una red sin ciclos innecesarios está bien. Si con los cables disponibles no se puede conectar todo, imprime `IMPOSIBLE`.

La suma de los costos puede no caber en 32 bits.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Siguen $m$ líneas con $u$ $v$ $w$ ($1 \le u,v \le n$, $1 \le w \le 10^9$).

## Salida

Un entero (el costo total) o la palabra `IMPOSIBLE`.
