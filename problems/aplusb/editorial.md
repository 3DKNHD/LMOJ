# Editorial: A más B

## Qué pide

$T$ consultas independientes. En cada una te dan $A$ y $B$ y debes imprimir $A+B$ en su propia línea.

## Idea

No hay algoritmo escondido: lees $T$ y, por cada caso, lees dos enteros, los sumas y los imprimes. El problema existe para entrenar **I/O rápido** y **enteros de 64 bits**.

## Por qué 64 bits

Los límites son $-10^{18} \le A,B \le 10^{18}$. Entonces:

- El peor valor de $A+B$ es $2 \cdot 10^{18}$, que **sí cabe** en un `long long` ($\approx 9 \cdot 10^{18}$).
- Un `int` de 32 bits llega solo hasta $\approx 2 \cdot 10^9$. $10^{18}+10^{18}$ se desborda y da basura (WA silencioso).

En C++ usa `long long`. En Python los `int` ya son arbitrarios, así que la suma es correcta sola.

## Por qué hay que leer rápido

$T$ llega a $10^5$. Si usas `cin` sin desactivar sync, o `print` de Python línea a línea sin buffer, puedes llevar **TLE** aun con un algoritmo $O(T)$.

En C++:

```cpp
ios::sync_with_stdio(false);
cin.tie(nullptr);
```

En Python conviene leer todo de una vez (`sys.stdin.buffer.read`) o al menos usar `sys.stdin.readline`.

## Otras soluciones

Todas son equivalentes: un `for` de $T$ pasos. No hace falta guardar las $T$ sumas en un arreglo; puedes imprimir al vuelo y ahorrar memoria.

## Trampas

- Declarar `int a, b` en C++.
- Olvidar el salto de línea entre respuestas.
- Leer $T$ y después intentar leer $T+1$ pares.

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
        long long a, b;
        cin >> a >> b;
        cout << a + b << "\n";
    }
}
```
