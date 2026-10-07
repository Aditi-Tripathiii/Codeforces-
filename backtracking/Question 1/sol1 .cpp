#include <bits/stdc++.h>
using namespace std;

// Corrected syntax while keeping the same recursive logic.
vector<vector<int>> f(int n) {
    if (n == 0) {
        return {{}}; // fixed base case initialization syntax
    }
    if (n < 0) {
        return {}; // fixed empty return syntax
    }

    auto small_ans1 = f(n - 1);
    auto small_ans2 = f(n - 2);

    vector<vector<int>> small_ans;

    for (int i = 0; i < small_ans1.size(); i++) {
        small_ans1[i].push_back(1); // fixed vector push_back syntax
        small_ans.push_back(small_ans1[i]);
    }

    for (int i = 0; i < small_ans2.size(); i++) {
        small_ans2[i].push_back(2); // fixed vector push_back syntax
        small_ans.push_back(small_ans2[i]);
    }

    return small_ans; // corrected return statement
}

int main() {
    int n;
    cin >> n;

    auto result = f(n);
    for (auto path : result) {
        for (int i = 0; i < path.size(); i++) {
            cout << path[i] << " ";
        }
        cout << endl;
    }

    return 0 ;
}
