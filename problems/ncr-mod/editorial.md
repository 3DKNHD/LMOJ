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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD = 1000000007LL;
ll binpow(ll a, ll e) {
    ll r=1; a%=MOD;
    while (e) { if (e&1) r=r*a%MOD; a=a*a%MOD; e>>=1; }
    return r;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    const int N=1000000;
    vector<ll> fac(N+1), ifac(N+1);
    fac[0]=1;
    for (int i=1;i<=N;++i) fac[i]=fac[i-1]*i%MOD;
    ifac[N]=binpow(fac[N], MOD-2);
    for (int i=N;i>=1;--i) ifac[i-1]=ifac[i]*i%MOD;
    int T; cin>>T;
    while (T--) {
        int n,k; cin>>n>>k;
        if (k<0 || k>n) cout<<"0\n";
        else cout << fac[n]*ifac[k]%MOD*ifac[n-k]%MOD << "\n";
    }
    return 0;
}
```
