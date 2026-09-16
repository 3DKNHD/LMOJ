#include <bits/stdc++.h>
using namespace std;

bool esta_en_rango(long long x, long long izq, long long der) {
    return izq <= x && x <= der;
}

int cuantos_en_rango(const vector<long long>& a, long long izq, long long der) {
    int cuantos = 0;
    for (long long x : a) {
        if (esta_en_rango(x, izq, der)) {
            ++cuantos;
        }
    }
    return cuantos;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long izq, der;
    cin >> n >> izq >> der;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << cuantos_en_rango(a, izq, der) << "\n";
    return 0;
}
