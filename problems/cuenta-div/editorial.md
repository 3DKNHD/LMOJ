# Editorial: Reparto exacto

## Qué hay que hacer

Los divisores de $6$ son $1,2,3,6$: hay $4$. De un primo hay $2$ (el $1$ y él mismo). Del $1$ hay $1$.

Te hacen $T$ preguntas, cada una un $n \le 10^6$. Si por cada $n$ recorres hasta $\sqrt{n}$, con $T=10^5$ te come el tiempo.

## La idea (como la tabla del $2$, pero para todos)

Arma un arreglo `d[1..1000000]` en $0$.

Para cada $i = 1, 2, 3, \ldots, 10^6$:
- Recorre los múltiplos $i, 2i, 3i, \ldots$ y a cada uno le sumas $1$ en $d$.

¿Por qué funciona? Cada divisor $i$ de $n$ se anota exactamente cuando el `for` de $i$ pasa por $n$. Al final $d[n]$ es cuántos divisores tiene.

Esto se hace **una vez** al inicio. Después cada pregunta es `d[n]`: tiempo constante.

## ¿No es lento el doble for?

El `i=1` toca $10^6$ celdas, el $i=2$ toca $5\cdot 10^5$, etc. El total es $10^6 \cdot (1+1/2+1/3+\cdots) \approx 10^6 \cdot 14$, unos $14$ millones. Entra holgado.

## Ejemplo

$n=6$: lo tocan $i=1,2,3,6$ → $d[6]=4$.

## Si te da TLE

$\sqrt{n}$ por consulta. O criba mal escrita que hace $n^2$.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    const int N = 1000000;
    vector<int> d(N + 1, 0);
    for (int i = 1; i <= N; ++i)
        for (int j = i; j <= N; j += i) ++d[j];
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << d[n] << "\n";
    }
    return 0;
}
```
