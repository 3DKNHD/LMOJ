#include <bits/stdc++.h>
using namespace std;

struct Intervalo {
    int inicio;
    int fin;
};

int maximo_sin_solape(vector<Intervalo> intervalos) {
    sort(intervalos.begin(), intervalos.end(), [](const Intervalo& a, const Intervalo& b) {
        return a.fin < b.fin;
    });

    int tomados = 0;
    long long ultimo_fin = -(1LL << 60);
    for (const auto& it : intervalos) {
        if (it.inicio > ultimo_fin) {
            ++tomados;
            ultimo_fin = it.fin;
        }
    }
    return tomados;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Intervalo> intervalos(n);
    for (int i = 0; i < n; ++i) {
        cin >> intervalos[i].inicio >> intervalos[i].fin;
    }

    cout << maximo_sin_solape(intervalos) << "\n";
    return 0;
}
