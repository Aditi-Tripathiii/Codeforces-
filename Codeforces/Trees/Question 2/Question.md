B. Inorder Traversal
time limit per test
1 second
memory limit per test
256 megabytes

You are given the root of a binary tree.

Return the inorder traversal of the tree.

In inorder traversal, nodes are visited in the following order:

    Traverse the left subtree
    Visit the current node
    Traverse the right subtree 

If the tree is empty, return an empty list.

You are required to implement only the function:


vector<int> inorderTraversal(TreeNode* root);

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

4 2 5 1 6 3 7

Note

In the first Example:

The tree is:


      1
     /
    2
   /
  3
 /
4

In inorder traversal:

    Traverse left subtree → 4 → 3 → 2
    Visit root → 1
    No right subtree 

