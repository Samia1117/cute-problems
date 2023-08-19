class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        numRows = len(grid)
        if numRows == 0:
            return 0
        numCols = len(grid[0])

        sumPaths = [[ {} for j in range(numCols)] for i in range(numRows)]
        sumPaths[0][0] = {grid[0][0]%k: 1}

        for i in range(numRows):
            for j in range(numCols):
                # print("sumPaths is ", sumPaths)
                if (i-1 >= 0):
                    # print("for i-1, j", sumPaths[i-1][j])
                    for oneSum in sumPaths[i-1][j]:
                        # print("key, val: ", [oneSum, sumPaths[i-1][j][oneSum]])
                        num = (oneSum + grid[i][j])%k
                        # print("num is ", num)
                        if num not in sumPaths[i][j]:
                            sumPaths[i][j][num] = sumPaths[i-1][j][oneSum]
                        else:
                            sumPaths[i][j][num] += sumPaths[i-1][j][oneSum]
                if (j-1 >= 0):
                    # print("for i, j-1", sumPaths[i][j-1])
                    for oneSum in sumPaths[i][j-1]:
                        # print("key, val: ", [oneSum, sumPaths[i][j-1][oneSum]])
                        num = (oneSum + grid[i][j])%k
                        # print("num is ", num)
                        if num not in sumPaths[i][j]:
                            sumPaths[i][j][num] = sumPaths[i][j-1][oneSum]
                        else:
                            sumPaths[i][j][num] += sumPaths[i][j-1][oneSum]
        paths = 0
        # print("sumPaths", sumPaths)
        for num in sumPaths[numRows - 1][numCols - 1]:
            if num%k == 0:
                paths += sumPaths[numRows - 1][numCols - 1][num]
        return paths % (10**9 + 7)

                

