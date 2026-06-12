class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l = 0
        min_diff = float('inf')
        for r in range(len(nums)):

            if r - l + 1 == k:
                min_diff = min(min_diff, nums[r] - nums[l])
                l += 1

        
        return min_diff


