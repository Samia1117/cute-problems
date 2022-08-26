class Solution:
    
    def minCoins(self, coins, amount, numCoins):
        if amount<0:
            return None
        if amount ==0:
            return numCoins
        else:
            currentMin = 10000
            for coin in coins:
                minCs = self.minCoins(coins, amount-coin, numCoins+1)
                if minCs == None:
                    continue
                if minCs < currentMin:
                    currentMin = minCs
            return currentMin
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [100003 for i in range(amount+1)]
        
        dp[0] = 0   # 0 coins for amount = 0
        
        for currentAmount in range(amount+1):
            for c in coins:
                if c+currentAmount <= amount:
                    dp[c+currentAmount] = min(dp[c+currentAmount], dp[currentAmount] + 1)
                
        n = len(dp)-1
        if dp[n] == 100003:
            return -1
        return dp[n]
        
        # if amount == 0:
        #     return 0
        
#         currentMin = 10000
#         for coin in coins:
#             minCs = self.minCoins(coins, amount-coin, 1)
#             if minCs == None:
#                 continue
#             if minCs < currentMin:
#                 currentMin = minCs
        
#         if currentMin == 10000:
#             return -1
#         return currentMin
