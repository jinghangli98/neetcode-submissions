class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0 
        nums_set = set(nums)
        
        for idx, num in enumerate(nums):

            if num-1 not in nums_set:
                sequence_len = 1
                #start of the sequence
                while num + 1 in nums_set:
                    sequence_len += 1
                    num = num + 1
                
                longest = max(longest, sequence_len)
        
        return longest
                


