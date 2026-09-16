#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<long long> t;

    Fenwick(int tam) : n(tam), t(tam + 1, 0) {}

    void agregar(int i, long long v) {
        for (; i <= n; i += i & -i) {
            t[i] += v;
        }
    }

    long long prefijo(int i) {
        long long s = 0;
        for (; i > 0; i -= i & -i) {
            s += t[i];
        }
        return s;
    }

    long long rango(int izq, int der) {
        return prefijo(der) - prefijo(izq - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, consultas;
    cin >> n >> consultas;
    Fenwick fw(n);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        fw.agregar(i, x);
    }

    while (consultas--) {
        int tipo;
        cin >> tipo;
        if (tipo == 1) {
            int i;
            long long x;
            cin >> i >> x;
            fw.agregar(i, x);
        } else {
            int izq, der;
            cin >> izq >> der;
            cout << fw.rango(izq, der) << "\n";
        }
    }
    return 0;
}
