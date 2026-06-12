class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        ans = float('inf')
        if sum(nums) < target or not nums:
            return 0

        
        for r in range(len(nums)):
            sub_array = nums[l:r+1]
            current_sum = sum(sub_array)

            while current_sum >= target:
                ans = min(ans, r-l+1)
                current_sum -= nums[l]
                l += 1
        
        return ans
                    

