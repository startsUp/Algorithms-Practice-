### 14. Longest Common Prefix [Easy] 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"

```

## Solution

### Sort Solution 
Sort the array. Make the first element the maxPrefix and reduce the maxPrefix if there a prefix mismatch down the array.

```python
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        strs.sort()
        maxPrefix = strs[0] # assign it to the first string in sorted array, and reduce if prefix don't match
        
        def checkIfPrefixMatch(prefix, word):
            if (len(word) < len(prefix)):
                return False
            else:
                return word[:len(prefix)] == prefix
    
        for i in range(1,len(strs)):
            if (not checkIfPrefixMatch(maxPrefix, strs[i])):
                n = min(len(maxPrefix), len(strs[i]))

                tempPrefix = ''
                j = 0
                while j < n:
                    if maxPrefix[j] == strs[i][j]:
                        tempPrefix+=maxPrefix[j]
                    else:
                        break
                    j+=1
                
                if j == 0:
                    return ''
                else:
                    maxPrefix=tempPrefix
        return maxPrefix
```



### Binary Search Solution

The idea is to apply binary search method to find the string with maximum value L, which is common prefix of all of the strings. The algorithm searches space is the interval (0 \ldots minLen)(0…minLen), where minLen is minimum string length and the maximum possible common prefix. Each time search space is divided in two equal parts, one of them is discarded, because it is sure that it doesn't contain the solution. There are two possible cases:

S[1...mid] is not a common string. This means that for each j > i S[1..j] is not a common string and we discard the second half of the search space.
S[1...mid] is common string. This means that for for each i < j S[1..i] is a common string and we discard the first half of the search space, because we try to find longer common prefix.
```python
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0)
        return "";
    int minLen = Integer.MAX_VALUE;
    for (String str : strs)
        minLen = Math.min(minLen, str.length());
    int low = 1;
    int high = minLen;
    while (low <= high) {
        int middle = (low + high) / 2;
        if (isCommonPrefix(strs, middle))
            low = middle + 1;
        else
            high = middle - 1;
    }
    return strs[0].substring(0, (low + high) / 2);
}

private boolean isCommonPrefix(String[] strs, int len){
    String str1 = strs[0].substring(0,len);
    for (int i = 1; i < strs.length; i++)
        if (!strs[i].startsWith(str1))
            return false;
    return true;
}
```