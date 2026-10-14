C. Postorder Traversal
time limit per test
1 second
memory limit per test
256 megabytes

You are given the root of a binary tree.

Return the postorder traversal of the tree.

In postorder traversal, nodes are visited in the following order:

    Traverse the left subtree
    Traverse the right subtree
    Visit the current node 

If the tree is empty, return an empty list.

You are required to implement only the function:


vector<int> postorderTraversal(TreeNode* root);

Do not modify any other part of the given code.

Here's the Template Code: C++ Java JS Python
Input

The input format and tree construction are handled by the provided template.
Output

The output format is also handled by the template. You only need to implement the required function correctly.
Examples
Input
Copy

7
1 2 null 3 null 4 null

Output
Copy

4 3 2 1

Input
Copy

7
1 2 3 4 5 6 7

Output
Copy

4 5 2 6 7 3 1
