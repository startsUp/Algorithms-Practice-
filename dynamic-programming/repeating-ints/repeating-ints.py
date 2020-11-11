def repeat(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2, 2]

    F = [1, 2, 2]

    for i in range(3, n+1):
        F += [i] * F[i-1]
        # 0 - 1
        # 1 - 2
        # 2 - 2
        # 3 - 3
        # 4 - 3
        # 5 - 3
        # 6 - 4
        # 7 - 4
        # 8 - 4

    print(F, len(F))
    return F[n]
# F[n] =  F / [i] 
# F[n] = F(n - i)
# F = []
# find the repeating num
# 1, 2, 2, 3, 3
print(repeat(20))