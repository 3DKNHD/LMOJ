# Editorial: K impresiones

## Qué pide

$n$ impresoras; la $i$-ésima produce una copia en $t_i, 2t_i, 3t_i, \ldots$. Mínimo $T$ tal que en el segundo $T$ hay al menos $k$ copias. $n \le 2\cdot 10^5$, $k,t_i \le 10^9$.

En tiempo $T$, la impresora $i$ produjo $\lfloor T / t_i \rfloor$ copias.

## Idea

$f(T) = \sum_i \lfloor T / t_i \rfloor$ es **monótona creciente**. Buscas el mínimo $T$ con $f(T) \ge k$ por búsqueda binaria sobre $T$.

## Rango de la binaria

Cota inferior: $T \ge 1$ (salvo $k=0$, que aquí no pasa).

Cota superior: con **solo** la impresora más rápida, tardas $t_{\min} \cdot k$ segundos. Eso es $\le 10^9 \cdot 10^9 = 10^{18}$, cabe en `long long`. El oficial usa `hi = mn * k`.

Nunca hagas `lo + hi` sin cuidado: usa `mid = lo + (hi - lo) / 2`.

## Overflow dentro de `ok`

Sin cortar, `done += mid / x` se suma $n$ veces y cada término puede ser $10^{18}$: $2\cdot 10^5 \cdot 10^{18}$ explota. Por eso, en cuanto `done >= k`, `return true`. No necesitas el valor exacto de $f(T)$, solo si alcanza.

`mn * k` también hay que hacerlo en `long long`.

## Por qué el mínimo existe y la binaria lo encuentra

En $T = 0$, $f=0 < k$. En $T = t_{\min} k$, la más rápida sola ya produjo $k$. Existe un primer $T$ que cumple. Si `ok(mid)`, pruebas más chico (`hi = mid-1`); si no, más grande.

## Complejidad

$O(n \log (t_{\min} k))$ $\approx n \cdot 60$, con $n=2\cdot 10^5$: $\approx 10^7$. Entra.

Simular segundo a segundo: TLE. Min-heap de “próxima impresión”: $O(k \log n)$ con $k=10^9$: TLE.

## Otras soluciones

La binaria es la solución. No hay fórmula cerrada simple con $n$ velocidades distintas.

## Trampas

- `int` en $T$ o en `mn * k`.
- No cortar `done` y desbordar.
- `mid / x` con $x = 0$ (los $t_i \ge 1$).
- Buscar el máximo $T$ en vez del mínimo (invertir `lo/hi`).
- Off-by-one: `lo=0` y $k\ge 1$ puede devolver $0$.

## Código de referencia (C++)

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
}
```
