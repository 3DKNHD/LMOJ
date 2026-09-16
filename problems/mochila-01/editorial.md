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

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Objeto {
    int peso;
    long long valor;
};

long long mochila(int capacidad, const vector<Objeto>& objetos) {
    vector<long long> dp(capacidad + 1, 0);
    for (const auto& obj : objetos) {
        for (int w = capacidad; w >= obj.peso; --w) {
            dp[w] = max(dp[w], dp[w - obj.peso] + obj.valor);
        }
    }
    return dp[capacidad];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, capacidad;
    cin >> n >> capacidad;
    vector<Objeto> objetos(n);
    for (int i = 0; i < n; ++i) {
        cin >> objetos[i].peso >> objetos[i].valor;
    }

    cout << mochila(capacidad, objetos) << "\n";
    return 0;
}
```
