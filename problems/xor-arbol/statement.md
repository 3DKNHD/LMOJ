# El rumor en el árbol

Los $n$ pueblos del valle están unidos por $n-1$ caminos de manera que forman un árbol: hay un único sendero entre cualquier par de pueblos. Cada pueblo $i$ guarda un secreto numérico $a_i$.

Cuando un rumor viaja de $u$ a $v$, por el camino único (incluyendo $u$ y $v$), los secretos se van combinando con XOR. El valor que llega es el XOR de todos los $a$ de los pueblos del camino. Si $u = v$, el rumor ni sale: el valor es $a_u$.

Te hacen $q$ preguntas, cada una un par $(u, v)$. Imprime el XOR de ese camino.

## Entrada

La primera línea contiene $n$ y $q$ ($1 \le n, q \le 2 \cdot 10^4$).

La segunda línea contiene $n$ enteros $a_i$ ($0 \le a_i < 2^{30}$).

Siguen $n-1$ líneas con aristas $u$ $v$.

Siguen $q$ líneas con consultas $u$ $v$.

## Salida

$q$ líneas, cada una con el XOR del camino pedido.
