class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        '''
        Two variables at play -> 1) whether I should sell today or 2) whether I should buy today (can't buy if I'm holding the stock)
        Kind of a dp problem -> if I had only the information until today, what would I do with it? 

        Some examples:
         / \  /  \ 
        /   \/    \ 
       1  2  3  4  5   
        
        If I have only Day 1 and Day 2 data, I want to buy on day 1 and sell on day 2
        If I have only Day 1, 2, 3 data, I want to: buy + sell + do nothing
        If I have... Day 1, 2, 3, 4 data: buy + sell + buy + sell

        At any given day, 
        let max_profit[i] = max profit if we only have data until day i
        Then, transition: max_profit[i] = max_profit[i-1] + max(prices[i]-prices[i-1], 0)
        Base case: max_profit[0] = 0 (no use buying and selling at the same price)
        max_profit[1] =  max(prices[i]-prices[i-1], 0) (if prices decreasing, no profit; if increasing then imagine buying and selling
        '''
        n = len(prices)
        if n <= 1:
            return 0
        
        max_profit = [0 for i in range(n)]

        for i in range(1, n):
             max_profit[i] = max_profit[i-1] + max(prices[i]-prices[i-1], 0)
        
        return max_profit[n-1]
