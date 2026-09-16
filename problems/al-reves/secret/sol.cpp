#include <bits/stdc++.h>
using namespace std;

void imprimir_reverso(const vector<long long>& a) {
    for (int i = (int)a.size() - 1; i >= 0; --i) {
        if (i + 1 != (int)a.size()) {
            cout << " ";
        }
        cout << a[i];
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    imprimir_reverso(a);
    return 0;
}
