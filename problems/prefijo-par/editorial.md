# Editorial: Prefijos pares

## Qué pide

Cuántos índices $i$ cumplen que $s_i = a_1+\cdots+a_i$ es **par**.

## Idea

Solo importa la paridad. Recorres una vez, mantienes la suma (o su bit de paridad) y cuentas cuántas veces queda par.

Un número es par sii su bit bajo es $0$. En complemento a dos, eso también vale para negativos: $-2$ es par, `-2 & 1 == 0` en C++.

Equivalente: `if (pref % 2 == 0)` con `pref` en `long long`. En C++, `(-2) % 2 == 0`, `(-1) % 2 == -1`, así que `== 0` detecta pares.

## Por qué no hace falta el valor de la suma

$s_i$ par $\iff s_{i-1}$ y $a_i$ tienen la **misma** paridad (par+par o impar+impar). Puedes guardar solo `pref ^= (a_i & 1)` o sumar `a_i` entero; ambas van.

El oficial suma el `long long` completo y mira `(pref & 1) == 0`. Correcto y simple.

## Complejidad

$O(n)$, memoria $O(1)$ extra. $n \le 2\cdot 10^5$.

## Otras soluciones

- Guardar todos los $s_i$ y filtrar: innecesario.
- Contar prefijos **impares** y restar de $n$: mismo trabajo.

No confundir con “cuántos **subarreglos** de suma par”. Eso es otro problema (mapa de paridades de prefijo, $O(n)$ también, pero no es este enunciado). Aquí son solo prefijos, no todos los $[L,R]$.

## Trampas

- Usar `pref % 2 == 1` para impares en C++ con negativos (`%` negativo).
- Olvidar que el prefijo de longitud $1$ también cuenta.
- Acumulador `int` (la suma puede no caber; la paridad sí, pero si sumas el valor crudo, desborda y el bit puede corromperse en `int`).

## Código de referencia (C++)

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
}
```
