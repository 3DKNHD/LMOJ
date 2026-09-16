#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> t;

    Fenwick(int tam) : n(tam), t(tam + 1, 0) {}

    void agregar(int i, int v) {
        for (; i <= n; i += i & -i) {
            t[i] += v;
        }
    }

    int prefijo(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) {
            s += t[i];
        }
        return s;
    }
};

vector<int> comprimir(vector<int> a) {
    vector<int> orden = a;
    sort(orden.begin(), orden.end());
    orden.erase(unique(orden.begin(), orden.end()), orden.end());
    for (int& x : a) {
        x = int(lower_bound(orden.begin(), orden.end(), x) - orden.begin()) + 1;
    }
    return a;
}

long long contar_inversiones(vector<int> a) {
    a = comprimir(a);
    int maximo = 0;
    for (int x : a) {
        maximo = max(maximo, x);
    }

    Fenwick fw(maximo);
    long long inversiones = 0;
    for (int i = 0; i < (int)a.size(); ++i) {
        inversiones += i - fw.prefijo(a[i]);
        fw.agregar(a[i], 1);
    }
    return inversiones;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << contar_inversiones(a) << "\n";
    return 0;
}
