#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; int X; cin>>n>>X;
    unordered_map<int,int> f;
    f.reserve(n*2);
    f[0]=1;
    int p=0; ll ans=0;
    for (int i=0;i<n;++i) {
        int a; cin>>a;
        p ^= a;
        auto it=f.find(p^X);
        if (it!=f.end()) ans += it->second;
        f[p]++;
    }
    cout << ans << "\n";
    return 0;
}
