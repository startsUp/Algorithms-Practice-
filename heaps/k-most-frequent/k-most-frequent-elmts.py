from heapq import *
def kMostFrequent(nums, k):
    heap = []
    countMap = {}
    for n in nums:
        c = str(n)
        if c in countMap:
            countMap[c] += 1
        else:
            countMap[c] = 1
    print(countMap)
    for key in countMap:
        print(countMap[key], key, heap)
        if(len(heap) < k):
            heappush(heap, (countMap[key], int(key)))
        elif countMap[key] > heap[0][0]:
            heapreplace(heap, (countMap[key], int(key)))
    return [item[1] for item in heap]