#include <bits/stdc++.h>
using namespace std;

int lis_estricta(const vector<long long>& a) {
    vector<long long> cola;
    for (long long x : a) {
        auto it = lower_bound(cola.begin(), cola.end(), x);
        if (it == cola.end()) {
            cola.push_back(x);
        } else {
            *it = x;
        }
    }
    return (int)cola.size();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << lis_estricta(a) << "\n";
    return 0;
}
