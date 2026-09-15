# Editorial: ¿Es bipartito?

## Qué pide

¿El grafo no dirigido es 2-coloreable? Componentes sueltas: todas deben serlo. Un triángulo $\Rightarrow$ `NO`.

## Idea

BFS (o DFS) por componente. Colores $0/1$. Al visitar $v$:

- sin color: `col[v] = col[u]^1`
- mismo color que $u$: arista impar, no bipartito

Un grafo es bipartito sii no tiene ciclos impares. El 2-coloreado lo detecta.

## Varias componentes

El `for s=1..n` arranca un BFS por cada no pintado. Un nodo aislado es bipartito (un color).

## Bucles $u-u$

Arista a sí mismo: `col[v]==col[u]` en el mismo nodo $\Rightarrow$ `NO`. Correcto (ciclo impar de longitud 1, o no 2-coloreable).

## Complejidad

$O(n+m)$.

## Trampas

- Pintar una sola componente.
- `SI`/`NO` mal escrito.
- DFS recursivo en estrella $10^5$: stack; BFS es más seguro.

## Código de referencia (C++)

```cpp
if (col[v] == -1) { col[v] = col[u] ^ 1; q.push(v); }
else if (col[v] == col[u]) { cout << "NO\n"; return 0; }
```
