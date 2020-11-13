from heapq import *
from collections import deque
def getTimes(numCustomers: int, arrTime, direction):
    # create two heaps?
    exitQ = deque()
    enterQ = deque()
    print(len(arrTime), len(direction))
    for indx, t in enumerate(arrTime):
      if direction[indx] == 1: #exiting
        # heappush(exitQ, (t, indx))
        exitQ.append((t, indx))
      else:
        enterQ.append((t, indx))
        # heappush(enterQ, (t, indx))
    
    times = [-1 for i in range(len(arrTime))]
    i=0
    last = (-2, 0)
    curTime = 0
    while enterQ and exitQ:
      entT, entI = enterQ[0]
      extT, extI = exitQ[0]
      entT = max(curTime, entT)
      extT = max(curTime, extT)
      if entT == extT:
        if entT - last[0] != 1 or last[1] == 1:
          
          last = (extT, 1)
          times[extI] = extT
          exitQ.popleft()

          # make person who needs to enter wait 1s
          entT+=1 
          enterQ[0] = (entT, entI)
          curTime = entT
        else: # last person enter
          last = (entT, 0)
          times[entI] = entT
          enterQ.popleft()

          # make person who needs to enter wait 1s
          extT+=1 
          # heapreplace(exitQ, (extT, extI))
          exitQ[0]=(extT, extI)
          curTime = extT
      else:
        minT = min(extT, entT)
        minI = extI if extT < entT else entI
        times[minI] = minT
        enterQ.popleft() if entT < extT else exitQ.popleft()
        last = (minT, direction[minI])
        curTime = minT + 1

    while enterQ:
      eT, eI = enterQ[0]
      eT = max(curTime, eT)
      times[eI] = eT
      enterQ.popleft()
      curTime+=1
    while exitQ:
      eT, eI = exitQ[0]
      eT = max(curTime, eT)
      times[eI] = eT
      exitQ.popleft()
      curTime+=1
    return times
  
# print(getTimes(4, [0, 0, 1, 5], [0, 1, 1, 0]))
print(getTimes(5, [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 15, 18, 18, 18, 18, 19, 21, 22, 22, 23, 24, 25, 27, 27, 28, 28, 28, 28, 29, 30, 30, 30, 31, 32, 32, 32, 33, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 42, 42, 43, 44, 45, 45, 45, 46, 46, 48, 48, 49, 49, 50, 50, 50, 50], [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0]))



"""
from collections import deque
def getTimes(numCustomers: int, arrTime: List[int], direction: List[int]) -> List[int]:
    exitQ = deque()
    enterQ = deque()
    if len(direction) != len(arrTime):
        direction.append(0)
    for indx, t in enumerate(arrTime):
      if direction[indx] == 1: #exiting
        # heappush(exitQ, (t, indx))
        exitQ.append((t, indx))
      else:
        enterQ.append((t, indx))
        # heappush(enterQ, (t, indx))
    
    times = [-1 for i in range(len(arrTime))]
    i=0
    last = (-2, 0)
    curTime = 0
    while enterQ and exitQ:
      entT, entI = enterQ[0]
      extT, extI = exitQ[0]
      entT = max(curTime, entT)
      extT = max(curTime, extT)
      if entT == extT:
        if entT - last[0] != 1 or last[1] == 1:
          
          last = (extT, 1)
          times[extI] = extT
          exitQ.popleft()

          # make person who needs to enter wait 1s
          entT+=1 
          enterQ[0] = (entT, entI)
          curTime = entT
        else: # last person enter
          last = (entT, 0)
          times[entI] = entT
          enterQ.popleft()

          # make person who needs to enter wait 1s
          extT+=1 
          # heapreplace(exitQ, (extT, extI))
          exitQ[0]=(extT, extI)
          curTime = extT
      else:
        minT = min(extT, entT)
        minI = extI if extT < entT else entI
        times[minI] = minT
        enterQ.popleft() if entT < extT else exitQ.popleft()
        last = (minT, direction[minI])
        curTime = minT + 1

    while enterQ:
      eT, eI = enterQ[0]
      eT = max(curTime, eT)
      times[eI] = eT
      enterQ.popleft()
      curTime+=1
    while exitQ:
      eT, eI = exitQ[0]
      eT = max(curTime, eT)
      times[eI] = eT
      exitQ.popleft()
      curTime+=1
    return times
  """