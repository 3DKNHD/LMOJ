#include <bits/stdc++.h>
using namespace std;

long long maximo(const vector<long long>& a) {
    long long mejor = a[0];
    for (int i = 1; i < (int)a.size(); ++i) {
        if (a[i] > mejor) {
            mejor = a[i];
        }
    }
    return mejor;
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

    cout << maximo(a) << "\n";
    return 0;
}
