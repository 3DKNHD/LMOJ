# Editorial: Cables del lab

## Qué hay que hacer

PCs y cables. Pregunta: ¿puedo ir de $u$ a $v$ tocando cables? Una PC se alcanza a sí misma siempre ($SI$).

## La idea: conjuntos disjuntos (DSU)

Cada computadora empieza en su propio grupo. El grupo tiene un **representante**. Cuando hay un cable entre $a$ y $b$, se unen los dos grupos: el representante de uno pasa a depender del otro.

Dos computadoras están en la misma red si y solo si tienen el **mismo representante**.

## Cómo hallar el representante (`find`)

Si `p[x] == x`, $x$ es el representante. Si no, sigue a `p[x]`, luego al siguiente, hasta llegar a uno que se apunta a sí mismo.

Al volver, se puede hacer que todos los nodos del camino apunten directo al representante. Así la próxima búsqueda es más corta.

## Cómo unir (`unite`)

Halla el representante de $a$ y el de $b$. Si ya son el mismo, no hagas nada. Si no, cuelga uno del otro. El código oficial cuelga el grupo más bajo del más alto (por “rango”) para que la cadena no crezca demasiado.

## Preguntas

Después de leer **todos** los cables (el grafo no cambia), por cada $u,v$: $find(u)==find(v)$ → `SI` si no `NO`.

## Si te da WA / TLE

- BFS por pregunta: $q$ veces el grafo, TLE.
- `u` y `u` contestaste `NO`.
- Uniste mal y mezclaste redes.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

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
    return 0;
}
```
