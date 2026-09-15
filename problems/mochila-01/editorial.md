# Editorial: Mochila 0/1

## Qué pide

Cada objeto **a lo sumo una vez**. Máximo valor con capacidad $W$. $n\cdot W \le 10^7$. Valores en 64 bits.

## Idea

`dp[j]` = mejor valor con capacidad exacta $\le j$ (el oficial usa capacidad $\le j$ implícita al tomar `max` hacia $W$).

Para cada objeto $(w,v)$, recorre $j$ **de $W$ bajando hasta $w$**:

```text
dp[j] = max(dp[j], dp[j-w] + v)
```

Al ir hacia atrás, `dp[j-w]` **aún no** incluye este objeto: no lo usas dos veces.

## Contrastar con monedas

Unbounded recorre $j$ hacia **adelante**. 0/1 hacia **atrás**. Es el único cambio de dirección que cambia el problema.

## Complejidad

$O(nW)$. Un `dp[n][W]` 2D también, pero $100\times 10^5$ enteros 64-bit pesan; 1D basta.

## Trampas

- Recorrer $j$ creciente: usas el objeto varias veces (unbounded).
- `int` en `v` y `dp` ($100\cdot 10^9$).
- Capacidad `j >= w` mal (olvidar el objeto si $w=W$).

## Código de referencia (C++)

```cpp
vector<ll> dp(W + 1, 0);
for (cada objeto w, v)
    for (int j = W; j >= w; --j)
        dp[j] = max(dp[j], dp[j - w] + v);
cout << dp[W] << "\n";
```
