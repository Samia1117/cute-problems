class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # Let # of uniquePaths ending at grid[i][j] be dp[i][j]
        # we need dp[m-1][n-1]

        # dp[i][j] = dp[i][j-1] # from left + dp[i-1][j] # from top
        
        rows = len(obstacleGrid)
        if rows == 0:
            return 0
        cols = len(obstacleGrid[0])

        dp = [[0 for i in range(cols)] for j in range(rows)]
        if obstacleGrid[0][0] == 1:
            return 0
            
        dp[0][0] = 1

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 0:
                    if i-1 >= 0:
                        dp[i][j] += dp[i-1][j]
                    if j-1 >= 0:
                        dp[i][j] += dp[i][j-1]
                    
        return dp[rows-1][cols-1]


        # max_sum = rows + cols - 1
        # for s in reversed(range(max_sum)): # s = sum
        #     # (2, 2), (1, 2), (2, 1), -> (2, 0), (1, 1), (0, 2)...
        #     # (3, 3), (3, 2), (2, 3), -> ()
        #     for j in range(max_sum):
        #         i = max_sum//2 - j
        #         j = s - i
        #         print(f'i, j = {i, j}')

        
