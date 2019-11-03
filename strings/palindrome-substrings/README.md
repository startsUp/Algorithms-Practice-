## Question 
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

Expand around center for each character. There will be two centers for each character. 


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
