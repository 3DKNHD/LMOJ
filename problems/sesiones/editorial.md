# Editorial: Un solo aula

## Qué hay que hacer

Tienes un aula y un montón de talleres con hora de inicio y fin. Quieres meter **la mayor cantidad** posible sin que se pisen. Si uno termina en el minuto $t$ y otro empieza en $t$, chocan (el aula no se clona).

## La idea greedy (voraz: siempre eliges lo que parece mejor, y aquí sí funciona)

Ordena los talleres por **quién termina antes**. Vas tomando el que termina más pronto, siempre que empiece **después** de que se liberó el aula.

¿Por qué funciona? El que termina antes deja el aula libre cuanto antes, así entra más gente después. Si en vez de ese tomas uno que termina tarde, estás ocupando el aula sin necesidad.

## Paso a paso

1. Guarda cada taller como `(fin, inicio)`.
2. Ordena de menor a mayor por `fin`.
3. `last = un número muy pequeño` (el aula está libre desde siempre).
4. Por cada taller en ese orden: si `inicio > last`, lo tomas, `ans++`, `last = fin`.
5. Imprime `ans`.

El `>` (no `>=`) es porque si `inicio == last` chocan.

## Ejemplo

Talleres $[1,3], [2,5], [4,7], [6,8]$.

Orden por fin: $[1,3], [2,5], [4,7], [6,8]$.

- Tomo $[1,3]$, last$=3$.
- $[2,5]$ empieza $2$, no es $>3$.
- $[4,7]$ empieza $4>3$: tomo, last$=7$.
- $[6,8]$ $6>7$? no.

Respuesta: $2$.

## Si te da WA

Ordenaste por inicio. O usaste `>=` y metiste dos que se tocan en $t$.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Intervalo {
    int inicio;
    int fin;
};

int maximo_sin_solape(vector<Intervalo> intervalos) {
    sort(intervalos.begin(), intervalos.end(), [](const Intervalo& a, const Intervalo& b) {
        return a.fin < b.fin;
    });

    int tomados = 0;
    long long ultimo_fin = -(1LL << 60);
    for (const auto& it : intervalos) {
        if (it.inicio > ultimo_fin) {
            ++tomados;
            ultimo_fin = it.fin;
        }
    }
    return tomados;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Intervalo> intervalos(n);
    for (int i = 0; i < n; ++i) {
        cin >> intervalos[i].inicio >> intervalos[i].fin;
    }

    cout << maximo_sin_solape(intervalos) << "\n";
    return 0;
}
```
