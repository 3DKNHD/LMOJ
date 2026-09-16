#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long caminos_hacia_n(int n, const vector<vector<int>>& g, vector<int> indeg) {
    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (indeg[i] == 0) {
            q.push(i);
        }
    }

    vector<long long> dp(n + 1, 0);
    dp[1] = 1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g[u]) {
            dp[v] = (dp[v] + dp[u]) % MOD;
            if (--indeg[v] == 0) {
                q.push(v);
            }
        }
    }
    return dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        indeg[v]++;
    }

    cout << caminos_hacia_n(n, g, indeg) << "\n";
    return 0;
}
