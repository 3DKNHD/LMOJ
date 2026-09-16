#include <bits/stdc++.h>
using namespace std;

long long suma(const vector<long long>& a) {
    long long total = 0;
    for (long long x : a) {
        total += x;
    }
    return total;
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

    cout << suma(a) << "\n";
    return 0;
}
