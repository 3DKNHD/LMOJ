#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        long long t;
        cin >> t;
        t %= 86400;
        int h = (int)(t / 3600);
        int m = (int)((t % 3600) / 60);
        int s = (int)(t % 60);
        cout << setfill('0') << setw(2) << h << ":"
             << setw(2) << m << ":"
             << setw(2) << s << "\n";
    }
    return 0;
}
