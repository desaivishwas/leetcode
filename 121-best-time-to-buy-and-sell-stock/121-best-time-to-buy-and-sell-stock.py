class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ O(n)  One Pass """
        
        minPrice = float('inf')
        maxP = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                
            elif prices[i] - minPrice > maxP:
                maxP = prices[i] - minPrice
                
        return maxP
                
 
        
        
#         buy, sell = 0, 1
#         maxP = 0
#         while sell < len(prices):
#             if prices[buy] < prices[sell]:
#                 profit = prices[sell] - prices[buy]
#                 maxP = max(maxP, profit)
#             else:
#                 buy = sell
            
#             sell += 1
            
#         return maxP