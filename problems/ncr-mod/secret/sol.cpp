#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;
const int MAXN = 1000000;

long long potencia(long long base, long long exp) {
    long long resultado = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) {
            resultado = resultado * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    return resultado;
}

struct Combinatoria {
    vector<long long> fact;
    vector<long long> inv_fact;

    Combinatoria(int tam) : fact(tam + 1), inv_fact(tam + 1) {
        fact[0] = 1;
        for (int i = 1; i <= tam; ++i) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        inv_fact[tam] = potencia(fact[tam], MOD - 2);
        for (int i = tam; i >= 1; --i) {
            inv_fact[i - 1] = inv_fact[i] * i % MOD;
        }
    }

    long long ncr(int n, int k) const {
        if (k < 0 || k > n) {
            return 0;
        }
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Combinatoria comb(MAXN);

    int casos;
    cin >> casos;
    while (casos--) {
        int n, k;
        cin >> n >> k;
        cout << comb.ncr(n, k) << "\n";
    }
    return 0;
}
