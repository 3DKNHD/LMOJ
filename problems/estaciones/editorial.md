# Editorial: Paradas más cercanas

## Qué hay que hacer

Varias estaciones. Para **cada** esquina, la distancia a la estación más cercana, o `-1`.

## Un solo BFS con muchas fuentes

En vez de un BFS por estación ($k$ veces el grafo), mete **todas** las estaciones en la cola al principio, con distancia $0$. El BFS normal hace el resto: la primera vez que tocas un nodo es desde la estación más cercana.

Si un nodo nunca se toca, `-1`.

Cuidado: las $k$ estaciones son distintas. Si por error metes dos veces la misma, no pasa nada si $d$ ya era $0$.

## Si te da TLE

BFS desde cada estación por separado.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> distancias_desde(int n, const vector<vector<int>>& g, const vector<int>& fuentes) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    for (int s : fuentes) {
        dist[s] = 0;
        q.push(s);
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g[u]) {
            if (dist[v] != -1) {
                continue;
            }
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    return dist;
}

void imprimir_desde_1(const vector<int>& dist) {
    for (int i = 1; i < (int)dist.size(); ++i) {
        if (i > 1) {
            cout << " ";
        }
        cout << dist[i];
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;
    vector<int> fuentes(k);
    for (int i = 0; i < k; ++i) {
        cin >> fuentes[i];
    }

    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    imprimir_desde_1(distancias_desde(n, g, fuentes));
    return 0;
}
```
