# Editorial: El mayor

## Qué pide

$\max(a_1,\dots,a_n)$. Un entero.

## Idea

Un único recorrido. Guardas el mejor visto hasta ahora. Al empezar, inicializa con el **primer** elemento (o con un centinela menor que cualquier $a_i$).

## Por qué no usar `0` de inicialización

Si pones `ans = 0` y todos los $a_i$ son negativos, el máximo real es negativo y tú imprimes $0$: WA.

Opciones correctas:

1. Leer el primero: `ans = a[0]`, luego comparar el resto.
2. Centinela: `ans = -1e18` (cualquier cota estrictamente menor que $-10^9$).
3. `*max_element(a.begin(), a.end())` después de leer.

## Por qué un pase es suficiente

El máximo de un conjunto es el único elemento $\ge$ todos los demás. Si en el índice $i$ ves un valor mayor que `ans`, ese pasa a ser el candidato. Al terminar, ningún elemento quedó sin comparar, así que `ans` es el máximo global.

No hace falta ordenar ($O(n \log n)$ también da AC aquí, pero es más lento y no es la idea).

## Empates

Si el máximo aparece varias veces, cualquiera de esas copias es un máximo válido: el enunciado pide el **valor**, no la posición. Da igual cuál copies.

## Complejidad

$O(n)$ tiempo, $O(1)$ extra si no guardas el arreglo. $n \le 2 \cdot 10^5$ entra holgado.

## Trampas

- Inicializar en $0$.
- Empezar el `for` en $i=0$ **y** haber puesto `ans = a[0]`, comparando `a[0]` de nuevo: no está mal, solo es redundante.

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long ans;
    cin >> ans;
    for (int i = 1; i < n; ++i) {
        long long x;
        cin >> x;
        if (x > ans) ans = x;
    }
    cout << ans << "\n";
}
```
