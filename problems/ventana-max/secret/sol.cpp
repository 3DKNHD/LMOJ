#include <bits/stdc++.h>
using namespace std;

vector<long long> maximos_ventana(const vector<long long>& a, int k) {
    deque<int> dq;
    vector<long long> respuesta;

    for (int i = 0; i < (int)a.size(); ++i) {
        while (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }
        while (!dq.empty() && a[dq.back()] <= a[i]) {
            dq.pop_back();
        }
        dq.push_back(i);
        if (i >= k - 1) {
            respuesta.push_back(a[dq.front()]);
        }
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

    int n, k;
    cin >> n >> k;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    imprimir(maximos_ventana(a, k));
    return 0;
}
