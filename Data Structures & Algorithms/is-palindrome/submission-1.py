class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [string.lower() for string in s if string.isalnum()]

        p_a = 0
        p_z = len(s) - 1

        for i in range(len(s)):
            
            if s[p_a] != s[p_z]:
                return False
            p_a += 1
            p_z -= 1
        
        return True
            
            