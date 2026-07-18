class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        table = {}
        most_frequent = 0
        l = 0
        longest = 0

        for r in range(len(s)):

            if s[r] not in table:
                table[s[r]] = 1
                most_frequent = max(most_frequent, table[s[r]])
            else:
                table[s[r]] += 1
                most_frequent = max(most_frequent, table[s[r]])
            
            if r -l + 1 - most_frequent > k:
                
                table[s[l]] -= 1
                l += 1
            else:
                longest = max(longest, r-l+1)
        
        return longest

