#include <bits/stdc++.h>

using namespace std;

void printPaths(int remaining, int maxJump, vector<int>& path) {
    if (remaining == 0) {
        for (size_t i = 0; i < path.size(); ++i) {
            if (i > 0) {
                cout << ' ';
            }
            cout << path[i];
        }
        cout << '\n';
        return;
    }

    for (int jump = 1; jump <= maxJump && jump <= remaining; ++jump) {
        path.push_back(jump);
        printPaths(remaining - jump, maxJump, path);
        path.pop_back();
    }
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> path;
    printPaths(n, k, path);

    return 0;
}
