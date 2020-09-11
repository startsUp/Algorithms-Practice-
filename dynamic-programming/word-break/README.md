## Word Break [Medium]

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```
```
Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

```
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

## Solution (Recursive) - Exceeds Time Limit

```
class Solution:
    def isSegmentable(self, s, i, wordDict):
        cur = ''
        while(i<len(s)):
            cur+=s[i]
            if (cur in wordDict):
                if (i == len(s) - 1): # last segment found
                    return True
                seg = self.isSegmentable(s, i+1, wordDict)
                if (seg):
                    return True
            i+=1
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # could make word dict
        return self.isSegmentable(s, 0, wordDict)
```
## Solution (Recursive) - With Dynamic Programming

```
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
```
