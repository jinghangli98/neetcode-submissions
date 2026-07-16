class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        running_prefix = 1
        running_postfix = 1
        for i in range(len(nums)):
            
            j = -i -1

            prefix[i] = running_prefix
            running_prefix *= nums[i]

            postfix[j] = running_postfix
            running_postfix *= nums[j]

        print(prefix)
        print(postfix)
        return [pre*post for pre, post in zip(prefix, postfix)]

            
