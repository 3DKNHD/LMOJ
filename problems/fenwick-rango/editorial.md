# Editorial: Suma con updates

## Qué pide

Point add y suma de rango. $n,q\le 2\cdot 10^5$: prefijos estáticos no sirven (el arreglo **cambia**).

## Idea

Fenwick (BIT). Índice $i$ cubre $(i\ \&\ -i)$ posiciones. 

- `add(i,x)`: $a_i \leftarrow a_i+x$
- `pref(r)`: suma $a_1+\cdots+a_r$
- rango: `pref(R)-pref(L-1)`

Construyes el BIT con $n$ `add` iniciales.

## Por qué no array de prefijos

Un update $a_i$ obliga a recomputar $p_i..p_n$: $O(n)$ por update, TLE.

Segment tree de suma también $O(\log n)$; Fenwick es más corto.

## 64 bits

Valores y $x$ $\pm 10^9$, $n$ updates: las celdas del BIT llegan a $\sim 2\cdot 10^5\cdot 10^9$. `long long`.

## Índices

BIT clásico es **1-based**. `i += i & -i`. `i==0` entra en bucle infinito.

## Complejidad

$O((n+q)\log n)$.

## Trampas

- Tipo 1 como *asignar* $a_i=x$ en vez de **sumar** $x$. El enunciado es add.
- `int` en el árbol.
- `pref(l)-pref(r)` invertido.

## Código de referencia (C++)

```cpp
void add(int i, ll v) { for (; i <= n; i += i & -i) t[i] += v; }
ll pref(int i) { ll r = 0; for (; i > 0; i -= i & -i) r += t[i]; return r; }
ll range(int l, int r) { return pref(r) - pref(l - 1); }
```
