class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []

        for idx, num in enumerate(nums):
            
            pre_prod = 1
            for prenum in nums[:idx]:
                pre_prod *= prenum
            
            post_prod = 1
            for postnum in nums[idx+1:]:
                post_prod *= postnum
            
            ans.append(pre_prod * post_prod)
        
        return ans
            
