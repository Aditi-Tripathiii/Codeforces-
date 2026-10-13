#include <bits/stdc++.h>

using namespace std;

void f(int row_idx, int col_idx, int n, int m, string  & path,  vector < string > & ans) {
    if (row_idx > n || col_idx > m) {
        return;
    }
    else if (row_idx == n and col_idx == m) {
        ans.push_back(path);
        return;
    }

    path.push_back('R');
    f(row_idx, col_idx + 1, n, m, path, ans);
    path.pop_back();


    path.push_back('D');
    f(row_idx + 1, col_idx, n, m, path, ans);
    path.pop_back();



}


int main() {
    int n, m;
    cin >> n >> m;
    vector < string> ans;
    string path;
    f(1, 1, n, m, path, ans);
    for (auto currAns: ans) {
        for (char x: currAns) {
            cout << x ;
        }
        cout << endl;
    }
}