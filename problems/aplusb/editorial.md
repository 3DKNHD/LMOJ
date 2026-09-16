# Editorial: Las dos facturas

## Qué hay que hacer

Te dan muchas parejas de números. En cada pareja hay que sumar los dos e imprimir el resultado en su propia línea.

No hay algoritmo escondido. Hay que cuidar dos cosas: **leer la entrada rápido** y **usar enteros de 64 bits**.

## Cómo se resuelve, paso por paso

1. Lee un número $T$. Eso es cuántas ventas hay.
2. Repite $T$ veces:
   - Lee dos números $A$ y $B$.
   - Calcula $A+B$.
   - Imprime ese número y un salto de línea.
3. No guardes las $T$ sumas en un arreglo. Imprime en el momento y listo.

## Un ejemplo a mano

Entrada:

```
3
2 3
-1 1
1000000000000000000 1000000000000000000
```

- $2+3=5$
- $-1+1=0$
- $10^{18}+10^{18}=2\cdot 10^{18}$

Salida:

```
5
0
2000000000000000000
```

## Enteros grandes (`long long`)

En C++ el tipo `int` llega como máximo a unos $2\cdot 10^9$. $A$ y $B$ pueden ser $10^{18}$. Su suma puede ser $2\cdot 10^{18}$. Eso **no cabe** en `int`. C++ no avisa: guarda un valor incorrecto y el juez da WA.

El tipo `long long` llega hasta unos $9\cdot 10^{18}$. Úsalo cuando el enunciado hable de $10^{18}$.

En Python los enteros crecen solos. Ahí el problema es otro: imprimir lento.

## Por qué te puede dar TLE

Hasta $10^5$ líneas. Si cada lectura es lenta, se te acaba el segundo. En C++ pon esto **una vez**, al arrancar:

```cpp
ios::sync_with_stdio(false);
cin.tie(nullptr);
```

Eso le dice a C++ que no se sincronice con `scanf` en cada número.

## Si te da WA

- Usaste `int` en vez de `long long`.
- Imprimiste todo pegado, sin `\n`.
- Leíste un par de más o de menos.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

long long suma(long long a, long long b) {
    return a + b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long a, b;
        cin >> a >> b;
        cout << suma(a, b) << "\n";
    }
    return 0;
}
```
