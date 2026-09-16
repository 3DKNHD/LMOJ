# La medida común

El archivo de la biblioteca es una estantería de $n$ tomos. El tomo $i$ tiene $a_i$ páginas (siempre al menos una).

La bibliotecaria hace $q$ preguntas. En cada una elige un tramo continuo de tomos, del $L$ al $R$ inclusive, y quiere el **mayor** número de páginas que divide a **todos** los tomos de ese tramo. En otras palabras, el máximo común divisor de $a_L, \dots, a_R$.

Los tomos no se mueven entre preguntas.

## Entrada

La primera línea contiene $n$ y $q$ ($1 \le n,q \le 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($1 \le a_i \le 10^9$).

Siguen $q$ líneas con $L$ $R$ ($1 \le L \le R \le n$).

## Salida

$q$ líneas, cada una con el gcd del rango pedido.
