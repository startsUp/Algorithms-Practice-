class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # keep going right if coming from left and the curr is 
        #   /
        #  /
        # / 
        #      / 
        #     /
        # the array if plotted will look something like above
        # hence, if we do a binary tree search our mid has the chance of being in the right or left sub array
        # if on the left: nums[left] <= nums[mid]
        #   then we check if target is greater than mid or less than left, then it has to be right subarray
        #   else its in the left
        # else: we are in the right        
        l,r= 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1