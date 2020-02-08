def moveZeroes(nums):
    length=len(nums)-1
    while length>=0:
        if nums[length]==0:
            nums.pop(length)
            nums.append(0)
            length=length-1
        else:
            length=length-1

    # alt:
    # keep non zero index
    # swap once zero with non-zero idex
    