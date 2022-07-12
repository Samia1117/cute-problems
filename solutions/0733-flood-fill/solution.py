class Solution(object):
    
    def offGrid(self, row, col, numRows, numCols):
        if (row >= numRows or col >= numCols
        or row < 0 or col < 0):
            return True
        return False
    
    def getPos(self, row, col, numCols):
        return ((numCols) * row) + col # e.g. 4*1 + 2
    
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if len(image) == 0:
            return image
        visited = set([])
        
        q = deque()
        numRows = len(image)
        numCols = len(image[0])
        # print("numRows: ", numRows)
        # print("numCols: ", numCols)
        
        qPos = self.getPos(sr, sc, numCols)
        q.append(qPos)
        startColor = image[sr][sc]
        
        while len(q) != 0:
            pix = q.popleft()
            visited.add(pix)
            row = pix // numCols
            col = pix % numCols
            # print("STATE of queue: ", q)
            # print("visited (row, col) are: ", row, col)
            
            if image[row][col] == startColor:
                
                if not (self.offGrid(row, col+1, numRows, numCols)):
                    right = self.getPos(row, col+1, numCols)
                    if (right not in visited and right not in q):
                        q.append(right)

                if not (self.offGrid(row, col-1, numRows, numCols)):
                    left = self.getPos(row, col-1, numCols)
                    if (left not in visited and left not in q):
                        q.append(left)

                if not (self.offGrid(row+1, col, numRows, numCols)):
                    down = self.getPos(row+1, col, numCols)
                    if (down not in visited and down not in q):
                        q.append(down)

                if not (self.offGrid(row-1, col, numRows, numCols)):
                    up = self.getPos(row-1, col, numCols)
                    if (up not in visited and up not in q):
                        q.append(up)

                image[row][col] = color
        
        return image
            
        
