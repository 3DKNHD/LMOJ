# Dos bandos

En el campamento hay $n$ chicos y $m$ «no me banco» bidireccionales: si $u$ no se banca a $v$, tampoco al revés. Puede haber gente sin enemigos.

Quieren partirlos en **dos equipos** (rojo y azul) para un juego. La regla es simple: dos enemigos **no** pueden quedar en el mismo equipo. Un chico sin enemigos puede ir a cualquiera. Si el grafo de enemistades tiene varias piezas sueltas, cada pieza tiene que poder pintarse por separado.

¿Es posible? Un triángulo de enemigos, por ejemplo, lo impide. Contesta `SI` o `NO`.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Siguen $m$ líneas con $u$ $v$ ($1 \le u,v \le n$).

## Salida

Una línea: `SI` o `NO`.
