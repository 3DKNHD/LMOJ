# Editorial: Sesiones sin choque

## Qué pide

Máximo número de intervalos **cerrados** $[L,R]$ que no se pisan. Si uno termina en $t$ y otro empieza en $t$, **chocan**. $n \le 2\cdot 10^5$.

## Idea

Greedy clásico de *activity selection*: ordena por **tiempo de fin** creciente y toma una sesión si su $L$ es **estrictamente mayor** que el fin de la última tomada.

Por qué greedy: entre todas las soluciones óptimas, existe una que incluye la actividad que termina primero (si no, reemplazas la primera de la óptima por esa: termina antes o igual y no empeora el resto). Inducción en el resto.

## Por qué $L > last$, no $L \ge last$

Intervalos cerrados. $[1,5]$ y $[5,8]$ comparten el instante $5$. Si usas `>=`, las cuentas como compatibles: WA.

El oficial guarda `last` = $R$ de la última aceptada, y exige `l > last`.

## Cómo guardar los pares

Ordenar por $R$. El oficial mete `(R, L)` en el `pair` para que `sort` use el primer campo:

```cpp
cin >> a[i].second >> a[i].first;  // L, R → pair es (R, L)
sort(a.begin(), a.end());
```

Si hay empate en $R$, da igual el $L$ para la corrección del greedy estándar (el que termina igual: tomar el de $L$ más grande no cambia el invariante de “terminar lo antes posible” entre iguales; ambas variantes dan óptimo).

## Complejidad

$O(n \log n)$ por el sort, $O(n)$ del barrido. Memoria $O(n)$.

## Otras soluciones

- DP $O(n^2)$: TLE.
- Ordenar por $L$: **no** es óptimo. Contraejemplo típico: $[1,100]$, $[2,3]$, $[4,5]$. Por $L$ tomas el largo y te quedas con $1$; por $R$ tomas los dos cortos.
- Sweep line con “máximo de activos” resuelve **pico de cobertura**, no este problema (aquí quieres un subconjunto independiente máximo, no el máximo solape).

## Trampas

- Tratar toque en un punto como compatible.
- Greedy por inicio o por duración.
- `int last` y $R=10^9$ está bien; el oficial usa `long long` de centinela inicial $-(2^{60})$.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].second >> a[i].first;
    sort(a.begin(), a.end());
    int ans = 0;
    long long last = -(1LL << 60);
    for (auto [r, l] : a) {
        if (l > last) {
            ++ans;
            last = r;
        }
    }
    cout << ans << "\n";
}
```
