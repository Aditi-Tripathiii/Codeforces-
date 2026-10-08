#include <bits/stdc++.h>

using namespace std;

void f(int currPos, int n, vector < int > & path, vector < vector < int >> & ans) {
    if (currPos > n) {
        return;
    }
    else if (currPos == n) {
        ans.push_back(path);
        return;
    }

    path.push_back(1);
    f(currPos + 1, n, path, ans);
    path.pop_back();

    path.push_back(2);
    f(currPos + 2, n, path, ans);
    path.pop_back();

}
int main() {
    int n;
    cin >> n;
    vector<vector<int>> ans;
    vector<int>path;
    f(0, n, path, ans);
    for (auto currAns: ans) {
        for (int x: currAns) {
            cout << x << " ";
        }
        cout << endl;
    }
}