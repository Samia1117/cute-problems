class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # currentMax = 0
        # for i in range(len(prices)-1):
        #     buyVal = prices[i]
        #     sellValMax = sorted(prices[i+1:], reverse=True)[0]
        #     maxProfit = sellValMax - buyVal
        #     if maxProfit > currentMax:
        #          currentMax = maxProfit
        #     # print("Current max profit was: ", maxProfit)
        # return currentMax
        
        # for each day see it as a 'sell day', and
        # keep a 'thisDayMaxProfit' variable for that day
        # if the next day is even more profitable to sell
        # then we can add this day's highest profit to the
        # difference: nextDaySellVal-thisDaySellVal
        

        
#         # maxProfitSellDay = 0
        
#         maxSellPrice = prices[0]
#         maxProfit = 0
        
#         for i in range(1, len(prices)):
#             print("Current sell price proposal ", prices[i])
#             print("Current max sell price: ", maxSellPrice)
#             if prices[i] > maxSellPrice:
#                 print("Found better sell price = ", prices[i])
#                 maxProfit += prices[i] - maxSellPrice
#                 maxSellPrice = prices[i]
#                 print("Improved profit to : ", maxProfit)
#                 print("Changed Sell Price to : ", maxSellPrice)
                
#             else:    # if I'm not improving profit
#                 if maxProfit == 0:
#                     maxSellPrice = min(maxSellPrice, prices[i])
#                     print("Changed Max Sell Price to: ", maxSellPrice)
#         return maxProfit

        diffarr=[]
        prev=prices[0]
        for i in range(len(prices)):
            diffarr.append(prices[i]-prev)
            prev=min(prices[i],prev) 
        return max(diffarr)

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                
                
                
                
                
                
                
                
                
                
