# Editorial: Red mínima

## Qué pide

MST: subconjunto de aristas de costo mínimo que conecta los $n$ nodos. Si el grafo no es conexo, `IMPOSIBLE`. Suma en 64 bits.

## Idea

Kruskal: ordena aristas por $w$ creciente. DSU: añade una arista si une componentes distintas. Al final necesitas exactamente $n-1$ aristas usadas.

El oficial guarda `array<ll,3>` como `(w, u, v)` para que `sort` ordene por peso.

## Por qué es óptimo

Cualquier arista de un corte que no sea de peso mínimo se puede intercambiar (propiedad de corte / greedy matroid). Kruskal recorre en orden y nunca rechaza una arista que haría falta para un MST.

## Prim

Igual de válido: crece un árbol desde un nodo con heap. Si el grafo no es conexo, algunos nodos quedan a distancia INF. Kruskal detecta conexidad con `used == n-1`.

## Un nodo

$n=1$, $m=0$: $0$ aristas, costo $0$. `used==0==n-1`.

## Complejidad

$O(m\log m)$ sort + $O(m\alpha(n))$ DSU.

## Trampas

- Suma en `int` ($m\cdot 10^9$).
- Aceptar grafos con `used < n-1`.
- Kruskal sin DSU (ciclos a mano: TLE).

## Código de referencia (C++)

```cpp
sort(e.begin(), e.end());  // (w, u, v)
for (auto &t : e)
    if (d.unite((int)t[1], (int)t[2])) {
        cost += t[0];
        ++used;
    }
if (used != n - 1) cout << "IMPOSIBLE\n";
```
