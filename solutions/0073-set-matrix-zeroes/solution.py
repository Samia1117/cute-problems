class Solution:
    
    def updateColumnRow(self, matrix, i, j, m, n):
        for k in range(m):
            matrix[k][j] = 0
        for l in range(n):
            matrix[i][l] = 0
        return
         
    def pos(self, i, j, m, n):
        return i*n + j
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        m = len(matrix)
        n = len(matrix[0])
        originalZeroes = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # originalZeroes.append(sorted([i,j]))
                    originalZeroes.append(self.pos(i, j, m, n))

        print("original zeroes are: ", originalZeroes)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    p = self.pos(i, j, m, n)
                    if p in originalZeroes:
                        self.updateColumnRow(matrix, i, j, m, n)
                        # originalZeroes.append(sorted([i, j]))
        return
        
        
