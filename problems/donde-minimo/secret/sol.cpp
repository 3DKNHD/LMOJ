#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long best;
    cin >> best;
    int pos = 1;
    for (int i = 2; i <= n; ++i) {
        long long x;
        cin >> x;
        if (x < best) {
            best = x;
            pos = i;
        }
    }
    cout << pos << "\n";
    return 0;
}
