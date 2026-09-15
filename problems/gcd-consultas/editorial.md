# Editorial: GCD en rango

## Qué pide

Arreglo estático, $q$ consultas $\gcd(a_L,\dots,a_R)$ en $O(1)$ tras preprocess. $n,q\le 10^5$.

## Idea

Sparse table. GCD es **idempotente y asociativo**: $\gcd(x,x)=x$, solapar rangos no cambia el gcd.

`st[k][i] = gcd` de $2^k$ elementos desde $i$. Transición:

$$
\mathrm{st}[k][i] = \gcd(\mathrm{st}[k-1][i],\ \mathrm{st}[k-1][i+2^{k-1}])
$$

Query de longitud $\ell=R-L+1$, $k=\lfloor\log_2 \ell\rfloor$:

$$
\gcd(\mathrm{st}[k][L],\ \mathrm{st}[k][R-2^k+1])
$$

Los dos bloques de longitud $2^k$ cubren $[L,R]$ y **se solapan**; para GCD está bien. Para suma **no** (por eso suma usa prefijos, no ST de este estilo).

## `log`

El oficial: `k = 31 - __builtin_clz(r-l+1)` para `int` positivo. No uses `log2` de `double`.

## Complejidad

Build $O(n\log n)$, query $O(1)$, memoria $O(n\log n)$.

## Otras soluciones

Segment tree $O(\log n)$ por query: más lento de escribir, válido. Euclidean saltando por $\sqrt{}$: no.

## Trampas

- Sparse table de **suma** copiada (solape doble cuenta).
- `gcd` de 0: aquí $a_i\ge 1$.
- `LOG` corto (`1<<LOG <= n`).

## Código de referencia (C++)

```cpp
for (int k = 1; k < LOG; ++k)
    for (int i = 1; i + (1 << k) - 1 <= n; ++i)
        st[k][i] = gcd(st[k-1][i], st[k-1][i + (1 << (k-1))]);
int k = 31 - __builtin_clz(r - l + 1);
gcd(st[k][l], st[k][r - (1 << k) + 1])
```
