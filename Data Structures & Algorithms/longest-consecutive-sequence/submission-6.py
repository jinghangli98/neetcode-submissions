class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        ans = 0
        
        for num in nums:
            sequence_length = 0
            if num-1 not in nums_set:
                #num is the starting number
                while num in nums_set:
                    num += 1
                    sequence_length += 1
                ans = max(ans, sequence_length)
        
        return ans

