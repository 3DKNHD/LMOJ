#include <bits/stdc++.h>
using namespace std;

struct DSU {
    vector<int> p, r;
    DSU(int n) : p(n + 1), r(n + 1, 0) { iota(p.begin(), p.end(), 0); }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return;
        if (r[a] < r[b]) swap(a, b);
        p[b] = a;
        if (r[a] == r[b]) ++r[a];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    cin >> n >> m >> q;
    DSU d(n);
    while (m--) {
        int u, v;
        cin >> u >> v;
        d.unite(u, v);
    }
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << (d.find(u) == d.find(v) ? "SI" : "NO") << "\n";
    }
    return 0;
}
