#include <bits/stdc++.h>
using namespace std;

int cobertura_maxima(int limite, const vector<pair<int, int>>& rangos) {
    vector<int> delta(limite + 2, 0);
    for (auto [izq, der] : rangos) {
        delta[izq] += 1;
        delta[der + 1] -= 1;
    }

    int actual = 0;
    int mejor = 0;
    for (int i = 1; i <= limite; ++i) {
        actual += delta[i];
        mejor = max(mejor, actual);
    }
    return mejor;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, limite;
    cin >> n >> limite;
    vector<pair<int, int>> rangos(n);
    for (int i = 0; i < n; ++i) {
        cin >> rangos[i].first >> rangos[i].second;
    }

    cout << cobertura_maxima(limite, rangos) << "\n";
    return 0;
}
