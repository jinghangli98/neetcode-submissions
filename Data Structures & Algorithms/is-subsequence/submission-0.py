class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ls = 0
        lr = 0
        while ls < len(s) and lr < len(t):
            if s[ls] == t[lr]:
                ls += 1
            lr += 1
        
        if ls == len(s):
            return True
        else:
            return False