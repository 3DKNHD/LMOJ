#include <bits/stdc++.h>
using namespace std;

vector<long long> prefijos(const vector<long long>& a) {
    int n = (int)a.size();
    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        p[i] = p[i - 1] + a[i - 1];
    }
    return p;
}

long long suma_rango(const vector<long long>& p, int izq, int der) {
    return p[der] - p[izq - 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, consultas;
    cin >> n >> consultas;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> p = prefijos(a);
    while (consultas--) {
        int izq, der;
        cin >> izq >> der;
        cout << suma_rango(p, izq, der) << "\n";
    }
    return 0;
}
