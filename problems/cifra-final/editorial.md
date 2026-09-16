# Editorial: El candado

## Qué hay que hacer

La última cifra de $17$ es $7$. La de $100$ es $0$. La de $-17$ **también** es $7$: el candado no entiende el signo, mira el valor absoluto.

Eso es $|n|$ módulo $10$. “Módulo $10$” = el resto de dividir por $10$ = el último dígito.

## Paso a paso

1. Lee $T$.
2. Por cada $n$:
   - Si $n$ es negativo, pon $n = -n$ (ahora es positivo o cero).
   - Imprime $n \% 10$.

## Por qué `n % 10` crudo te rompe en C++

En C++ el `%` **copia el signo** del número de la izquierda.

| $n$ | $n % 10$ en C++ | lo que el juez quiere |
|-----|-----------------|------------------------|
| $17$ | $7$ | $7$ |
| $-17$ | $-7$ | $7$ |
| $-10$ | $0$ | $0$ |

Si imprimes `-7`, WA. Por eso **primero** sacas el signo.

En Python `(-17) % 10` da $3$ (regla distinta). Tampoco sirve crudo. Haz $abs(n) % 10$.

## Ejemplo

$-17 \to 17 \to 7$.  
$0 \to 0$.  
$100 \to 0$.

## Si te da WA

No sacaste el signo. O imprimiste el número entero en vez de un dígito.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

long long ultima_cifra(long long n) {
    if (n < 0) {
        n = -n;
    }
    return n % 10;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long n;
        cin >> n;
        cout << ultima_cifra(n) << "\n";
    }
    return 0;
}
```
