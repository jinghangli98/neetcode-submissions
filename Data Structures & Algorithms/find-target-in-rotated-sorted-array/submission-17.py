class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bsearch(array, target):
            l = 0
            r = len(array) -1

            while l <=r:
                mid = (l+r)//2
                if array[mid] == target:
                    return mid
                elif array[mid] < target:
                    l = mid + 1
                elif array[mid] > target:
                    r = mid - 1
            
            return -1
        
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
        
        pivot = l
        lhalf = nums[0:pivot]
        rhalf = nums[pivot:]

        if bsearch(lhalf, target) != -1:
            return bsearch(lhalf, target)
        elif bsearch(rhalf, target) != -1:
            return pivot +  bsearch(rhalf, target)
        else:
            return -1

 