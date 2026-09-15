#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    const int LOG = 16;
    vector<int> depth(n + 1), pxor(n + 1);
    vector<array<int, 16>> up(n + 1);
    for (int i = 0; i <= n; ++i) up[i].fill(0);

    function<void(int, int)> dfs = [&](int u, int p) {
        up[u][0] = p;
        for (int k = 1; k < LOG; ++k) up[u][k] = up[up[u][k - 1]][k - 1];
        for (int v : g[u]) {
            if (v == p) continue;
            depth[v] = depth[u] + 1;
            pxor[v] = pxor[u] ^ a[v];
            dfs(v, u);
        }
    };
    pxor[1] = a[1];
    dfs(1, 1);

    auto lca = [&](int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; ++k)
            if (diff >> k & 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; --k)
            if (up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        return up[u][0];
    };

    while (q--) {
        int u, v;
        cin >> u >> v;
        int w = lca(u, v);
        int ans = pxor[u] ^ pxor[v] ^ a[w];
        cout << ans << "\n";
    }
    return 0;
}
