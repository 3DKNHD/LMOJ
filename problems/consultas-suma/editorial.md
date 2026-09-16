# Editorial: El libro de caja

## Qué hay que hacer

El arreglo **no cambia**. Te preguntan muchas veces “suma del índice $L$ al $R$”. Si cada vez recorres $L..R$, en el peor caso haces $n\cdot q \approx 4\cdot 10^{10}$ sumas. Eso no entra en tiempo.

## La idea: suma acumulada

Arma `p[0] = 0` y

$$
p[i] = a_1 + a_2 + \cdots + a_i
$$

O sea `p[i] = p[i-1] + a[i]`.

La suma $a_L+\cdots+a_R$ es “todo hasta $R$” menos “todo hasta $L-1$”:

$$
p[R] - p[L-1]
$$

Si $L=1$, $p[0]=0$ y queda $p[R]$. Por eso el arreglo $p$ tiene tamaño $n+1$ y empieza en índice $1$.

## Ejemplo

$a = [3, 1, 4, 2]$ (índices $1..4$)

| $i$ | $p[i]$ |
|-----|--------|
| $0$ | $0$ |
| $1$ | $3$ |
| $2$ | $4$ |
| $3$ | $8$ |
| $4$ | $10$ |

Suma $2..4$: $p[4]-p[1] = 10-3 = 7$. Chequeo: $1+4+2=7$.

## 64 bits

Cada $a_i$ $\pm 10^9$, $n=2\cdot 10^5$: el prefijo llega a $2\cdot 10^{14}$. `long long`.

## Si te da TLE / WA

- Recorrer el rango cada vez.
- `p[R]-p[L]` olvidándote el $-1$ (omites $a_L$).
- `int` en `p`.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> p(n + 1);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        p[i] = p[i - 1] + x;
    }
    while (q--) {
        int L, R;
        cin >> L >> R;
        cout << p[R] - p[L - 1] << "\n";
    }
    return 0;
}
```
