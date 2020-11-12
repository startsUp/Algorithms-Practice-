def getPrimes(n):
    isPrime = [True for i in range(n+1)]
    isPrime[0] = False
    isPrime[1] = False
    p = 2
    while (p * p <= n):
        if (isPrime[p]):
            for i in range(p*p, n+1, p):
                isPrime[i] = False
        p += 1
    return isPrime

def count_string_primes(s):
    isPrime = getPrimes(1000000)
    dp = [-1 for i in range(len(s) + 1)]
    dp[0] = 1 # base case => if reached, means that the split is valid
    mod = 1000000007
    def findAllPrimes(num, i):
        if dp[i] != -1: # index has already been counted
            return dp[i]
        cnt = 0    
        
        # starting from cur index i, test all possible 6 digit primes
        for j in range(1, 7):
            if (i - j >= 0 and num[i-j]!= '0' and isPrime[int(num[i-j:i])]):
                cnt+= findAllPrimes(num, i - j)
                cnt %= mod          

        # memoize the result
        dp[i] = cnt 
        return cnt
    return findAllPrimes(s, len(s)) 

print(count_string_primes('3175'))
assert(count_string_primes('11373') == 6)