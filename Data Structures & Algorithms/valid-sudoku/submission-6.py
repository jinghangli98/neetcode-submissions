class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isvalid(array):
            table = {}

            for c in array:
                if c == "." :
                    continue
                elif c in table:
                    return False
                elif c not in table:
                    table[c] = 1

            return True

        
        for row in board:
            if not isvalid(row):
                return False
        
        for j in range(len(board[0])):
            col = [row[j] for row in board]
            if not isvalid(col):
                return False
        
        
        for i in range(0, 3):
            for j in range(0, 3):
                sub_row = board[i*3:(i+1)*3]
                sub_board = [val for row in sub_row for val in row[j*3:(j+1)*3]]

                if not isvalid(sub_board):
                    return False
        
        return True

                    

                








