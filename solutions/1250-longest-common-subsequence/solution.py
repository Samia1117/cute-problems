class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if not text1 or not text2:
            return 0

        ''' Recursive
        lcs = 0
        if text1[0] == text2[0]:
            lcs = 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        else:
            lcs = max(
                self.longestCommonSubsequence(text1[1:], text2), 
                self.longestCommonSubsequence(text1, text2[1:])
            )
        return lcs
        '''

        '''dp
        '''
        # Let dp[i][j] := lcs using text1[:i], text2[:j]
        # dp[i][j] = {
            # if text1[i] == text2[j]:
                # dp[i-1][j-1] + 1 
            # else:
                # max (
                    # dp[i-1][j], dp[i][j-1]
                # )
            # }
        #}
        
        n = len(text1)
        m = len(text2)
        if m == 0 or n == 0:
            return 0
        
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        # dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[n][m] 
