class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0 for i in range(n)]
        dp[0] = nums[0]

        max_so_far = dp[0]

        for i in range(1, n):
            if i > 1:
                # dp[i] = max(max(dp[:i-1]) + nums[i], max(dp[:i]))
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            else:
                dp[i] = max(nums[i], dp[0])
        
        return max(dp)
