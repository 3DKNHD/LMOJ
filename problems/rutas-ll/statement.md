# El colectivo más barato

La ciudad tiene $n$ paradas y $m$ tramos de colectivo. Cada tramo une dos paradas $u$ y $v$ y se puede viajar en los dos sentidos; el boleto de ese tramo cuesta $w$ (un entero positivo). Puede haber varias líneas entre el mismo par, y hasta un tramo que sale y vuelve a la misma parada.

Quieres ir de la parada $s$ a la parada $t$ pagando lo **mínimo** posible. El costo de un viaje es la suma de los boletos de los tramos que tomas. Si $s = t$, no te subes a nada: el costo es $0$. Si no hay forma de llegar, imprime $-1$.

Los boletos y los caminos largos pueden hacer que la suma sea enorme.

## Entrada

La primera línea contiene $n$, $m$, $s$ y $t$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$, $1 \le s,t \le n$).

Siguen $m$ líneas con $u$ $v$ $w$ ($1 \le u,v \le n$, $1 \le w \le 10^9$).

## Salida

Un único entero: el costo mínimo, o $-1$.
