## Question [Medium]
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

## Solution
Intuition: We know right and bottom are higher numbers, so if we DFS in either direction and backtrack if we encounter a element less than the target, we will eventually find the element or not.

### My solution
```python
def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        bT = False
        while (i < m and j < n and i >= 0 and j >= 0):
            if (matrix[i][j] == target): return True # if found return
            if (matrix[i][j] < target): 
                # if backtracking and we find an element < target, or on last row, go right
                if (bT or i == m - 1): j+=1 
                else: i+=1 # go bottom
            else: i-=1; bT=True 
            # if current element is greater than target, we gotta backtrack to explore right elements 
            
        return False
```


### Alternate Solution `O(m+n)`