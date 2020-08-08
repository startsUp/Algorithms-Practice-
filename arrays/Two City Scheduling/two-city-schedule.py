class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffOrder = sorted(costs, key = lambda x: x[0]-x[1])
            
        half = len(costs) // 2
        mincost = 0
        for i in range(len(diffOrder)):
            if i < half:
                mincost += diffOrder[i][0]
            else:
                mincost += diffOrder[i][1]
        
        return mincost
        