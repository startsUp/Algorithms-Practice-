## Question [Medium]
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

### Example:

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Solution
For every element, append the index and the path to the queue. For every element that comes after the dequeued element append the path. 

```python
from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        q = deque()
        for i in range(len(nums)):
            q.append([i, [nums[i]]])
            ans.append([nums[i]])
            while q:
                v = q.popleft()
                j = v[0] + 1
                while j < len(nums):
                    path = v[1] + [nums[j]]
                    ans.append(path)
                    q.append([j, path])
                    j+=1
            
            
        return ans
```
