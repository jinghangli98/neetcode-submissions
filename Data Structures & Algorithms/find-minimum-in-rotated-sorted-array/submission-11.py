class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                #ans is in the right of the l
                l = mid + 1
            else:
                r = mid

        return nums[l]            
