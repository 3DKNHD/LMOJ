#include <bits/stdc++.h>
using namespace std;

int distancia(int n, const vector<vector<int>>& g, int origen, int destino) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[origen] = 0;
    q.push(origen);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        if (u == destino) {
            break;
        }
        for (int v : g[u]) {
            if (dist[v] != -1) {
                continue;
            }
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    return dist[destino];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    cout << distancia(n, g, 1, n) << "\n";
    return 0;
}
