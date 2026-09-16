# Editorial: La cosecha del plano

## Qué hay que hacer

Misma idea que “suma de un tramo de arreglo”, pero en 2D: suma de un rectángulo.

## Prefijo 2D

`p[i][j]` = suma de todo el rectángulo que va de $(1,1)$ a $(i,j)$.

Cómo armarlo (inclusión-exclusión de primaria):

$$
p[i][j] = a[i][j] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
$$

El menos es porque la esquina de arriba a la izquierda la sumaste dos veces.

Suma del rectángulo $(r_1,c_1)$–$(r_2,c_2)$:

$$
p[r_2][c_2] - p[r_1-1][c_2] - p[r_2][c_1-1] + p[r_1-1][c_1-1]
$$

El más del final: esa esquina la restaste dos veces.

Índices desde $1$. Fila/columna $0$ del `p` son ceros. `long long`.

## Si te da WA

Signos dados vuelta. O `int`. O índices desde $0$ mezclados con el enunciado que pide $1$.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
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
```
