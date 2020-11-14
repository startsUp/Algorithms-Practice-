def maxPackage(items):
    # first item should be 1
    # adjacent items cannot have difference of more than 1

    n = len(items)
    count = [0 for i in range(len(items)+1)]
    for i in items:
        count[min(i, n)]+=1
    print(count)
    size = 0
    ans = 0
    for k in range(1, n+1):
        while count[k] > 0 and size < k:
            size+=1
            ans = size
            count[k] -= 1
    print(count)
    return ans

print(maxPackage([5, 2, 3, 7, 1, 2, 2]))
