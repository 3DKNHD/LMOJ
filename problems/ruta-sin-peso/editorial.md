# Editorial: Ruta sin peso

## Qué pide

Grafo no dirigido **sin pesos**. Distancia (número de aristas) de $1$ a $n$, o $-1$ si no hay camino. Si $n=1$, la respuesta es $0$. $n\le 10^5$, $m\le 2\cdot 10^5$. Bucles y aristas repetidas permitidos.

## Idea

BFS desde $1$. En un grafo no ponderado, la primera vez que alcanzas un nodo es por un camino **mínimo** en número de aristas.

`dist[v] = dist[u] + 1` al relajar la arista $u\to v$ con `dist[v]` aún vacío (`-1`).

## Por qué no Dijkstra

Dijkstra también da el más corto, pero con pesos positivos y un heap es $O(m\log n)$. Aquí todas las aristas valen $1$: BFS es $O(n+m)$ y más simple. Usar Dijkstra no está mal, es innecesario.

DFS **no** da distancias mínimas (puede encontrar un camino largo primero).

## $n = 1$

`dist[1] = 0` al empezar. No necesitas aristas. Imprimes $0$. Si olvidas inicializar y dejas `-1`, WA.

## Bucles y múltiples aristas

Un bucle $u\to u$ no mejora distancia. Aristas dobles: la primera vez que visitas $v$ lo marcas; las siguientes `dist[v] != -1` y se ignoran. Correcto.

## Complejidad

$O(n+m)$. Memoria $O(n+m)$ para la lista de adyacencia.

## Otras soluciones

- 0-1 BFS / deque: equivalente a BFS aquí.
- Dijkstra: AC más lento de escribir.

## Trampas

- Grafo dirigido (olvidar `g[v].push_back(u)`).
- DFS.
- No poner `dist[1]=0`.
- Índices $0$ vs $1$.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[1] = 0;
    q.push(1);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        if (u == n) break;
        for (int v : g[u]) {
            if (dist[v] != -1) continue;
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    cout << dist[n] << "\n";
}
```
