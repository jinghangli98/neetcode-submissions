class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        running = 1
        for i in range(len(nums)):
            prefix[i] = running
            running = running * nums[i]
        
        postfix = [1] * len(nums)
        running = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = running
            running = running * nums[i]
        
        ans = []
        for i in range(len(prefix)):
            ans.append(prefix[i]*postfix[i])
        
        return ans
