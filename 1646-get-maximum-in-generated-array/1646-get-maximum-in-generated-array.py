class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0,1,1]
        for i in range(3, n + 1):
            dp.append(dp[i//2] + dp[i//2 + 1]*(i%2))
            
            
        return max(dp)
            