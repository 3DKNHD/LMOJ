#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,k; cin>>n>>k;
    vector<ll> a(n);
    for (int i=0;i<n;++i) cin>>a[i];
    deque<int> dq;
    vector<ll> out;
    for (int i=0;i<n;++i) {
        while (!dq.empty() && dq.front()<=i-k) dq.pop_front();
        while (!dq.empty() && a[dq.back()]<=a[i]) dq.pop_back();
        dq.push_back(i);
        if (i>=k-1) out.push_back(a[dq.front()]);
    }
    for (int i=0;i<(int)out.size();++i) {
        if (i) cout<<" ";
        cout<<out[i];
    }
    cout<<"\n";
    return 0;
}
