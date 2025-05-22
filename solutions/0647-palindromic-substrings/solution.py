class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        if n <= 1:
            return n
        
        # let dp[i][j] = True is s[i:j+1] is a palindrome
        dp = [[False for i in range(n)] for j in range(n)]

        # base cases: 
        # 1. s[i:i+1] (one letter) is a palindrome
        # 2. s[i:i+1] double matching letters are a palindrome
        for i in range(n):
            dp[i][i] = True
            if i < n - 1:
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
        
        for window_size in range(3, n+1):
            for start in range(n):
                end = start + window_size - 1
                if end < n and s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end-1]
        ans = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] == True:
                    ans += 1
        
        return ans
    

        
