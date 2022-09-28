class Solution:
    
    def all_blanks(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m): 
                if grid[i][j] != 0:
                    return False
        return True
    
    def all_rotten(self, grid):
        blanks = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return False
                elif grid[i][j] == 0:
                    blanks +=1
                    
        if blanks == n*m:   # all blanks
            return False
        
        return True
    
    def getPos(self, row, col, maxCol):
        return row*maxCol + col
    
    def offGrid(self, row, col, maxCol, maxRow):
        if row>=maxRow or col>=maxCol or row<0 or col<0:
            return True
        return False
    
    #def dfsOranges(self, row, col, maxCol, maxRow, visited)
                
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        visited = set()
        rotten_ones = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    pos = self.getPos(i, j, m)
                    rotten_ones.append(pos)
        i = 0
        visited = set()
        # print("rotten ones at start are: ", rotten_ones)
        while rotten_ones and not self.all_rotten(grid):
            next_cohort = []
            while rotten_ones:
                rotten = rotten_ones.pop()
                visited.add(rotten)
            
                rottenx = rotten//m
                rotteny = rotten%m

                moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for move in moves:
                    x = move[0] + rottenx
                    y =  move[1] + rotteny
                    if not self.offGrid(x, y, m, n):
                        xyPos = self.getPos(x, y, m)
                        if xyPos not in visited:
                            if grid[x][y] == 1:
                                grid[x][y] = 2
                                next_cohort.append(xyPos)

            rotten_ones.extendleft(next_cohort)
                        
            # print("Got grid now:", grid)
            # print("rotten ones at i are: ", rotten_ones)
            # print("visited are: ", visited)
            i+=1
            
        if self.all_blanks(grid):
            return 0
        
        if not self.all_rotten(grid):
            return -1
        
        return i
        
        
        
        
        
        
        
        
        
