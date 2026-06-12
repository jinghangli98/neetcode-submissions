class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_table = {}
        t_table = {}

        for l in s:
            if l in s_table:
                s_table[l] += 1
            else:
                s_table[l] = 1
        
        for l in t:
            if l in t_table:
                t_table[l] += 1
            else:
                t_table[l] = 1

        return s_table == t_table