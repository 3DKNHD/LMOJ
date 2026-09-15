# Editorial: Subsecuencia creciente

## Qué pide

Longitud de la LIS **estricta**. $n=2\cdot 10^5$: $O(n^2)$ no entra.

## Idea

Patience sorting / `lower_bound`. Mantén `d` donde `d[k]` es el **menor** valor que puede terminar una LIS creciente de longitud $k+1`.

Para cada $x$:

- `lower_bound(d, x)`: primer $\ge x$. Como quieres estricta, reemplazas esa posición (o append si $x$ es mayor que todos).
- `upper_bound` sería LIS **no decreciente** ($\le$ permitido).

`d` queda ordenado. El tamaño de `d` es la LIS.

`d` **no** es una LIS real, solo las colas. La longitud sí es correcta (clasificación clásica).

## Por qué `lower_bound` y no `upper_bound`

Estricta: $2,2$ no alarga. `lower_bound` encuentra el primer $2$ y lo pisa: longitud sigue $1$. `upper_bound` append-earía un segundo $2$: LIS no decreciente.

## Complejidad

$O(n\log n)$.

## Fenwick / segment tree

Máximo de `dp` en valores $< x$, más compresión: $O(n\log n)$, reconstruye más fácil si piden la secuencia. Aquí solo la longitud.

## Trampas

- `upper_bound` (acepta iguales).
- DP $O(n^2)$.
- Pensar que `d` es la subsecuencia (imprimir `d` como respuesta de valores estaría mal; el tamaño sí).

## Código de referencia (C++)

```cpp
vector<ll> d;
for (ll x : a) {
    auto it = lower_bound(d.begin(), d.end(), x);
    if (it == d.end()) d.push_back(x);
    else *it = x;
}
cout << d.size() << "\n";
```
