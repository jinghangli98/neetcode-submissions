class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        for idx, num in enumerate(nums[:-1]):
            if num > nums[idx+1]:
                return nums[idx+1]
            
        return nums[0]

        


        