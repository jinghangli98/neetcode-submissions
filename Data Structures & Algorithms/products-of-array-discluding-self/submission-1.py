class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_array = [0] * len(nums)
        r_array = [0] * len(nums)

        l_prod = 1
        r_prod = 1
        for i in range(len(nums)):
            j = -i -1
            l_array[i] = l_prod
            r_array[j] = r_prod

            l_prod *= nums[i]
            r_prod *= nums[j]
        
        return [l_array[i]*r_array[i] for i in range(len(l_array))] 