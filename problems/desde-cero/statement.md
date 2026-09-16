# El reloj del aula

En el aula 12 hay un reloj digital de 24 horas. No guarda la fecha: cada $86400$ segundos (un día entero) vuelve a mostrar `00:00:00` y sigue como si nada. Lo único que ves son horas, minutos y segundos, siempre con dos dígitos.

El portero te pasa $T$ instantes medidos en segundos desde un origen cualquiera. Un instante puede ser de hace muchos días: $t$ llega a $10^{18}$. Lo que hay que imprimir no es “cuántas horas absolutas pasaron”, sino **lo que marca el reloj** en ese momento: la hora del día correspondiente.

Para cada $t$, escribe `HH:MM:SS`. Por ejemplo, $0$ es `00:00:00`, $3661$ es `01:01:01`, y $86400$ otra vez `00:00:00`.

## Entrada

La primera línea contiene un entero $T$ ($1 \le T \le 10^5$).

Siguen $T$ líneas con un entero $t$ ($0 \le t \le 10^{18}$).

## Salida

$T$ líneas con `HH:MM:SS` (siempre dos dígitos por campo).
