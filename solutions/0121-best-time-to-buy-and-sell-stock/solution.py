class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_bought_at = sys.maxsize

        for price in prices:
            min_bought_at = min(min_bought_at, price)
            diff = price - min_bought_at
            max_profit = max(max_profit, diff)
        
        return max_profit
        
