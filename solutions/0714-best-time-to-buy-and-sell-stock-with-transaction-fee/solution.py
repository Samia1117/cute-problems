class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        Again, max_profit at day 0 will be 0.
        max_profit at day 1 will be maximum of doing nothing and buying at day 0 and selling at day 1 minus the transaction fee

        It's clear what we need: given I am granted one more forecast, I would find the max profit on the day of the last 'sell', and either: 1) delete that sell and instead sell on this i+1 day, OR 2) do nothing and return max_profit[i]. We can go to the last price index that was lower than current price and instead replace it with current transaction. 
        I.e. max_profit[i] = max(max_profit[i-1], max_profit[j] + prices[i] - prices[j] s.t. j is the first instance where prices[j] < prices[i] 

        Yeah the following doesn't really work
    
        n = len(prices)
        max_profit = [0 for i in range(n)]

        for i in range(1, n):
            
            last_idx = -1
            for k in reversed(range(i-1)):
                if prices[k] < prices[i]:
                    last_idx = k
                    break
            max_profit[i] = max(0, max_profit[i-1] + prices[i] - prices[i-1] - fee)
            if last_idx != -1:
                max_profit[i] = max(max_profit[i], max_profit[last_idx] + prices[i] - prices[last_idx])
        
        return max_profit[n-1]
        '''
        
        # dp_hold = [0 for i in range(n)] # where dp[i] = max profit when holding the stock at day i
        # dp_free = [0 for i in range(n)] # where dp[i] = max profit when not holding the stock at day i

        '''
        Base cases:
        dp_hold[0] = -fee
        dp_free[0] = 0

        dp_free = max(dp_hold[i-1] - fee + prices[i] - prices[i-1], dp_free[i-1])
        dp_hold[i] = max(dp_free[i-1], dp_hold[i-1]-prices[i])
        '''
        n = len(prices)
        if n <= 1:
            return 0

        dp_free = [0 for i in range(n)]
        dp_hold = [0 for i in range(n)]
        dp_hold[0] = -prices[0]
        
        for i in range(1, n):
            dp_free[i] = max(dp_hold[i-1] - fee + prices[i], dp_free[i-1])
            dp_hold[i] = max(dp_free[i-1] - prices[i], dp_hold[i-1])
        
        return max(dp_free[n-1], dp_hold[n-1])
        # return dp_free[-1]



