class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minSoFar = 10000
        maxProfit = 0

        for price in prices:
            if (price < minSoFar):
                minSoFar = price

            profit = price - minSoFar
            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit
        
