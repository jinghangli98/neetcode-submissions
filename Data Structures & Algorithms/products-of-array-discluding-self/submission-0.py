class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i, num in enumerate(nums):
            latter = 1
            for num in nums[i+1::]:
                latter *= num
            former = 1
            for num in nums[0:i]:
                former *= num
            
            current = former * latter
            ans.append(current)
        
        return ans


