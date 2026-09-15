#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long L, R;
    cin >> n >> L >> R;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (L <= x && x <= R) ++ans;
    }
    cout << ans << "\n";
    return 0;
}
