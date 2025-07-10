class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            if not nums[0] == k:
                return 0
            else:
                return 1

        # dp  = [ [0 for i in range(n)] for j in range(n)]
        # dp = [0 for i in range(n)]
        # dp[0] = nums[0]
        num_subarrays = 0

        # first build a cumulative sums array
        hmap = {}
        hmap[0] = 1
        
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            # We know curr_sum + k - curr_sum = k, so check if curr_sum - k is in hmap
            if curr_sum - k in hmap:
                num_subarrays += hmap[curr_sum - k]

            if curr_sum not in hmap:
                hmap[curr_sum] = 0
            hmap[curr_sum] += 1

        # if nums[j] - nums[i] == k: then nums[i:j+1] has a sum equaling k
        # for i in range(n):
        #     for j in range(i, n):
        #         if dp[i][j] == k:
        #             num_subarrays += 1
        
        return num_subarrays



            

        
