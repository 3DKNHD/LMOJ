#include <bits/stdc++.h>
using namespace std;

struct TablaGcd {
    vector<vector<int>> st;
    int logn;

    TablaGcd(const vector<int>& a) {
        int n = (int)a.size() - 1;
        logn = 1;
        while ((1 << logn) <= n) {
            ++logn;
        }
        st.assign(logn, vector<int>(n + 1));
        for (int i = 1; i <= n; ++i) {
            st[0][i] = a[i];
        }
        for (int k = 1; k < logn; ++k) {
            for (int i = 1; i + (1 << k) - 1 <= n; ++i) {
                st[k][i] = gcd(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
    }

    int consulta(int izq, int der) const {
        int k = 31 - __builtin_clz(der - izq + 1);
        return gcd(st[k][izq], st[k][der - (1 << k) + 1]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, consultas;
    cin >> n >> consultas;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    TablaGcd tabla(a);
    while (consultas--) {
        int izq, der;
        cin >> izq >> der;
        cout << tabla.consulta(izq, der) << "\n";
    }
    return 0;
}
