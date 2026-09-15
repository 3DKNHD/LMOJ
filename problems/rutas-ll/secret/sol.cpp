#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll INF = 1LL << 62;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, s, t;
    cin >> n >> m >> s >> t;
    vector<vector<pair<int, ll>>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; ll w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }
    vector<ll> d(n + 1, INF);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    d[s] = 0;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [du, u] = pq.top();
        pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : g[u])
            if (d[v] > du + w) {
                d[v] = du + w;
                pq.push({d[v], v});
            }
    }
    cout << (d[t] >= INF / 2 ? -1 : d[t]) << "\n";
    return 0;
}
