class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(1, len(prices)):
        #     profit += max(prices[i] - prices[i-1] , 0)
        # return profit
        
        i = 0
        valley, peak = prices[0], prices[0]
        profit = 0
        
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
                
            peak = prices[i]
            profit += peak - valley
            
        return profit