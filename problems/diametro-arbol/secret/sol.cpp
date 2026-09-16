#include <bits/stdc++.h>
using namespace std;

pair<int, int> mas_lejano(int origen, const vector<vector<int>>& g) {
    int n = (int)g.size() - 1;
    vector<int> dist(n + 1, -1);
    queue<int> q;
    q.push(origen);
    dist[origen] = 0;
    int mejor = origen;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        if (dist[u] > dist[mejor]) {
            mejor = u;
        }
        for (int v : g[u]) {
            if (dist[v] != -1) {
                continue;
            }
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    return {mejor, dist[mejor]};
}

int diametro(const vector<vector<int>>& g) {
    int extremo = mas_lejano(1, g).first;
    return mas_lejano(extremo, g).second;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    cout << diametro(g) << "\n";
    return 0;
}
