class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        t_table = {}
        s_table = {}

        for c in t:
            t_table[c] = 1 + t_table.get(c, 0)
        
        l = 0
        have = 0 
        need = len(t_table)
        ans = [-1, -1]
        min_length = float('inf')

        for r in range(len(s)):
            c = s[r]
            s_table[c] = 1 + s_table.get(c, 0)

            if c in t_table and s_table[c] == t_table[c]:
                have += 1
            
            while have == need:
                
                if r-l+1 < min_length:
                    min_length = r-l+1
                    ans = [l, r]
                
                left_char = s[l]
                s_table[left_char] -= 1
                if left_char in t_table and s_table[left_char] < t_table[left_char]:
                    have -= 1
                l += 1
        
        return s[ans[0]:ans[1]+1]





