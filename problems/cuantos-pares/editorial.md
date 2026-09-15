# Editorial: Cuántos pares

## Qué pide

Cuántos $a_i$ son **pares**. El $0$ es par. Los negativos pares ($-2$, $-4$, …) también.

## Idea

Un entero es par sii es divisible por $2$, es decir $a \equiv 0 \pmod{2}$. Cuentas cuántos cumplen eso.

## Cómo chequear paridad (y los negativos)

En matemáticas, $-4 = 2 \cdot (-2)$, así que es par.

**C++:** `x % 2 == 0` funciona para negativos en la práctica del juez (`-4 % 2 == 0`, `-3 % 2 == -1`). No uses `x % 2 == 1` para impares: en C++ un impar negativo da `-1`, no `1`. Si algún día quieres impares, usa `x % 2 != 0`.

**Python:** el módulo es no negativo, así que `x % 2 == 0` también detecta pares negativos.

Equivalente y a prueba de signo:

$$
|x| \bmod 2 = 0
$$

En C++: `llabs(x) % 2 == 0` (ojo: `abs` de `int` no sirve si $x$ es `long long`).

**No uses** `x & 1` sin pensar: en negativos depende de la representación. Para este problema, `% 2 == 0` es lo limpio.

## El cero

$0 = 2 \cdot 0$, es par. Si escribes `if (x != 0 && x % 2 == 0)` estás mal.

## Complejidad

$O(n)$. El contador cabe en `int`.

## Otras soluciones

Convertir a string y mirar el último carácter: funciona, es más lento de escribir y falla si olvidas el signo (`"-4"` termina en `'4'`). No vale la pena.

## Trampas

- Tratar negativos como impares “porque el `%` da raro”.
- Excluir el $0$.
- Usar `x % 2 == 1` copiado de un código de impares.

## Código de referencia (C++)

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
}
```
