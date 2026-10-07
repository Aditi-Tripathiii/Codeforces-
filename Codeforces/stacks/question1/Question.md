A. Balanced Parentheses
time limit per test
1 second
memory limit per test
256 megabytes

You are given a string s consisting only of the characters ( ) [ ] { }.

A string is called balanced if:

    Every opening bracket has a corresponding closing bracket of the same type.
    Brackets are closed in the correct order. 

For each test case, determine whether s is balanced.
Input

The first line contains an integer T (1≤T≤104) — the number of test cases.

Each test case contains a single string s (1≤|s|≤105).

It is guaranteed that the sum of lengths of all strings does not exceed 2⋅105.
Output

For each test case, print Yes if the string is balanced, otherwise print No.
Example
Input
Copy

4
{([])}
()
([)]
(((

Output
Copy

Yes
Yes
No
No

