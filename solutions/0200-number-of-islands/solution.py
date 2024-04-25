class Solution:
    def idx(self, row, col, maxRow, maxCol):
        return (row * maxCol) + col

    def is_in_bounds(self, i, j, maxRow, maxCol):
        return i >= 0 and j >= 0 and i < maxRow and j < maxCol

    def dfs_and_mark(self, visited, grid, i, j, maxRow, maxCol):
        st = deque()
        st.append([i,j])

        # print("i, j: ", [i,j])
        while st:
            popped = st.pop()
            visited[popped[0]][popped[1]] = True
            # print("New visited: ", visited)
            # left
            left_i, left_j = popped[0], popped[1] - 1
            # print("left i, j: ", [left_i, left_j])
            if self.is_in_bounds(left_i, left_j, maxRow, maxCol) and grid[left_i][left_j] == '1' and not visited[left_i][left_j]:
                st.append([left_i, left_j])

            # right
            right_i, right_j = popped[0], popped[1] + 1
            # print("right i, j: ", [right_i, right_j])
            if self.is_in_bounds(right_i, right_j, maxRow, maxCol) and grid[right_i][right_j] == '1' and not visited[right_i][right_j]:
                st.append([right_i, right_j])

            # up
            up_i, up_j = popped[0] - 1, popped[1]
            # print("up i, j: ", [up_i, up_j])
            if self.is_in_bounds(up_i, up_j, maxRow, maxCol) and grid[up_i][up_j] == '1' and not visited[up_i][up_j]:
                st.append([up_i, up_j])

            # down
            down_i, down_j = popped[0] + 1, popped[1]
            # print("down i, j: ", [down_i, down_j])
            if self.is_in_bounds(down_i, down_j, maxRow, maxCol) and grid[down_i][down_j] == '1' and not visited[down_i][down_j]:
                st.append([down_i, down_j])
            
        return

    def numIslands(self, grid: List[List[str]]) -> int:

        maxRow = len(grid)
        if maxRow == 0:
            return 0
        maxCol = len(grid[0])

        visited = [[False for i in range(maxCol)] for j in range(maxRow)]

        conn_components = 0
        for i in range(maxRow):
            for j in range(maxCol):

                # check connnected components 
                if grid[i][j] == '1' and not visited[i][j]:
                    # print("found land at: ", [i, j])
                    self.dfs_and_mark(visited, grid, i, j, maxRow, maxCol)
                    conn_components += 1
                # print("One connected component down. I, j: ", [i,j])
                        
        return conn_components
        
