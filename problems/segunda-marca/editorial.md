# Editorial: Segunda marca

## Qué pide

La **segunda más grande entre los valores distintos**. Si todos los números son iguales, no existe: imprime `-1`.

Ejemplo del enunciado: $5,1,5,3,3,4$. Los distintos ordenados desc. son $5,4,3,1$. La segunda marca es $4$ (no $5$, aunque $5$ aparezca dos veces).

## Idea (un pase)

Mantén dos variables:

- `m1`: el máximo distinto visto.
- `m2`: el segundo máximo distinto visto.

Centinela `NEG` menor que cualquier $a_i$ (por ejemplo $-2^{60}$).

Para cada $x$:

1. Si $x > m1$: el viejo máximo baja a segundo, $x$ es el nuevo máximo.  
   `m2 = m1; m1 = x;`
2. Si $x < m1$ **y** $x > m2$: $x$ es un valor distinto del máximo y mejor que el segundo actual.  
   `m2 = x;`
3. Si $x == m1`: es **otro** del mismo máximo. No tocas `m2`. Eso es lo que ignora duplicados del mayor.

Al final, si `m2` sigue en el centinela, no hubo un segundo valor distinto → `-1`.

## Por qué no basta “el segundo del arreglo ordenado”

Si ordenas $5,5,4$ descendente y tomas `a[1]`, obtienes $5$. El enunciado quiere $4$. Tienes que **saltar iguales**.

Versión con sort, también correcta:

1. Ordena desc.
2. Busca el primer `a[i] < a[0]`.
3. Si no existe, `-1`.

Es $O(n \log n)$. El pase lineal es $O(n)$ y no usa memoria extra.

Un `set` / `std::set` de mayores también sirve: insertas todo y miras el segundo `rbegin()`. $O(n \log n)$ y más pesado.

## Invariante

Después de cada elemento, `{m1, m2}` (ignorando centinelas) son los dos mayores **distintos** del prefijo, o solo uno si el prefijo es constante. Se demuestra por casos en la actualización: o llega un nuevo máximo, o un valor estrictamente entre `m2` y `m1`, o un duplicado / algo $\le m2$.

## Complejidad

$O(n)$ tiempo, $O(1)$ memoria extra. Obligatorio pensar $O(n)$ con $n = 2 \cdot 10^5$, aunque $O(n \log n)$ también entra.

## Trampas

- Segunda posición tras sort **sin** compactar iguales.
- Inicializar `m1 = m2 = 0` (falla si todo es negativo: el segundo real puede ser $< 0$ y confundes centinela con un valor).
- Actualizar `m2` cuando $x == m1$.
- $n = 1$: no hay segundo → `-1`.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    const long long NEG = -(1LL << 60);
    long long m1 = NEG, m2 = NEG;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        if (x > m1) {
            m2 = m1;
            m1 = x;
        } else if (x < m1 && x > m2) {
            m2 = x;
        }
    }
    if (m2 == NEG) cout << -1 << "\n";
    else cout << m2 << "\n";
}
```
