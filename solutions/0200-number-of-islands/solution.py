class Solution:
    def isInBounds(self, row, col):
        return 0 <= row < self.maxRow and 0 <= col < self.maxCol

    def dfsAndMark(self, grid, row, col):
        # dfs
        grid[row][col] = "X"
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for d in deltas:
            new_row, new_col = row + d[0], col + d[1]
            if self.isInBounds(new_row, new_col) and grid[new_row][new_col] == "1":
                self.dfsAndMark(grid, new_row, new_col)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # rows
        if m == 0:
            return 0
        n = len(grid[0]) # columns

        self.maxCol = n
        self.maxRow = m

        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfsAndMark(grid, i, j)
                    numIslands += 1
        
        return numIslands

        
