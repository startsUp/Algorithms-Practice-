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