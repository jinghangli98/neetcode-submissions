class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s)-1

        while l<r:
            if s[l] != s[r]:
                newL = s[l+1:r+1]
                newR = s[l:r]
                return newL==newL[::-1] or newR==newR[::-1]

            l += 1
            r -= 1
        return True