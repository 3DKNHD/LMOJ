# Rutas con peso

Grafo **no dirigido** con pesos no negativos. Distancia mínima de $s$ a $t$.
Si no hay camino, $-1$.

Los pesos llegan a $10^9$ y un camino puede tener $10^5$ aristas: usa `long long`.
`int` + `INF = 2^{31}-1` revienta (trampa de tu sparty).

## Entrada

$n$ $m$ $s$ $t$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$, $1 \le s,t \le n$).

$m$ líneas $u$ $v$ $w$ ($1 \le w \le 10^9$). Puede haber múltiples aristas y bucles.

## Salida

Un entero.
