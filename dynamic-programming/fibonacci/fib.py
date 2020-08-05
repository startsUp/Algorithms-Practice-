def fib(n):
    # fib(n) = fib(n-1) + fib(n-2)
    a = 0
    b = 1
    if n == 0:
        return a
    for i in range(2, n+1):
        # print(i)
        c = b
        b = a + b
        a = c
    return b
print(fib(7))