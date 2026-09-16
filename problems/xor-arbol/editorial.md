# Editorial: El rumor en el árbol

## Qué hay que hacer

Árbol. Cada nodo un número. Preguntas: XOR de todos los nodos del camino $u$–$v$, **incluyendo** las dos puntas. Si $u=v$, es $a_u$.

## Prefijo XOR desde la raíz + LCA

Fija el nodo $1$ como raíz. Para cada nodo $x$, guarda `pxor[x]`: el XOR de todos los valores en el camino de la raíz hasta $x$ (incluido $x$).

El camino entre $u$ y $v$ pasa por su ancestro común más cercano, llamado LCA y aquí $w$. La fórmula es:

$$
pxor[u] \oplus pxor[v] \oplus a[w]
$$

Por qué hay que volver a aplicar $a[w]$: `pxor[u] ⊕ pxor[v]` recorre $u$–$w$–$v$, pero $w$ aparece dos veces y el XOR de un número consigo mismo es $0$. Entonces $w$ desaparece. Hay que volver a incluir $a[w]$.

## Cómo calcular el LCA

`up[x][k]` es el padre de $x$ al subir $2^k$ aristas. Se llena con un DFS.

Para dos nodos: primero sube el más profundo hasta que ambos estén a la misma profundidad. Luego súbelos a la vez mientras sus padres no coincidan. Un paso más y llegas al LCA.

Con $n \le 2\cdot 10^4$, basta $2^{16} = 65536$ (por eso `LOG = 16`).

## Si te da TLE / WA

XOR recorriendo el camino en cada pregunta ($O(n)$ por query). Olvidar el $⊕ a[w]$.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    const int LOG = 16;
    vector<int> depth(n + 1), pxor(n + 1);
    vector<array<int, 16>> up(n + 1);
    for (int i = 0; i <= n; ++i) up[i].fill(0);

    function<void(int, int)> dfs = [&](int u, int p) {
        up[u][0] = p;
        for (int k = 1; k < LOG; ++k) up[u][k] = up[up[u][k - 1]][k - 1];
        for (int v : g[u]) {
            if (v == p) continue;
            depth[v] = depth[u] + 1;
            pxor[v] = pxor[u] ^ a[v];
            dfs(v, u);
        }
    };
    pxor[1] = a[1];
    dfs(1, 1);

    auto lca = [&](int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; ++k)
            if (diff >> k & 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; --k)
            if (up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        return up[u][0];
    };

    while (q--) {
        int u, v;
        cin >> u >> v;
        int w = lca(u, v);
        int ans = pxor[u] ^ pxor[v] ^ a[w];
        cout << ans << "\n";
    }
    return 0;
}
```
