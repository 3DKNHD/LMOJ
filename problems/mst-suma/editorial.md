# Editorial: Cablear el campus

## Qué hay que hacer

Quieres conectar $n$ edificios pagando lo menos posible. Eso es un **árbol recubridor mínimo** (MST): $n-1$ cables, sin ciclos, suma mínima. Si no se puede, `IMPOSIBLE`.

## Kruskal, en humano

1. Ordena **todos** los cables de más barato a más caro.
2. Recórrelos en ese orden. Si los dos edificios **aún no** están en la misma red (DSU, como en “Cables del lab”), usa el cable, sumá el costo.
3. Si usaste exactamente $n-1$ cables, imprime el costo. Si no, el grafo no era conexo.

¿Por qué el más barato primero? Cualquier ciclo futuro, el cable más caro del ciclo sobra. Kruskal nunca se arrepiente.

Suma en `long long`.

## Si te da WA

No comprobaste `used == n-1`. Uniste cables que formaban ciclo y sumaste de más.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct DSU {
    vector<int> p, r;
    DSU(int n): p(n+1), r(n+1,0) { iota(p.begin(), p.end(), 0); }
    int find(int x) { return p[x]==x ? x : p[x]=find(p[x]); }
    bool unite(int a, int b) {
        a=find(a); b=find(b); if (a==b) return false;
        if (r[a]<r[b]) swap(a,b);
        p[b]=a; if (r[a]==r[b]) ++r[a];
        return true;
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<array<ll,3>> e(m);
    for (int i=0;i<m;++i) cin >> e[i][1] >> e[i][2] >> e[i][0];
    sort(e.begin(), e.end());
    DSU d(n);
    ll cost=0; int used=0;
    for (auto &t: e) if (d.unite((int)t[1], (int)t[2])) { cost += t[0]; ++used; }
    if (used != n-1) cout << "IMPOSIBLE\n";
    else cout << cost << "\n";
    return 0;
}
```
