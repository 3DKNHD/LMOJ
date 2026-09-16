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

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> t;

    Fenwick(int tam) : n(tam), t(tam + 1, 0) {}

    void agregar(int i, int v) {
        for (; i <= n; i += i & -i) {
            t[i] += v;
        }
    }

    int prefijo(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) {
            s += t[i];
        }
        return s;
    }
};

vector<int> comprimir(vector<int> a) {
    vector<int> orden = a;
    sort(orden.begin(), orden.end());
    orden.erase(unique(orden.begin(), orden.end()), orden.end());
    for (int& x : a) {
        x = int(lower_bound(orden.begin(), orden.end(), x) - orden.begin()) + 1;
    }
    return a;
}

long long contar_inversiones(vector<int> a) {
    a = comprimir(a);
    int maximo = 0;
    for (int x : a) {
        maximo = max(maximo, x);
    }

    Fenwick fw(maximo);
    long long inversiones = 0;
    for (int i = 0; i < (int)a.size(); ++i) {
        inversiones += i - fw.prefijo(a[i]);
        fw.agregar(a[i], 1);
    }
    return inversiones;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << contar_inversiones(a) << "\n";
    return 0;
}
```
