# Editorial: La cosecha del plano

## Qué hay que hacer

Misma idea que “suma de un tramo de arreglo”, pero en 2D: suma de un rectángulo.

## Prefijo 2D

`p[i][j]` = suma de todo el rectángulo que va de $(1,1)$ a $(i,j)$.

Cómo armarlo (inclusión-exclusión de primaria):

$$
p[i][j] = a[i][j] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
$$

El menos es porque la esquina de arriba a la izquierda la sumaste dos veces.

Suma del rectángulo $(r_1,c_1)$–$(r_2,c_2)$:

$$
p[r_2][c_2] - p[r_1-1][c_2] - p[r_2][c_1-1] + p[r_1-1][c_1-1]
$$

El más del final: esa esquina la restaste dos veces.

Índices desde $1$. Fila/columna $0$ del `p` son ceros. `long long`.

## Si te da WA

Signos dados vuelta. O `int`. O índices desde $0$ mezclados con el enunciado que pide $1$.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m,q; cin>>n>>m>>q;
    vector<vector<ll>> p(n+1, vector<ll>(m+1,0));
    for (int i=1;i<=n;++i)
        for (int j=1;j<=m;++j) {
            ll x; cin>>x;
            p[i][j]=x+p[i-1][j]+p[i][j-1]-p[i-1][j-1];
        }
    while (q--) {
        int r1,c1,r2,c2; cin>>r1>>c1>>r2>>c2;
        cout << p[r2][c2]-p[r1-1][c2]-p[r2][c1-1]+p[r1-1][c1-1] << "\n";
    }
    return 0;
}
```
