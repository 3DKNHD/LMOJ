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
