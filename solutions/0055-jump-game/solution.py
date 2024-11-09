class Solution:

    # def canReachIndex(self, index, nums):

    #     if index == 0:
    #         return True
        
    #     if nums[index-1]
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        if n <= 1:
            return True
        
        '''
        Forward pass way
        '''
        # dp = [False for i in range(n)] # dp[i] = canJump to state i
        # dp[0] = True

        # for i in range(n):
        #     if dp[i] == True:
        #         jump = nums[i]
        #         furthest_jump = min(n-1, i + jump)
        #         print(f"furthest jump = {furthest_jump}")
        #         for j in range(i+1, furthest_jump+1):
        #             dp[j] = True
        
        # return dp[n-1]

        '''
        Backward pass way
        '''
        dp = [False for i in range(n)] 
        # dp[i] = can reach final state from position i
        dp[-1] = True

        for i in range(n-2, -1, -1):
            jump = nums[i]
            furthest_jump = min(n-1, i + jump)
            for j in range(i + 1, furthest_jump + 1):
                if dp[j] == True:
                    dp[i] = True
                    break
        return dp[0]
        # print("DP: ", dp)
        
