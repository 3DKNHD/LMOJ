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

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<ll> d;
    for (int i = 0; i < n; ++i) {
        ll x;
        cin >> x;
        auto it = lower_bound(d.begin(), d.end(), x);
        if (it == d.end()) d.push_back(x);
        else *it = x;
    }
    cout << d.size() << "\n";
    return 0;
}
```
