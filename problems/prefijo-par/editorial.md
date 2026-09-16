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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long pref = 0;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        pref += x;
        if ((pref & 1) == 0) ++ans;
    }
    cout << ans << "\n";
    return 0;
}
```
