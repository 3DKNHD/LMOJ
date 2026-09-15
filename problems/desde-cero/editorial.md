# Editorial: Desde las cero

## Qué pide

Un reloj 24 h que se reinicia cada $86400$ segundos ($24 \cdot 3600$). Para cada $t$ (segundos desde un origen, puede ser **muchos** días), imprime la hora que se ve: `HH:MM:SS` con dos dígitos siempre.

## Idea

El reloj solo ve la posición dentro del día actual:

$$
t \leftarrow t \bmod 86400
$$

Eso deja $t$ en $[0, 86399]$. Luego:

$$
\begin{align*}
H &= \lfloor t / 3600 \rfloor \\
M &= \lfloor (t \bmod 3600) / 60 \rfloor \\
S &= t \bmod 60
\end{align*}
$$

## Por qué el módulo va primero

Si $t = 10^{18}$, no puedes hacer `t / 3600` pensando en “hora absoluta” para imprimirla: esa hora no cabe en el reloj. El enunciado pide lo que **marca el reloj**, y el reloj vive en un ciclo de un día.

$86400$ cabe en `int`, pero $t$ no: lee `long long` y haz `t %= 86400`. En C++ el módulo de un `long long` positivo con un `int` se promociona bien.

$t \ge 0$, así que no hay módulo negativo.

## Por qué dos dígitos

`3:7:8` es WA. Tiene que ser `03:07:08`. En C++:

```cpp
cout << setfill('0') << setw(2) << h << ":"
     << setw(2) << m << ":"
     << setw(2) << s << "\n";
```

`setw` se gasta en el siguiente campo: por eso se repite. `setfill('0')` queda puesto.

En Python: `f"{h:02d}:{m:02d}:{s:02d}"`.

## Comprobación mental

- $t = 0$ → `00:00:00`
- $t = 3661$ → $1$ h $1$ min $1$ s → `01:01:01`
- $t = 86400$ → `00:00:00` (justo un día)
- $t = 86399$ → `23:59:59`

## Complejidad

$O(T)$. Aritmética $O(1)$ por caso.

## Otras soluciones

Usar `std::chrono` es overkill. Restar $86400$ en un `while` con $t = 10^{18}$ es TLE infinito a efectos prácticos: **tiene** que ser módulo, no un bucle.

## Trampas

- Olvidar `t %= 86400`.
- `int t` y perder $10^{18}$.
- Un solo dígito (`9:0:0`).
- Dividir mal: `t / 60` para minutos **del día** sin quitar las horas.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        long long t;
        cin >> t;
        t %= 86400;
        int h = (int)(t / 3600);
        int m = (int)((t % 3600) / 60);
        int s = (int)(t % 60);
        cout << setfill('0') << setw(2) << h << ":"
             << setw(2) << m << ":"
             << setw(2) << s << "\n";
    }
}
```
