class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:
                #left is sorted
                if nums[l] <= target and target < nums[mid]:
                    #target within left side
                    r = mid -1
                else:
                    #target within right side
                    l = mid + 1

            else:
                #right is sorted
                if nums[mid] < target and target <= nums[r]:
                    #target within left side
                    l = mid + 1
                else:
                    #target within right side
                    r = mid - 1

        return -1


