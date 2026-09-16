#include <bits/stdc++.h>
using namespace std;

struct Objeto {
    int peso;
    long long valor;
};

long long mochila(int capacidad, const vector<Objeto>& objetos) {
    vector<long long> dp(capacidad + 1, 0);
    for (const auto& obj : objetos) {
        for (int w = capacidad; w >= obj.peso; --w) {
            dp[w] = max(dp[w], dp[w - obj.peso] + obj.valor);
        }
    }
    return dp[capacidad];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, capacidad;
    cin >> n >> capacidad;
    vector<Objeto> objetos(n);
    for (int i = 0; i < n; ++i) {
        cin >> objetos[i].peso >> objetos[i].valor;
    }

    cout << mochila(capacidad, objetos) << "\n";
    return 0;
}
