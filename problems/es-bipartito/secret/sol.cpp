#include <bits/stdc++.h>
using namespace std;

bool pinta_componente(int s, const vector<vector<int>>& g, vector<int>& color) {
    queue<int> q;
    color[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g[u]) {
            if (color[v] == -1) {
                color[v] = color[u] ^ 1;
                q.push(v);
                continue;
            }
            if (color[v] == color[u]) {
                return false;
            }
        }
    }
    return true;
}

bool es_bipartito(int n, const vector<vector<int>>& g) {
    vector<int> color(n + 1, -1);
    for (int s = 1; s <= n; ++s) {
        if (color[s] != -1) {
            continue;
        }
        if (!pinta_componente(s, g, color)) {
            return false;
        }
    }
    return true;
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

    cout << (es_bipartito(n, g) ? "SI" : "NO") << "\n";
    return 0;
}
