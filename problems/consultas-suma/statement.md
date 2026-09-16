# El libro de caja

La cooperativa anota el día en $n$ renglones, en orden cronológico. El renglón $i$ tiene un entero $a_i$: positivo si entró plata, negativo si salió (devolución, pago a un proveedor, etc.).

El tesorero no pide siempre el total del día. Viene con $q$ preguntas del estilo: «mira solo del renglón $L$ al $R$ inclusive, ¿cuál es el saldo de ese tramo?»

Los renglones no cambian entre pregunta y pregunta. Puede haber muchas consultas. Cada respuesta es un solo entero, que puede ser negativo o muy grande.

## Entrada

La primera línea contiene $n$ y $q$ ($1 \le n,q \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

Siguen $q$ líneas con $L$ $R$ ($1 \le L \le R \le n$).

## Salida

$q$ líneas, cada una con $a_L + \cdots + a_R$.
