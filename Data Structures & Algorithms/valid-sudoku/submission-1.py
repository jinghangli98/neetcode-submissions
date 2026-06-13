class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def has_dup(nums):
            seen = set()
            for num in nums:
                if num == ".":
                    continue
                if num in seen:
                    return True
                seen.add(num)
            return False
        
        for r in range(len(board)):
            row = board[r]
            if has_dup(row):
                return False
            
        for c in range(9):
            col = [row[c] for row in board]
            if has_dup(col):
                return False

        
        for r in range(0, 3):
            for c in range(0, 3):
                mat = [row[c*3:(c+1)*3] for row in board[r*3:(r+1)*3]]
                mat = [num for r in mat for num in r]
                if has_dup(mat):
                    return False
        
        return True
