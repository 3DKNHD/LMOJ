#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,S; cin>>n>>S;
    vector<int> c(n);
    for (int i=0;i<n;++i) cin>>c[i];
    const int INF=1e9;
    vector<int> dp(S+1, INF);
    dp[0]=0;
    for (int x: c)
        for (int j=x;j<=S;++j) dp[j]=min(dp[j], dp[j-x]+1);
    cout << (dp[S]>=INF ? -1 : dp[S]) << "\n";
    return 0;
}
