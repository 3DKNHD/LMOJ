# Editorial: Hora pico

## Qué hay que hacer

Cada persona está en la fila desde el minuto $L$ hasta el $R$ inclusive. Quieres el minuto con **más gente a la vez**.

## No simules persona por persona

$M$ llega a $10^6$ y $n$ a $2\cdot 10^5$. Si por cada persona recorres $L..R$ sumando $1$ en un arreglo, puedes llegar a $n\cdot M$ y no entra en tiempo.

## Arreglo de diferencia (entradas y salidas)

Piensa un arreglo `d[1..M]`. Cuando alguien **entra** en $L$, $d[L] += 1$. Cuando **se va después de $R$**, en el minuto $R+1$ hay uno menos: $d[R+1] -= 1$.

Después caminas los minutos $1..M$ llevando $cur$ = gente ahora:

```
cur += d[i]
ans = max(ans, cur)
```

`cur` es la suma de todos los $+1$ y $-1$ hasta $i$: o sea, cuántos intervalos cubren el minuto $i$.

## Ejemplo

$M=5$, intervalos $[1,3]$ y $[3,5]$.

- `d[1]+=1`, `d[4]-=1`
- `d[3]+=1`, `d[6]-=1`

Minutos: $1$ → cur $1$; $2$ → $1$; $3$ → $2$; $4$ → $1$; $5$ → $1$. Máximo $2$ (el minuto $3$).

## Si te da WA

Pusiste `-1` en $R$ en vez de $R+1$ y el último minuto no cuenta. O el arreglo no llega a $M+1$.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

int cobertura_maxima(int limite, const vector<pair<int, int>>& rangos) {
    vector<int> delta(limite + 2, 0);
    for (auto [izq, der] : rangos) {
        delta[izq] += 1;
        delta[der + 1] -= 1;
    }

    int actual = 0;
    int mejor = 0;
    for (int i = 1; i <= limite; ++i) {
        actual += delta[i];
        mejor = max(mejor, actual);
    }
    return mejor;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, limite;
    cin >> n >> limite;
    vector<pair<int, int>> rangos(n);
    for (int i = 0; i < n; ++i) {
        cin >> rangos[i].first >> rangos[i].second;
    }

    cout << cobertura_maxima(limite, rangos) << "\n";
    return 0;
}
```
