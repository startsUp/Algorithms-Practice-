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