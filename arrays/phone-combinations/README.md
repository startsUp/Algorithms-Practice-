## Question [Medium]

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
```
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

## Solution
Basic idea is to build the array bottom up. Starting from the last digit we duplicate the current array `n` (current array size) number of times, and prepend all characters corresponding to the digit.

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        x = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return
        ans = ['']
        for n in range(len(digits)-1, -1, -1):
            i = digits[n]
            curLen = len(ans)
            ans = ans*len(x[i])
            for j in range(len(x[i])):
                for k in range(curLen):
                    ans[curLen*j+k] =  x[i][j] + ans[curLen*j+k]
        return ans
```
