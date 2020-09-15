## Maximal square [Medium]
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

## Solution
 - Keep track of area by seeing if the current element forms a sqaure with its preceeding neighbours `left, above, top-left diagonal`
  ```
  1 1
  1 (1) # -> this one can be written as 2 as it forms a 2 sided square
  ```
 - If a bigger square is encountered all of its neighbours `l,a,d` will have the same value

```
1 1 1
1 2 2
1 2 (3) # -> example
```
Runtime: `O(m x n)`
> Note: Here we use 2D space as we are keeping track of areas in 2d array.

# TODO: ADD 1D DP Solution