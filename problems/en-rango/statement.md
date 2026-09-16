# En el presupuesto

La cooperativa escolar compra lotes para la feria. Cada lote tiene un precio $a_i$ (a veces negativo: son devoluciones o créditos). El presupuesto de esta semana es un intervalo cerrado $[L, R]$: sirve cualquier lote cuyo precio caiga **dentro**, incluidos los extremos.

Hay $n$ lotes sobre la mesa. ¿Cuántos se pueden comprar con ese presupuesto?

## Entrada

La primera línea contiene tres enteros $n$, $L$ y $R$ ($1 \le n \le 2 \cdot 10^5$, $-10^9 \le L \le R \le 10^9$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Un único entero: cuántos $a_i$ cumplen $L \le a_i \le R$.
