class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        maxlength = 0
        
        for num in nums:
            length = 0
            if num - 1 not in numset:
                #start of a sequence
                length += 1
                while num + 1 in numset:
                    num += 1
                    length += 1
                     
                maxlength = max(maxlength, length)
        
        return maxlength

                


            
