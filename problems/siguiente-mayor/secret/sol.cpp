#include <bits/stdc++.h>
using namespace std;

vector<long long> siguiente_mayor(const vector<long long>& a) {
    int n = (int)a.size();
    vector<long long> respuesta(n, -1);
    vector<int> pila;

    for (int i = n - 1; i >= 0; --i) {
        while (!pila.empty() && a[pila.back()] <= a[i]) {
            pila.pop_back();
        }
        if (!pila.empty()) {
            respuesta[i] = a[pila.back()];
        }
        pila.push_back(i);
    }
    return respuesta;
}

void imprimir(const vector<long long>& a) {
    for (int i = 0; i < (int)a.size(); ++i) {
        if (i) {
            cout << " ";
        }
        cout << a[i];
    }
    cout << "\n";
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

    imprimir(siguiente_mayor(a));
    return 0;
}
