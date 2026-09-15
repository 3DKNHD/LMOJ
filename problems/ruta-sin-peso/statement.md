# Ruta sin peso

Grafo no dirigido **sin pesos**. ¿Cuál es la distancia (número de aristas) de $1$ a $n$? Si no hay camino, imprime $-1$.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Siguen $m$ líneas con $u$ $v$ ($1 \le u,v \le n$). El grafo puede tener bucles y aristas repetidas.

## Salida

Un único entero: $\mathrm{dist}(1,n)$ o $-1$. Si $n=1$ la respuesta es $0$.
