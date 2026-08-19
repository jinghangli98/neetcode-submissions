class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        self.max_area = 0
        

        def dfs(r, c):
            grid[r][c] = 0
            self.curr_area += 1
            self.max_area = max(self.max_area, self.curr_area)
            directions = [[0,1], [1,0], [-1,0], [0,-1]]

            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if nr in range(row) and nc in range(col) and grid[nr][nc] == 1:
                    dfs(nr, nc)
            
            return self.max_area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    self.curr_area = 0
                    dfs(r, c)
        
        return self.max_area
        