# Editorial: Ocurrencias del patrón

## Qué pide

Cuántas veces $P$ aparece en $T$, **con overlaps**. `|P|+|T|\le 10^6`. `aaa` con `aa` vale $2$.

## Idea

KMP. Concatenas `s = P + "#" + T` (el `#` no aparece en el alfabeto de letras). El prefijo-función $\pi[i]$ = largo del borde propio de $s[0..i]$.

Cada vez que $\pi[i] = |P|$, hay una ocurrencia que termina en esa posición de $s$. El separador impide que el match cruce de $P$ a $T$ de forma espuria.

Overlaps: KMP no “salta” el patrón entero a ciegas; $\pi$ puede ser $|P|-1$ y contar otra ocurrencia ya en el siguiente carácter (`aa` en `aaa`).

## Alternativa

KMP clásico: construyes $\pi$ solo de $P$ y recorres $T$ con un puntero $j$. Cuentas cuando $j==|P|$ y haces $j=\pi[j-1]$. Equivalente.

`std::string::find` en bucle desde `pos+1` también cuenta overlaps y es $O(|P||T|)$ worst-case: TLE en peores casos.

## Complejidad

$O(|P|+|T|)$.

## Trampas

- Contar sin overlaps (`pos += |P|`).
- Olvidar el separador y que $P$ sea sufijo de un prefijo raro.
- `int` vs tamaño `size_t` en índices. El contador cabe en `int` ($10^6$).

## Código de referencia (C++)

```cpp
string s = p + "#" + t;
// pi estándar
if (j == m) ++ans;
```
