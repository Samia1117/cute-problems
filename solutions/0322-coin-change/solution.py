class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # min number of coins to make up amount

        # let dp[i] = min number of coins to make up amount i
        # dp[0] = 0

        # dp[i] = infinity / sys.maxsize if not possible to make i with coins

        # dp[i] = for all denominations d, min(dp[i-d] + 1)

        if amount == 0:
            return 0
        
        max_coin = max(coins) + 1
        dp = [-1 for i in range(amount+1)]
        # dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for d in coins:
                if i-d < 0:
                    continue
                if dp[i-d] == -1:
                    continue
                else:
                    if dp[i] == -1:
                        dp[i] = dp[i-d] + 1
                    else:
                        dp[i] = min(dp[i], dp[i-d] + 1)
            
            # dp[i] = min([dp[i-d] + 1 for d in coins])
        
        # if dp[amount] == float('inf'):
        #     return -1
        return dp[amount]



        
