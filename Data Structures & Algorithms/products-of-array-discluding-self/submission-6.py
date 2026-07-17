class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        preprod = [1] * len(nums)
        postprod = [1] * len(nums)

        prerunning = 1
        postrunning = 1

        for i in range(len(nums)):
            j = -i - 1
            preprod[i] = prerunning
            prerunning *= nums[i]

            postprod[j] = postrunning
            postrunning *= nums[j]
        
        return [pre*post for pre, post in zip (preprod, postprod)]
            