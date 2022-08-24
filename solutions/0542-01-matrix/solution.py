class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
#         q = deque()
#         maxRow = len(mat)
#         maxCol = len(mat[0])
        
#         dist = [[10000 for i in range(maxCol)] for j in range(maxRow)]
#         for row in range(maxRow):
#             for col in range(maxCol):
#                 if mat[row][col] == 0:
#                     dist[row][col] = 0
#                     q.append([row, col])
        
#         directions =[ [0, 1], [1, 0], [0, -1], [-1, 0] ]
#         while q:
#             pair = q.popleft()
#             for i in range(4):
#                 dirc = directions[i]
#                 newPair = [pair[0]+dirc[0], pair[1]+dirc[1]]
#                 newR = newPair[0]
#                 newC = newPair[1]
#                 if self.within_bounds(mat, newR, newC, maxRow, maxCol):
#                     if (dist[newR][newC] > dist[pair[0]][pair[1]]+1):
#                         dist[newR][newC] = dist[pair[0]][pair[1]]+1
#                         q.append(newPair)
        
        maxRow = len(mat)
        maxCol = len(mat[0])
        
        dist = [[10000 for i in range(maxCol)] for j in range(maxRow)]
        
        for i in range(maxRow):
            for j in range(maxCol):
                if mat[i][j]==0:
                    dist[i][j]=0
                else:
                    if j>0:
                        dist[i][j] = min(dist[i][j-1]+1, dist[i][j])
                    if i>0:
                        dist[i][j] = min(dist[i-1][j]+1, dist[i][j])
                        
        for i in reversed(range(maxRow)):
            for j in reversed(range(maxCol)):
                if mat[i][j]==0:
                    dist[i][j]=0
                else:
                    if i<maxRow-1:
                        dist[i][j] = min(dist[i+1][j]+1, dist[i][j])
                    if j<maxCol-1:
                        dist[i][j] = min(dist[i][j+1]+1, dist[i][j])
        
                
        return dist
    
    def within_bounds(self, mat, row, col, maxRow, maxCol):
        if row>=maxRow or row<0:
            return False
        if col>=maxCol or col<0:
            return False
        return True
    
    def hashNum(self, row, col, maxCol, mat):
        return row*maxCol + col
    
    def matDistance(self, my_coords, other_coords):
        myrow =  my_coords[0]
        mycol = my_coords[1]
        otherrow = other_coords[0]
        othercol = other_coords[1]
        # print("my row, col: ", [myrow, mycol], "other row, col: ", other_coords)
        return abs(myrow-otherrow) + abs(mycol-othercol)

        
        
