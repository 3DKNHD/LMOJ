#include <bits/stdc++.h>
using namespace std;

bool es_par(long long x) {
    return x % 2 == 0;
}

int contar_pares(const vector<long long>& a) {
    int cuantos = 0;
    for (long long x : a) {
        if (es_par(x)) {
            ++cuantos;
        }
    }
    return cuantos;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << contar_pares(a) << "\n";
    return 0;
}
