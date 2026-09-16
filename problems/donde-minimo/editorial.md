# Editorial: El más barato

## Qué hay que hacer

Quieres el número más pequeño de la lista, **pero no el número**: la **posición** (empezando en $1$, no en $0$). Si el mínimo aparece varias veces, te quedas con la aparición **más a la izquierda**.

## Paso a paso

1. Lee $n$.
2. Lee el primer número: `best` es ese valor, `pos = 1`.
3. Para $i = 2, 3, \ldots, n$: lees $x$. **Solo si** $x$ es **estrictamente menor** que $best$, actualizas `best = x` y `pos = i`.
4. Imprime `pos`.

Si $x$ empata con $best$, **no** toques `pos`. Así te quedas con el índice más pequeño.

## Ejemplo

Lista (posiciones $1..6$): $4,\ 2,\ 5,\ 2,\ 9,\ 2$.

- pos $1$: best $4$, pos $1$
- pos $2$: $2<4$ → best $2$, pos $2$
- pos $3$: $5$ no
- pos $4$: $2$ empata, no cambio → sigo en pos $2$
- pos $5$, $6$: no

Respuesta: $2$. No $4$ ni $6$.

## Si te da WA

- Imprimiste el valor en vez del índice.
- Índices desde $0$ (C++) y el juez espera desde $1$.
- Usaste `<=` y te quedaste con la **última** aparición.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

int posicion_del_minimo(const vector<long long>& a) {
    int pos = 0;
    for (int i = 1; i < (int)a.size(); ++i) {
        if (a[i] < a[pos]) {
            pos = i;
        }
    }
    return pos + 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << posicion_del_minimo(a) << "\n";
    return 0;
}
```
