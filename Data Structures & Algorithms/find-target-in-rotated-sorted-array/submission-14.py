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

        #0 <-> pivot-1; pivot <-> len(nums)-1
        def bsearch(l, r):
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            
            return -1
        
        l_result = bsearch(0, pivot - 1)
        if l_result == -1:
            r_result = bsearch(pivot, len(nums) - 1)
            if r_result == -1:
                return -1
            else:
                return r_result
        else:
            return l_result
                


        
