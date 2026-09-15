# Editorial: Cifra final

## Qué pide

Para cada $n$, su **última cifra decimal** (un dígito $0$–$9$). Si $n$ es negativo, usas el valor absoluto: $-17$ termina en $7$.

## Idea

La última cifra de un no negativo es $n \bmod 10$. Para negativos, primero quitas el signo y después el módulo.

$$
\text{respuesta} = |n| \bmod 10
$$

## Por qué `n % 10` crudo falla en C++

El operador `%` en C++ sigue el signo del dividendo:

| $n$ | $n \% 10$ en C++ | lo que queremos |
|-----|------------------|-----------------|
| $17$ | $7$ | $7$ |
| $-17$ | $-7$ | $7$ |
| $-10$ | $0$ | $0$ |

Si imprimes `-7`, el juez espera `7`: WA. Por eso el oficial hace:

```cpp
if (n < 0) n = -n;
cout << n % 10;
```

**Python** (`n % 10`) ya da un resto $0..9$ incluso para negativos (`(-17) % 10 == 3` — **espera**). Eso **no** es la última cifra de $-17$. En Python hay que hacer `abs(n) % 10` igual que en C++.

## Overflow al negar

`n = -n` explota si $n$ es exactamente $-2^{63}$ (`LONG_MIN`). Aquí $n \ge -10^{18}$, y $-10^{18} > -2^{63}$, así que es seguro. Si copias este truco a otro problema con todo el rango de `long long`, usa `unsigned` o `std::llabs` con cuidado.

## 64 bits

$|n|$ llega a $10^{18}$. Lee `long long`. El dígito de salida cabe en `int`.

## Complejidad

$O(T)$ con $T \le 10^5$. I/O rápido.

## Otras soluciones

Pasar a string y tomar el último carácter que sea dígito (saltando un `-` inicial). Correcto, más lento de tipear. La aritmética es la idea.

## Trampas

- Imprimir el `%` negativo de C++.
- En Python, usar `n % 10` sin `abs` (para $-17$ sale $3$, no $7$).
- Leer `int` y perder los $10^{18}$.

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
        long long n;
        cin >> n;
        if (n < 0) n = -n;
        cout << n % 10 << "\n";
    }
}
```
