class Solution:

    def product(self, nums: List[int]) -> int: 
        res = 1
        for num in nums:
            res *= num
        return res

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        max_combo_chains = [nums[i] for i in range(n)]
        # max_combo_chains[i] = max combo chain starting from i

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, n):
            curr = nums[i]
            # maybe the sign will flip based on sign of 'curr'
            # so keep track of both 'max_so_far' and 'min_so_far'
            temp_max = max(curr, max(max_so_far * curr, min_so_far * curr) )
            min_so_far = min(curr, min(max_so_far * curr, min_so_far * curr))

            max_so_far = temp_max
            result = max(max_so_far, result)
        return result

        #     for j in range(i+1, n):
        #         if nums[i] <= 0 or nums[j] <= 0:
        #             break
        #         else:
        #             max_combo_chains[i] *= nums[j]
        # print(f'max_combo_chains = {max_combo_chains}')
        # return max(max_combo_chains)

        # dp[i][j] = product from nums[i] to nums[j]
        # Note: subarray is a contiguous segment of array

        # Base case: dp[i][i] = nums[i] for all i
        # dp[i][j] = product(nums[i:j+1]) --> but recomputing products might be expensive!

        # first row: nums[0], nums[0] * nums[1], 
        # instead do:
            # while j:
                # dp[i][j] = dp[i][j-1] * nums[j]
            # while i:
                # dp[i][j] = dp[i-1][j] / nums[i-1]
        '''
        [2,3,-2,4]
        dp[0][0] = 2
        dp[0][1] = 2, 3
        dp[0][2] = 2, 3, -2
        dp[0][3] = 2, 3, -2, 4
        dp[0][4] = 2, 3, -2, 4, 5
        dp[0][5] = 2, 3, -2, 4, 5, 6

        dp[1][1] = 3  <-- makes more sense to use dp[i-1][j]/nums[i-1]
        dp[1][2] = 3, -2  <-- makes more sense to use dp[i-1][j]/nums[i-1]
        dp[1][3] = 3, -2, 4  <-- makes more sense to use dp[i-1][j]/nums[i-1]
        dp[1][4] = 3, -2, 4, 5  <-- makes more sense to use dp[i-1][j]/nums[i-1]
        dp[1][5] = 3, -2, 4, 5, 6  <-- makes more sense to use dp[0][5]/nums[0] (2)

        '''

        '''
        n = len(nums)

        if n == 0:
            return 0
        # if n == 1:
        #     return nums[0]

        current_max_product = nums[0]
        min_product = nums[0]
        max_product = nums[0]

        for i in range(1, n):
            current_max_product = max(nums[0], max(min_product * nums[i], current_max_product * nums[i]))

            min_product = min(nums[0], min(min_product * nums[i], current_max_product * nums[i]))

            max_prodict = max(max_product, current_max_product)

        return max_product
        
        
        dp = [[-sys.maxsize for i in range(n)] for j in range(n)]

        max_product = -sys.maxsize
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    # dp[i][j] = self.product(nums[i:j+1])

                    # time to optimize
                    if j > 0:
                        dp[i][j] = dp[i][j-1] * nums[j]
                    else:
                        dp[i][j] = dp[i-1][j] / nums[i-1]

        
                max_product = max(dp[i][j], max_product)
        
        # print(f'dp = {dp}')
        return max_product
        '''
