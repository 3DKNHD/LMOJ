#include <bits/stdc++.h>
using namespace std;

long long contar_pares(const vector<long long>& a, long long objetivo) {
    map<long long, long long> freq;
    for (long long x : a) {
        freq[x]++;
    }

    long long respuesta = 0;
    for (auto [valor, veces] : freq) {
        long long falta = objetivo - valor;
        if (falta < valor) {
            continue;
        }
        if (falta == valor) {
            respuesta += veces * (veces - 1) / 2;
            continue;
        }
        auto it = freq.find(falta);
        if (it != freq.end()) {
            respuesta += veces * it->second;
        }
    }
    return respuesta;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long objetivo;
    cin >> n >> objetivo;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << contar_pares(a, objetivo) << "\n";
    return 0;
}
