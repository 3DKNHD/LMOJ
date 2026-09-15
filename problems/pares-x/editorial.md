# Editorial: Pares que suman X

## Qué pide

Número de pares de **índices** $i < j$ con $a_i + a_j = X$. Puede haber repetidos. $n \le 2\cdot 10^5$: $O(n^2)$ no entra. La respuesta cabe en 64 bits.

## Idea

Frecuencias. Si $v$ aparece $c_v$ veces, un par $\{v, X-v\}$ aporta:

- Si $v \ne X-v$: $c_v \cdot c_{X-v}$ pares, pero eso cuenta cada par **una vez por extremo**. Para no duplicar, iteras solo $v \le X-v$.
- Si $v = X-v$ (o sea $X = 2v$): son pares dentro del mismo valor: $\binom{c_v}{2} = c_v(c_v-1)/2$.

El oficial mete todo en un `map`, recorre cada $v$, y si `need = X-v` cumple `need >= v`, suma lo anterior.

## Por qué índices, no valores

$(i,j)$ distintos. Dos copias del mismo número son dos índices: $a = [5,5]$, $X=10$ da $1$ par, no $0$. Por eso $\binom{c}{2}$, no “si existe el valor”.

## 64 bits

$n=2\cdot 10^5$, peor caso todo igual y $X=2a_1$: $\binom{n}{2} \approx 2\cdot 10^{10}$. `long long`. Multiplica con `long long`: `c * (c-1) / 2`.

## Complejidad

`std::map` da $O(n \log n)$ inserciones y $O(u \log u)$ consultas, $u \le n$. Entra.

`unordered_map` es $O(n)$ esperado; hay que hashear `long long` (valores negativos). Two pointers tras ordenar también es $O(n \log n)$ y no usa mapa: dos índices en el arreglo **ordenado de valores**, con cuidado de no contar índices originales mal — más limpio contar sobre frecuencias o sobre el arreglo ordenado de pares `(valor, índice)`.

Two pointers sobre el arreglo ordenado de **valores** (cada aparición aparte):

```text
i = 0, j = n-1
mientras i < j:
  si a[i]+a[j] == X: hay que contar el bloque de iguales
  ...
```

Es fácil equivocarse con repetidos. El mapa es más difícil de romper.

## Otras soluciones

- Hashmap valor → cantidad, un pase: al ver $a_j$ sumas `freq[X - a_j]` (los de la **izquierda**) y luego incrementas `freq[a_j]`. Cuenta $i<j$ automáticamente, duplicados incluidos. $O(n)$ esperado. Muy limpio.

```cpp
long long ans = 0;
map<long long, long long> f;
for (long long x : a) {
    ans += f[X - x];
    f[x]++;
}
```

Equivale al oficial y evita el `need < v`.

## Trampas

- Contar cada par dos veces ($v$ y $X-v$).
- Usar `int` en el producto.
- `need = X - v` en `int` ( $X-v$ sale del 32-bit).
- Tratar $v$ y $X-v$ iguales como $c_v \cdot c_v$ (cuenta pares $(i,i)$).

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long X;
    cin >> n >> X;
    map<long long, long long> f;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        f[x]++;
    }
    long long ans = 0;
    for (auto [v, c] : f) {
        long long need = X - v;
        if (need < v) continue;
        if (need == v) ans += c * (c - 1) / 2;
        else {
            auto it = f.find(need);
            if (it != f.end()) ans += c * it->second;
        }
    }
    cout << ans << "\n";
}
```
