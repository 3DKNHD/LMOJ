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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m,k; cin>>n>>m>>k;
    vector<int> src(k);
    for (int i=0;i<k;++i) cin>>src[i];
    vector<vector<int>> g(n+1);
    for (int i=0;i<m;++i) {
        int u,v; cin>>u>>v;
        g[u].push_back(v); g[v].push_back(u);
    }
    vector<int> d(n+1, -1);
    queue<int> q;
    for (int s: src) { d[s]=0; q.push(s); }
    while (!q.empty()) {
        int u=q.front(); q.pop();
        for (int v: g[u]) if (d[v]==-1) { d[v]=d[u]+1; q.push(v); }
    }
    for (int i=1;i<=n;++i) {
        if (i>1) cout<<" ";
        cout<<d[i];
    }
    cout<<"\n";
    return 0;
}
```
