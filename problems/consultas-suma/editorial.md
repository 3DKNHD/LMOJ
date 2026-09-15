# Editorial: Consultas de suma

## Qué pide

Arreglo **estático** $a_1,\dots,a_n$ y $q$ consultas $[L,R]$ (cerrado, 1-indexado). Imprime $a_L+\cdots+a_R$. $n,q \le 2\cdot 10^5$: $O(nq)$ no entra.

## Idea

Prefijos. Definís

$$
p_0 = 0,\qquad p_i = a_1 + \cdots + a_i
$$

Entonces

$$
a_L + \cdots + a_R = p_R - p_{L-1}
$$

Precomputas $p$ en $O(n)$ y cada consulta es $O(1)$. Total $O(n+q)$.

## Por qué es cierto

$p_R$ suma todo hasta $R$. $p_{L-1}$ suma todo **antes** de $L$. Al restar quedan exactamente las posiciones $L..R$. Si $L=1$, $p_{L-1}=p_0=0$. Por eso el arreglo de prefijos tiene tamaño $n+1$ y arranca en $0$.

## 64 bits

Cada $|a_i|\le 10^9$, $n\le 2\cdot 10^5$, así que $|p_i|\le 2\cdot 10^{14}$. `long long` en $p$ y en la respuesta.

## Por qué no Fenwick / segment tree

Funcionan, pero el arreglo **no cambia**. Un BIT es $O(\log n)$ por consulta: más código para nada. Prefijo es la herramienta exacta.

## Complejidad

Tiempo $O(n+q)$, memoria $O(n)$.

## Otras soluciones

- Sparse table de sumas: overkill (la suma no es idempotente de la misma forma que el mínimo; se puede, pero no aporta).
- Recalcular cada rango: TLE.

## Trampas

- Usar $p_R - p_L$ en vez de $p_R - p_{L-1}$ (te comes $a_L$).
- Prefijos en `int`.
- Consultas 0-indexadas contra arreglo 1-indexado.

## Código de referencia (C++)

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
}
```
