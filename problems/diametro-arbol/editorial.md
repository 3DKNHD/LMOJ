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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<vector<int>> g;
pair<int,int> farthest(int src) {
    vector<int> d(n+1, -1);
    queue<int> q; q.push(src); d[src]=0;
    int best=src;
    while (!q.empty()) {
        int u=q.front(); q.pop();
        if (d[u]>d[best]) best=u;
        for (int v: g[u]) if (d[v]==-1) { d[v]=d[u]+1; q.push(v); }
    }
    return {best, d[best]};
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    g.assign(n+1, {});
    for (int i=0;i<n-1;++i) {
        int u,v; cin>>u>>v;
        g[u].push_back(v); g[v].push_back(u);
    }
    int u = farthest(1).first;
    cout << farthest(u).second << "\n";
    return 0;
}
```
