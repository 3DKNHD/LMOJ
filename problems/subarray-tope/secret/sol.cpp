#include <bits/stdc++.h>
using namespace std;

int ventana_mas_larga(const vector<long long>& a, long long tope) {
    int mejor = 0;
    int izq = 0;
    long long suma = 0;

    for (int der = 0; der < (int)a.size(); ++der) {
        suma += a[der];
        while (izq <= der && suma > tope) {
            suma -= a[izq];
            ++izq;
        }
        mejor = max(mejor, der - izq + 1);
    }
    return mejor;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long tope;
    cin >> n >> tope;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << ventana_mas_larga(a, tope) << "\n";
    return 0;
}
