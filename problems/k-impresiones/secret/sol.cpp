#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<long long> t(n);
    long long mn = (1LL << 62);
    for (int i = 0; i < n; ++i) {
        cin >> t[i];
        mn = min(mn, t[i]);
    }
    auto ok = [&](long long mid) {
        long long done = 0;
        for (long long x : t) {
            done += mid / x;
            if (done >= k) return true;
        }
        return false;
    };
    long long lo = 1, hi = mn * k, ans = hi;
    while (lo <= hi) {
        long long mid = lo + (hi - lo) / 2;
        if (ok(mid)) {
            ans = mid;
            hi = mid - 1;
        } else lo = mid + 1;
    }
    cout << ans << "\n";
    return 0;
}
