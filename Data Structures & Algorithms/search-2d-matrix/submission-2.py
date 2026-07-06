class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        array = [num for row in matrix for num in row]

        l = 0 
        r = len(array) - 1
        while l <= r:
            mid = l + (r - l)//2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                r = mid - 1
            elif array[mid] < target:
                l = mid + 1
        
        return False