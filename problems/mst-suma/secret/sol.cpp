#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct DSU {
    vector<int> p, r;
    DSU(int n): p(n+1), r(n+1,0) { iota(p.begin(), p.end(), 0); }
    int find(int x) { return p[x]==x ? x : p[x]=find(p[x]); }
    bool unite(int a, int b) {
        a=find(a); b=find(b); if (a==b) return false;
        if (r[a]<r[b]) swap(a,b);
        p[b]=a; if (r[a]==r[b]) ++r[a];
        return true;
    }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<array<ll,3>> e(m);
    for (int i=0;i<m;++i) cin >> e[i][1] >> e[i][2] >> e[i][0];
    sort(e.begin(), e.end());
    DSU d(n);
    ll cost=0; int used=0;
    for (auto &t: e) if (d.unite((int)t[1], (int)t[2])) { cost += t[0]; ++used; }
    if (used != n-1) cout << "IMPOSIBLE\n";
    else cout << cost << "\n";
    return 0;
}
