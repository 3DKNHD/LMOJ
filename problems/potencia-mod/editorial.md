# Editorial: Potencia módulo

## Qué pide

$T$ consultas independientes: $a^b \bmod (10^9+7)$. Convención: $0^0 = 1$. $a$ y $b$ llegan a $10^{18}$.

## Idea

Exponenciación binaria (binpow). Escribes $b$ en binario. Si $b = \sum b_k 2^k$, entonces

$$
a^b = \prod_k a^{2^k}
$$

solo en los bits $b_k = 1$. Empiezas con `r = 1`, `base = a`, y en cada paso:

- si el bit bajo de $b$ está prendido, `r = r * base % MOD`
- `base = base * base % MOD`
- `b >>= 1`

Son $O(\log b)$ multiplicaciones, no $O(b)$.

## Por qué $0^0 = 1$ sale sola

Con `r = 1` y `while (b > 0)`, si $b = 0$ no entras al bucle y devuelves $1$. Eso cubre $0^0$ y también $a^0 = 1$ para cualquier $a$.

Si haces `if (a == 0) return 0;` te comes $0^0$ y $0^b$ con $b>0$ a la vez: WA en $0^0$.

## Reducir $a$ antes

$a$ puede ser $10^{18}$. Una multiplicación `a * a` sin módulo explota hasta $10^{36}$. Hay que hacer `a %= MOD` **antes** del bucle. $10^9+7$ es primo, no hace falta Euler para este problema: $b$ no se reduce módulo $\varphi(M)$ a menos que sepas lo que haces (y $0^b$ se complica). Aquí $b$ entra crudo al binpow; solo $a$ se reduce.

`a %= MOD` con $a \ge 0$ deja $a$ en $[0, M)$. El oficial también contempla $a < 0$ por costumbre; los límites son $\ge 0$.

## Multiplicar en 64 bits

`r * a % MOD`: `r` y `a` son $< M \approx 10^9$, el producto cabe en `long long` ($< 10^{18}$). Si usas `int`, el producto se desborda **antes** del `%`.

## Complejidad

$O(T \log b)$ con $T \le 10^5$, $\log(10^{18}) \approx 60$. Entra. Un bucle `for (i=0;i<b;i++)` es TLE.

## Otras soluciones

- Recursivo `if (b even) sq(a^{b/2})` es lo mismo; iterativo evita stack.
- `std::pow` de `double` pierde enteros grandes: WA.
- Fermat $a^{b \bmod (M-1)}$ **solo** si $M \nmid a$. Falla en múltiplos de $M$ y en $0^0$. No lo uses aquí.

## Trampas

- No modular el producto.
- Tratar $0^0$ como $0$.
- `int` en las multiplicaciones.
- I/O lento con $T = 10^5$.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long binpow(long long a, long long b) {
    a %= MOD;
    long long r = 1;
    while (b > 0) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        long long a, b;
        cin >> a >> b;
        cout << binpow(a, b) << "\n";
    }
}
```
