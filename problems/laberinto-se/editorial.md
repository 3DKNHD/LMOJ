# Editorial: Del patio al aula

## Qué hay que hacer

Grilla. `S` inicio, `E` fin, `#` pared, `.` piso. Pasos en cruz. Distancia mínima o `-1`.

Es el mismo BFS de “Hasta la sala $n$”, pero las “salas” son celdas.

## Paso a paso

1. Lee la grilla. Busca dónde está `S` y `E`.
2. `dist` todo `-1`. `dist[S] = 0`. Cola con `S`.
3. Vecinos: $\pm 1$ en fila o columna. Si te salís, si es $#$, o si ya tiene dist, skip.
4. `dist[vecino] = dist[actual]+1`.
5. Imprime `dist[E]`.

`S` y `E` se caminan (no son pared).

## Si te da WA

Diagonales. DFS. Tratar `E` como pared.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (int i = 0; i < n; ++i) cin >> g[i];
    int sr = 0, sc = 0, er = 0, ec = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            if (g[i][j] == 'S') sr = i, sc = j;
            if (g[i][j] == 'E') er = i, ec = j;
        }
    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};
    vector<vector<int>> dist(n, vector<int>(m, -1));
    queue<pair<int, int>> q;
    dist[sr][sc] = 0;
    q.push({sr, sc});
    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
            if (g[nr][nc] == '#' || dist[nr][nc] != -1) continue;
            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }
    cout << dist[er][ec] << "\n";
    return 0;
}
```
