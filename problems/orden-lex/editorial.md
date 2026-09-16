# Editorial: El cronograma

## Qué hay que hacer

Tareas con “esto antes que esto”. Quieres un orden válido. Si hay varios, el **más pequeño en orden de diccionario**: el que en la primera diferencia tiene el número menor. Si hay ciclo, `IMPOSIBLE`.

## Kahn + montículo de mínimos

`indeg[v]` = cuántas tareas tienen que ir **antes** que $v$.

Las que tienen `indeg 0` se pueden hacer ya. Para el orden lex, entre las disponibles **siempre elige el número más pequeño** (priority_queue de menores).

Cuando “haces” $u$, a cada vecino $v$ le bajas el indeg. Si llega a $0$, entra a la cola.

Si al final no salieron $n$ tareas, había ciclo.

## Si te da WA

Cola FIFO normal: te da *un* orden topológico, no el lex menor. O imprimes `IMPOSIBLE` con otro texto.

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
    vector<vector<int>> g(n + 1);
    vector<int> indeg(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        indeg[v]++;
    }
    priority_queue<int, vector<int>, greater<>> pq;
    for (int i = 1; i <= n; ++i)
        if (indeg[i] == 0) pq.push(i);
    vector<int> ord;
    while (!pq.empty()) {
        int u = pq.top();
        pq.pop();
        ord.push_back(u);
        for (int v : g[u])
            if (--indeg[v] == 0) pq.push(v);
    }
    if ((int)ord.size() != n) {
        cout << "IMPOSIBLE\n";
        return 0;
    }
    for (int i = 0; i < n; ++i) {
        if (i) cout << " ";
        cout << ord[i];
    }
    cout << "\n";
    return 0;
}
```
