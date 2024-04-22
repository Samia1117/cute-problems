class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        totalProfit = 0
        n = len(prices)
        boughtAt = None

        for i in range(n):
            if i < n-1:
                if prices[i+1] <= prices[i]: # decreasing, so sell
                    if boughtAt != None:
                        # sell
                        print("Bought at ", boughtAt)
                        print("Sold at", prices[i])

                        profit = prices[i] - boughtAt
                        print("Profit: ", profit)

                        totalProfit += profit
                        # buy later
                        boughtAt = None
                    continue
                if boughtAt == None:
                    boughtAt = prices[i]
                elif prices[i] < boughtAt:
                    boughtAt = prices[i]

                # totalProfit += profit

                # boughtAt = prices[i]
            if i == n-1:
                if boughtAt != None:
                    totalProfit += prices[i] - boughtAt
                    
        return totalProfit
            

        
