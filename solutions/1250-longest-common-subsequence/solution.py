class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        if (n == 0 or m == 0):
            return 0
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        # for i in range(n):
        #     for j in range(m):
        #         if i == 0 or j== 0:
        #             dp[i][j] = 0

        # dp[i][j] = lcs ending at text1[i] and text2[j]
        # need dp[n][m]
        # base case: dp[0][m] = 0
        # base case: dp[0][n] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                # print("matching ", [text1[i-1], text2[j-1]])
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # print("dp[i][j]: ", dp[i][j])

        return dp[n][m]
