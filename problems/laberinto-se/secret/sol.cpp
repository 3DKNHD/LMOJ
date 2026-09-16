#include <bits/stdc++.h>
using namespace std;

const int DR[4] = {-1, 1, 0, 0};
const int DC[4] = {0, 0, -1, 1};

pair<int, int> buscar(const vector<string>& grid, char marca) {
    for (int i = 0; i < (int)grid.size(); ++i) {
        for (int j = 0; j < (int)grid[i].size(); ++j) {
            if (grid[i][j] == marca) {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

bool dentro(int r, int c, int filas, int cols) {
    return r >= 0 && c >= 0 && r < filas && c < cols;
}

int distancia(const vector<string>& grid, pair<int, int> inicio, pair<int, int> fin) {
    int filas = (int)grid.size();
    int cols = (int)grid[0].size();
    vector<vector<int>> dist(filas, vector<int>(cols, -1));
    queue<pair<int, int>> q;

    dist[inicio.first][inicio.second] = 0;
    q.push(inicio);

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();
        for (int k = 0; k < 4; ++k) {
            int nr = r + DR[k];
            int nc = c + DC[k];
            if (!dentro(nr, nc, filas, cols) || grid[nr][nc] == '#' || dist[nr][nc] != -1) {
                continue;
            }
            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }
    return dist[fin.first][fin.second];
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

    cout << distancia(grid, buscar(grid, 'S'), buscar(grid, 'E')) << "\n";
    return 0;
}
