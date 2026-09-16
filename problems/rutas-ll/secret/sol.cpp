#include <bits/stdc++.h>
using namespace std;

const long long INF = 1LL << 62;

long long dijkstra(int n, const vector<vector<pair<int, long long>>>& g, int origen, int destino) {
    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    dist[origen] = 0;
    pq.push({0, origen});

    while (!pq.empty()) {
        auto [du, u] = pq.top();
        pq.pop();
        if (du != dist[u]) {
            continue;
        }
        for (auto [v, w] : g[u]) {
            if (dist[v] > du + w) {
                dist[v] = du + w;
                pq.push({dist[v], v});
            }
        }
    }

    if (dist[destino] >= INF / 2) {
        return -1;
    }
    return dist[destino];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    cin >> n >> m >> s >> t;
    vector<vector<pair<int, long long>>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }

    cout << dijkstra(n, g, s, t) << "\n";
    return 0;
}
