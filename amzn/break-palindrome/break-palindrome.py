class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
         
        # only need to look at the first half since its a palindrome
        for i in range(len(palindrome)//2):
            # if char can be changed to 'a', we break since that is most optimal
                if palindrome[i]!='a':
                    return palindrome[:i]+'a'+palindrome[i+1:]
        
        # corner case - all 'a' replace last element with b
        
        return palindrome[:-1]+'b' if len(palindrome)>1 else ""
       