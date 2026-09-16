# Editorial: La puja

## Qué hay que hacer

Te dan $n$ números. Quieres el más grande. Como buscar el más alto en una fila de personas: miras al primero, y cada vez que aparece alguien más alto, te acuerdas de ese.

## Paso a paso

1. Lee $n$.
2. Lee el primer número y lo guardas en `best`. Por ahora es el campeón.
3. Lee los $n-1$ que faltan. Si alguno es **estrictamente mayor** que $best$, `best` pasa a ser ese.
4. Imprime `best`.

## Ejemplo

Lista: $4,\ 10,\ 3,\ 10,\ -2$.

- empiezo con $4$
- $10 > 4$ → campeón $10$
- $3$ no
- $10$ empata, no cambia (el máximo sigue siendo $10$)
- $-2$ no

Respuesta: $10$.

## Detalles que importan

Los números pueden ser **negativos**. El máximo de $-5,-1,-8$ es $-1$, no $0$. No inicialices $best$ en $0$. Inicializalo con el **primer** elemento de la lista.

Usa `long long` por las dudas (llegan a $10^9$, `int` alcanza, pero no te cuesta nada).

## Si te da WA

Inicializaste el máximo en $0$ y todos los números eran negativos.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

long long maximo(const vector<long long>& a) {
    long long mejor = a[0];
    for (int i = 1; i < (int)a.size(); ++i) {
        if (a[i] > mejor) {
            mejor = a[i];
        }
    }
    return mejor;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << maximo(a) << "\n";
    return 0;
}
```
