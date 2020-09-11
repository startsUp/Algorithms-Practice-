class Solution:
    def isSegmentable(self, s, i, wordDict, dp):
        cur = ''
        index = i
        if (dp[index] != -1):
            return True if dp[index] == 1 else False
        while(i<len(s)):
            cur+=s[i]
            if (cur in wordDict):
                if (i == len(s) - 1): # last segment found
                    dp[index] = 1
                    return True
                seg = self.isSegmentable(s, i+1, wordDict, dp)
                if (seg):
                    dp[index] = 1
                    return True
            i+=1
        dp[index] = 0
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # could make word dict
        dp = [-1 for i in s]
        return self.isSegmentable(s, 0, wordDict, dp)