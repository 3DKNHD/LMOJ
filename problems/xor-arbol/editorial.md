# Editorial: XOR en el árbol

## Qué pide

XOR de los $a_i$ en el camino $u$–$v$ (ambos extremos). $n,q\le 2\cdot 10^4$. Árbol.

## Idea

XOR de prefijos a la raíz más LCA.

`pxor[x]` = $a_{r} \oplus \cdots \oplus a_x$ en el camino raíz $\to x$ (el oficial: raíz $=1$, `pxor[1]=a[1]`).

El camino $u$–$v$ es $u\rightsquigarrow\mathrm{lca}$ más $\mathrm{lca}\rightsquigarrow v$. En XOR:

$$
\mathrm{pxor}[u] \oplus \mathrm{pxor}[v] \oplus a[\mathrm{lca}]
$$

Porque `pxor[u] ^ pxor[v]` cancela el camino raíz–lca **dos veces** (queda $0$) y deja $(u..\mathrm{lca})$ y $(v..\mathrm{lca})$ **sin** $a[\mathrm{lca}]$. Hay que volver a XOR-ear $a[\mathrm{lca}]$.

Si $u=v$: `pxor[u]^pxor[u]^a[u] = a[u]`. Correcto.

## LCA

Binary lifting: `up[x][k]` = $2^k$-ésimo padre. `LOG=16` porque $2^{16}>2\cdot 10^4$. Subes el más profundo, luego subes a la vez hasta que los padres coinciden.

## Complejidad

Build $O(n\log n)$, query $O(\log n)$. $q\cdot 16$ holgado.

DFS recursivo con $n=2\cdot 10^4$ suele vivir; una cadena profunda en otros jueces pediría DFS iterativo. Aquí $n$ es chico a propósito.

## Otras soluciones

Euler tour + RMQ sobre `depth` para LCA. O HLD. Overkill.

## Trampas

- Olvidar `^ a[lca]` (camino sin el lca).
- `pxor` sin incluir $a$ del nodo.
- `LOG` corto.
- Tratar el grafo como dirigido.

## Código de referencia (C++)

```cpp
int w = lca(u, v);
int ans = pxor[u] ^ pxor[v] ^ a[w];
```
