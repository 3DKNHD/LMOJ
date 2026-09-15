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
