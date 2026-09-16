# Editorial: Tierra y mar

## Qué hay que hacer

El mapa es un rectángulo de tierra `.` y agua `#`. Una isla es un grupo de tierra donde puedes caminar en cruz (arriba/abajo/izq/der). **No en diagonal**.

Cada grupo cuenta $1$. Tierra suelta: isla de una celda. Todo agua: $0$.

## Cómo contarlas

Recorre todas las celdas. Cada vez que ves un `.` que **todavía no visitaste**, encontraste una isla nueva: `ans++`, y **pintas** toda esa isla para no contarla de nuevo.

Pintar = BFS (cola):

1. Mete la celda en la cola y marcala visitada **ya**.
2. Mientras la cola tenga algo: saca la de adelante, mira los $4$ vecinos.
3. Si el vecino es `.`, está dentro del mapa, y no está visitado: marcalo y encolalo.

Marcar **al encolar** (no al sacar) evita meter la misma celda mil veces.

## Por qué no DFS recursivo

Una isla puede tener $1000\times 1000$ celdas. Cada llamada recursiva come stack. En muchos sistemas eso es SIGSEGV (el programa se cae). La cola vive en el heap y aguanta.

## Ejemplo

```
.##
#..
```

Tres tierras: $(0,0)$ sola, y $(1,1)-(1,2)$ juntas. Las de la esquina $(0,0)$ y $(1,1)$ se tocan en diagonal → **dos** islas distintas. Total $2$.

## Si te da WA

8 vecinos. O no marcar visitado y contar la misma isla mil veces. O DFS recursivo (SE/RTE).

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int DR[4] = {-1, 1, 0, 0};
const int DC[4] = {0, 0, -1, 1};

bool dentro(int r, int c, int filas, int cols) {
    return r >= 0 && c >= 0 && r < filas && c < cols;
}

void marcar_isla(int sr, int sc, const vector<string>& grid, vector<vector<char>>& vis) {
    int filas = (int)grid.size();
    int cols = (int)grid[0].size();
    queue<pair<int, int>> q;
    q.push({sr, sc});
    vis[sr][sc] = 1;

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();
        for (int k = 0; k < 4; ++k) {
            int nr = r + DR[k];
            int nc = c + DC[k];
            if (!dentro(nr, nc, filas, cols) || vis[nr][nc] || grid[nr][nc] != '.') {
                continue;
            }
            vis[nr][nc] = 1;
            q.push({nr, nc});
        }
    }
}

int contar_islas(const vector<string>& grid) {
    int filas = (int)grid.size();
    int cols = (int)grid[0].size();
    vector<vector<char>> vis(filas, vector<char>(cols, 0));
    int islas = 0;

    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] != '.' || vis[i][j]) {
                continue;
            }
            ++islas;
            marcar_isla(i, j, grid, vis);
        }
    }
    return islas;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
    }

    cout << contar_islas(grid) << "\n";
    return 0;
}
```
