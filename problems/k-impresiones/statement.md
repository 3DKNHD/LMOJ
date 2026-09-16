# Las copias

Hay que sacar $k$ copias del reglamento y hay $n$ impresoras independientes. La $i$-ésima es constante como un metrónomo: produce **una** copia exactamente en los segundos $t_i$, $2t_i$, $3t_i$, … y en ningún otro instante. En el segundo $0$ no ha salido nada.

Las impresoras trabajan a la vez. En un segundo $T$, el total de copias listas es, para cada impresora, cuántos múltiplos de $t_i$ hay que no superan $T$, y eso sumado.

¿Cuál es el menor tiempo $T$ en el que ya hay **al menos** $k$ copias? $k$ y los $t_i$ pueden ser grandes.

## Entrada

La primera línea contiene $n$ y $k$ ($1 \le n \le 2 \cdot 10^5$, $1 \le k \le 10^9$).

La segunda línea contiene $n$ enteros $t_i$ ($1 \le t_i \le 10^9$).

## Salida

Un único entero: el mínimo $T$.
