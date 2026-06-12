class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = []
        max_length = 0
        count_table = {}
        maxf = 0
        for r in range(len(s)):
            if s[r] in count_table:
                count_table[s[r]] += 1
            else:
                count_table[s[r]] = 1

            maxf = max(maxf, count_table[s[r]])
            if (r-l+1) - maxf > k:
                
                count_table[s[l]] -= 1
                l += 1
        
        return r-l + 1



            

            