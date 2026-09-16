# Editorial: Adelantamientos

## Qué hay que hacer

Una inversión es un par “adelante más alto que atrás”: $i<j$ y $a_i > a_j$. Empate no cuenta.

Contar todos los pares recorriendo todo es $n^2$. No entra.

## La idea

Vas de **izquierda a derecha**. Cuando estás en la posición $i$, ya procesaste $i$ personas de adelante. ¿Cuántas de esas son **más altas** que $a_i$? Esas forman inversión con $i$.

Eso es: total procesadas $i$, menos cuántas son $\le a_i$.

Para responder “cuántos ya vi que son $\le x$” rápido, usas un árbol de frecuencias (Fenwick) sobre los **valores**. Como los valores llegan a $10^9$, primero los comprimes: el más pequeño pasa a $1$, el siguiente distinto a $2$, etc. El orden se mantiene.

## Paso a paso

1. Copia la lista, ordénala, saca repetidos: eso es el diccionario.
2. Reemplazá cada $a_i$ por su ranking ($1..$cuántos distintos).
3. Fenwick vacío. `ans=0`.
4. Para $i = 0..n-1$:
   - `ans += i - fw.sum(a[i])`  // procesados menos los $\le a_i$
   - `fw.add(a[i], 1)`          // ahora esta persona existe
5. Imprime `ans` en `long long`.

## Ejemplo

$3, 1, 2$

- $3$: nadie adelante → $0$, anoto el $3$
- $1$: hay $1$ adelante y ninguno $\le 1$ → $+1$
- $2$: hay $2$ adelante, uno $\le 2$ (el $1$) → $+1$

Total $2$: $(3,1)$ y $(3,2)$. $(1,2)$ no es inversión.

## Si te da TLE / WA

$O(n^2)$. O $i < j$ con $a_i \ge a_j$ (contaste empates).

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> t;
    Fenwick(int n) : n(n), t(n + 1, 0) {}
    void add(int i, int v) {
        for (; i <= n; i += i & -i) t[i] += v;
    }
    int sum(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += t[i];
        return s;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    vector<int> b = a;
    sort(b.begin(), b.end());
    b.erase(unique(b.begin(), b.end()), b.end());
    for (int &x : a) x = int(lower_bound(b.begin(), b.end(), x) - b.begin()) + 1;
    Fenwick fw((int)b.size());
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += i - fw.sum(a[i]);
        fw.add(a[i], 1);
    }
    cout << ans << "\n";
    return 0;
}
```
