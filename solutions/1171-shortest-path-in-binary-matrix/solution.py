class Solution:

    def in_bounds(self, tup, n):
        if tup[0] < 0 or tup[0] >= n:
            return False
        if tup[1] < 0 or tup[1] >= n:
            return False
        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # perform a bfs
        if not grid:
            return None
        
        n = len(grid)
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        if grid[0][0] != 0:
            return -1

        q = deque()
        q.append((0,0))
        grid[0][0] = 1

        row_dirs = [1, 1, -1, -1, 0, 0, 1, -1]
        col_dirs = [-1, 1, -1, 1, -1, 1, 0, 0]

        while q:
            row, col = q.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for i in range(len(row_dirs)):
                curr_dir = (row + row_dirs[i], col + col_dirs[i])
                
                if self.in_bounds(curr_dir, n) and grid[curr_dir[0]][curr_dir[1]] == 0:
                    q.append( (curr_dir[0], curr_dir[1]) )
                    grid[curr_dir[0]][curr_dir[1]] = distance + 1

        return -1
        
