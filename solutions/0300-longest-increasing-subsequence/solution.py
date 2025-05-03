class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        # def dp[i] = longest increasing subseq. ending at i
        # def dp[0] = 1 (1-elt sequence)

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)
        
