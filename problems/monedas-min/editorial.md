# Editorial: Mínimas monedas

## Qué pide

Monedas **ilimitadas** de $n\le 100$ tipos. Mínimo número para sumar exactamente $S\le 10^5$, o $-1$.

## Idea

DP unbounded knapsack / coin change. `dp[j]` = mínimo monedas para sumar $j$. `dp[0]=0`, resto `INF`.

**Hacia adelante:** para cada moneda $x$, `for j = x..S: dp[j] = min(dp[j], dp[j-x]+1)`.

Así reúsas `dp[j-x]` **ya actualizado** en el mismo pase: puedes usar $x$ varias veces. Eso es ilimitado.

## Contrastar con 0/1

En mochila 0/1 recorres $j$ **de atrás**. Si aquí recorrieras de atrás, cada moneda se usaría **a lo sumo una vez**: otro problema.

## Complejidad

$O(nS) = 100 \cdot 10^5 = 10^7$. Entra.

Greedy por denominación (siempre la más grande) **falla** si las monedas no son canónicas (p.ej. $1,3,4$ y $S=6$: greedy $4+1+1=3$, óptimo $3+3=2$).

## `INF`

`1e9` basta: nunca usas más de $S$ monedas de $1$. Si `dp[S]>=INF`, imposible.

## Trampas

- Recorrer $W$ hacia atrás (0/1).
- Greedy.
- `int` overflow si `INF+1` (usa `min` solo cuando `dp[j-x]` no es INF, o un INF chico).

## Código de referencia (C++)

```cpp
vector<int> dp(S + 1, INF);
dp[0] = 0;
for (int x : c)
    for (int j = x; j <= S; ++j)
        dp[j] = min(dp[j], dp[j - x] + 1);
```
