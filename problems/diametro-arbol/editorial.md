# Editorial: Los dos pueblos más lejanos

## Qué hay que hacer

Un árbol: $n$ pueblos, $n-1$ caminos, sin ciclos, todo conectado. El diámetro es la pareja más lejana (en cantidad de caminos).

## Dos BFS, no $n$

Un hecho útil: toma cualquier pueblo $s$. Busca el más lejano $u$. Desde $u$, busca el más lejano $v$. La distancia $u$–$v$ **es** el diámetro.

Intuición: $u$ tiene que ser una “punta” del árbol. La otra punta está lo más lejos de esa.

BFS = distancia cuando cada arista vale $1$ (cola, como siempre).

Si $n=1$, $0$.

## Si te da WA

Mediste desde el nodo $1$ y te quedaste con eso (el $1$ puede estar en el medio).

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

pair<int, int> mas_lejano(int origen, const vector<vector<int>>& g) {
    int n = (int)g.size() - 1;
    vector<int> dist(n + 1, -1);
    queue<int> q;
    q.push(origen);
    dist[origen] = 0;
    int mejor = origen;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        if (dist[u] > dist[mejor]) {
            mejor = u;
        }
        for (int v : g[u]) {
            if (dist[v] != -1) {
                continue;
            }
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    return {mejor, dist[mejor]};
}

int diametro(const vector<vector<int>>& g) {
    int extremo = mas_lejano(1, g).first;
    return mas_lejano(extremo, g).second;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    cout << diametro(g) << "\n";
    return 0;
}
```
