# Editorial: Caminos en DAG

## Qué pide

Número de caminos $1\rightsquigarrow n$ módulo $10^9+7$ en un DAG. `dp[1]=1`. El pack no mete ciclos.

## Idea

$dp[v]$ = número de formas de llegar de $1$ a $v$. Para cada arco $u\to v$:

$$
dp[v] \leftarrow (dp[v] + dp[u]) \bmod M
$$

Hay que procesar $u$ **antes** que $v$: orden topológico (Kahn). `dp[1]=1` de entrada; si $1$ no tiene arcos salientes y $n\neq 1$, $dp[n]=0$.

## Por qué toposort

Si procesas en orden arbitrario, usas $dp[u]$ incompleto. En un DAG el toposort existe. El generador garantiza aciclicidad; si hubiera ciclo, Kahn no vacía la cola y $dp[n]$ quedaría corto.

## $n=1$

`dp[1]=1`, cero arcos: $1$ camino “vacío” (el nodo solo). Suele ser la convención pedida.

## Complejidad

$O(n+m)$.

## DFS + memo

`f(v)` = suma `f(u)` sobre arcos a $v$, o al revés desde $1$ hacia vecinos. Cuidado con el stack. Kahn es iterativo.

## Trampas

- No modular.
- `dp[1]=0`.
- Contar caminos **simples** vs todas las walks: en DAG no hay ciclos, coinciden.
- Grafos con aristas a $1$ que inflan `dp[1]` si las procesas encima del $1$ inicial (el pack parte $1$ como fuente).

## Código de referencia (C++)

```cpp
dp[1] = 1;
// Kahn
for (int v : g[u]) {
    dp[v] = (dp[v] + dp[u]) % MOD;
    if (--indeg[v] == 0) q.push(v);
}
cout << dp[n] << "\n";
```
