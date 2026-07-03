class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        running = 1
        for i in range(len(nums)):
            prefix[i] = running
            running *= nums[i]

        postfix = [1] * len(nums)
        running = 1
        for j in range(len(nums)-1, -1, -1):
            postfix[j] = running
            running *= nums[j]
        
        return [pre*post for pre, post in zip(prefix, postfix)]