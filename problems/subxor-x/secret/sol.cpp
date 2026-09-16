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
