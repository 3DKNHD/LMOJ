#include <bits/stdc++.h>
using namespace std;

string formatear_hora(long long segundos) {
    segundos %= 86400;
    int h = (int)(segundos / 3600);
    int m = (int)((segundos % 3600) / 60);
    int s = (int)(segundos % 60);

    ostringstream out;
    out << setfill('0') << setw(2) << h << ":"
        << setw(2) << m << ":"
        << setw(2) << s;
    return out.str();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int casos;
    cin >> casos;
    while (casos--) {
        long long segundos;
        cin >> segundos;
        cout << formatear_hora(segundos) << "\n";
    }
    return 0;
}
