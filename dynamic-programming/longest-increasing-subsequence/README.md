Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

```python
# O(n^2) naive solution without optimization.
def lengthOfLIS(self, nums: List[int]) -> int:
    lis = [0 for i in range(len(nums))]
    if not nums:
        return 0
    ans = 0
    def findPrevLIS(i):
        prevLIS = 1
        j = 0
        while j < i:
            if (nums[j] < nums[i]):
                prevLIS = max(prevLIS, lis[j] + 1)
            j+=1
        return prevLIS
        
    for i in range(len(nums)):
        lis[i] = findPrevLIS(i)
        ans = max(ans, lis[i])
    return ans

```



Follow up: Could you improve it to O(n log n) time complexity?