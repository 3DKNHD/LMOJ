# Editorial: El reloj del aula

## Qué hay que hacer

El reloj tiene $24$ horas = $86400$ segundos y **se reinicia**. No le importa si pasaron $3$ días: muestra la hora **dentro del día actual**.

Te dan $t$ segundos desde un origen (puede ser un número gigante). Quieres `HH:MM:SS` con **siempre dos dígitos** (`09` no `9`).

## Paso a paso

1. Quita los días enteros: $t \leftarrow t \bmod 86400$. Ahora $t$ está entre $0$ y $86399$.
2. Horas: $H = t / 3600$ (división entera: $3661/3600=1$).
3. Lo que sobra: $t \bmod 3600$. Minutos: eso $/ 60$.
4. Segundos: lo que sobra al dividir por $60$.
5. Imprime con ceros a la izquierda.

## Ejemplo

$t = 3661$.

- $3661 < 86400$, no da vueltas el día.
- $H = 3661 / 3600 = 1$
- resto $61$ → $M = 1$, $S = 1$
- `01:01:01`

$t = 86400$ → resto $0$ → `00:00:00`.

$t = 10^{18}$: **primero** el módulo. Si haces $10^{18}/3600$ pensando en “hora absoluta” sale un resultado incorrecto y además no es lo que marca el reloj.

## Ceros a la izquierda en C++

```cpp
cout << setfill('0') << setw(2) << h << ":" << setw(2) << m << ":" << setw(2) << s << "\n";
```

Hace falta `#include <iomanip>` (en `bits/stdc++.h` ya está).

`t` es `long long`. `86400` entra en `int`, el módulo funciona.

## Si te da WA

- No hiciste $t \bmod 86400$.
- Imprimiste `1:1:1` sin ceros.
- Usaste `int` para $t$ ($10^{18}$ no entra).

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

string formatear_hora(long long segundos) {
    segundos %= 86400;
    int h = (int)(segundos / 3600);
    int m = (int)((segundos % 3600) / 60);
    int s = (int)(segundos % 60);

    ostringstream out;
    out << setfill('0') << setw(2) << h << ":"
        << setw(2) << m << ":"
        << setw(2) << s;
    return out.str();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long segundos;
        cin >> segundos;
        cout << formatear_hora(segundos) << "\n";
    }
    return 0;
}
```
