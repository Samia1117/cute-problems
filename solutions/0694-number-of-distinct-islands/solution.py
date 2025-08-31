class Solution:

    # def collapseIslands(self, islands):
    #     new_islands = {}
    #     for k, v in islands.items():
    #         for 

    def isInBounds(self, row, col):
        return 0 <= row < self.max_row and 0 <= col < self.max_col

    def dfsAndRecordIsland(self, grid, row, col, vertices, path_list):
        # print(f'path = {path_str}')
        vertices.append((row, col))
        grid[row][col] = 0 # marks as visited

        dirs = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
        for i in range(4):
            d = dirs[i] # i = 0 -> 'R', i = 1 -> 'L', i = 2 -> 'D', i = 3 -> 'U'
            new_row, new_col = row + d[0], col + d[1]
            if self.isInBounds(new_row, new_col) and grid[new_row][new_col] == 1:
                path_list.append(d[2])
                self.dfsAndRecordIsland(grid, new_row, new_col, vertices, path_list)
                path_list.append('B')

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # top left: rows = (0, 1), cols = (0, -1) 
        # bottom right: (0, 1) (1, 1)

        # top right: rows = (0, 1), cols = {}
        # bottom left: rows = (0, 1), cols = {}

        # (0,0) (0,1) (1, 0) (1, 1)
        # (3,3) (3, 4) (4, 3) (4, 4) 
        # diff: (-3, -3) (-3, -3) (-3, -3) (-3, -3)

        # (0,0) (0,1) (1, 0) (1, 1)
        # (0,1) (0,2) (1, 1) (1, 2)
        # diff: (0, -1) (0, -1) (0, -1) (0, -1)

        # Observation 1: if two islands have:
        #   i) same # of vertices AND
        #   ii) there is an ordering of vertices such that:
        #       1) Row diff is the same across all vertices
        #       2) Col diff is the same across all vertices
        # QQ: how do we find this ordering? We might sort the shapes according to row then column indices - but that would be high complexity timewise

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        self.max_row = m
        self.max_col = n
        # islands = {} # num vertices to islands (list of tuples)
        paths = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    vertices = []
                    path_list = ["S"] # start
                    # print(f'Recording starting at ({i, j})')
                    self.dfsAndRecordIsland(grid, i, j, vertices, path_list)
                    # print(f'path_list = {path_list}')

                    paths.add(''.join(path_list))

                    # k = len(vertices)
                    # if k not in islands:
                    #     islands[k] = []
                    # islands[k].append(vertices)
        
        # print(f'Paths = {paths}')
        # print(f"Islands = {islands}")
        # islands = collapseIslands(islands)

        return len(paths)

        
