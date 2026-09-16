# Editorial: El libro que se corrige

## Qué hay que hacer

El arreglo **cambia**. Operación $1$: suma $x$ a la posición $i$ (no reemplaza el valor; le suma $x$). Operación $2$: imprime la suma de $a_L + \cdots + a_R$.

Si guardas sumas de prefijo y luego cambia una casilla, tendrías que recalcular todo lo que está a su derecha. Eso es demasiado lento.

## Fenwick (árbol binario indexado)

Usa un arreglo extra `t[1..n]`. Cada índice $i$ guarda la suma de un bloque que **termina** en $i`. El largo de ese bloque es $i\ \&\ -i$ (en bits: el $1$ más a la derecha de $i$). No hace falta entender esa fórmula para usar las dos funciones:

**Sumar $v$ en $i$:**

```
for (; i <= n; i += i & -i) t[i] += v;
```

**Suma $1..i$:**

```
for (; i > 0; i -= i & -i) r += t[i];
```

Suma $L..R$ = $pref(R) - pref(L-1)$.

Índices desde **$1$**. Si pones $0$, el $i += i & -i$ se queda en $0$ para siempre: loop infinito.

Al principio, por cada $a_i$ haces $add(i, a_i)$. Un update del enunciado es **sumar** $x$, no reemplazar.

Todo en `long long`.

## Si te da WA / TLE

Tratar tipo $1$ como “poner $a_i = x$”. Sumar $L..R$ uno por uno. `int`.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<long long> t;

    Fenwick(int tam) : n(tam), t(tam + 1, 0) {}

    void agregar(int i, long long v) {
        for (; i <= n; i += i & -i) {
            t[i] += v;
        }
    }

    long long prefijo(int i) {
        long long s = 0;
        for (; i > 0; i -= i & -i) {
            s += t[i];
        }
        return s;
    }

    long long rango(int izq, int der) {
        return prefijo(der) - prefijo(izq - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, consultas;
    cin >> n >> consultas;
    Fenwick fw(n);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        fw.agregar(i, x);
    }

    while (consultas--) {
        int tipo;
        cin >> tipo;
        if (tipo == 1) {
            int i;
            long long x;
            cin >> i >> x;
            fw.agregar(i, x);
        } else {
            int izq, der;
            cin >> izq >> der;
            cout << fw.rango(izq, der) << "\n";
        }
    }
    return 0;
}
```
