#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Fenwick {
    int n; vector<ll> t;
    Fenwick(int n): n(n), t(n+1,0) {}
    void add(int i, ll v) { for (; i<=n; i+=i&-i) t[i]+=v; }
    ll pref(int i) { ll r=0; for (; i>0; i-=i&-i) r+=t[i]; return r; }
    ll range(int l, int r) { return pref(r)-pref(l-1); }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,q; cin>>n>>q;
    Fenwick fw(n);
    for (int i=1;i<=n;++i) { ll x; cin>>x; fw.add(i,x); }
    while (q--) {
        int tp; cin>>tp;
        if (tp==1) { int i; ll x; cin>>i>>x; fw.add(i,x); }
        else { int l,r; cin>>l>>r; cout<<fw.range(l,r)<<"\n"; }
    }
    return 0;
}
