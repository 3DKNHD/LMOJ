# Editorial: Hasta la sala n

## Qué hay que hacer

Pasillos todos de largo $1$. De la sala $1$ a la $n$, ¿cuántos pasillos como mínimo? Si no se puede, $-1$. Si $n=1$, la respuesta es $0$.

## Por qué BFS (cola) y no “el camino que se me ocurre”

Cuando todos los pasillos valen $1$, la **primera** vez que llegas a una sala es por un camino más corto. Siempre. Por eso usas una cola: primero los que están a distancia $0$, después $1$, después $2$, …

## Paso a paso

1. Armá la lista de vecinos de cada sala (el grafo va en los dos sentidos).
2. `dist[i] = -1` para todos (“nunca fui”). `dist[1] = 0`. Cola con $1$.
3. Mientras la cola no esté vacía: saca $u$. Por cada vecino $v$ que siga en $-1$: `dist[v] = dist[u]+1`, encola $v$.
4. Imprime `dist[n]` (si nunca lo tocaste, sigue `-1`).

## Ejemplo

$1-2-4$, y $1-3$. $n=4$.

- dist $1 = 0$
- de $1$ salís a $2$ y $3$ → dist $1$
- de $2$ a $4$ → dist $2$

Respuesta: $2$.

## Si te da WA / TLE

DFS (el primer camino que encuentras no es el más corto). O Dijkstra con pesos $1$: funciona pero es más código y más lento. O grafo dirigido de un solo lado.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

int distancia(int n, const vector<vector<int>>& g, int origen, int destino) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[origen] = 0;
    q.push(origen);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        if (u == destino) {
            break;
        }
        for (int v : g[u]) {
            if (dist[v] != -1) {
                continue;
            }
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    return dist[destino];
}

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

    cout << distancia(n, g, 1, n) << "\n";
    return 0;
}
```
