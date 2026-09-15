# Editorial: Dónde está el mínimo

## Qué pide

El **índice más chico** (1-based) donde aparece $\min a$. Si el mínimo se repite, te quedas con la primera ocurrencia.

## Idea

Recorres de izquierda a derecha. Guardas el mínimo actual **y** su índice. Solo actualizas cuando ves un valor **estrictamente menor**. Si es igual, no tocas el índice: así gana la aparición más a la izquierda.

## Por qué “estrictamente menor”

Ejemplo: $a = [3, 1, 4, 1]$.

- $i=1$, mín $=3$, pos $=1$
- $i=2$, $1 < 3$ → mín $=1$, pos $=2$
- $i=3$, $4$ no mejora
- $i=4$, $1 = 1$ → **no** cambias pos

Respuesta $2$, no $4$. Si usas `<=` en vez de `<`, te quedarías con la **última** aparición: WA.

## 1-indexado

El enunciado cuenta posiciones desde $1$. Si tu `for` va de $0$ a $n-1$, imprime `i+1`. Olvidarlo es el WA más común de este problema.

## Por qué no hace falta buscar dos veces

Podrías: (1) hallar el mínimo, (2) recorrer de nuevo hasta encontrarlo. Es correcto y $O(n)$, pero un solo pase ya lleva el índice.

## Complejidad

$O(n)$ tiempo, $O(1)$ extra.

## Trampas

- Usar `<=` y devolver la última posición.
- Imprimir índice 0-based.
- Inicializar el mínimo en $0$ (mismo error que en “El mayor”, ahora con negativos).

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long best;
    cin >> best;
    int pos = 1;
    for (int i = 2; i <= n; ++i) {
        long long x;
        cin >> x;
        if (x < best) {
            best = x;
            pos = i;
        }
    }
    cout << pos << "\n";
}
```
