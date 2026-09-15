# Estaciones más cercanas

Grafo no dirigido sin pesos. Hay $k$ estaciones. Para **cada** nodo $1..n$ imprime
la distancia a la estación más cercana, o $-1$ si no alcanza ninguna.

BFS multi-fuente: mete las $k$ estaciones en la cola a distancia 0.

## Entrada

$n$ $m$ $k$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$, $1 \le k \le n$).

$k$ enteros distintos: nodos estación.

$m$ líneas $u$ $v$.

## Salida

$n$ enteros en una línea.
