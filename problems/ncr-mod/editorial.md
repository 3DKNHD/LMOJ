# Editorial: Combinatoria módulo

## Qué pide

$T\le 10^5$ veces $C(n,k)\bmod 10^9+7$, $n,k\le 10^6$. $C(n,k)=0$ si $k>n$. $C(0,0)=1$.

## Idea

$$
C(n,k) = \frac{n!}{k!(n-k)!}
$$

Módulo primo $M=10^9+7$, el inverso de $k!$ existe. Precalcula:

- `fac[i] = i!`
- `ifac[N] = (N!)^{-1}` con Fermat: `binpow(fac[N], M-2)`
- `ifac[i-1] = ifac[i] * i` hacia atrás

Query: `fac[n] * ifac[k] * ifac[n-k] % M` si $0\le k\le n$, else $0$.

## Por qué no binpow por query para el inverso

$T\cdot\log M$ de un inverso suelto entra, pero $k!$ distinto cada vez sin `ifac` sería lento o repetido. Un pase $O(N+\log M)$ y luego $O(1)$ por query es lo limpio.

## $C(0,0)$

`fac[0]=ifac[0]=1`. Fórmula da $1$.

## Complejidad

$O(N + T)$. $N=10^6$.

## Otras soluciones

Lucas si $n$ fuera $\gg M$ (aquí $n < M$). Pascal $O(n^2)$: muerto.

## Trampas

- Multiplicar sin `%` intermedio (`fac*ifac*ifac` puede $10^{27}$).
- No tratar $k>n$.
- Inverso de $0$ si alguien hace `ifac[k]` con $k>n$ sin el `if`.

## Código de referencia (C++)

```cpp
fac[0] = 1;
for (int i = 1; i <= N; ++i) fac[i] = fac[i-1] * i % MOD;
ifac[N] = binpow(fac[N], MOD - 2);
for (int i = N; i >= 1; --i) ifac[i-1] = ifac[i] * i % MOD;
// query:
fac[n] * ifac[k] % MOD * ifac[n-k] % MOD
```
