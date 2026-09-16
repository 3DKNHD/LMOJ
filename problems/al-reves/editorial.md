# Editorial: La cinta al revés

## Qué hay que hacer

Te dan una fila de números. Los tienes que imprimir al revés: el último primero, el primero último.

Es como una pila de platos: El último que pones es el primero que sale.

## Paso a paso

1. Lee $n$.
2. Guarda los $n$ números en un arreglo $a[0] … a[n-1]$. Aquí sí hace falta guardarlos, porque el primero que lees es el último que imprimes.
3. Recorre el arreglo **de atrás hacia adelante**: `i = n-1, n-2, …, 0`.
4. Imprime `a[i]` separado por espacios, y al final un salto de línea.

## Ejemplo

Entrada: `n=5` y `1 2 3 4 5`.

En el arreglo: posiciones $0..4$ tienen $1,2,3,4,5$.

Imprime desde $4$ hasta $0$: $5 4 3 2 1$.

## El espacio entre medio

Si imprimes un espacio **después** de cada número, te queda un espacio de más al final. Algunos jueces lo aceptan, otros no. El oficial pone el espacio **antes** de cada número excepto el primero.

## Si te da WA

- Imprimiste en el mismo orden que leíste.
- Te comiste el último o el primero.
- Pusiste saltos de línea en vez de espacios (el enunciado pide **una** línea).

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = n - 1; i >= 0; --i) {
        if (i + 1 != n) cout << " ";
        cout << a[i];
    }
    cout << "\n";
    return 0;
}
```
