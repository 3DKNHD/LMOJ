# Editorial: El vuelto

## Qué hay que hacer

Monedas **ilimitadas** de cada tipo. Mínima cantidad para sumar exactamente $S$, o $-1$.

## DP hacia adelante (al revés que la mochila $0/1$)

`dp[j]` = mínimas monedas para armar $j$. $dp[0]=0$, el resto “infinito” (`1e9`).

Por cada tipo $c$:

```
for j = c; j <= S; j++
    dp[j] = min(dp[j], dp[j-c] + 1)
```

Para **adelante**: `dp[j-c]` **ya puede** haber usado $c$, así que puedes repetir el tipo. Eso es lo que quieres aquí.

Si `dp[S]` sigue infinito, `-1`.

## Contrastá con el bolso

Mochila $0/1$: $j$ **baja**. Monedas: $j$ **sube**. Ese es el único cambio de dirección y cambia el problema por completo.

## Si te da WA

Loop hacia atrás (cada moneda una vez). O no imprimir `-1`.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,S; cin>>n>>S;
    vector<int> c(n);
    for (int i=0;i<n;++i) cin>>c[i];
    const int INF=1e9;
    vector<int> dp(S+1, INF);
    dp[0]=0;
    for (int x: c)
        for (int j=x;j<=S;++j) dp[j]=min(dp[j], dp[j-x]+1);
    cout << (dp[S]>=INF ? -1 : dp[S]) << "\n";
    return 0;
}
```
