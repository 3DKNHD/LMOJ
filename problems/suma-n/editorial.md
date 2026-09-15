# Editorial: Suma de la lista

## Qué pide

La suma $a_1 + \cdots + a_n$. Un solo número de salida.

## Idea

Recorre el arreglo una vez y acumula. Complejidad $O(n)$, memoria $O(1)$ extra si no necesitas guardar el arreglo después (aunque guardarlo también cabe).

## Por qué 64 bits (otra vez)

$n \le 2 \cdot 10^5$ y cada $|a_i| \le 10^9$. El peor caso:

$$
2 \cdot 10^5 \cdot 10^9 = 2 \cdot 10^{14}
$$

Eso **no cabe** en 32 bits. El acumulador tiene que ser `long long` (o `int` de Python).

Cuidado con este bug clásico:

```cpp
int n, x, s = 0;
for (...) { cin >> x; s += x; }  // s se desborda
```

Aunque `x` quepa en `int`, **la suma no**. Declara `long long s = 0`.

Los $a_i$ también pueden ser negativos: la suma mínima es $-2 \cdot 10^{14}$, que sigue cabiendo en `long long`.

## Por qué un solo pase alcanza

La suma es asociativa y conmutativa. No importa el orden. No hay que ordenar, no hay que usar fórmulas raras. Si haces dos pases (uno para leer, otro para sumar) también es $O(n)$ y está bien; solo no hagas $O(n^2)$.

## Otras soluciones

- Recursión para “sumar el resto” es innecesaria y se come el stack con $n = 2 \cdot 10^5$.
- `std::accumulate` es lo mismo que el bucle, siempre que el tipo inicial sea `0LL`.

## Trampas

- Acumulador `int`.
- Leer mal: a veces ponen $n$ en la misma línea que los $a_i$. Aquí $n$ va **solo** en la primera línea.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long s = 0;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        s += x;
    }
    cout << s << "\n";
}
```
