class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_prod = [1] * len(nums)
        postfix_prod = [1] * len(nums)

        running_prefix = 1
        running_postfix = 1
        for i in range(len(nums)):
            j = -i-1
            prefix_prod[i] = running_prefix
            running_prefix *= nums[i]

            postfix_prod[j] = running_postfix
            running_postfix *= nums[j]
        
        return [pre*post for pre, post in zip(prefix_prod, postfix_prod)]