class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix = [num for row in matrix for num in row]

        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                l = mid + 1
            elif matrix[mid] > target:
                r = mid - 1
        return False