#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    const long long NEG = -(1LL << 60);
    long long m1 = NEG, m2 = NEG;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (x > m1) {
            m2 = m1;
            m1 = x;
        } else if (x < m1 && x > m2) {
            m2 = x;
        }
    }
    if (m2 == NEG) cout << -1 << "\n";
    else cout << m2 << "\n";
    return 0;
}
