#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, M;
    cin >> n >> M;
    vector<int> d(M + 2, 0);
    for (int i = 0; i < n; ++i) {
        int L, R;
        cin >> L >> R;
        d[L] += 1;
        d[R + 1] -= 1;
    }
    int cur = 0, ans = 0;
    for (int i = 1; i <= M; ++i) {
        cur += d[i];
        if (cur > ans) ans = cur;
    }
    cout << ans << "\n";
    return 0;
}
