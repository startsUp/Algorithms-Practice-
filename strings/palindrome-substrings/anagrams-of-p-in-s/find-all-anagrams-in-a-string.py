import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window with ord sum 
        ans = []
        pLen = len(p)
        cMap = Counter(p)
        mCount = 0
        start, end = 0, pLen - 1
        if (end > pLen):
            return []
        
        #compute the initial match count
        
        
        while(end < len(s)):
            if(start == 0):
                for i in range(pLen):
                    if (s[i] in cMap):
                        cMap[s[i]]-=1
                        if(cMap[s[i]] >= 0):
                            mCount+=1
            else:
                if(s[end] in cMap):
                    cMap[s[end]]-=1
                    if (cMap[s[end]] >= 0):
                        mCount+=1
            
            if(mCount == pLen):
                ans.append(start)
                
            if (s[start] in cMap):
                if (cMap[s[start]] >= 0):
                    mCount-=1
                cMap[s[start]]+=1
                
            start+=1
            end+=1
                
                
                
        return ans