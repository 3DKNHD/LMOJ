#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        long long a, b, c;
        cin >> a >> b >> c;
        bool ok = a + b > c && a + c > b && b + c > a;
        cout << (ok ? "SI" : "NO") << "\n";
    }
    return 0;
}
