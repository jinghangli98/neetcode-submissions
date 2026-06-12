class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        ans = []
        current_max = 0
        for r in range(len(nums)):
            if r - l + 1 == k:
                max_num = max(nums[l:r+1])
                ans.append(max_num)
                l += 1
        return ans

