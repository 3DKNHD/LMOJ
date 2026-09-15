# Orden lexicográfico

$n$ tareas, arista $u \rightarrow v$ significa "$u$ antes que $v$". Imprime el orden
**lexicográficamente menor** (Kahn + heap de mínimos). Si hay ciclo: `IMPOSIBLE`.

## Entrada

$n$ $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

$m$ líneas $u$ $v$ ($1 \le u,v \le n$).

## Salida

$n$ enteros, o la palabra `IMPOSIBLE`.
