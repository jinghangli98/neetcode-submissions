class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        l = 0
        string = []
        for r in range(len(s)):

            while string and s[r] in string:
                l += 1
                string.pop(0)

            string.append(s[r])
            longest = max(longest, len(string))
        
        return longest
            
