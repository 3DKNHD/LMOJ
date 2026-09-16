#include <bits/stdc++.h>
using namespace std;

vector<int> distancias_desde(int n, const vector<vector<int>>& g, const vector<int>& fuentes) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    for (int s : fuentes) {
        dist[s] = 0;
        q.push(s);
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g[u]) {
            if (dist[v] != -1) {
                continue;
            }
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    return dist;
}

void imprimir_desde_1(const vector<int>& dist) {
    for (int i = 1; i < (int)dist.size(); ++i) {
        if (i > 1) {
            cout << " ";
        }
        cout << dist[i];
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;
    vector<int> fuentes(k);
    for (int i = 0; i < k; ++i) {
        cin >> fuentes[i];
    }

    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    imprimir_desde_1(distancias_desde(n, g, fuentes));
    return 0;
}
