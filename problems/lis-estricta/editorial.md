# Editorial: La colección creciente

## Qué hay que hacer

La subsecuencia creciente más larga, **estricta**, no tiene por qué ser contigua. $n=2\cdot 10^5$: $n^2$ no entra.

## El arreglo `d`

`d[k]` = el **menor último valor** posible de una creciente de largo $k+1$ que viste.

Por cada $x$:

- Busca el primer lugar en `d` que sea $\ge x$ (`lower_bound`).
- Si no hay, $x$ alarga la colección: $d.push_back(x)$.
- Si hay, **reemplazas** ese último valor por $x$ (queda un final más pequeño, más fácil de extender después).

`d.size()` al final es la respuesta. `d` **no** es la subsecuencia, solo su largo.

Como es estricta, `lower_bound` ($\ge$) y no `upper_bound`. Si $x$ empata, reemplaza y no alarga.

## Ejemplo

$1, 3, 2$

- $1$ → $d=[1]$
- $3$ → $d=[1,3]$
- $2$ reemplaza el $3$ → `d=[1,2]` largo $2$

## Si te da TLE / WA

$n^2$. O subarreglo contiguo. O creciente no estricta ($<=$).

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

int lis_estricta(const vector<long long>& a) {
    vector<long long> cola;
    for (long long x : a) {
        auto it = lower_bound(cola.begin(), cola.end(), x);
        if (it == cola.end()) {
            cola.push_back(x);
        } else {
            *it = x;
        }
    }
    return (int)cola.size();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << lis_estricta(a) << "\n";
    return 0;
}
```
