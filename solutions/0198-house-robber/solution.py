# from functools import cache

class Solution:
    '''
    Approach 1: Recursion
    '''
    def rob_recursive(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            a = self.rob_recursive(nums[1:])
            b = nums[0] + self.rob_recursive(nums[2:])
            return max(a, b)

    '''
    Approach 2: Dynamic Programming
    '''
    def rob_dp(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for i in range(n)]
        # dp[i] = total reward by robbing houses up to i^th house
        # Want: dp[n] := total reward by robbing houses up to n^th house
        # dp[i] = max { 1. dp[i-2] + nums[i] # rob house i; 2. dp[i-1] # don't rob house i}


        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        # return self.rob_recursive(nums)
        return self.rob_dp(nums)
        
