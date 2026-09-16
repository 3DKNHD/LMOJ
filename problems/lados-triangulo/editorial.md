# Editorial: Tres varillas

## Qué hay que hacer

Tres palos arman un triángulo de verdad (con área, no una línea) si **cada lado es más corto que la suma de los otros dos**. Las tres a la vez:

$$
a+b > c,\quad a+c > b,\quad b+c > a
$$

Ojo: es $>$ estricto. Si $a+b=c$ los tres palos quedan en una línea: área $0$. El problema dice $NO$.

## Paso a paso

1. Lee $T$.
2. $T$ veces: lees $a,b,c$. Si las tres desigualdades se cumplen, imprimes $SI$. Si no, `NO`.
3. Exactamente esas letras, mayúsculas, sin tilde. No `Si`, no `YES`.

## Ejemplo

- $3,4,5$: $3+4>5$, $3+5>4$, $4+5>3$ → $SI$
- $1,2,3$: $1+2=3$, no es $>$ → $NO$
- $1,100,1$: $1+1>100$ es falso → $NO$

## La trampa de la suma

$a$ y $b$ llegan a $10^9$, entonces $a+b$ llega a $2\cdot 10^9$. En `int` de 32 bits **justo entra**, pero no arriesgues: lee `long long`. No cuesta nada.

## Atajo

Si ordenas para que $a\le b\le c$, alcanza con comprobar $a+b>c$. Las otras dos se cumplen solas. El oficial no ordena y escribe las tres. Las dos valen.

## Si te da WA

- Imprimiste `YES` / `Sí`.
- Usaste $\ge$ y aceptaste triángulos planitos.
- Solo comprobaste dos desigualdades.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

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
    return 0;
}
```
