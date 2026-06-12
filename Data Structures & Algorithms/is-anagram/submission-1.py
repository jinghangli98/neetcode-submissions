class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lut_s = {}
        lut_t = {}
        for string in s:
            if string in lut_s:
                lut_s[string] += 1
            else:
                lut_s[string] = 1
        
        for string in t:
            if string in lut_t:
                lut_t[string] += 1
            else:
                lut_t[string] = 1
        
        return lut_s == lut_t
        