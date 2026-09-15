#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long best;
    cin >> best;
    for (int i = 1; i < n; ++i) {
        long long x;
        cin >> x;
        if (x > best) best = x;
    }
    cout << best << "\n";
    return 0;
}
