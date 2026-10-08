#include <bits/stdc++.h>

using namespace std;


int main() {
    int T;
    cin >> T;

    while (T--) {
        string s;
        cin >> s;

        stack < char > st;
        bool ok = true;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                st.push(s[i]);
            } else {
                if (st.empty()) {
                    ok = false;
                    break;
                }

                if ((s[i] == ')' && st.top() == '(') ||
                    (s[i] == ']' && st.top() == '[') ||
                    (s[i] == '}' && st.top() == '{')) {
                    st.pop();
                } else {
                    ok = false;
                    break;
                }
            }
        }

        if (!st.empty()) ok = false;

        if (ok)
            cout << "Yes\n";
        else
            cout << "No\n";
    }

    return 0;
}


