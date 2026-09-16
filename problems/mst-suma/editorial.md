# Editorial: Cablear el campus

## Qué hay que hacer

Quieres conectar $n$ edificios pagando lo menos posible. Eso es un **árbol recubridor mínimo** (MST): $n-1$ cables, sin ciclos, suma mínima. Si no se puede, `IMPOSIBLE`.

## Kruskal, en humano

1. Ordena **todos** los cables de más barato a más caro.
2. Recórrelos en ese orden. Si los dos edificios **aún no** están en la misma red (DSU, como en “Cables del lab”), usa el cable, sumá el costo.
3. Si usaste exactamente $n-1$ cables, imprime el costo. Si no, el grafo no era conexo.

¿Por qué el más barato primero? Cualquier ciclo futuro, el cable más caro del ciclo sobra. Kruskal nunca se arrepiente.

Suma en `long long`.

## Si te da WA

No comprobaste `used == n-1`. Uniste cables que formaban ciclo y sumaste de más.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Arista {
    int u;
    int v;
    long long peso;
};

struct DSU {
    vector<int> padre;
    vector<int> rango;

    DSU(int tam) : padre(tam + 1), rango(tam + 1, 0) {
        iota(padre.begin(), padre.end(), 0);
    }

    int raiz(int x) {
        if (padre[x] == x) {
            return x;
        }
        return padre[x] = raiz(padre[x]);
    }

    bool unir(int a, int b) {
        a = raiz(a);
        b = raiz(b);
        if (a == b) {
            return false;
        }
        if (rango[a] < rango[b]) {
            swap(a, b);
        }
        padre[b] = a;
        if (rango[a] == rango[b]) {
            ++rango[a];
        }
        return true;
    }
};

long long kruskal(int n, vector<Arista> aristas) {
    sort(aristas.begin(), aristas.end(), [](const Arista& a, const Arista& b) {
        return a.peso < b.peso;
    });

    DSU dsu(n);
    long long costo = 0;
    int usadas = 0;
    for (const auto& e : aristas) {
        if (dsu.unir(e.u, e.v)) {
            costo += e.peso;
            ++usadas;
        }
    }
    if (usadas != n - 1) {
        return -1;
    }
    return costo;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<Arista> aristas(m);
    for (int i = 0; i < m; ++i) {
        cin >> aristas[i].u >> aristas[i].v >> aristas[i].peso;
    }

    long long costo = kruskal(n, aristas);
    if (costo < 0) {
        cout << "IMPOSIBLE\n";
    } else {
        cout << costo << "\n";
    }
    return 0;
}
```
