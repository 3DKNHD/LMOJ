# ¿Misma red?

Hay $n$ computadoras y $m$ cables bidireccionales. Después, $q$ preguntas: ¿están $u$ y $v$ en la misma componente conexa?

## Entrada

La primera línea contiene $n$, $m$ y $q$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m,q \le 2 \cdot 10^5$).

Siguen $m$ líneas con $u$ $v$ ($1 \le u,v \le n$). Puede haber bucles o aristas repetidas.

Siguen $q$ líneas con $u$ $v$ ($1 \le u,v \le n$).

## Salida

$q$ líneas: `SI` o `NO`. Un nodo está en la misma red que sí mismo.
