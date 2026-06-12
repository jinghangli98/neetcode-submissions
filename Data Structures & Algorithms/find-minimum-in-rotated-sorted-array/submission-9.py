class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # for idx, num in enumerate(nums):
        #     if num < nums[idx-1]:
        #         return num
        #     elif num == nums[idx-1]:
        #         return num



        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = l + (r-l)//2

            if nums[mid] < nums[r]:
                # right half is sorted, search the left half including the mid
                r = mid
            elif nums[mid] > nums[r]:
                # there's a break in the right half, search right half. because mid is already greater than right most; exlude mid
                l = mid + 1
            elif l == r:
                return nums[mid]
            
