# Suma de submatriz

Matriz $n \times m$ y $q$ consultas: suma del rectángulo $[r_1,r_2] \times [c_1,c_2]$ (1-indexado, inclusivo).

Prefijo 2D. $n,m \le 1000$, $q \le 10^5$.

## Entrada

$n$ $m$ $q$.

$n$ líneas con $m$ enteros ($-10^9 \le a_{ij} \le 10^9$).

$q$ líneas $r_1$ $c_1$ $r_2$ $c_2$ ($1 \le r_1 \le r_2 \le n$, $1 \le c_1 \le c_2 \le m$).

## Salida

$q$ líneas (64 bits).
