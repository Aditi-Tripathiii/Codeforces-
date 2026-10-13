C. Print All Paths I
time limit per test
1 second
memory limit per test
256 megabytes

You are given a grid of size N×M. You start at cell (1,1) and want to reach cell (N,M).

You can move only:

    Right (R) → move to (i,j+1)
    Down (D) → move to (i+1,j) 

Your task is to print all possible paths from (1,1) to (N,M).

Each path should be represented as a string consisting of characters:

    R for right move
    D for down move 

Input

A single line containing two integers N and M (1≤N,M≤10).

If N = M , N != 1.
Output

Print all valid paths from (1,1) to (N,M), one per line. Paths can be printed in any order.
Examples
Input
Copy

2 2

Output
Copy

RD
DR

Input
Copy

3 4

Output
Copy

RRRDD
RRDRD
RRDDR
RDRRD
RDRDR
RDDRR
DRRRD
DRRDR
DRDRR
DDRRR

