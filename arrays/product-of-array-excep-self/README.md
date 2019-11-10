## Question [Medium]
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

### Example:
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Solution
For any element ***i***, the ```output[i]``` will be product of left subarray multiplied by product of the right subarray.
Since the problem statement says division is not permitted, we use seperate loops to find the left subarray product and right subarray product for each element.

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        ans = []
        for i in range(len(nums)): # find left subarray product for each element
            ans.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1): # find right subarray product
            ans[i] *= prod
            prod *= nums[i]
            
        return ans
```

