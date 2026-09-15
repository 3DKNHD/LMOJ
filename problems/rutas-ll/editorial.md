# Editorial: Rutas con peso

## Qué pide

Grafo no dirigido, pesos **no negativos**. Distancia mínima $s\rightsquigarrow t$, o $-1$. $n\le 10^5$, $w\le 10^9$, caminos de hasta $10^5$ aristas.

## Idea

Dijkstra con heap. Distancia `long long`, `INF = 2^{62}`. Relajas $v$ si `d[v] > d[u] + w`. Saltas entradas viejas del heap con `if (du != d[u]) continue`.

## Por qué no BFS

BFS minimiza **número de aristas**, no la suma de pesos. Un camino de 2 aristas de peso $10^9$ pierde frente a 100 aristas de peso $1$.

## Por qué `long long`

Peor camino: $10^5$ aristas $\times 10^9 = 10^{14}$. Un `int` con `INF=2^{31}-1` **revienta**: sumas se saturan o se vuelven negativas (la trampa que menciona el enunciado).

## Grafo no dirigido

Inserta $u\to v$ y $v\to u$ con el mismo $w$. Bucles: relajar $u$ consigo mismo con $w\ge 0$ no mejora. Múltiples aristas: te quedas con la relajación mejor.

## Complejidad

$O((n+m)\log n)$ con binary heap.

## $s=t$

`d[s]=0`, respuesta $0$ sin aristas.

## Trampas

- `int` / `INF` 32-bit.
- Grafo dirigido por olvido.
- Imprimir `INF` en vez de `-1`.
- Dijkstra sin skip de pares obsoletos: correcto pero más lento; no suele TLE aquí.

## Código de referencia (C++)

```cpp
vector<ll> d(n + 1, INF);
priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
d[s] = 0;
pq.push({0, s});
while (!pq.empty()) {
    auto [du, u] = pq.top(); pq.pop();
    if (du != d[u]) continue;
    for (auto [v, w] : g[u])
        if (d[v] > du + w) {
            d[v] = du + w;
            pq.push({d[v], v});
        }
}
cout << (d[t] >= INF / 2 ? -1 : d[t]) << "\n";
```
