class Solution:

    def minDistanceRec(self, s1, s2):
        if len(s1) == 0:
            return len(s2)
        if len(s2) == 0:
            return len(s1)
        
        noop = sys.maxsize
        deletes1 = sys.maxsize
        deletes2 = sys.maxsize
        sub = sys.maxsize

        if s1[0] == s2[0]:
            noop = self.minDistanceRec(s1[1:], s2[1:])
        else:
            # delete s1[0]
            deletes1 = self.minDistanceRec(s1[1:], s2) + 1
            # delete s1[0]
            deletes2 = self.minDistanceRec(s1, s2[1:]) + 1

            ## Note, these two cases end up the same as above 2 -> can be combined
            # insert s1[0] right before s2[0]
            # inserts1 = minDistanceRec(s1[1:], s2) + 1
            # # insert s2[0] right before s1[0]
            # inserts2 = minDistanceRec(s1, s2[1:]) + 1
            
            # substitute s1[0] with s2[0] or vice versa
            sub = self.minDistanceRec(s1[1:], s2[1:]) + 1
        return min(sub, min(deletes1, min(deletes2, noop)))
        

    def minDistance(self, word1: str, word2: str) -> int:

        '''
        Works but gives me a TLE!
        # return self.minDistanceRec(word1, word2)
        '''

        # Try a DP approach

        # dp[i][j] = min distance using up to (not including) s1[:i], s2[:j]

        # dp[0][0] = 0 because we consider s1[0] and s2[0] the empty string
        # dp[0][j] = len(s2[0:j]) 
        # dp[i][0] = len(s1[0:i])  

        s1 = word1
        s2 = word2

        n = len(s1)
        m = len(s2)
        dp = [[10000 for j in range(m+1)] for i in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                # if i == 0:
                #     dp[i][j] = len(s2[:j])
                # if j == 0:
                #     dp[i][j] = len(s1[:i])
                if i != 0 and j != 0:
                    # print(f"i = {i}, j={j}, dp = {dp}")
                    noop = sys.maxsize
                    deletes1 = sys.maxsize
                    deletes2 = sys.maxsize
                    sub = sys.maxsize

                    if s1[i-1] == s2[j-1]:
                        noop = dp[i-1][j-1]
                        # dp[i][j] = dp[i-1][j-1]
                    # else:
                    # delete s1[i]
                    deletes1 = dp[i-1][j] + 1
                    # delete s2[j]
                    deletes2 = dp[i][j-1] + 1
                    # sub s1[i] with s2[j] or vice versa
                    sub = dp[i-1][j-1] + 1

                    dp[i][j] = min(sub, min(deletes1, min(deletes2, noop)))
                        # dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1
        
        # print(f"num rows = {len(dp)} ")
        # print(f"n+1 = {n+1} ")
        # print(f"num columns = {len(dp[0])} ")
        # print(f"m+1 = {m+1} ")

        return dp[n][m]
















        # let dp[i][j] := edit distance between word1[0:i] and word2[0:j]

        # want: dp[m][n] where m=len(word1), n=len(word2)
        
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

                # sub word[i] -> match word[i], word[j] for +1 + dp[i-1][j-1]
                # del word[i] -> dp[i-1][j] +1
                # insert -> dp[i][j-1] + 1 (match current word[j] with inserted word)
                elif word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min([dp[i][j-1], dp[i-1][j], dp[i-1][j-1]])
        
        return dp[m][n]
        
