from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        q = deque()
        # to skip duplicates sort and only check numbers greater than the current number
        candidates.sort() 
        ans = []
        
        # populate all valid (< target) candidates
        for i in range(len(candidates)):
            if(i < target):
                q.append([candidates[i] , [candidates[i]], i]) # will need index, sum and path (could calculate sum everytime using path but space tradeoff is minimal so store it)
                
        #bfs
        while q:
            v = q.popleft()
            i = v[2]
            if(v[0] == target):
                ans.append(v[1])
            while(i<len(candidates)):
                n = candidates[i]
                newS = v[0] + n
                if(newS == target): # combination found
                    ans.append(v[1] + [n])
                    break
                if(newS > target): # sum (combination) > target
                    break
                q.append([newS, v[1] + [n], i]) # add current path to queue
                i+=1
        return ans