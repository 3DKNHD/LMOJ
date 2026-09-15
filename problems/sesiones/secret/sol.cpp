#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].second >> a[i].first;
    sort(a.begin(), a.end());
    int ans = 0;
    long long last = -(1LL << 60);
    for (auto [r, l] : a) {
        if (l > last) {
            ++ans;
            last = r;
        }
    }
    cout << ans << "\n";
    return 0;
}
