#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long potencia(long long base, long long exp) {
    base %= MOD;
    long long resultado = 1;
    while (exp > 0) {
        if (exp & 1) {
            resultado = resultado * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    return resultado;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long a, b;
        cin >> a >> b;
        cout << potencia(a, b) << "\n";
    }
    return 0;
}
