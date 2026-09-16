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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; cin>>n>>m;
    vector<vector<int>> g(n+1);
    for (int i=0;i<m;++i) {
        int u,v; cin>>u>>v;
        g[u].push_back(v); g[v].push_back(u);
    }
    vector<int> col(n+1, -1);
    for (int s=1;s<=n;++s) {
        if (col[s]!=-1) continue;
        queue<int> q; col[s]=0; q.push(s);
        while (!q.empty()) {
            int u=q.front(); q.pop();
            for (int v: g[u]) {
                if (col[v]==-1) { col[v]=col[u]^1; q.push(v); }
                else if (col[v]==col[u]) { cout<<"NO\n"; return 0; }
            }
        }
    }
    cout<<"SI\n";
    return 0;
}
```
