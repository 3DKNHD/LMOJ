# Editorial: Cuántos divisores

## Qué pide

$T \le 10^5$ consultas: $d(n) = $ número de divisores positivos de $n$, $1 \le n \le 10^6$. $\sqrt{n}$ **por consulta** es $10^5 \cdot 10^3 = 10^8$ operaciones justas o TLE según implementación; la idea del pack es precalcular.

## Idea

Criba lineal de divisores. Para cada $i$, marcas múltiplos:

```text
d[1..N] = 0
para i = 1..N:
    para j = i, 2i, 3i, ... ≤ N:
        d[j]++
```

Cada $i$ es un divisor de cada múltiplo $j$. Al terminar, `d[n]` es exactamente el número de divisores.

## Complejidad del precompute

El bucle interno corre $\lfloor N/1 \rfloor + \lfloor N/2 \rfloor + \cdots + \lfloor N/N \rfloor \approx N \ln N$. Con $N=10^6$, $\approx 1.4 \cdot 10^7$ operaciones. Una vez. Después cada query es $O(1)$.

## Por qué $1$ y los primos salen bien

- $1$: solo el múltiplo $j=1$ cuando $i=1$ → `d[1]=1`.
- Primo $p$: lo tocan $i=1$ e $i=p$ → $2$ divisores.

## SPF / factorizar

Otra vía: criba de menor primo (`spf`). Luego para cada $n$:

$$
n = p_1^{e_1} \cdots p_k^{e_k} \implies d(n) = (e_1+1)\cdots(e_k+1)
$$

Precalculas `d[n]` con SPF en $O(N \log \log N)$ más un pase, o factorizas cada query en $O(\log n)$. También entra. El doble bucle de arriba es más corto.

## Complejidad total

$O(N \log N + T)$ tiempo, $O(N)$ memoria.

## Otras soluciones

- $\sqrt{n}$ por query: en C++ rápido a veces pasa, en Python no. El enunciado pide criba.
- Factorizar sin SPF hasta $\sqrt{n}$ por query: mismo problema.

## Trampas

- `int n` y leer mal $T$.
- Criba hasta $10^6$ pero olvidar `d[0]` o indexar en $0$.
- Recalcular divisores de $n$ desde cero $T$ veces.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    const int N = 1000000;
    vector<int> d(N + 1, 0);
    for (int i = 1; i <= N; ++i)
        for (int j = i; j <= N; j += i) ++d[j];
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << d[n] << "\n";
    }
}
```
