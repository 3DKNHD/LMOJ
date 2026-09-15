#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> t;
    Fenwick(int n) : n(n), t(n + 1, 0) {}
    void add(int i, int v) {
        for (; i <= n; i += i & -i) t[i] += v;
    }
    int sum(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += t[i];
        return s;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    vector<int> b = a;
    sort(b.begin(), b.end());
    b.erase(unique(b.begin(), b.end()), b.end());
    for (int &x : a) x = int(lower_bound(b.begin(), b.end(), x) - b.begin()) + 1;
    Fenwick fw((int)b.size());
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += i - fw.sum(a[i]);
        fw.add(a[i], 1);
    }
    cout << ans << "\n";
    return 0;
}
