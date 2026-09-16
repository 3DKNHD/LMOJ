#include <bits/stdc++.h>
using namespace std;

int posicion_del_minimo(const vector<long long>& a) {
    int pos = 0;
    for (int i = 1; i < (int)a.size(); ++i) {
        if (a[i] < a[pos]) {
            pos = i;
        }
    }
    return pos + 1;
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

    cout << posicion_del_minimo(a) << "\n";
    return 0;
}
