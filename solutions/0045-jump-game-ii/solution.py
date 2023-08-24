class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Let dp[i][j] mean the minimum number of jumps to get from nums[i] to nums[j]
        # Need to find min(dp[i][n-1])
        n = len(nums)
        if n <= 1:
            return 0
        # dp = [ [0 if i==j else 100000 for i in range(n)] for j in range(n)]
        minJumps = [10000 for i in range(n)]
        canReach = [False for i in range(n)]
        minJumps[0] = 0
        canReach[0] = True

        for i in range(n):
            if not canReach[i]:
                continue
            for j in range(i+1, min(nums[i] + i + 1, n)):
                # dp[i][j] = min(dp[i][j], dp[])
                canReach[j] = True
                minJumps[j] = min(minJumps[j], minJumps[i] + 1)

        return minJumps[n-1]

