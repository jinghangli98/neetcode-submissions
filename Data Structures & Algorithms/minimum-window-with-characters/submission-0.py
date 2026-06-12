class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_table = {}
        for c in t:
            if c  in t_table:
                t_table[c] += 1
            else:
                t_table[c] = 1

        l = 0
        s_table = {}
        min_length = float('inf')
        smallest_string = None

        for r in range(len(s)):
            
            if s[r]  in s_table:
                s_table[s[r]] += 1
            else:
                s_table[s[r]] = 1
            
            is_valid = True
            for k, v in t_table.items():
                if s_table.get(k, 0) < v:
                    is_valid = False
                    break
            
            while is_valid:
                valid_string = s[l:r+1]

                if len(valid_string) < min_length:
                    min_length = len(valid_string)
                    smallest_string = valid_string

                s_table[s[l]] -= 1
                l += 1

                for k, v in t_table.items():
                    if s_table.get(k, 0) < v:
                        is_valid = False
                        break
                
        if smallest_string:
            return smallest_string
        else:
            return ""
            







