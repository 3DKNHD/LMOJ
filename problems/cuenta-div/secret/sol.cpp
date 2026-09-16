#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000;

vector<int> contar_divisores_hasta(int limite) {
    vector<int> divisores(limite + 1, 0);
    for (int i = 1; i <= limite; ++i) {
        for (int j = i; j <= limite; j += i) {
            ++divisores[j];
        }
    }
    return divisores;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> divisores = contar_divisores_hasta(MAXN);

    int casos;
    cin >> casos;
    while (casos--) {
        int n;
        cin >> n;
        cout << divisores[n] << "\n";
    }
    return 0;
}
