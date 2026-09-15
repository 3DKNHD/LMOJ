# Editorial: ¿Misma red?

## Qué pide

Grafo no dirigido con $n \le 2\cdot 10^5$, $m$ cables, $q$ preguntas “¿$u$ y $v$ están en la misma componente?”. Un nodo está en la misma red que sí mismo. Puede haber bucles y aristas repetidas.

## Idea

Union-Find (DSU). Cada componente es un árbol de padres. `find(x)` sube hasta la raíz (con path compression). `unite(a,b)` cuelga la raíz más chica (por rango) de la otra.

Tras procesar las $m$ aristas, $u$ y $v$ están conectados sii `find(u) == find(v)`.

## Por qué DSU y no BFS en cada query

$q$ también es $2\cdot 10^5$. BFS por pregunta es $O(q(n+m))$: muerto. Alternativa válida: **una** DFS/BFS para etiquetar componentes (`comp[u] = id`) en $O(n+m)$, luego cada query es `comp[u]==comp[v]`. Eso también es $O(n+m+q)$ y está perfecto.

DSU es más cómodo si más adelante el grafo crece online. Aquí las aristas llegan **antes** de las queries, así que ambas sirven.

## Path compression + union by rank

Sin ellos, `find` puede ser $O(n)$ y $m$ uniones $O(nm)$. Con ambos, $\approx O(\alpha(n))$ por operación, casi $O(1)$. El oficial:

```cpp
int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
```

y compara `r[a], r[b]` al unir.

## Bucles y repetidas

`unite(u,u)`: `find` igual, return. Arista doble: segunda `unite` no hace nada. Correcto.

## $u = v$ en una query

Misma raíz. `SI`. El enunciado lo pide explícitamente.

## Complejidad

$O((n+m+q)\,\alpha(n))$. Memoria $O(n)$.

## Otras soluciones

- BFS/DFS de componentes + color.
- Lista de adyacencia + `visited` por query: TLE.

## Trampas

- Imprimir `YES` en vez de `SI`.
- Indexar DSU en $0..n-1$ y leer nodos $1..n$.
- DFS recursivo en una estrella de $2\cdot 10^5$: stack overflow; DSU o BFS no tienen ese problema.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, r;
    DSU(int n) : p(n + 1), r(n + 1, 0) { iota(p.begin(), p.end(), 0); }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return;
        if (r[a] < r[b]) swap(a, b);
        p[b] = a;
        if (r[a] == r[b]) ++r[a];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    cin >> n >> m >> q;
    DSU d(n);
    while (m--) {
        int u, v;
        cin >> u >> v;
        d.unite(u, v);
    }
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << (d.find(u) == d.find(v) ? "SI" : "NO") << "\n";
    }
}
```
