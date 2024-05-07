class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
                # let dp[i][j] = edit distance between word1[0:i] and word2[0:j]
        # want: dp[m][n] where m-len(word1), n=len(word2)
        
        m = len(word1)
        n = len(word2)
        if m==0:
            return n
        if n==0:
            return m
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                # case 1: word[i]==word[j]
                # case 2: word[i]!=word[j]
                # sub word[i]-> match word[i], word[j] for +1 + dp[i-1][j-1]
                # del word[i] -> dp[i-1][j] +1
                # insert -> dp[i][j-1] + 1 (match current word[j] with inserted word)
                elif word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min([dp[i][j-1], dp[i-1][j], dp[i-1][j-1]])
        
        return dp[m][n]
        
