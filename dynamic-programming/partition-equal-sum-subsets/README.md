# Question [Medium]


# Solution 
Refer [this](https://leetcode.com/problems/partition-equal-subset-sum/discuss/462699/Whiteboard-Editorial.-All-Approaches-explained) detailed write up.
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If two parition have equal sums that means the sum(nums) should be even (return False if sum(nums) / 2 % 2 != 0)
        # therefore if we need to find a subset that adds to sum(nums) / 2 we return True 
        # recursive:
        # helper(target, nums, i=0, sums=0):
        #   if (target == sums):
        #       return True
        #   else if (target < sum):
        #       return False
        #   else:
        #       return helper(target, nums, i+1, sum) or helper(target, nums, i+1, sum+nums[i])
        # 
        # Can be classified as a knapsack problem since an element can be in the first parition or not
        # dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]] where i is the number of elements to achieve sum j
    
        # total = sum(nums)
        # if total % 2 != 0:
        #     return False
        # target = int(total/2)
        # dp = [False for i in range(target+1)]
        # dp[0] = True
        # for i in range(1,len(nums)+1):
        #     for j in range(target, 0, -1):
        #         if (j - nums[i-1] >= 0):
        #             dp[j] = dp[j - nums[i-1]] or dp[j]
        # return dp[-1]
        total = 0
        for n in nums:
            total+= n
        if total%2 != 0:
            return False
        target = int(total/2)
        nums.sort(reverse=True)
        return self.helper(0, target, nums)
    def helper(self, i, sum, nums):
        
        if(i >= len(nums)):
            return False
        elif (sum == nums[i]):
            return True
        elif (sum < nums[i]):
            return False
        else:
            return self.helper(i+1, sum-nums[i], nums) or self.helper(i+1, sum, nums)
```