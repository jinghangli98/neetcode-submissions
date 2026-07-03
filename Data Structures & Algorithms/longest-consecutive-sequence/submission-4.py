class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)

        
        max_length = 0
        for num in nums:
            if num-1 not in numset:
                #we are at the start of the sequence
                length = 1
                while num + 1 in numset:
                    length += 1
                    num += 1
                    
                max_length = max(length, max_length)
        
        return max_length
                    