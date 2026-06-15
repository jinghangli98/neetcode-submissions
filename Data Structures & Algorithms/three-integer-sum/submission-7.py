class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        ans = []
        for idx, num in enumerate(nums):
            
            if idx > 0 and num == nums[idx-1]:
                continue

            l = idx + 1
            r = len(nums) - 1
            target = 0 - num
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] == target:
                    sub_ans = [num, nums[l], nums[r]]             
                    ans.append(sub_ans)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return ans