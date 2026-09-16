# Editorial: La balanza

## Qué hay que hacer

Vas sumando de izquierda a derecha. Después de cada número miras si la suma hasta ahí es par. Cuenta cuántas veces lo fue.

## Truco: no hace falta la suma gigante

Un número es par o impar. La paridad de la suma:

- par + par = par
- impar + impar = par
- par + impar = impar

En código: `pref += x` y después `if (pref % 2 == 0)`. O más limpio con bit: `if ((pref & 1) == 0)` (el último bit es $0$ ⇔ par).

`pref` igual en `long long` porque vas acumulando de verdad.

## Ejemplo

Lista $1, 2, 3, 4$

- pref $1$ impar
- pref $3$ impar
- pref $6$ par → $+1$
- pref $10$ par → $+2$

Respuesta: $2$.

## Si te da WA

Chequeaste si **el elemento** era par, no la **suma del prefijo**.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

bool es_par(long long x) {
    return x % 2 == 0;
}

int contar_prefijos_pares(const vector<long long>& a) {
    long long prefijo = 0;
    int cuantos = 0;
    for (long long x : a) {
        prefijo += x;
        if (es_par(prefijo)) {
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

    cout << contar_prefijos_pares(a) << "\n";
    return 0;
}
```
