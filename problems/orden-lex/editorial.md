# Editorial: Orden lexicográfico

## Qué pide

Orden topológico **lexicográficamente mínimo**. Arista $u\to v$: $u$ antes que $v$. Si hay ciclo: `IMPOSIBLE`.

## Idea

Kahn, pero la cola es un **heap de mínimos**. Siempre extraes el índice más chico con indegree $0$.

Si al final no sacaste $n$ nodos, quedó un ciclo.

## Por qué el heap da el lex menor

Entre los nodos que **pueden** salir ahora, el lex menor orden pone el menor índice posible. Si eligieras uno mayor, podrías intercambiarlo por el menor disponible y obtener un orden lexicográficamente más chico. Inducción en la posición.

Una cola FIFO da **algún** toposort, no el mínimo.

## DFS toposort

El orden inverso de salida de DFS es un toposort, pero **no** el lex menor sin trabajo extra (tendrías que probar candidatos en orden). Kahn+heap es el estándar.

## Complejidad

$O(n + m\log n)$.

## $n$ aislados

Todos indegree 0: el heap saca $1,2,\dots,n$. Correcto.

## Trampas

- `queue` en vez de `priority_queue<..., greater<>>`.
- No chequear `ord.size()==n`.
- Tratar el grafo como no dirigido.

## Código de referencia (C++)

```cpp
priority_queue<int, vector<int>, greater<>> pq;
for (int i = 1; i <= n; ++i) if (indeg[i] == 0) pq.push(i);
while (!pq.empty()) {
    int u = pq.top(); pq.pop();
    ord.push_back(u);
    for (int v : g[u]) if (--indeg[v] == 0) pq.push(v);
}
if ((int)ord.size() != n) cout << "IMPOSIBLE\n";
```
