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