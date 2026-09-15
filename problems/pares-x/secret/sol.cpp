#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long X;
    cin >> n >> X;
    map<long long, long long> f;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        f[x]++;
    }
    long long ans = 0;
    for (auto [v, c] : f) {
        long long need = X - v;
        if (need < v) continue;
        if (need == v) ans += c * (c - 1) / 2;
        else {
            auto it = f.find(need);
            if (it != f.end()) ans += c * it->second;
        }
    }
    cout << ans << "\n";
    return 0;
}
