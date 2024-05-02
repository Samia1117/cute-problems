import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1

        # dp[i][j] = min number of coins I need to make j amount using first i coins
        # dp[n][amount] = min number of coins I need to make 'amount' amount using first n (all) coins

        # base case
        # dp[i][0] = 0, since no coins needed to make amount 0
        # dp[0][j] = inf, since cannot make any amount j unless 

        # transition:
        # dp[i-1][j-coins(i)] = min # of coins to make j-coins using first i-1 coins - assumes we use i^th coin 
        # dp[i-1][j] = min # of coins to make j using first i coins - assumes we DON'T use ith coin 
        # dp[i][j] = min(dp[i-1][j], 
        n = len(coins)

        dp = [ [10001 for j in range(amount + 1)] for i in range(n+1)]

        for i in range(n+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 0
                    continue
                
                elif i == 0:
                    continue

                # print("i, j: ", [i, j])
                # print("DP so far: ", dp)
                
                # 1. Don't use coin i
                best_without_coin_i = dp[i-1][j] 

                # Note coins index is 1 lower
                amount_without_coin_i = j - coins[i-1]

                # Check if coin i can be used to make amount j
                if amount_without_coin_i >= 0: 
                    # 2. Use coin i (at index i-1) 
                    best_with_coin_i = dp[i][amount_without_coin_i] + 1

                    dp[i][j] = min(best_without_coin_i, best_with_coin_i)
                else:
                    dp[i][j] = best_without_coin_i

        
        if dp[n][amount] == 10001:
            return -1
        return dp[n][amount]

        



        

        
