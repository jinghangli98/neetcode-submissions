class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        res = []
        max_length = 0
        for r in range(len(s)):

            if max_length < len(res):
                max_length = len(res)

            while s[r] in res:
                res.pop(0)
                l += 1
            
            res.append(s[r])
        
        return max(max_length, len(res))


