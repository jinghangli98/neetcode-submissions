class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        for idx, num in enumerate(nums):
            if num < nums[idx-1]:
                return num
            elif num == nums[idx-1]:
                return num