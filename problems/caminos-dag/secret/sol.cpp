#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD=1000000007LL;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; cin>>n>>m;
    vector<vector<int>> g(n+1);
    vector<int> indeg(n+1);
    for (int i=0;i<m;++i) {
        int u,v; cin>>u>>v;
        g[u].push_back(v); indeg[v]++;
    }
    queue<int> q;
    for (int i=1;i<=n;++i) if (!indeg[i]) q.push(i);
    vector<ll> dp(n+1,0);
    dp[1]=1;
    while (!q.empty()) {
        int u=q.front(); q.pop();
        for (int v: g[u]) {
            dp[v]=(dp[v]+dp[u])%MOD;
            if (--indeg[v]==0) q.push(v);
        }
    }
    cout << dp[n] << "\n";
    return 0;
}
