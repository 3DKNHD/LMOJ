#include <bits/stdc++.h>
using namespace std;

vector<vector<long long>> prefijo_2d(const vector<vector<long long>>& a) {
    int filas = (int)a.size();
    int cols = (int)a[0].size();
    vector<vector<long long>> p(filas + 1, vector<long long>(cols + 1, 0));
    for (int i = 1; i <= filas; ++i) {
        for (int j = 1; j <= cols; ++j) {
            p[i][j] = a[i - 1][j - 1] + p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1];
        }
    }
    return p;
}

long long suma_submatriz(const vector<vector<long long>>& p, int r1, int c1, int r2, int c2) {
    return p[r2][c2] - p[r1 - 1][c2] - p[r2][c1 - 1] + p[r1 - 1][c1 - 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, consultas;
    cin >> n >> m >> consultas;
    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    vector<vector<long long>> p = prefijo_2d(a);
    while (consultas--) {
        int r1, c1, r2, c2;
        cin >> r1 >> c1 >> r2 >> c2;
        cout << suma_submatriz(p, r1, c1, r2, c2) << "\n";
    }
    return 0;
}
