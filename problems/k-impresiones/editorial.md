# Editorial: Las copias

## Qué hay que hacer

$n$ impresoras. La $i$ saca una copia cada $t_i$ segundos. ¿En cuánto tiempo mínimo juntas $k$ copias?

En tiempo $T$, la impresora $i$ saca $\lfloor T / t_i \rfloor$ copias. El total es la suma de eso. Quieres el $T$ más pequeño con total $\ge k$.

No puedes probar $T=1,2,3,\ldots$ hasta $10^{18}$.

## Búsqueda binaria en la respuesta

La función “¿en tiempo $T$ llego?” es: no, no, no, **sí, sí, sí…** Una sola vez cambia de no a sí. Ahí sirve buscar el primer sí.

1. `lo = 1`, `hi = (la t_i más pequeña) * k` (en el peor caso una sola impresora hace todo).
2. Mientras `lo <= hi`:
   - `mid` el medio.
   - Si en `mid` segundos ya hay $\ge k$ copias: guarda $ans = mid$ y busca más a la izquierda (`hi = mid-1`).
   - Si no: `lo = mid+1`.
3. Imprime `ans`.

## Overflow

`mid / t_i` está bien (no se pasa). `mn * k` puede ser $10^9 \cdot 10^9 = 10^{18}$: `long long`. En el chequeo, si `done` ya llegó a $k$, corta: no sigas sumando.

## Si te da WA / TLE

Simular segundo a segundo. O `int` en `hi`. O `lo=0` y $k\ge 1$ (en $T=0$ hay $0$ copias).

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<long long> t(n);
    long long mn = (1LL << 62);
    for (int i = 0; i < n; ++i) {
        cin >> t[i];
        mn = min(mn, t[i]);
    }
    auto ok = [&](long long mid) {
        long long done = 0;
        for (long long x : t) {
            done += mid / x;
            if (done >= k) return true;
        }
        return false;
    };
    long long lo = 1, hi = mn * k, ans = hi;
    while (lo <= hi) {
        long long mid = lo + (hi - lo) / 2;
        if (ok(mid)) {
            ans = mid;
            hi = mid - 1;
        } else lo = mid + 1;
    }
    cout << ans << "\n";
    return 0;
}
```
