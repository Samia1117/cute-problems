class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Let dp[i][j] = if it is possible to go from index i to j
        # Return true if dp[i][n-1] true for any i s.t. i <= n-2
        n = len(nums)
        if n <= 1:
            return True

        canReach = [False for i in range(n)]
        canReach[0] = True

        # Keep track of index up to which we already know we can jump
        maxJumpSofar = 0
        for i in range(n):
            if not canReach[i]:
                continue
            # If we can't reach beyond what we already know we can reach using nums[i], then skip nums[i]
            if i + nums[i] <= maxJumpSofar:
                continue
            # Only start from
            maxJumpForIdx = min(nums[i] + i, n)
            for j in reversed(range(maxJumpSofar + 1, min(maxJumpForIdx + 1, n))):
                if j == n-1:
                    return True
                canReach[j] = True

            if maxJumpSofar < maxJumpForIdx:
                maxJumpSofar = maxJumpForIdx
        
        return canReach[n-1]
                
