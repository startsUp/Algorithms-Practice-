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