# Editorial: La colecta

## Qué hay que hacer

Te dan una lista de $n$ números. Los sumas todos. Imprime un solo número: el total.

## Paso a paso

1. Lee $n$.
2. Crea una variable `s = 0` de tipo `long long`.
3. Repite $n$ veces: lees un número y se lo sumas a $s$.
4. Imprime `s`.

No hace falta guardar la lista. Vas sumando al vuelo.

## Ejemplo

`n=4` y la lista `3 -1 10 0`.

- empiezo en $0$
- $+3 \to 3$
- $-1 \to 2$
- $+10 \to 12$
- $+0 \to 12$

Respuesta: $12$.

## Por qué `long long`

Cada $a_i$ llega a $10^9$ y hay hasta $2\cdot 10^5$ números. El peor total es $2\cdot 10^5 \cdot 10^9 = 2\cdot 10^{14}$. Eso **no entra en `int`**. Entra en `long long`.

Si usas `int`, en un caso grande el total se da vuelta y el juez te pone WA. En el sample chico te va a dar bien y puede parecer que está todo OK.

## Si te da WA

`int` en el acumulador. O te olvidaste de leer los $n$ números y sumaste basura.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

long long suma(const vector<long long>& a) {
    long long total = 0;
    for (long long x : a) {
        total += x;
    }
    return total;
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

    cout << suma(a) << "\n";
    return 0;
}
```
