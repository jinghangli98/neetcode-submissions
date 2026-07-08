class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count_table = {}
        l = 0
        max_length = 0
        for idx in range(len(s)):
            if s[idx] in count_table:
                count_table[s[idx]] += 1
            else:
                count_table[s[idx]] = 1
            
            while (idx-l + 1) - max(count_table.values()) > k:
                count_table[s[l]] -= 1
                l += 1

            max_length = max(max_length, (idx-l+1))
        
        
        return max_length