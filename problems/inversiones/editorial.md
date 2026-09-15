# Editorial: Inversiones

## Qué pide

Número de pares $i < j$ con $a_i > a_j$. Empates **no** cuentan. $n \le 2\cdot 10^5$, $a_i \le 10^9$: $O(n^2)$ no entra. La respuesta cabe en 64 bits ($\binom{n}{2} \approx 2\cdot 10^{10}$).

## Idea

Procesas de izquierda a derecha. Cuando estás en $j$, cuántos $i < j$ tienen $a_i > a_j$. Eso es “cuántos ya vistos son **estrictamente mayores** que $a_j$”.

Estructura: Fenwick (BIT) de frecuencias sobre valores. Tras comprimir coordenadas:

- `fw.sum(x)` = cuántos ya insertados tienen valor $\le x$.
- Ya insertaste $j$ elementos (índices $0..j-1$, o sea $i$ en el oficial).
- Mayores que $a_j$: `i - fw.sum(a[j])`.

Luego `fw.add(a[j], 1)`.

Por qué $\le$ y no $<$: si usas `sum(a[j]-1)` cuentas valores $< a_j$, y $i$ menos eso incluye los **iguales**. Los iguales no son inversión. `sum(a[j])` incluye iguales, y al restar de $i$ **excluyes** iguales y menores: quedan solo los mayores. Exacto.

## Compresión

$a_i$ llega a $10^9$; el BIT necesita índices $1..u$ con $u\le n$. Ordenas una copia, `unique`, y reemplazas cada $a_i$ por su rango $1..u$.

Valores iguales reciben el **mismo** rango, y el argumento de arriba sigue valiendo.

## Merge sort

Al mergear dos mitades ordenadas, cada elemento de la derecha “se come” los de la izquierda que aún no salieron (son mayores y estaban antes). Es el conteo clásico $O(n\log n)$ sin BIT. También es la solución de libro.

`std::policy` / `__gnu_pbds` tree con order statistics: mismo $O(n\log n)$.

## Complejidad

$O(n \log n)$ tiempo, $O(n)$ memoria.

## Otras soluciones

- $O(n^2)$ doble `for`: TLE.
- `std::set` y `distance`: $O(n^2)$.
- Invertir el arreglo y contar “menores a la izquierda”: simétrico, mismo BIT.

## Trampas

- Contar $a_i \ge a_j$ (incluye iguales).
- BIT 0-indexado mal implementado (`i += i & -i` necesita índices $\ge 1$).
- Acumulador `int`.
- Comprimir sin `unique` (rangos con huecos no rompen, pero duplicar índices iguales sí si asignas posiciones distintas a empates).

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> t;
    Fenwick(int n) : n(n), t(n + 1, 0) {}
    void add(int i, int v) {
        for (; i <= n; i += i & -i) t[i] += v;
    }
    int sum(int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += t[i];
        return s;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    vector<int> b = a;
    sort(b.begin(), b.end());
    b.erase(unique(b.begin(), b.end()), b.end());
    for (int &x : a) x = int(lower_bound(b.begin(), b.end(), x) - b.begin()) + 1;
    Fenwick fw((int)b.size());
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans += i - fw.sum(a[i]);
        fw.add(a[i], 1);
    }
    cout << ans << "\n";
}
```
