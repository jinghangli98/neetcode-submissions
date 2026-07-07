class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stack = []
        max_length = 0
        for i in range(len(s)):

            while s[i] in stack:

                stack.pop(0)
            
            stack.append(s[i])

            max_length = max(max_length, len(stack))
        
        return max_length
