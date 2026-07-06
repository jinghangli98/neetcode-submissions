class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        def bsearch(array):
            l = 0 
            r = len(array) - 1
            while l <= r:
                mid = (l+r)//2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return -1
        
        left_half = nums[:pivot]
        right_half = nums[pivot:]

        left_ans = bsearch(left_half)
        right_ans = bsearch(right_half)

        if left_ans == -1 and right_ans == -1:
            return -1
        elif left_ans != -1:
            return left_ans
        elif right_ans != -1:
            return right_ans + pivot