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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

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
    return 0;
}
```
