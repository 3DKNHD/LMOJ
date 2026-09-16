# Editorial: Dos bandos

## Qué hay que hacer

¿Se puede pintar cada persona de rojo o azul de modo que cada “enemistad” (arista) una rojo con azul? Eso es: el grafo es **bipartito**. Un triángulo imposibilita (tres personas, dos colores: dos del mismo color quedan enemigas).

## Cómo chequearlo

BFS (o DFS) pintando.

1. `col[i] = -1` (sin pintar).
2. Por cada componente (gente suelta también): si no está pintada, pintala $0$ y BFS.
3. Un vecino sin pintar: pintalo del color contrario (`col[u]^1`, el XOR con $1$ da vuelta el $0$ y el $1$).
4. Un vecino ya pintado **del mismo color que vos**: conflicto → `NO` y corta.

Si terminas todas las componentes: `SI`.

Nodos sin aristas: los pintas de $0$ y no molestan.

## Si te da WA

Solo miraste si hay un triángulo explícito (hay ciclos impares más largos). O grafo dirigido.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

bool pinta_componente(int s, const vector<vector<int>>& g, vector<int>& color) {
    queue<int> q;
    color[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g[u]) {
            if (color[v] == -1) {
                color[v] = color[u] ^ 1;
                q.push(v);
                continue;
            }
            if (color[v] == color[u]) {
                return false;
            }
        }
    }
    return true;
}

bool es_bipartito(int n, const vector<vector<int>>& g) {
    vector<int> color(n + 1, -1);
    for (int s = 1; s <= n; ++s) {
        if (color[s] != -1) {
            continue;
        }
        if (!pinta_componente(s, g, color)) {
            return false;
        }
    }
    return true;
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

    cout << (es_bipartito(n, g) ? "SI" : "NO") << "\n";
    return 0;
}
```
