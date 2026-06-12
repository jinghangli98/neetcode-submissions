class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        frequency_counter = {}
        ans = 0
        for r in range(len(s)):
            if s[r] not in frequency_counter:
                frequency_counter[s[r]] = 1
            else:
                frequency_counter[s[r]] += 1
            
            while (r-l+1) - max(frequency_counter.values()) > k:
                
                frequency_counter[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans







            

            