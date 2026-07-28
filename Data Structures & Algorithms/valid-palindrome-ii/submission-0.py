class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) -1
        limit = 0 
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            
            elif s[l] != s[r] and limit <= 1:
                l += 1
                limit += 1
            
            else:
                return False
        
        return True