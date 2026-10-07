#include <bits/stdc++.h>

using namespace std;

// Same logic kept; only syntax and formatting cleaned.
void f(int curr_pos, int n, string path) {
    if (curr_pos > n) {
        return;
    }
    if (curr_pos == n) {
        cout << path << endl;
        return;
    }

    // 1 step move
    f(curr_pos + 1, n, path + " 1");

    // 2 step move
    f(curr_pos + 2, n, path + " 2");
}

int main() {
    int n;
    cin >> n;
    f(0, n, " ");
    return 0; // fixed return statement for main
}