class Solution:

    def numDecodings(self, s: str) -> int:
        # Let dp[i] = num ways to decode s[:i+1]
        # dp[i] += dp[i-1] if s[i] in 'digits'
        # dp[i] += dp[i-2] if s[i-2:i] in digits

        # dp[0] = s[0] if s[0] in digits

        digits = [str(i) for i in range(1, 27)]

        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1 if s[0] in digits else 0

        dp = [0 for i in range(n)]

        dp[0] = 1 if s[0] in digits else 0
        dp[1] += dp[0] if s[1] in digits else 0
        dp[1] += 1 if s[:2] in digits else 0

        for i in range(2, n):
            dp[i] += dp[i-1] if s[i] in digits else 0
            dp[i] += dp[i-2] if s[i-1:i+1] in digits else 0
        
        return dp[n-1]


        '''
        def numWays(s, index):
            if index == len(s):
                return 1
            # print(f'index, s[index] = {index, s[index]}')
            
            if s[index] not in digits:
                return 0

            if index == len(s) - 1:
                return 1
                
            total = numWays(s, index+1)
            # print(f'total = {total}')
            if s[:2] in digits:
                total += numWays(s, index+2)
            return total

        # print(f'digits ==== {list(digits)}')

        val = numWays(s, 0)
        return val
        '''
        
