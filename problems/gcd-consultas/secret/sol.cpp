#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,q; cin>>n>>q;
    int LOG=1; while ((1<<LOG)<=n) ++LOG;
    vector<vector<int>> st(LOG, vector<int>(n+1));
    for (int i=1;i<=n;++i) cin>>st[0][i];
    for (int k=1;k<LOG;++k)
        for (int i=1;i+(1<<k)-1<=n;++i)
            st[k][i]=gcd(st[k-1][i], st[k-1][i+(1<<(k-1))]);
    while (q--) {
        int l,r; cin>>l>>r;
        int k = 31 - __builtin_clz(r-l+1);
        cout << gcd(st[k][l], st[k][r-(1<<k)+1]) << "\n";
    }
    return 0;
}
