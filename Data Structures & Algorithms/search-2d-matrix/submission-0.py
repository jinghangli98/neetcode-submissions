class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l = 0
        r = r*c-1
        while l <= r:
            mid = l + (r-l)//2
            mid_r = mid // c
            mid_c = mid % c

            if target < matrix[mid_r][mid_c]:
                # search left
                r = mid -1
            elif target > matrix[mid_r][mid_c]:
                # search right
                l = mid + 1
            elif target == matrix[mid_r][mid_c]:
                return True
        
        return False

        