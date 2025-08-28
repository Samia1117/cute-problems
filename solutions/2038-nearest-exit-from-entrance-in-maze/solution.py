class Solution:
    def __init__(self):
        self.min_path = sys.maxsize

    def isInBounds(self, row, col):
        return 0 <= row < self.maxRow and 0 <= col < self.maxCol

    def isExit(self, row, col, maze):
        if (row == self.maxRow - 1 or row == 0 or col == self.maxCol - 1 or col == 0) and maze[row][col] == '.':
            return True
        return False
    '''
    def nearestExitRec(self, row, col, maze, visited, path_len) -> int:
        # visited.add((row, col))
        maze[row][col] = '+'
        if self.isExit(row, col, self.maxRow, self.maxCol, maze):
            self.min_path = min(self.min_path, path_len)
        
        deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(4):
            delta = deltas[i]
            newRow, newCol = row + delta[0], col + delta[1]
            if self.isInBounds(newRow, newCol, self.maxRow, self.maxCol) and maze[newRow][newCol] != '+':
                self.nearestExitRec(newRow, newCol, maze, visited, path_len + 1)
    '''

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.entrance = entrance
        self.maxRow = len(maze)
        if self.maxRow == 0:
            return 0
        self.maxCol = len(maze[0])

        ''' dfs -> does not work - I may visit a cell in a long-winded path first
        '''
        # visited = set()
        # visited.add((entrance[0], entrance[1]))
        
        # self.nearestExitRec(entrance[0], entrance[1], maze, visited, 0)
        # if self.min_path == sys.maxsize:
        #     return -1
        # return self.min_path

        ''' bfs
        '''
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            item = q.popleft()
            row, col, path_len = item[0], item[1], item[2]

            deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for i in range(4):
                delta = deltas[i]
                newRow, newCol = row + delta[0], col + delta[1]

                # If neighbor within grid and is not a wall, traverse
                if self.isInBounds(newRow, newCol)and maze[newRow][newCol] != '+':
                    if self.isExit(newRow, newCol, maze):
                        return path_len + 1
                
                    # mark this cell as visited, not an exit
                    maze[newRow][newCol] = '+'
                    q.append((newRow, newCol, path_len+1))
        
        return -1

