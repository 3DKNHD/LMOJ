# Editorial: Pico de cobertura

## Qué pide

$n$ intervalos cerrados $[L,R]$ sobre la línea $1..M$. Máximo número de intervalos que cubren **el mismo** instante. $M \le 10^6$, $n \le 2\cdot 10^5$.

## Idea

Arreglo de diferencia. Quieres el máximo de la función

$$
c(x) = \#\{ i : L_i \le x \le R_i \}
$$

En vez de pintar cada intervalo (eso sería $O(nM)$), marcas bordes:

```text
d[L]   += 1    // a partir de L hay uno más
d[R+1] -= 1    // al salir de R deja de contar
```

Luego un prefijo:

$$
c(1) = d[1],\qquad c(x) = c(x-1) + d[x]
$$

El máximo de $c(x)$ en $1..M$ es la respuesta.

## Por qué $R+1$ y no $R$

El intervalo es cerrado. En $R$ todavía cubres. El $-1$ tiene que actuar en el **siguiente** entero. Si haces `d[R] -= 1`, el punto $R$ queda descubierto de más: WA.

`d` necesita índice $M+1$, por eso el vector es `M+2`.

## Por qué cabe

Memoria $O(M)$. Tiempo $O(n+M)$: $n$ actualizaciones $O(1)$ y un barrido de $M$. No hay que comprimir coordenadas porque $M \le 10^6$.

Si $M$ fuera $10^9$, comprimirías los $L$ y $R+1$ y barrerías eventos ordenados (sweep). Aquí no hace falta.

## Relación con “sesiones sin choque”

Ahí querías un **subconjunto sin solapes**. Aquí quieres el **máximo solape**. Son duales: greedy vs diferencia. No mezclar las ideas.

## Complejidad

$O(n+M)$ tiempo, $O(M)$ memoria.

## Otras soluciones

- Sweep: eventos $(L, +1)$ y $(R+1, -1)$, ordenas, recorres. $O(n \log n)$, útil si $M$ es enorme.
- Segment tree con lazy: overkill.

## Trampas

- `d[R] -= 1` en vez de `d[R+1]`.
- Barrer hasta $M$ pero el vector corto (acceso `d[M+1]` fuera).
- Confundir con el greedy de intervalos independientes.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, M;
    cin >> n >> M;
    vector<int> d(M + 2, 0);
    for (int i = 0; i < n; ++i) {
        int L, R;
        cin >> L >> R;
        d[L] += 1;
        d[R + 1] -= 1;
    }
    int cur = 0, ans = 0;
    for (int i = 1; i <= M; ++i) {
        cur += d[i];
        if (cur > ans) ans = cur;
    }
    cout << ans << "\n";
}
```
