class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # starting at the 0th index
        purchase = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i]-purchase)
            purchase = min(purchase, prices[i])
        return maxProfit