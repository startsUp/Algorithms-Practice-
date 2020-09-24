from collections import deque
def maxInDiskSpaceMins(diskSpaces, k):
  minIndex, minSpace = 0, diskSpace[0]
  largest = min(diskSpaces[:k])
  dq = deque()
  # keep track of smallest nums in sliding window
  for i in range(numComputer):
      if dq and dq[0] < i-k+1: # if min is the first element in the sliding window
          dq.popleft()
      while dq and diskSpaces[dq[-1]] > diskSpaces[i]:
          dq.pop() # ensure invariant, minima = dq[0] always
      dq.append(i)
      if i >= k-1: # don't check of largest while going thru the first segment
          largest = max(largest, diskSpaces[dq[0]])
  return largest
