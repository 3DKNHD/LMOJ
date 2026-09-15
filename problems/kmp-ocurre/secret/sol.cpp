#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string p, t;
    cin >> p >> t;
    string s = p + "#" + t;
    int m = (int)p.size();
    vector<int> pi(s.size());
    int ans = 0;
    for (int i = 1; i < (int)s.size(); ++i) {
        int j = pi[i - 1];
        while (j && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) ++j;
        pi[i] = j;
        if (j == m) ++ans;
    }
    cout << ans << "\n";
    return 0;
}
