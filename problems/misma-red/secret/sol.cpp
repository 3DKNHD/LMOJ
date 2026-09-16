#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> padre;
    vector<int> rango;

    DSU(int tam) : padre(tam + 1), rango(tam + 1, 0) {
        iota(padre.begin(), padre.end(), 0);
    }

    int raiz(int x) {
        if (padre[x] == x) {
            return x;
        }
        return padre[x] = raiz(padre[x]);
    }

    void unir(int a, int b) {
        a = raiz(a);
        b = raiz(b);
        if (a == b) {
            return;
        }
        if (rango[a] < rango[b]) {
            swap(a, b);
        }
        padre[b] = a;
        if (rango[a] == rango[b]) {
            ++rango[a];
        }
    }

    bool mismo(int a, int b) {
        return raiz(a) == raiz(b);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;
    DSU dsu(n);
    while (m--) {
        int u, v;
        cin >> u >> v;
        dsu.unir(u, v);
    }

    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << (dsu.mismo(u, v) ? "SI" : "NO") << "\n";
    }
    return 0;
}
