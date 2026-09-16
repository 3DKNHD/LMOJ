# Editorial: El colectivo más barato

## Qué hay que hacer

Pasillos **con precio**. Camino más barato de $s$ a $t$, o $-1$. Si $s=t$, $0$.

BFS ya no sirve: un pasillo de costo $1000$ no es “un paso”.

## Dijkstra

Tienes `d[u]`: lo más barato conocido para llegar a $u$. Empieza en $0$ para $s$ y en infinito para el resto.

Siempre tomas el nodo cuyo `d` actual es el más pequeño (cola de prioridad, la de menores primero). Cuando lo tomas, esa distancia **ya es definitiva** (pesos $\ge 0$). Actualiza vecinos: si $d[u]+w < d[v]$, actualizas y metes $(d[v], v)$ en la cola.

Puede haber una distancia vieja en la cola. Si `du != d[u]` la ignoras.

## Por qué `long long`

Un camino de $10^5$ aristas de $10^9$ suma $10^{14}$. `int` se se sale del rango y el juez da WA. `INF = 1LL<<62`. Si `d[t]` sigue enorme, `-1`.

## Si te da WA

BFS. `int`. `INF = 2^31-1` y un camino legal es más grande → parece inalcanzable.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll INF = 1LL << 62;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, s, t;
    cin >> n >> m >> s >> t;
    vector<vector<pair<int, ll>>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; ll w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }
    vector<ll> d(n + 1, INF);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    d[s] = 0;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [du, u] = pq.top();
        pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : g[u])
            if (d[v] > du + w) {
                d[v] = du + w;
                pq.push({d[v], v});
            }
    }
    cout << (d[t] >= INF / 2 ? -1 : d[t]) << "\n";
    return 0;
}
```
