from collections import Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        t = Counter(tasks)
        heap = [[-t[i], i] for i in list(t)] # make it max heap by storing -ve count
        heapify(heap)
        ans = 0
        while True:
            i, p = 0, []
            while i <= n and heap:
                nextTask = heappop(heap)
                ans, i = ans + 1, i + 1
                nextTask[0] += 1
                if not nextTask[0] == 0:
                    p.append(nextTask)
            if not p and not heap:
                break
            if i <= n:
                ans+= (n+1) - i 
            for task in p:
                heappush(heap, task)
        return ans
        