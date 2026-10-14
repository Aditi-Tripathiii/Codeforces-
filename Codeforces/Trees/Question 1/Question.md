A. Preorder Traversal
time limit per test
1 second
memory limit per test
256 megabytes

You are given the root of a binary tree.

Return the preorder traversal of the tree.

In preorder traversal, nodes are visited in the following order:

    Visit the current node
    Traverse the left subtree
    Traverse the right subtree 

If the tree is empty, return an empty list.

You are required to implement only the function:


vector<int> preorderTraversal(TreeNode* root);

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

1 2 3 4

Input
Copy

1
null

Output
Copy


Note

In the 1st Example,

The level-order representation corresponds to the following binary tree:


      1
     /
    2
   /
  3
 /
4

Preorder traversal visits nodes in the order:

    Visit root: 1
    Traverse left subtree → 2 → 3 → 4
    No right subtree exists 

In the 2nd Example,

Since there are no nodes to visit, the preorder traversal is empty.

