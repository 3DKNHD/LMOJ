# Editorial: Chapas pares

## Qué hay que hacer

Un número es **par** si al dividirlo por $2$ el resto es $0$. Ejemplos: $4$, $0$, $-2$. Impares: $3$, $-1$.

Te dan $n$ números. Cuenta cuántos son pares. Imprime ese contador.

## Paso a paso

1. Lee $n$.
2. `ans = 0`.
3. Por cada número $x$: si $x$ es par, $ans++$.
4. Imprime `ans`.

## Cómo saber si es par en C++

```cpp
if (x % 2 == 0)
```

`%` es el resto. El $0$ es par: $0\% 2 = 0$. Un negativo par ($-4$) también: en C++ $(-4)\% 2 = 0$.

## Ejemplo

Lista: $5,\ 0,\ -4,\ 7,\ 8$.

- $5$ impar
- $0$ par → $1$
- $-4$ par → $2$
- $7$ impar
- $8$ par → $3$

Respuesta: $3$.

## Si te da WA

Trataste el $0$ como impar. O usaste $x % 2 == 1$ para “impar”: en C++ los negativos pueden dar resto $-1$, no $1$. Para pares, comparado con $0$ estás bien.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (x % 2 == 0) ++ans;
    }
    cout << ans << "\n";
    return 0;
}
```
