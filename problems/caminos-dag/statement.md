# Caminos en DAG

Grafo **dirigido acíclico**. Número de caminos de $1$ a $n$ módulo $10^9+7$.
DP en orden topológico: $dp[v] += dp[u]$ para cada $u \rightarrow v$.

El generador no mete ciclos. $dp[1]=1$.

## Entrada

$n$ $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

$m$ líneas $u$ $v$ (arco $u \rightarrow v$, $1 \le u,v \le n$).

## Salida

Un entero.
