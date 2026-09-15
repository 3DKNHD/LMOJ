# Editorial: Al revés

## Qué pide

Los $n$ enteros en orden inverso, en una sola línea, separados por espacios.

## Idea

Lees el arreglo y lo escribes de atrás hacia adelante. $O(n)$ tiempo y $O(n)$ memoria.

## Por qué guardar el arreglo

Para imprimir $a_n$ primero necesitas haber leído $a_n$. Con entrada secuencial no hay otra: hay que almacenar (o usar una pila).

```text
entrada:  1 2 3 4
salida:   4 3 2 1
```

## Espacios

El formato típico que aceptan los jueces:

```cpp
for (int i = n - 1; i >= 0; --i) {
    if (i != n - 1) cout << ' ';
    cout << a[i];
}
cout << '\n';
```

Un espacio de más al final a veces pasa, a veces no. Aquí lo seguro es no dejar espacio colgante, o imprimir `a[i] << " \n"[i==0]`.

## Otras soluciones

- `reverse(a.begin(), a.end())` y luego imprimir en orden. Igual de bien.
- Recursión “imprime el resto y luego el actual” revienta el stack.
- Insertar al frente de un `vector` en cada lectura es $O(n^2)$: TLE.

## Complejidad

$O(n)$ tiempo y memoria. $2 \cdot 10^5$ enteros caben.

## Trampas

- Invertir solo a medias (`i` de $n$ a $1$ pero índices 0-based mal).
- Imprimir un número por línea (el enunciado pide **una** línea).

## Código de referencia (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = n - 1; i >= 0; --i) {
        if (i != n - 1) cout << ' ';
        cout << a[i];
    }
    cout << "\n";
}
```
