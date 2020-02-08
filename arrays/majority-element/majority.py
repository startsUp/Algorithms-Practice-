def majorityElement(nums):
    # boyer moore voting algorithm
    # [ 3, 1, 3, 5, 3, 3]
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

print('Expected -> 7')
print('Actual -> ' + str(majorityElement([7, 7, 5, 7, 5, 1, 5, 7 , 5, 5, 7, 7 , 7, 7, 7, 7])))
