#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll MOD = 1000000007LL;
ll binpow(ll a, ll e) {
    ll r=1; a%=MOD;
    while (e) { if (e&1) r=r*a%MOD; a=a*a%MOD; e>>=1; }
    return r;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    const int N=1000000;
    vector<ll> fac(N+1), ifac(N+1);
    fac[0]=1;
    for (int i=1;i<=N;++i) fac[i]=fac[i-1]*i%MOD;
    ifac[N]=binpow(fac[N], MOD-2);
    for (int i=N;i>=1;--i) ifac[i-1]=ifac[i]*i%MOD;
    int T; cin>>T;
    while (T--) {
        int n,k; cin>>n>>k;
        if (k<0 || k>n) cout<<"0\n";
        else cout << fac[n]*ifac[k]%MOD*ifac[n-k]%MOD << "\n";
    }
    return 0;
}
