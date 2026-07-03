class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isvalid(array):
            table = {}
            for item in array:
                if item == ".":
                    continue
                elif item in table:
                    return False
                else:
                    table[item] = 1
            return True

        for row in board:
            if not isvalid(row):
                return False
        
        for j in range(len(board[0])):
            col = [row[j] for row in board]
            if not isvalid(col):
                return False

        
        for i in range(3):
            for j in range(3):
                sub_board = [num for row in board[i*3:(i+1)*3] for num in row[j*3:(j+1)*3]]
                if not isvalid(sub_board):
                    return False
        
        return True
                    
        


