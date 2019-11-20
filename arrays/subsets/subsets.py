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