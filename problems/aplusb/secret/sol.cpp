#include <bits/stdc++.h>
using namespace std;

long long suma(long long a, long long b) {
    return a + b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long a, b;
        cin >> a >> b;
        cout << suma(a, b) << "\n";
    }
    return 0;
}
