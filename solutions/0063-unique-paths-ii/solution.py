class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        numRows = len(obstacleGrid)
        if numRows == 0:
            return 0
        numCols = len(obstacleGrid[0]) # square grid so numCols != 0 
        if (obstacleGrid[numRows-1][numCols-1] == 1):
            return 0

        paths = [[ 0 for j in range(numCols)] for i in range(numRows)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            paths[0][0] = 1
        for i in range(numRows):
            for j in range(numCols):
                if obstacleGrid[i][j] == 0:
                    if (i-1) >= 0:
                        paths[i][j] += paths[i-1][j]
                    if (j-1 >= 0):
                        paths[i][j] += paths[i][j-1]
        return paths[numRows-1][numCols-1]




