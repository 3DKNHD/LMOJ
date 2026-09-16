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

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

bool es_par(long long x) {
    return x % 2 == 0;
}

int contar_pares(const vector<long long>& a) {
    int cuantos = 0;
    for (long long x : a) {
        if (es_par(x)) {
            ++cuantos;
        }
    }
    return cuantos;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << contar_pares(a) << "\n";
    return 0;
}
```
