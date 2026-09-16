# Editorial: El código X

## Qué hay que hacer

XOR compara cada bit: si los dos bits son distintos, el resultado es $1$; si son iguales, $0$.
Dos reglas útiles: $x \oplus x = 0$ y $x \oplus 0 = x$.
También: si $p \oplus y = X$, entonces $y = p \oplus X$.

Hay que contar cuántos trozos **contiguos** del arreglo tienen XOR igual a $X$.

## Prefijo XOR

Define $p_0 = 0$ y $p_i = a_1 \oplus a_2 \oplus \cdots \oplus a_i$.

El XOR del intervalo $L..R$ es $p_R \oplus p_{L-1}$, porque los elementos anteriores a $L$ se cancelan ($x \oplus x = 0$).

Se busca $p_R \oplus p_{L-1} = X$, que es lo mismo que $p_{L-1} = p_R \oplus X$.

Recorre el arreglo de izquierda a derecha y mantén el prefijo actual $p$. Un mapa guarda cuántas veces apareció cada prefijo. Antes de anotar el $p$ actual, pregunta al mapa cuántas veces ya viste el valor $p \oplus X$. Cada una corresponde a un $L$ válido que termina en esta posición. Después suma $1$ a la cuenta de $p$.

Empieza el mapa con `{0: 1}`: el prefijo vacío, para intervalos que empiezan en $1$.

## Si te da TLE

$O(n^2)$ calculando XOR de cada par $L,R$.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

long long contar_subxor(const vector<int>& a, int objetivo) {
    unordered_map<int, int> freq;
    freq.reserve((int)a.size() * 2);
    freq[0] = 1;

    int prefijo = 0;
    long long respuesta = 0;
    for (int x : a) {
        prefijo ^= x;
        auto it = freq.find(prefijo ^ objetivo);
        if (it != freq.end()) {
            respuesta += it->second;
        }
        freq[prefijo]++;
    }
    return respuesta;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, objetivo;
    cin >> n >> objetivo;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << contar_subxor(a, objetivo) << "\n";
    return 0;
}
```
