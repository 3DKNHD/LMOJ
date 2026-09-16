#include <bits/stdc++.h>
using namespace std;

const long long MENOS_INF = -(1LL << 60);

long long segundo_maximo_estricto(const vector<long long>& a) {
    long long primero = MENOS_INF;
    long long segundo = MENOS_INF;

    for (long long x : a) {
        if (x > primero) {
            segundo = primero;
            primero = x;
        } else if (x < primero && x > segundo) {
            segundo = x;
        }
    }

    if (segundo == MENOS_INF) {
        return -1;
    }
    return segundo;
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

    cout << segundo_maximo_estricto(a) << "\n";
    return 0;
}
