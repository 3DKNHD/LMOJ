# Editorial: ¿Forman triángulo?

## Qué pide

Para cada tripleta $a,b,c > 0$, si pueden ser lados de un **triángulo no degenerado**. Salida `SI` o `NO` (sin tilde, mayúsculas).

## Idea

La desigualdad del triángulo, **estricta** en los tres pares:

$$
a+b > c,\quad a+c > b,\quad b+c > a
$$

Si alguna es $\ge$ en vez de $>$ estás permitiendo área $0$ (degenerado: los tres puntos alineados). El enunciado lo prohíbe.

## Por qué las tres

Si asumes $a \le b \le c$, basta $a+b > c$ (las otras dos se cumplen solas porque $c$ ya es el mayor). Eso es correcto **después de ordenar**. Si no ordenas, tienes que escribir las tres: un caso $1, 100, 1$ falla $1+1 > 100$ pero $1+100 > 1$ sí pasa.

Ordenar y chequear solo la mayor es una solución alternativa igual de válida.

## 64 bits en la suma

$a,b,c \le 10^9$, entonces $a+b \le 2 \cdot 10^9$, que **justo no cabe** en `int` con signo ($2^{31}-1 \approx 2.14 \cdot 10^9$… en realidad $2 \cdot 10^9$ **sí cabe** en `int` de 32 bits). $10^9+10^9 = 2 \cdot 10^9 < 2^{31}-1$, así que `int` no explota **en este límite**.

Aun así el oficial usa `long long` porque:

- Es el hábito correcto cuando sumas cotas de $10^9$.
- Si el límite subiera a $2 \cdot 10^9$, `int` sí muere.

Lee `long long` y compara `a + b > c` en 64 bits. No hay desbordamiento.

## Degenerados que el juez va a meter

- $1,1,2$: $1+1 \not> 2$ → `NO` (es un segmento).
- $5,5,5$: equilátero → `SI`.
- $3,4,5$: pitagórico, área $> 0$ → `SI`.

## Complejidad

$O(T)$ con $T \le 10^5$.

## Otras soluciones

Fórmula de Herón y exigir área $> 0$: inestable con enteros grandes si usas `double`. No lo hagas. La desigualdad es exacta.

## Trampas

- Imprimir `Sí` / `si` / `YES`. El juez quiere `SI` y `NO`.
- Usar `>=` (acepta degenerados).
- Chequear una sola desigualdad sin ordenar.

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
        long long a, b, c;
        cin >> a >> b >> c;
        bool ok = a + b > c && a + c > b && b + c > a;
        cout << (ok ? "SI" : "NO") << "\n";
    }
}
```
