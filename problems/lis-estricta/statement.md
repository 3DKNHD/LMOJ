# La colección creciente

Tienes $n$ figuritas en una fila, cada una con un número $a_i$ (puede repetirse, puede ser negativo). Quieres quedarte con una **colección** lo más larga posible, sacando figuritas de la fila **sin reordenar las que dejas**: si te quedas con las posiciones $i_1 < i_2 < \cdots < i_k$, tiene que cumplirse $a_{i_1} < a_{i_2} < \cdots < a_{i_k}$ (estrictamente creciente).

No hace falta que las posiciones sean consecutivas: puedes saltar figuritas. Empates no sirven: dos iguales no forman subida.

Imprime la mayor $k$ posible. Si la fila tiene un solo número, la respuesta es $1$.

## Entrada

La primera línea contiene $n$ ($1 \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Un único entero: la longitud de la colección más larga.
