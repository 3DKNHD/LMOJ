#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long pref = 0;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        pref += x;
        if ((pref & 1) == 0) ++ans;
    }
    cout << ans << "\n";
    return 0;
}
