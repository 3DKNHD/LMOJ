#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long s = 0;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        s += x;
    }
    cout << s << "\n";
    return 0;
}
