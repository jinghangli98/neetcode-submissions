class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target < nums[mid]:
                # search left half
                r = mid - 1
            elif target > nums[mid]:
                # search right half
                l = mid + 1
            elif target == nums[mid]:
                return mid
        
        return -1