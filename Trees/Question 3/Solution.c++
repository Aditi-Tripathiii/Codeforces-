#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode * left, * right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

TreeNode * buildTree(const vector < string > & nodes) {
    if (nodes.empty() || nodes[0] == "null") return nullptr;

    TreeNode * root = new TreeNode(stoi(nodes[0]));
    queue < TreeNode * > q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < nodes.size()) {
        TreeNode * cur = q.front();
        q.pop();

        if (nodes[i] != "null") {
            cur -> left = new TreeNode(stoi(nodes[i]));
            q.push(cur -> left);
        }
        i++;

        if (i < nodes.size() && nodes[i] != "null") {
            cur -> right = new TreeNode(stoi(nodes[i]));
            q.push(cur -> right);
        }
        i++;
    }
    return root;
}

// ================= STUDENT FUNCTION =================
vector < int > postorderTraversal(TreeNode * root) {

    vector < int > ans;
    if (root == NULL) {
        return ans;
    }



    vector < int > left = postorderTraversal(root -> left);
    ans.insert(ans.end(), left.begin(), left.end());



    vector < int > right = postorderTraversal(root -> right);
    ans.insert(ans.end(), right.begin(), right.end());

    ans.push_back(root -> val);

    return ans;

}
// ====================================================

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector < string > nodes(n);
    for (int i = 0; i < n; i++) cin >> nodes[i];

    TreeNode * root = buildTree(nodes);

    vector < int > result = postorderTraversal(root);

    for (int i = 0; i < result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << '\n';
}