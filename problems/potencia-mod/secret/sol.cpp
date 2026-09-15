#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long binpow(long long a, long long b) {
    a %= MOD;
    if (a < 0) a += MOD;
    long long r = 1;
    while (b > 0) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        long long a, b;
        cin >> a >> b;
        cout << binpow(a, b) << "\n";
    }
    return 0;
}
