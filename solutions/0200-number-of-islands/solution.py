class Solution:
    def offGrid(self, row, col, numRows, numCols):
        if (row >= numRows or col >= numCols
        or row < 0 or col < 0):
            return True
        return False
    
    def getPos(self, row, col, maxCol):
        return maxCol*row + col
    
    def markVisitedDFS(self, row, col, grid, numRows, numCols, posVisited):
        pos = self.getPos(row, col, numCols)
        if pos not in posVisited:
            posVisited.add(pos)
            # print("Now marking visited: ", [row, col])
            neigh_index = [[0,1], [1, 0], [-1, 0], [0, -1]]
            for i in range(4):
                x = neigh_index[i][0]
                y = neigh_index[i][1]
                if not self.offGrid(row+x, col+y, numRows, numCols):
                    if grid[row+x][col+y] == "1":
                        self.markVisitedDFS(row+x, col+y, grid, numRows, numCols, posVisited)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid == []:
            return 0
        
        numRows = len(grid)
        numCols = len(grid[0])
        posVisited = set([])
        
        islandCount = 0
        
        for i in range(numRows):
            for j in range(numCols):
                pos = self.getPos(i, j, numCols)
                if pos not in posVisited:
                    if grid[i][j] == "1":
                        # print("Found a non visited one")
                        islandCount +=1
                        self.markVisitedDFS(i, j, grid, numRows, numCols, posVisited)   # mark all neighboring 1's as visited
                else:
                    posVisited.add(pos)
                # print("Positions visited: ", posVisited)
                      
        return islandCount
                        
                        
                        
        
