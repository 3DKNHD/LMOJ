#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m,q; cin>>n>>m>>q;
    vector<vector<ll>> p(n+1, vector<ll>(m+1,0));
    for (int i=1;i<=n;++i)
        for (int j=1;j<=m;++j) {
            ll x; cin>>x;
            p[i][j]=x+p[i-1][j]+p[i][j-1]-p[i-1][j-1];
        }
    while (q--) {
        int r1,c1,r2,c2; cin>>r1>>c1>>r2>>c2;
        cout << p[r2][c2]-p[r1-1][c2]-p[r2][c1-1]+p[r1-1][c1-1] << "\n";
    }
    return 0;
}
