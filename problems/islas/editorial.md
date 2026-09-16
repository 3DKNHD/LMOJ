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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (int i = 0; i < n; ++i) cin >> g[i];
    vector<vector<char>> vis(n, vector<char>(m, 0));
    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (g[i][j] != '.' || vis[i][j]) continue;
            ++ans;
            queue<pair<int, int>> q;
            q.push({i, j});
            vis[i][j] = 1;
            while (!q.empty()) {
                auto [r, c] = q.front();
                q.pop();
                for (int k = 0; k < 4; ++k) {
                    int nr = r + dr[k], nc = c + dc[k];
                    if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
                    if (vis[nr][nc] || g[nr][nc] != '.') continue;
                    vis[nr][nc] = 1;
                    q.push({nr, nc});
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
```
