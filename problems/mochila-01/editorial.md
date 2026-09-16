# Editorial: El bolso de la olimpiada

## Qué hay que hacer

$n$ objetos, cada uno **como máximo una vez**. Capacidad $W$. Máximo valor.

## DP de una dimensión, de atrás para adelante

`dp[j]` = mejor valor usando **capacidad exactamente hasta $j$**.

Por cada objeto $(w,v)$:

```
for j = W; j >= w; j--
    dp[j] = max(dp[j], dp[j-w] + v)
```

¿Por qué para atrás? `dp[j-w]` todavía **no** incluye este objeto. Si recorrieras $j$ para adelante, podrías usar el mismo objeto mil veces (eso es el otro problema, el de las monedas).

`dp` en `long long`: $100 \times 10^9$.

## Ejemplo

$W=5$, objetos $(2,3)$ y $(3,4)$.

Después del primero: capacidad $2..5$ valen $3$.
Después del segundo: `dp[5]=max(3, dp[2]+4)=7`, `dp[3]=4`. Respuesta $7$.

## Si te da WA

Loop creciente (unbounded). `int` en `dp`.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, W;
    cin >> n >> W;
    vector<ll> dp(W + 1, 0);
    for (int i = 0; i < n; ++i) {
        int w; ll v;
        cin >> w >> v;
        for (int j = W; j >= w; --j) dp[j] = max(dp[j], dp[j - w] + v);
    }
    cout << dp[W] << "\n";
    return 0;
}
```
