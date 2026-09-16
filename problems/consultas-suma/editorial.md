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

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<long long> prefijos(const vector<long long>& a) {
    int n = (int)a.size();
    vector<long long> p(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        p[i] = p[i - 1] + a[i - 1];
    }
    return p;
}

long long suma_rango(const vector<long long>& p, int izq, int der) {
    return p[der] - p[izq - 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, consultas;
    cin >> n >> consultas;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> p = prefijos(a);
    while (consultas--) {
        int izq, der;
        cin >> izq >> der;
        cout << suma_rango(p, izq, der) << "\n";
    }
    return 0;
}
```
