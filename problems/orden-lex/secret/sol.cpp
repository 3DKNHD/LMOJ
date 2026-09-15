#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    vector<int> indeg(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        indeg[v]++;
    }
    priority_queue<int, vector<int>, greater<>> pq;
    for (int i = 1; i <= n; ++i)
        if (indeg[i] == 0) pq.push(i);
    vector<int> ord;
    while (!pq.empty()) {
        int u = pq.top();
        pq.pop();
        ord.push_back(u);
        for (int v : g[u])
            if (--indeg[v] == 0) pq.push(v);
    }
    if ((int)ord.size() != n) {
        cout << "IMPOSIBLE\n";
        return 0;
    }
    for (int i = 0; i < n; ++i) {
        if (i) cout << " ";
        cout << ord[i];
    }
    cout << "\n";
    return 0;
}
