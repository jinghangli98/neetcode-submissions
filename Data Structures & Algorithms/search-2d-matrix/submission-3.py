class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix = [num for row in matrix for num in row]

        l = 0
        r = len(matrix) - 1
        
        while l <= r:
            mid = l + (r-l)//2
            if target == matrix[mid]:
                return True
            elif target > matrix[mid]:
                l = mid + 1
            elif target < matrix[mid]:
                r = mid - 1
        
        return False

