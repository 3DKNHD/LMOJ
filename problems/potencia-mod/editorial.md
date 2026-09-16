# Editorial: El sello

## Qué hay que hacer

Quieres $a^b$ (a multiplicado por sí mismo $b$ veces) y después el resto al dividir por $10^9+7$. Ese resto es un número entre $0$ y $10^9+6$.

$0^0$ el problema lo define como $1$. Por definición: imprime $1$.

No puedes hacer un `for` de $b$ vueltas: $b$ llega a $10^{18}$. Tu programa tarda demasiado.

## La idea: duplicar el exponente

Mira $3^{13}$. $13$ en binario es $1101_2 = 8+4+1$. Entonces

$$
3^{13} = 3^8 \cdot 3^4 \cdot 3^1
$$

Vas calculando $3, 3^2, 3^4, 3^8, \ldots$ (al cuadrado cada vez) y, si el bit de $b$ vale 1, multiplicas eso al resultado.

Eso se llama **exponenciación binaria**. Hace $\approx 60$ pasos, no $10^{18}$.

## Paso a paso de la función

Empiezas `r = 1` (el valor 1: multiplicar por 1 no cambia el número) y `a = a % MOD` (por si $a$ es más grande que el módulo).

Mientras $b > 0$:

- Si $b$ es impar ($b & 1$), `r = r * a % MOD`.
- `a = a * a % MOD` (pasas al siguiente cuadrado).
- `b = b / 2` (en código `b >>= 1`).

Cuando $b$ llega a $0$, $r$ es la respuesta.

Si $b=0$, el `while` no entra y devuelves $1$. Por eso $0^0$ queda $1$.

## El módulo en cada cuenta

Si haces `r * a` sin `%`, el producto de dos números de mil millones no cabe en `long long`. Multiplica y recorta: `(r * a) % MOD`. Ambos factores deben ser `long long`; si no, C++ multiplica en 32 bits y el resultado ya está mal antes del `%`.

## Si te da TLE / WA

- `for (i=0;i<b;i++)` con $b$ enorme: TLE.
- No recortar módulo en cada producto: overflow → WA.
- Tratar $0^0$ como $0$.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long potencia(long long base, long long exp) {
    base %= MOD;
    long long resultado = 1;
    while (exp > 0) {
        if (exp & 1) {
            resultado = resultado * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    return resultado;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long a, b;
        cin >> a >> b;
        cout << potencia(a, b) << "\n";
    }
    return 0;
}
```
