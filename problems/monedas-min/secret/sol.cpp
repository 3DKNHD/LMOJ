#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int min_monedas(const vector<int>& monedas, int objetivo) {
    vector<int> dp(objetivo + 1, INF);
    dp[0] = 0;
    for (int moneda : monedas) {
        for (int s = moneda; s <= objetivo; ++s) {
            dp[s] = min(dp[s], dp[s - moneda] + 1);
        }
    }
    if (dp[objetivo] >= INF) {
        return -1;
    }
    return dp[objetivo];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, objetivo;
    cin >> n >> objetivo;
    vector<int> monedas(n);
    for (int i = 0; i < n; ++i) {
        cin >> monedas[i];
    }

    cout << min_monedas(monedas, objetivo) << "\n";
    return 0;
}
