# Editorial: El tramo del viaje

## Qué hay que hacer

Números $\ge 0$. Quieres el intervalo **contiguo más largo** cuya suma sea $\le S$. Si ni un elemento entra, $0$.

## Dos punteros (la ventana que se mueve)

Como todo es $\ge 0$, si un tramo $L..R$ ya se pasó de $S$, agrandar $R$ lo empeora. Hay que mover $L$ hacia la derecha.

1. `L=0`, `sum=0`, `ans=0`.
2. `R` recorre $0..n-1$: sumas `a[R]`.
3. Mientras `sum > S` y `L <= R`: restas `a[L]`, `L++`.
4. Ahora $L..R$ es el tramo más largo que termina en $R$ y entra. `ans = max(ans, R-L+1)`.

Cada índice entra y sale de la ventana **una vez**. Lineal.

## Ejemplo

$a=[1,2,3,4]$, $S=5$

- $R=0$ sum $1$ largo $1$
- $R=1$ sum $3$ largo $2$
- $R=2$ sum $6>5$ → saco $1$, sum $5$, largo $2$
- $R=3$ sum $9>5$ → saco hasta que entre, queda $[4]$ largo $1$

Respuesta $2$.

## Si te da TLE

Probar todos los $L,R$.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

int ventana_mas_larga(const vector<long long>& a, long long tope) {
    int mejor = 0;
    int izq = 0;
    long long suma = 0;

    for (int der = 0; der < (int)a.size(); ++der) {
        suma += a[der];
        while (izq <= der && suma > tope) {
            suma -= a[izq];
            ++izq;
        }
        mejor = max(mejor, der - izq + 1);
    }
    return mejor;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long tope;
    cin >> n >> tope;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << ventana_mas_larga(a, tope) << "\n";
    return 0;
}
```
