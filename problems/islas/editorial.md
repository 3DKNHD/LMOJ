# Editorial: Islas de puntos

## Qué pide

Grilla $n\times m$ ($n,m\le 1000$) de `.` tierra y `#` agua. Cuántas componentes 4-conectadas de `.` (no diagonales).

## Idea

Cada isla es una componente conexa. Recorres celdas; cuando ves un `.` no visitado, sumas $1$ y **inundas** toda la isla (BFS o DFS iterativo).

4 direcciones: $(-1,0),(1,0),(0,-1),(0,1)$.

## Por qué no DFS recursivo

Una isla puede ser $1000\times 1000 = 10^6$ celdas. DFS recursivo usa $O(\text{tamaño})$ de stack de C++ y en muchos jueces muere (`SIGSEGV`). BFS con `queue` o DFS con `vector` como pila viven en el heap.

El oficial es BFS: al descubrir la celda la marcas visitada **antes** de encolar, para no encolarla mil veces.

## Complejidad

Cada celda se visita $O(1)$ veces. $O(nm)$ tiempo y memoria. $10^6$ está bien.

## Diagonales

Dos `.` en diagonal **no** son la misma isla. Si pones 8 vecinos, unes de más.

## Bordes

Chequea `nr,nc` dentro de $[0,n)\times[0,m)$. El agua `#` no se visita.

## Otras soluciones

- DFS iterativo: equivalente.
- DSU en celdas de tierra, uniendo vecinos `.`: $O(nm\alpha)$. Más código.
- Flood fill recursivo con `ulimit` enorme: no lo hagas.

## Trampas

- DFS de sistema.
- 8-conectividad.
- Leer la grilla con `cin >> char` mezclando espacios (aquí cada fila es un `string` sin espacios).
- No marcar visitado al encolar: la cola explota.

## Código de referencia (C++)

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
}
```
