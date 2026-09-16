# El libro que se corrige

El tesorero tiene un libro de $n$ renglones $a_1, \dots, a_n$ y va a hacer $q$ operaciones, de dos tipos:

- Corregir el renglón $i$: **sumarle** un entero $x$ (puede ser negativo: es una enmienda).
- Preguntar el saldo del tramo $L..R$: imprime $a_L + \cdots + a_R$ con los valores **actuales**.

Las correcciones quedan para las preguntas que vienen después. Hay al menos una pregunta. Una suma puede no caber en 32 bits.

## Entrada

La primera línea contiene $n$ y $q$ ($1 \le n,q \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

Siguen $q$ líneas, cada una de la forma:

- `1 i x` — suma $x$ a $a_i$ ($1 \le i \le n$, $-10^9 \le x \le 10^9$), o
- `2 L R` — pregunta el tramo ($1 \le L \le R \le n$).

Hay al menos una operación de tipo `2`.

## Salida

Una línea por cada operación de tipo `2`.
