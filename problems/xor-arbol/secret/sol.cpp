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
