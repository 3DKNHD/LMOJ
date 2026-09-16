# Editorial: En el presupuesto

## Qué hay que hacer

Te dan un intervalo cerrado $[L, R]$: “desde $L$ hasta $R$, **incluyendo** los dos extremos”. Después una lista. Cuenta cuántos de la lista caen adentro.

“Cerrado” quiere decir: si el número es exactamente $L$ o exactamente $R$, **cuenta**.

## Paso a paso

1. Lee $n$, $L$ y $R$.
2. `ans = 0`.
3. Por cada $x$: si $L \le x$ **y** $x \le R$, sumas uno.
4. Imprime `ans`.

En código:

```cpp
if (L <= x && x <= R) ++ans;
```

Las dos condiciones. Si pones solo una, estás contando de más o de menos.

## Ejemplo

$L=3$, $R=7$, lista $1,\ 3,\ 5,\ 7,\ 8$.

- $1$ no
- $3$ sí (es el borde)
- $5$ sí
- $7$ sí (el otro borde)
- $8$ no

Respuesta: $3$.

## Si te da WA

Usaste $<$ en vez de $\le$ y te comiste los bordes. O te mezclaste $L$ y $R$.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

bool esta_en_rango(long long x, long long izq, long long der) {
    return izq <= x && x <= der;
}

int cuantos_en_rango(const vector<long long>& a, long long izq, long long der) {
    int cuantos = 0;
    for (long long x : a) {
        if (esta_en_rango(x, izq, der)) {
            ++cuantos;
        }
    }
    return cuantos;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long izq, der;
    cin >> n >> izq >> der;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << cuantos_en_rango(a, izq, der) << "\n";
    return 0;
}
```
