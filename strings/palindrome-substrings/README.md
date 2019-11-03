## Question [Medium]
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

### Example 1:
```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

### Example 2:
```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```


## Solution

Let N be the length of the string. The middle of the palindrome could be in one of 2N - 1 positions: either at letter or between two letters.

For each center, let's count all the palindromes that have this center. Notice that if [a, b] is a palindromic interval (meaning S[a], S[a+1], ..., S[b] is a palindrome), then [a+1, b-1] is one too. 


```
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        c = 0
        for i in range(len(s)):
            c1 = countSubstrings(s, i, i) 
            c2 = countSubstrings(s, i, i + 1)
            c = c + c1 + c2
        return c

def countSubstrings(s, left, right):
    l, r = left, right
    c = 0
    while(l >= 0 and r < len(s) and s[l] == s[r]):
        c+=1
        l-=1
        r+=1
    return c
```
