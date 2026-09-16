# Editorial: El tramo del viaje

## Qué hay que hacer

Números $\ge 0$. Quieres el intervalo **contiguo más largo** cuya suma sea $\le S$. Si ni un elemento entra, $0$.

## Dos punteros (la ventana que se mueve)

Como todo es $\ge 0$, si un tramo $L..R$ ya se pasó de $S$, agrandar $R$ lo empeora. Hay que mover $L$ hacia la derecha.

1. `L=0`, `sum=0`, `ans=0`.
2. `R` recorre $0..n-1$: sumas `a[R]`.
3. Mientras `sum > S` y `L <= R`: restas `a[L]`, `L++`.
4. Ahora $L..R$ es el tramo más largo que termina en $R$ y entra. `ans = max(ans, R-L+1)`.

Cada índice entra y sale de la ventana **una vez**. Lineal.

## Ejemplo

$a=[1,2,3,4]$, $S=5$

- $R=0$ sum $1$ largo $1$
- $R=1$ sum $3$ largo $2$
- $R=2$ sum $6>5$ → saco $1$, sum $5$, largo $2$
- $R=3$ sum $9>5$ → saco hasta que entre, queda $[4]$ largo $1$

Respuesta $2$.

## Si te da TLE

Probar todos los $L,R$.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; ll S; cin>>n>>S;
    vector<ll> a(n);
    for (int i=0;i<n;++i) cin>>a[i];
    int ans=0, L=0; ll sum=0;
    for (int R=0;R<n;++R) {
        sum += a[R];
        while (L<=R && sum>S) { sum -= a[L]; ++L; }
        ans = max(ans, R-L+1);
    }
    cout << ans << "\n";
    return 0;
}
```
