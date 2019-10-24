## Question
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

### Example 1:
```
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
```

## Solution

```
 def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)-1
        left, right = 0, l
        stopleft = stopright = True
        while (stopleft or stopright) and left < right:
            if nums[left] > nums[left+1]: stopleft = False
            else: left += 1
            if nums[right] < nums[right-1]: stopright = False
            else: right -= 1
        if left >= right: return 0
        m, n = max(nums[left:right+1]), min(nums[left:right+1])
        stopleft = stopright = True
        while stopleft or stopright:
            if left > 0 and n < nums[left-1]: left -= 1
            else: stopleft = False
            if right < l and m > nums[right+1]: right += 1
            else: stopright = False
        return right - left + 1
        
```