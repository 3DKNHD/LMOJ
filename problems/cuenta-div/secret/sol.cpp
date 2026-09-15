#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    const int N = 1000000;
    vector<int> d(N + 1, 0);
    for (int i = 1; i <= N; ++i)
        for (int j = i; j <= N; j += i) ++d[j];
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << d[n] << "\n";
    }
    return 0;
}
