#include <bits/stdc++.h>
using namespace std;

long long ultima_cifra(long long n) {
    if (n < 0) {
        n = -n;
    }
    return n % 10;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long n;
        cin >> n;
        cout << ultima_cifra(n) << "\n";
    }
    return 0;
}
