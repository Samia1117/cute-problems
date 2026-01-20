class Solution:
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def _in_bounds(self, x: int, y: int, max_row: int, max_col: int) -> bool:
        if x < 0 or x >= max_row:
            return False
        if y < 0 or y >= max_col:
            return False
        return True

    def numIslands(self, grid: List[List[str]]) -> int:

        # traverse the grid, one cell at a time, modifying it in place to mark cells as having been visited
        # each cell can be part of exactly one island so marking it as soon as it's seen is good enough

        max_row = len(grid)
        if max_row <= 0:
            return 0
        max_col = len(grid[0])

        def dfs_and_mark(row: int, col: int) -> None:
            grid[row][col] = 'x'
            for delta in Solution.deltas:
                new_row, new_col = row + delta[0], col + delta[1]
                if self._in_bounds(new_row, new_col, max_row, max_col) and grid[new_row][new_col] == '1':
                    dfs_and_mark(new_row, new_col)

        num_components = 0
        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == '1':
                    dfs_and_mark(i, j)
                    num_components += 1
        
        return num_components


        
