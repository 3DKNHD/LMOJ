#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; cin>>n>>m;
    vector<vector<int>> g(n+1);
    for (int i=0;i<m;++i) {
        int u,v; cin>>u>>v;
        g[u].push_back(v); g[v].push_back(u);
    }
    vector<int> col(n+1, -1);
    for (int s=1;s<=n;++s) {
        if (col[s]!=-1) continue;
        queue<int> q; col[s]=0; q.push(s);
        while (!q.empty()) {
            int u=q.front(); q.pop();
            for (int v: g[u]) {
                if (col[v]==-1) { col[v]=col[u]^1; q.push(v); }
                else if (col[v]==col[u]) { cout<<"NO\n"; return 0; }
            }
        }
    }
    cout<<"SI\n";
    return 0;
}
