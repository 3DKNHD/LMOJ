#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; ll S; cin>>n>>S;
    vector<ll> a(n);
    for (int i=0;i<n;++i) cin>>a[i];
    int ans=0, L=0; ll sum=0;
    for (int R=0;R<n;++R) {
        sum += a[R];
        while (L<=R && sum>S) { sum -= a[L]; ++L; }
        ans = max(ans, R-L+1);
    }
    cout << ans << "\n";
    return 0;
}
