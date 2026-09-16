# Editorial: La plata

## Qué hay que hacer

Quieres la **segunda más grande**, pero mirando valores **distintos**. Si el oro es $10$ y aparece diez veces, esas diez no sirven para la plata. La plata es el siguiente número más grande que **no sea** $10$.

Si todos son iguales, no hay plata: imprimes `-1`.

## La idea (un solo pase)

Guarda dos variables:

- `m1`: lo más grande que viste hasta ahora (el oro).
- `m2`: lo segundo más grande distinto (la plata). Al principio las dos valen un número muy pequeño, tipo $-2^{60}$, que no puede aparecer en la lista.

Por cada $x$:

1. Si $x > m1$: el oro viejo baja a plata, $x$ es el oro nuevo. $m2 = m1; m1 = x;$
2. Si $x$ es más pequeño que el oro **y** más grande que la plata: $x$ es una plata mejor. $m2 = x;$
3. Si $x$ es igual al oro: no hagas nada. Es otro intento del mismo salto.

Al final, si `m2` sigue siendo el número ridículo, no hubo plata → `-1`.

## Ejemplo del enunciado

$5,1,5,3,3,4$

| $x$ | oro $m1$ | plata `m2` |
|-----|----------|------------|
| $5$ | $5$ | (vacío) |
| $1$ | $5$ | $1$ |
| $5$ | $5$ | $1$ (no cambia) |
| $3$ | $5$ | $3$ |
| $3$ | $5$ | $3$ |
| $4$ | $5$ | $4$ |

Respuesta: $4$.

## Si te da WA

- Tomaste el segundo del arreglo ordenado **con repetidos**: en $5,5,4$ dirías $5$ y es $4$.
- Ordenaste y agarraste `a[n-2]` sin sacar duplicados.
- Inicializaste en $0$ y había negativos.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MENOS_INF = -(1LL << 60);

long long segundo_maximo_estricto(const vector<long long>& a) {
    long long primero = MENOS_INF;
    long long segundo = MENOS_INF;

    for (long long x : a) {
        if (x > primero) {
            segundo = primero;
            primero = x;
        } else if (x < primero && x > segundo) {
            segundo = x;
        }
    }

    if (segundo == MENOS_INF) {
        return -1;
    }
    return segundo;
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

    cout << segundo_maximo_estricto(a) << "\n";
    return 0;
}
```
