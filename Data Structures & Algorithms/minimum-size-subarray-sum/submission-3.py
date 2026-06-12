class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        ans = float('inf')
        if sum(nums) < target or not nums:
            return 0

        current_sum = 0
        for r in range(len(nums)):
            current_sum += nums[r]

            while current_sum >= target:
                ans = min(ans, r-l+1)
                current_sum -= nums[l]
                l += 1
        
        return ans
                    

