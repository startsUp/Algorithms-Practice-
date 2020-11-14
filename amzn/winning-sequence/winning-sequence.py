def sequence(n, upperBound, lowerBound):
    nums = (upperBound - lowerBound) * 2 + 1
    if nums < n:
        return [-1]
    ans = []
    for i in range(min(upperBound - lowerBound + 1, n - 1)):
        ans.append(upperBound - i)
    for i in range(n - len(ans)):
        ans.insert(0, upperBound - i - 1)
    return ans


print(sequence(5, 10, 3), "should be [9,10,9,8,7]")
print(sequence(5, 10, 8), "should be [8, 9, 10, 9, 8]")
print(sequence(5, 9, 10), "should be [-1]")
print(sequence(4, 6, 3), "should be [5, 6, 5, 4]")
print(sequence(10, 30,20), "should be [29, 30, 29, 28, 27, 26, 25, 24, 23, 22]")
print(sequence(3, 8, 7), "should be [7, 8, 7]")
print(sequence(10, 10,3), "should be [8, 9, 10, 9, 8, 7, 6, 5, 4, 3]")