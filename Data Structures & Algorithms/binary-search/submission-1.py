class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pa = 0
        pb = len(nums) - 1

        while pa <= pb:

            mid = pa + (pb - pa)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                pb = mid -1
            else:
                pa = mid + 1

        return -1