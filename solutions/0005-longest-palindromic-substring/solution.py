class Solution:
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        if s[0] != s[1]:
            return False
        return self.isPalindrome(s[0:-1])

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 
        
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        ans = [0,0]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]
        start, end = ans
        return s[start:end+1]
        
        
