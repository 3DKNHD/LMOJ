# Editorial: Suma de submatriz

## Qué pide

Suma del rectángulo inclusivo $[r_1,r_2]\times[c_1,c_2]$. $n,m\le 1000$, $q\le 10^5$: no sumes $O(nm)$ por query.

## Idea

Prefijo 2D. $p_{i,j}$ = suma del rectángulo $(1,1)$–$(i,j)$:

$$
p_{i,j} = a_{i,j} + p_{i-1,j} + p_{i,j-1} - p_{i-1,j-1}
$$

(el último se restaba dos veces). Inclusión-exclusión de la query:

$$
S = p_{r_2,c_2} - p_{r_1-1,c_2} - p_{r_2,c_1-1} + p_{r_1-1,c_1-1}
$$

Dibuja el rectángulo grande y quita la franja de arriba y la de la izquierda; el rectángulo esquina se restó dos veces, hay que sumarlo.

## 64 bits

$1000^2 \cdot 10^9 = 10^{15}$. `long long` en $p$ y en la salida.

## Complejidad

Precompute $O(nm)$, cada query $O(1)$. Total $O(nm+q)$.

## Otras soluciones

Fenwick 2D: $O(\log n\log m)$ y sirve con updates. Aquí la matriz es estática.

## Trampas

- Olvidar el $+p_{r_1-1,c_1-1}$.
- 0-indexar $p$ y leer $r_1$ 1-based.
- `int` en $p$.

## Código de referencia (C++)

```cpp
p[i][j] = x + p[i-1][j] + p[i][j-1] - p[i-1][j-1];
// query:
p[r2][c2] - p[r1-1][c2] - p[r2][c1-1] + p[r1-1][c1-1]
```
