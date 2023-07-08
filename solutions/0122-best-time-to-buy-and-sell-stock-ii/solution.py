class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        anchor = prices[0]
        sumProfit = 0
        for i in range(1, len(prices)):
            if (prices[i] - anchor > 0):
                sumProfit += prices[i] - anchor
            anchor = prices[i]
        
        return sumProfit

