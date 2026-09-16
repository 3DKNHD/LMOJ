# Cables del lab

El laboratorio tiene $n$ computadoras, numeradas $1..n$, y $m$ cables. Cada cable une dos máquinas y se puede usar en los dos sentidos. La instalación es un desastre: puede haber un cable de una máquina a sí misma, o varios cables entre el mismo par. Eso no cambia lo esencial.

Dos máquinas «se hablan» si existe una cadena de cables (posiblemente vacía) que las conecta. En particular, cada PC se habla consigo misma, aunque no tenga ningún cable.

El técnico hace $q$ preguntas: dadas $u$ y $v$, ¿están en la misma red? Contesta `SI` o `NO` (mayúsculas, sin tilde).

## Entrada

La primera línea contiene $n$, $m$ y $q$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m,q \le 2 \cdot 10^5$).

Siguen $m$ líneas con $u$ $v$ ($1 \le u,v \le n$).

Siguen $q$ líneas con $u$ $v$ ($1 \le u,v \le n$).

## Salida

$q$ líneas: `SI` o `NO`.
