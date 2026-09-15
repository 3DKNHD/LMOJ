# Editorial: Dentro del rango

## Qué pide

Cuántos $a_i$ cumplen $L \le a_i \le R$. El intervalo es **cerrado**: $L$ y $R$ sí cuentan.

## Idea

Un contador. Por cada $a_i$, si está entre $L$ y $R$ (inclusive), sumas $1$. No hace falta guardar los que sí entran.

## Por qué no ordenar

Ordenar y luego lower/upper bound también funciona y es $O(n \log n)$. Con $n \le 2 \cdot 10^5$ entra, pero es más código y no aporta. El chequeo directo es $O(n)$ y obvio.

## Inclusivo

$[L, R]$ significa:

- $a_i = L$ **sí**
- $a_i = R$ **sí**
- $a_i = L-1$ no
- $a_i = R+1$ no

El bug `L < a_i < R` (extremos abiertos) falla en cuanto hay un valor igual a $L$ o $R$. El juez mete esos casos.

También te garantizan $L \le R$, así que no hay que invertir el intervalo.

## Negativos

$L$, $R$ y $a_i$ llegan a $-10^9$. Comparar enteros con `<=` funciona igual en negativos. No uses `unsigned`.

## Complejidad

$O(n)$. El contador cabe en `int` ($n \le 2 \cdot 10^5$).

## Otras soluciones

Si más adelante ves **muchas** consultas $[L,R]$ sobre el mismo arreglo, ahí sí ordenas una vez y binarias. Aquí hay **un solo** intervalo.

## Trampas

- Comparación estricta.
- Leer $n$, $L$, $R$ en líneas separadas (van en la **primera** línea, los $a_i$ en la segunda).

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long L, R;
    cin >> n >> L >> R;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (L <= x && x <= R) ++ans;
    }
    cout << ans << "\n";
}
```
