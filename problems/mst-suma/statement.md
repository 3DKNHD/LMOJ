# Red mínima

Conecta los $n$ nodos con un subconjunto de las aristas de **costo mínimo** (MST).
Si no es conexo, `IMPOSIBLE`. Suma de pesos en 64 bits.

## Entrada

$n$ $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

$m$ líneas $u$ $v$ $w$ ($1 \le u,v \le n$, $1 \le w \le 10^9$). No dirigido.

## Salida

Un entero o `IMPOSIBLE`.
