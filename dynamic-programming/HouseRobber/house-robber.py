class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        prev1 = 0
        prev2 = 0
        for n in nums:
            t = prev1
            prev1 = max(prev2 + n, prev1)
            prev2 = t
        return prev1