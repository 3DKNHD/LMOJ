#include <bits/stdc++.h>
using namespace std;

bool forman_triangulo(long long a, long long b, long long c) {
    return a + b > c && a + c > b && b + c > a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long a, b, c;
        cin >> a >> b >> c;
        cout << (forman_triangulo(a, b, c) ? "SI" : "NO") << "\n";
    }
    return 0;
}
