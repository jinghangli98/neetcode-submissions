class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        table_s = {}
        for c in s:
            if c in table_s:
                table_s[c] += 1
            else:
                table_s[c] = 1
        
        table_t = {}
        for c in t:
            if c in table_t:
                table_t[c] += 1
            else:
                table_t[c] = 1
        
        return table_t == table_s