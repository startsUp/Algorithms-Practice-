def lengthOfLIS(self, nums) -> int:
    ## naive solution O(n^2)
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