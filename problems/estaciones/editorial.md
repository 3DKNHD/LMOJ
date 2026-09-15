# Editorial: Estaciones más cercanas

## Qué pide

Para **cada** nodo, distancia (en aristas) a la estación más cercana, o $-1$. $k$ estaciones, grafo no dirigido sin pesos.

## Idea

BFS **multi-fuente**: metes las $k$ estaciones en la cola con `dist=0` **al mismo tiempo**. Un BFS normal desde un super-nodo virtual conectado a las estaciones (peso 0) es lo mismo.

La primera vez que visitas $v$ es desde la estación más cercana: todas las aristas pesan $1$.

## Por qué no $k$ BFS

$k\cdot(n+m)$ con $k,n\sim 10^5$: TLE. Un solo BFS $O(n+m)$.

## Estaciones repetidas

El enunciado dice distintas. Si duplicaras, `d[s]==0` ya puesto evita reencolar.

## Complejidad

$O(n+m)$.

## Trampas

- BFS desde cada estación.
- Dijkstra (innecesario).
- No imprimir $n$ números (uno por nodo, `-1` incluidos).
- Nodo estación: distancia $0$, no $-1`.

## Código de referencia (C++)

```cpp
vector<int> d(n + 1, -1);
queue<int> q;
for (int s : src) { d[s] = 0; q.push(s); }
while (!q.empty()) {
    int u = q.front(); q.pop();
    for (int v : g[u]) if (d[v] == -1) {
        d[v] = d[u] + 1;
        q.push(v);
    }
}
```
