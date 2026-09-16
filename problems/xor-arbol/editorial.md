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

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int LOG = 16;

struct ArbolXor {
    int n;
    vector<int> valor;
    vector<int> profundidad;
    vector<int> xor_desde_raiz;
    vector<vector<int>> g;
    vector<array<int, LOG>> padre;

    ArbolXor(int tam)
        : n(tam),
          valor(tam + 1),
          profundidad(tam + 1),
          xor_desde_raiz(tam + 1),
          g(tam + 1),
          padre(tam + 1) {
        for (int i = 0; i <= n; ++i) {
            padre[i].fill(0);
        }
    }

    void arista(int u, int v) {
        g[u].push_back(v);
        g[v].push_back(u);
    }

    void preparar() {
        xor_desde_raiz[1] = valor[1];
        dfs(1, 1);
    }

    int xor_camino(int u, int v) const {
        int w = lca(u, v);
        return xor_desde_raiz[u] ^ xor_desde_raiz[v] ^ valor[w];
    }

private:
    void dfs(int u, int p) {
        padre[u][0] = p;
        for (int k = 1; k < LOG; ++k) {
            padre[u][k] = padre[padre[u][k - 1]][k - 1];
        }
        for (int v : g[u]) {
            if (v == p) {
                continue;
            }
            profundidad[v] = profundidad[u] + 1;
            xor_desde_raiz[v] = xor_desde_raiz[u] ^ valor[v];
            dfs(v, u);
        }
    }

    int subir(int u, int pasos) const {
        for (int k = 0; k < LOG; ++k) {
            if (pasos >> k & 1) {
                u = padre[u][k];
            }
        }
        return u;
    }

    int lca(int u, int v) const {
        if (profundidad[u] < profundidad[v]) {
            swap(u, v);
        }
        u = subir(u, profundidad[u] - profundidad[v]);
        if (u == v) {
            return u;
        }
        for (int k = LOG - 1; k >= 0; --k) {
            if (padre[u][k] != padre[v][k]) {
                u = padre[u][k];
                v = padre[v][k];
            }
        }
        return padre[u][0];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;
    ArbolXor arbol(n);
    for (int i = 1; i <= n; ++i) {
        cin >> arbol.valor[i];
    }
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        arbol.arista(u, v);
    }
    arbol.preparar();

    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << arbol.xor_camino(u, v) << "\n";
    }
    return 0;
}
```
