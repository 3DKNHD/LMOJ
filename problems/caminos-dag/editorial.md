# Editorial: Senderos hacia el auditorio

## Qué hay que hacer

Calles de **un solo sentido**, **sin ciclos**. Caminos de $1$ a $n$, módulo $10^9+7$. Quedarte en $1$ cuando $n=1$ cuenta $1$.

## DP en orden topológico

`dp[v]` = formas de llegar a $v$ desde $1$. `dp[1]=1`. El resto $0$.

Procesa los nodos en un orden donde $u$ aparece **antes** que $v$ si hay arco $u\to v$ (Kahn: cola de indeg $0$).

Cuando procesas $u$, para cada salida $v$: $dp[v] += dp[u]$ (con módulo).

Si nunca llega nada a $n$, $dp[n]$ quedó $0$.

## Si te da WA

DFS recursivo sin orden: puedes contar dos veces o usar `dp[v]` antes de estar listo. Olvidar el módulo.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long caminos_hacia_n(int n, const vector<vector<int>>& g, vector<int> indeg) {
    queue<int> q;
    for (int i = 1; i <= n; ++i) {
        if (indeg[i] == 0) {
            q.push(i);
        }
    }

    vector<long long> dp(n + 1, 0);
    dp[1] = 1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g[u]) {
            dp[v] = (dp[v] + dp[u]) % MOD;
            if (--indeg[v] == 0) {
                q.push(v);
            }
        }
    }
    return dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        indeg[v]++;
    }

    cout << caminos_hacia_n(n, g, indeg) << "\n";
    return 0;
}
```
