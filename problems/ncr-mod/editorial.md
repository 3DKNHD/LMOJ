# Editorial: El jurado

## Qué hay que hacer

$C(n,k)$ = de $n$ personas, cuántos jurados de $k$. Fórmula:

$$
C(n,k) = \frac{n!}{k!\,(n-k)!}
$$

Módulo $10^9+7$ (un primo). Si $k>n$ o $k<0$, $0$. $C(0,0)=1$.

No puedes calcular el factorial y dividir en enteros normales: $1000000!$ tiene más dígitos que el universo.

## Cómo “dividir” módulo un primo

No se puede dividir en enteros y luego recortar. El inverso de $x$ es un $y$ tal que $x\cdot y$ deja resto $1$ al dividir por $p$. Entonces “dividir por $x$” es multiplicar por $y$.

Si $p$ es primo, $y = x^{p-2} \bmod p$ (teorema de Fermat). Esa potencia se calcula igual que en “El sello”.

Precalculas **una vez**:

- `fac[i] = i! % MOD`
- `ifac[N] = inverso de fac[N]`
- `ifac[i-1] = ifac[i] * i % MOD` (para atrás)

Consulta: `fac[n] * ifac[k] * ifac[n-k] % MOD`.

## Si te da TLE / WA

Factorial por consulta. O `double`. O no hacer `%` en el producto de tres números.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;
const int MAXN = 1000000;

long long potencia(long long base, long long exp) {
    long long resultado = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) {
            resultado = resultado * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    return resultado;
}

struct Combinatoria {
    vector<long long> fact;
    vector<long long> inv_fact;

    Combinatoria(int tam) : fact(tam + 1), inv_fact(tam + 1) {
        fact[0] = 1;
        for (int i = 1; i <= tam; ++i) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        inv_fact[tam] = potencia(fact[tam], MOD - 2);
        for (int i = tam; i >= 1; --i) {
            inv_fact[i - 1] = inv_fact[i] * i % MOD;
        }
    }

    long long ncr(int n, int k) const {
        if (k < 0 || k > n) {
            return 0;
        }
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Combinatoria comb(MAXN);

    int casos;
    cin >> casos;
    while (casos--) {
        int n, k;
        cin >> n >> k;
        cout << comb.ncr(n, k) << "\n";
    }
    return 0;
}
```
