# Climb Stairs Backtracking - Quick Revision

## Main variables

- `currPos`: current stair reached.
- `n`: target stair.
- `path` (`vector<int>`): one current sequence of jumps, such as `{1, 2}`.
- `ans` (`vector<vector<int>>`): all completed paths, such as `{{1,1,1}, {1,2}, {2,1}}`.
- `&` passes `path` and `ans` by reference, so the function changes the original vectors.

Key invariant: `currPos` equals the sum of all jumps in `path`.

## Why `&` is used

Without `&`, a function receives a separate copy. Changes to that copy do not update the vector in `main`.

```cpp
vector<vector<int>>& ans  // use the original ans
vector<int>& path         // use the same path while backtracking
```

Therefore, `ans.push_back(path)` saves results in the original `ans`. References also avoid repeatedly copying the vectors. `currPos` and `n` are small integers, so passing them normally is fine.

## Base cases

```cpp
if (currPos > n) return;           // overshot the target
if (currPos == n) {
    ans.push_back(path);           // save a copy of the valid path
    return;
}
```

## Choose, explore, undo

```cpp
path.push_back(1);                 // record jump 1
f(currPos + 1, n, path, ans);      // move 1 stair and explore
path.pop_back();                   // undo the choice
```

`push_back(1)` changes only `path`, so `currPos + 1` is needed to update the position. For jump `2`, push `2` and call with `currPos + 2`.

This pattern is called **backtracking**:

```
make a choice -> explore it -> undo the choice
```

Trying `1` before `2` produces paths in lexicographical order.

## Printing all paths

```cpp
for (const auto& currAns : ans) {  // take one complete path
    for (int x : currAns) {        // take one jump from that path
        cout << x << " ";
    }
    cout << '\n';                  // next path goes on a new line
}
```

For `ans = {{1,1,1}, {1,2}, {2,1}}`, the output is:

```
1 1 1
1 2
2 1
