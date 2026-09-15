#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<vector<int>> g;
pair<int,int> farthest(int src) {
    vector<int> d(n+1, -1);
    queue<int> q; q.push(src); d[src]=0;
    int best=src;
    while (!q.empty()) {
        int u=q.front(); q.pop();
        if (d[u]>d[best]) best=u;
        for (int v: g[u]) if (d[v]==-1) { d[v]=d[u]+1; q.push(v); }
    }
    return {best, d[best]};
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    g.assign(n+1, {});
    for (int i=0;i<n-1;++i) {
        int u,v; cin>>u>>v;
        g[u].push_back(v); g[v].push_back(u);
    }
    int u = farthest(1).first;
    cout << farthest(u).second << "\n";
    return 0;
}
