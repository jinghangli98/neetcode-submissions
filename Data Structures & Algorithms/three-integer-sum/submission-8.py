class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        ans = []
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx -1]:
                continue

            l = idx + 1
            r = len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum == 0:
                    
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                    
                elif three_sum < 0 :
                    l += 1
                elif three_sum > 0 :
                    r -= 1
        
        return ans
                