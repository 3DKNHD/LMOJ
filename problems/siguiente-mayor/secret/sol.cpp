#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin>>n;
    vector<ll> a(n);
    for (int i=0;i<n;++i) cin>>a[i];
    vector<int> ans(n, -1);
    vector<int> st;
    for (int i=n-1;i>=0;--i) {
        while (!st.empty() && a[st.back()]<=a[i]) st.pop_back();
        if (!st.empty()) ans[i]=a[st.back()];
        st.push_back(i);
    }
    for (int i=0;i<n;++i) {
        if (i) cout<<" ";
        cout<<ans[i];
    }
    cout<<"\n";
    return 0;
}
